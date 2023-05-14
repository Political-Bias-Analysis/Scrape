CREATE DATABASE Articles;

DROP TABLE IF EXISTS biases;
DROP TABLE IF EXISTS articles;
DROP TABLE IF EXISTS media_source;
DROP TABLE IF EXISTS elections;


CREATE TABLE biases(
    main_bias TEXT,
    sub_biases TEXT[],
    PRIMARY KEY(main_bias)
);


CREATE TABLE articles(
    headline TEXT,
    author TEXT,
    source TEXT,
    published_date DATE, 
    article_content TEXT,
    main_bias TEXT,
    query_bias TEXT,
    url TEXT,
    PRIMARY KEY(headline, published_date, url),
    FOREIGN KEY(source) REFERENCES media_source(source_name)
);


-- new article that allows query bias as primary key
CREATE TABLE all_articles(
    headline TEXT,
    author TEXT,
    source TEXT,
    published_date DATE, 
    article_content TEXT,
    main_bias TEXT,
    query_bias TEXT,
    url TEXT,
    PRIMARY KEY(headline, author, published_date, url, query_bias)
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


-- for electiondb
create table stateKeys (
	state TEXT,
	state_name TEXT
);

-- create view for clean table 
CREATE TABLE voters_cleans AS
	SELECT year, voters.state, state_name, registered, voted, ROUND((norm_voter_reg * 100)::numeric, 2) as norm_voter_reg, ROUND((norm_voter_pop * 100)::numeric, 2) as norm_voter_pop
	FROM stateKeys natural join voters;

