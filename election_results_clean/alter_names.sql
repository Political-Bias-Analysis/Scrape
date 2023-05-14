ALTER TABLE results 
RENAME COLUMN "Year" TO year;

ALTER TABLE results 
RENAME COLUMN "Office" TO office;

ALTER TABLE results 
RENAME COLUMN "State" TO state;

ALTER TABLE results 
RENAME COLUMN "Last Name" TO last_name;

ALTER TABLE results 
RENAME COLUMN "Party" TO party;

ALTER TABLE results 
RENAME COLUMN "Vote %" TO vote_percentage;

ALTER TABLE results 
RENAME COLUMN "Vote count" TO vote_count;

ALTER TABLE voters 
RENAME COLUMN "Year" TO year;

ALTER TABLE voters 
RENAME COLUMN "State" TO state;

ALTER TABLE voters 
RENAME COLUMN "Population" TO population;

ALTER TABLE voters 
RENAME COLUMN "Registered" TO registered;

ALTER TABLE voters 
RENAME COLUMN "Voted" TO voted;

ALTER TABLE voters 
RENAME COLUMN "Norm_Voter_Reg" TO norm_voter_reg;

ALTER TABLE voters 
RENAME COLUMN "Norm_Voter_Pop" TO norm_voter_pop;


