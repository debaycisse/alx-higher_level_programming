-- This script lists all shows contained in the database hbtn_0d_tvshows.
SELECT tv_shows.title, IF(tv_show_genres.genre_id IS NULL, 'NULL', tv_show_genres.genre_id) FROM tv_shows JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id;
