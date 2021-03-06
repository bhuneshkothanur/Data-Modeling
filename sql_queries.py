# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(
      songplay_id BIGSERIAL PRIMARY KEY, 
      start_time bigint NOT NULL, 
      user_id int NOT NULL, 
      level varchar, 
      song_id varchar, 
      artist_id varchar, 
      session_id int, 
      location varchar, 
      user_agent text)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(
      user_id int PRIMARY KEY, 
      first_name varchar,
      last_name varchar, 
      gender char(1), 
      level varchar)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(
       song_id varchar PRIMARY KEY, 
       title varchar, 
       artist_id varchar, 
       year int, 
       duration float)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(
    artist_id varchar PRIMARY KEY,
    name varchar, 
    location varchar, 
    latitude decimal(9,6), 
    longitude decimal(9,6))
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
    start_time bigint PRIMARY KEY, 
    hour int, 
    day int, 
    week int, 
    month int, 
    year int, 
    weekday varchar)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays
(
start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
)
values(%s,%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT (songplay_id) DO NOTHING;
""")

user_table_insert = ("""
INSERT INTO users
(
user_id, first_name, last_name, gender, level
)
values (%s,%s,%s,%s,%s)
ON CONFLICT(user_id) DO UPDATE SET level = excluded.level;
""")

song_table_insert = ("""
INSERT INTO songs
(
song_id, title, artist_id, year, duration
)
values (%s,%s,%s,%s,%s)
ON CONFLICT (song_id) DO NOTHING;
""") 

artist_table_insert = ("""
INSERT INTO artists
(
artist_id, name, location, latitude, longitude
)
values(%s,%s,%s,%s,%s)
ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time
(
start_time, hour, day, week, month, year, weekday
)
values(%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT song_id, artists.artist_id from songs 
inner join artists on songs.artist_id=artists.artist_id 
where songs.title=(%s) and artists.name=(%s) and songs.duration=(%s)
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]