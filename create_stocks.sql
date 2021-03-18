CREATE TABLE IF NOT EXISTS stocks (
    symbol TEXT,
    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,
    adjusted_close FLOAT,
    volume INT,
    transactions_date DATETIME
);

CREATE INDEX IF NOT EXISTS i_transactions_date
ON stocks(transactions_date);
