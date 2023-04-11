DROP TABLE IF EXISTS biases;
DROP TABLE IF EXISTS articles;
DROP TABLE IF EXISTS media_source;
DROP TABLE IF EXISTS elections;


CREATE TABLE biases(
    main_bias TEXT,
    sub_bias TEXT[],
    PRIMARY KEY(main_bias)
);


CREATE TABLE articles(
    headline TEXT,
    author TEXT,
    source TEXT,
    published_date DATE, 
    article_content TEXT,
    bias TEXT[],
    url TEXT,
    PRIMARY KEY(headline, published_date),
    FOREIGN KEY(source) REFERENCES media_source(source_name)
);

CREATE TABLE media_source(
    source_name TEXT,
    PRIMARY KEY(source_name)
);

CREATE TABLE elections(
    election_year INT,
    election_type TEXT, 
    candidate_name TEXT,
    candidate_party TEXT,
    general_vote_count BIGINT,
    general_vote_percentage DECIMAL,
    PRIMARY KEY(candidate_name, election_year)
    
);