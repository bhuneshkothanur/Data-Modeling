# PROJECT:  SPARKIFY DATABASE

### Project Summary: 
Sparkify is a music streaming app who wants to analyze the user activity and song details through their streaming app. The data regarding what users are listening to is being sent in json format. Since the logs of user activity and metadata of songs are present in json format, it is difficult for them to query. 
I would like to create a database for this work called sparkifydb and create tables for the songs and user activity. I have used PostgreSQL and build a ETL pipeline using python.
            
**Songs Dataset Example:**
Song dataset contains metadata about the artist and the songs they composed.

**Path:** song_data/A/A/B/TRAABJL12903CDCF1A.json

{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}


**Logs Dataset Example:**
Logs dataset contains activity of the users from the streaming app based on certain configurations.

**Path:** log_data/2018/11/2018-11-12-events.json

The json contains details regarding the users such as firstname, lastname, gender, artists, songs, length of the song, starttime, userid.


**Schema:** I have created a STAR schema with the below details:

**FACT Table:**

> **songplays:** records in log data associated with song plays i.e. records with page NextSong

>> songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

**Dimension Tables:**

> **users:** users in the app
>>    user_id, first_name, last_name, gender, level

> **songs:** songs in music database
>>    song_id, title, artist_id, year, duration

>**artists:** artists in music database
>>    artist_id, name, location, latitude, longitude

>**time:** timestamps of records in songplays broken down into specific units
>>    start_time, hour, day, week, month, year, weekday

    
### Python Script:

!python create_tables.py *(used to call create_tables.py script)*

**CREATE TABLES**
   1. CREATE statements are written in sql_queries.py to create each table.
   2. DROP statements are written in sql_queries.py to drop each table if it exists.
   3. Run create_tables.py to create your database and tables.
   4. Run test.ipynb to confirm the creation of your tables with the correct columns. Make sure to click "Restart      kernel" to close the connection to the database after running this notebook.

**ETL PROCESSES**
   1. etl.ipynb notebook is used to develop ETL processes for each table. Run the test.ipynb after inserting           records    into the table to confirm if the records were inserted correctly.
   2. Rerun create_tables.py to reset the tables before running this notebook.

**ETL PIPELINE**
   1. Use etl.ipynb as reference and insert all the records using etl.py.
   2. Remember to run create_tables.py before running etl.py to reset the tables. 
   3. Run test.ipynb to confirm the records were successfully inserted into each table.


**REFERENCES**

> Udacity Knowledge hub.