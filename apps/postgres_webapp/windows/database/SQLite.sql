-- table
CREATE TABLE database_sapmletable (sample_data VARCHAR(20));

DROP TABLE database_sapmletable;

-- recode
INSERT INTO database_sapmletable (id, sample_data) VALUES (1, 'data-1'), (2, 'data-2');

DELETE FROM database_sapmletable; 
--WHERE id = X;

SELECT * FROM database_sapmletable;

UPDATE database_sapmletable SET sample_data = 'data-X' WHERE id = X; 
