"""Truncate reviews table and repopulate from processed CSV.

This script DOES NOT create backups. It truncates `reviews` and inserts
rows from the processed CSV (prefers `outputs/models/reviews_with_sentiment_and_themes.csv`).
Use with caution.
"""
from __future__ import annotations

import os
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd
from src.customer_analytics.config import settings
from src.customer_analytics.utils.db_helper import PostgresDB


def load_processed(path_override: str | None = None) -> pd.DataFrame:
    if path_override:
        p = Path(path_override)
    else:
        p = Path('outputs') / 'models' / 'reviews_with_sentiment_and_themes.csv'
        if not p.exists():
            p = Path(settings.DATA_PATHS.get('processed_reviews'))

    if not p.exists():
        raise FileNotFoundError(f'Processed reviews CSV not found at {p}')

    df = pd.read_csv(p)
    return df


def main():
    processed_path = os.getenv('PROCESSED_REVIEWS_PATH')
    df = load_processed(processed_path)
    print(f'Loaded {len(df)} rows from processed CSV')

    db = PostgresDB()
    db.init_pool()
    try:
        # Ensure schema exists
        db.create_tables()

        # Truncate reviews table (no backups, per request)
        with db.get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute('TRUNCATE TABLE reviews RESTART IDENTITY CASCADE;')
            conn.commit()
        print('Truncated reviews table')

        # Insert from DataFrame
        inserted = db.insert_reviews_from_df(df)
        print(f'Inserted (attempted) {inserted} rows')

        counts = db.query_review_count_by_bank()
        print('Review counts by bank:')
        for bank, cnt in counts.items():
            print(f'  {bank}: {cnt}')

    finally:
        db.close_pool()


if __name__ == '__main__':
    main()
