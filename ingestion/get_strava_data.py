import requests
import json
import duckdb
import csv
from datetime import datetime
import os
from dotenv import load_dotenv
import time
# Load environment variables from .env file
load_dotenv()

# to be stored in the .env file
CLIENT_ID = os.getenv('STRAVA_CLIENT_ID')
CLIENT_SECRET = os.getenv('STRAVA_CLIENT_SECRET')
REFRESH_TOKEN = os.getenv('STRAVA_REFRESH_TOKEN')
PER_PAGE = 200

# Add decorator

# Step 1: Get the access token
def get_access_token(client_id, client_secret, refresh_token=None):
    url = "https://www.strava.com/oauth/token"
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        raise Exception(f"Failed to get access token: {response.text}")

# Step 2: Fetch activity data
def fetch_activities(access_token, per_page=10):
    url = "https://www.strava.com/api/v3/athlete/activities"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    params = {
        'per_page': per_page
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch activities: {response.text}")

# Step 3: Store data in DuckDB
def store_in_duckdb(activities):
    # Connect to DuckDB (in-memory or file)
    conn = duckdb.connect(database='data/strava_data.duckdb')

    # Create a table
    conn.execute("""
    CREATE TABLE IF NOT EXISTS strava_activities (
        id BIGINT,
        name VARCHAR,
        distance FLOAT,
        moving_time INTEGER,
        elapsed_time INTEGER,
        total_elevation_gain FLOAT,
        type VARCHAR,
        start_date TIMESTAMP,
        average_speed FLOAT,
        max_speed FLOAT,
        average_heartrate FLOAT,
        max_heartrate FLOAT,
        ingestion_at_ts TIMESTAMP
    )
    """)

    # Insert data
    for activity in activities:
        conn.execute("""
        INSERT INTO strava_activities VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, current_localtimestamp()
        )
        """, (
            activity.get('id'),
            activity.get('name'),
            activity.get('distance'),
            activity.get('moving_time'),
            activity.get('elapsed_time'),
            activity.get('total_elevation_gain'),
            activity.get('type'),
            activity.get('start_date'),
            activity.get('average_speed'),
            activity.get('max_speed'),
            activity.get('average_heartrate'),
            activity.get('max_heartrate')
        ))

    # Print the table
    print(f"{len(activities)} activities stored in DuckDB")
    
    # Close the connection
    conn.close()
    
# Step 4: Store activities in a csv file for debugging with the name files contains the timestamp of the ingestion
def store_in_csv(activities):
    with open(f'data/raw/activities_{datetime.now().strftime("%Y%m%d%H%M%S")}.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(activities[0].keys())
        for activity in activities:
            writer.writerow(activity.values())

if __name__ == "__main__":
    # Get access token
    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)

    # Fetch activities
    activities = fetch_activities(access_token, PER_PAGE)
    
    # Store activities in a csv file for debugging
    store_in_csv(activities)


    # Store in DuckDB
    store_in_duckdb(activities)