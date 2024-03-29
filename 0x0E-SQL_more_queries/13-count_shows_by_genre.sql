-- This script lists all genres and the number of shows, linked to each of them
SELECT tv_genres.name, COUNT(tv_show_genres.genre_id) AS 'number_of_shows' FROM tv_genres JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.name ORDER BY `number_of_shows` DESC;
