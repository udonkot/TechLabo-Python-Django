-- SQLite
SELECT id, sample_data
FROM hazeyama_hazeyamatable;

INSERT INTO hazeyama_hazeyamatable (sample_data) VALUES ('data-1');
SELECT id, hazeyama_hazeyamatable FROM sample_table;

【補足】デリート時に使用
DELETE FROM hazeyama_hazeyamatable WHERE id = '1';
DELETE FROM hazeyama_hazeyamatable;