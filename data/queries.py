from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')

def get_most_rated_shows(offset):
    return data_manager.execute_select('''SELECT shows.id, 
    shows.title,
    shows.year,
    shows.runtime,
    to_char(shows.rating::float,'999.9') AS rating_string,
    string_agg(genres.name,',' ORDER BY genres.name) AS genres_list,
    shows.trailer,
    shows.homepage
    FROM shows
    JOIN show_genres ON shows.id = show_genres.show_id
    JOIN genres on show_genres.genre_id = genres.id
    GROUP BY shows.id
    ORDER BY rating_string DESC
    LIMIT 15
    OFFSET %(offset)s;''',{"offset": offset })

def get_all_shows():
    return data_manager.execute_select('''SELECT shows.id, 
    shows.title,
    shows.year,
    shows.runtime,
    to_char(shows.rating::float,'999.9') AS rating_string,
    string_agg(genres.name,',' ORDER BY genres.name) AS genres_list,
    shows.trailer,
    shows.homepage
    FROM shows
    JOIN show_genres ON shows.id = show_genres.show_id
    JOIN genres on show_genres.genre_id = genres.id
    GROUP BY shows.id
    ORDER BY rating_string DESC;''')