-- This script lists all the cities of Carlifonia that can be found in the table, named cities, inside a passed database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'Carlifornia') ORDER BY id;
