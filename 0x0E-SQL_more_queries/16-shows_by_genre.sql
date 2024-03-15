-- This script lists all shows and their genres. It displays 'NULL' for any show without genre
SELECT tv_shows.title, IF(tv_show_genres.genre_id IS NULL, 'NULL', tv_genres.name) AS 'name' FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id LEFT JOIN tv_genres ON tv_show_genres.genre_id=tv_genres.id ORDER BY tv_shows.title, tv_genres.name;
