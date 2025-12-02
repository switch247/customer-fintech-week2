-- SQL schema for bank_reviews database

CREATE TABLE IF NOT EXISTS banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name TEXT UNIQUE NOT NULL,
    app_name TEXT
);

CREATE TABLE IF NOT EXISTS reviews (
    review_id SERIAL PRIMARY KEY,
    orig_review_id TEXT UNIQUE,
    bank_id INTEGER REFERENCES banks(bank_id) ON DELETE SET NULL,
    review_text TEXT,
    rating INTEGER,
    review_date DATE,
    sentiment_label TEXT,
    sentiment_score REAL,
    source TEXT
);
