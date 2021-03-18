CREATE TABLE IF NOT EXISTS articles (
	source_id TEXT,
	source_name TEXT, 
	author TEXT,
	title TEXT,
	description TEXT,
	url TEXT,
	url_to_image TEXT,
	published_at TIMESTAMP,
	content TEXT
);

CREATE INDEX i_published_at
ON articles(published_at);
