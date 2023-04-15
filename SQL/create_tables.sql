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

INSERT INTO biases (main_bias, sub_bias) VALUES ('immigration', ARRAY['immigration','undocumented','refugees','nationalism','border','Dreamers', 'asylum seekers','xenophobia']);
INSERT INTO biases(main_bias, sub_bias) VALUES ('racial', ARRAY['racial', 'disparities', 'white privilege', 'black lives matter', 'segregation', 'critical race theory', 'criminal', 'racial discrimination', 'CRT', 'woke', 'wokeness']);
INSERT INTO biases(main_bias, sub_bias) VALUES ('Abortion', ARRAY['Abortion', 'Pro-life', 'pro-choice', 'consent', 'mifepristone', 'abortion pill', 'planned parenthood','rape','reproductive rights','women’s right','reproductive rights','abortion bans','birth control']);
INSERT INTO biases(main_bias, sub_bias) VALUES ('socioeconomic', ARRAY['socioeconomic','poverty line','class privilege','working class','pro-public assistance','marginalized','middle class','poverty','food stamps','medicare','medical','rich','wealthy']);



INSERT INTO media_source(source_name) VALUES('FOX');
INSERT INTO media_source(source_name) VALUES('NPR');
INSERT INTO media_source(source_name) VALUES('CBS');