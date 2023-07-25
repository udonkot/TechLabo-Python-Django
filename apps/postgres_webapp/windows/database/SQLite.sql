-- SQLite
CREATE TABLE sample_table (sample_data VARCHAR(20));

DROP TABLE sample_table;

INSERT INTO database_sapmletable (id, sample_data) VALUES (1, 'data-1'), (2, 'data-2');

DELETE FROM database_sapmletable; 
--WHERE sample_data = 'sample data';

SELECT * FROM database_sapmletable;
