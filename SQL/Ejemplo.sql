CREATE TEMPORARY TABLE csvtable

LOAD DATA INFILE 'Popular_Baby_Names.csv' 
INTO TABLE csvtable 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
