select *
from {{ source('strava_raw', 'strava_activities') }}