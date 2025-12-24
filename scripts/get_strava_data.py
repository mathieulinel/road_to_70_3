import requests
import json
import duckdb

# Replace these with your Strava API credentials
CLIENT_ID = '186926'
CLIENT_SECRET = '79fbb5fb15243ed9259ffd5a8ad62f6d3bc5173e'
REFRESH_TOKEN = 'd2563983165e6d93d156dff07f40a366de8756b2'  # Optional, if you want to refresh the token
PER_PAGE = 50

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
    conn = duckdb.connect(database='strava_data.duckdb')

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
        max_heartrate FLOAT
    )
    """)

    # Insert data
    for activity in activities:
        conn.execute("""
        INSERT INTO strava_activities VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
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
    print("Data stored in DuckDB:")
    result = conn.execute("SELECT * FROM strava_activities").fetchall()
    for row in result:
        print(row)

    # Close the connection
    conn.close()

# Example usage
if __name__ == "__main__":
    # Get access token
    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)

    # Fetch activities
    activities = fetch_activities(access_token, PER_PAGE)

    # Store in DuckDB
    store_in_duckdb(activities)