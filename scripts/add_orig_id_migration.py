"""Migration to add `orig_review_id` column and unique constraint if missing.

Run this after applying schema changes or to ensure existing DB has the
column required for idempotent upserts.
"""
from __future__ import annotations

import os
from urllib.parse import urlparse
import psycopg2


def main():
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise EnvironmentError("DATABASE_URL not set")
    parsed = urlparse(database_url)
    conn = psycopg2.connect(host=parsed.hostname, port=parsed.port, dbname=parsed.path.lstrip('/'), user=parsed.username, password=parsed.password)
    cur = conn.cursor()
    # Add column if not exists
    cur.execute("ALTER TABLE reviews ADD COLUMN IF NOT EXISTS orig_review_id TEXT;")
    # Create unique index if not exists
    cur.execute("DO $$ BEGIN IF NOT EXISTS (SELECT 1 FROM pg_indexes WHERE tablename='reviews' AND indexname='reviews_orig_review_id_key') THEN CREATE UNIQUE INDEX reviews_orig_review_id_key ON reviews(orig_review_id); END IF; END$$;")
    conn.commit()
    cur.close()
    conn.close()
    print('Migration applied: orig_review_id column ensured.')


if __name__ == '__main__':
    main()
