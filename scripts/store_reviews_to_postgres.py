"""Script to store processed reviews into PostgreSQL using db helper.

Reads the processed reviews CSV (path from settings) and inserts rows into
the database using `PostgresDB` helper. The database connection can be
configured via environment variables: `PGHOST`, `PGPORT`, `PGDATABASE`,
`PGUSER`, `PGPASSWORD`.

Example:
    python scripts/store_reviews_to_postgres.py --min-rows 400
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import pandas as pd

# Ensure project root is on path
ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from src.customer_analytics.config.settings import DATA_PATHS
from src.customer_analytics.utils.db_helper import PostgresDB


def load_processed_reviews(path: str) -> pd.DataFrame:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Processed reviews file not found: {path}")
    df = pd.read_csv(p)
    return df


def main(min_rows: int = 400, batch_size: int = 1000) -> int:
    # Prefer the processed path defined in settings
    processed_path = DATA_PATHS.get("processed_reviews")
    # Allow override via env var
    processed_path = os.getenv("PROCESSED_REVIEWS_PATH", processed_path)

    df = load_processed_reviews(processed_path)
    total_rows = len(df)
    print(f"Loaded {total_rows} processed reviews from {processed_path}")

    if total_rows == 0:
        print("No reviews to insert. Exiting.")
        return 0

    # Optionally sample to ensure at least min_rows are inserted
    if total_rows < min_rows:
        print(f"Warning: only {total_rows} rows available, less than requested {min_rows} rows.")

    db = PostgresDB()
    db.init_pool()
    try:
        db.create_tables()
        inserted = db.insert_reviews_from_df(df, batch_size=batch_size)
        print(f"Attempted to insert {inserted} review rows.")

        counts = db.query_review_count_by_bank()
        print("Review counts by bank:")
        for bank, cnt in counts.items():
            print(f"  {bank}: {cnt}")

        return inserted
    finally:
        db.close_pool()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Store processed reviews into Postgres DB")
    parser.add_argument("--min-rows", type=int, default=400, help="minimum rows expected to insert")
    parser.add_argument("--batch-size", type=int, default=1000, help="batch size for inserts")
    args = parser.parse_args()

    try:
        n = main(min_rows=args.min_rows, batch_size=args.batch_size)
        print(f"Done. Inserted (attempted) rows: {n}")
    except Exception as exc:
        print(f"Error: {exc}")
        raise
