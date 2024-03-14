-- This script lists all cities contained in the cities table, along with their states from the states table.
SELECT c.id, c.name, s.name FROM cities AS c JOIN states AS s ON c.state_id = s.id ORDER BY c.id;
