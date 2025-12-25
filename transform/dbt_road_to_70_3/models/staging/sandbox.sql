select *
from {{ source('strava_data', 'strava_activities') }}