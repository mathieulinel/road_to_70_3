select 
    date_trunc('week', activity_start_date) as week_start_date,
    activity_type,
    SUM(activity_distance) as total_distance,
    SUM(activity_moving_time) as total_moving_time,
    SUM(activity_elapsed_time) as total_elapsed_time,
    SUM(activity_total_elevation_gain) as total_elevation_gain,
    AVG(activity_average_speed) as total_average_speed,
    MAX(activity_max_speed) as total_max_speed,
    AVG(activity_average_heartrate) as total_average_heartrate,
    MAX(activity_max_heartrate) as total_max_heartrate
from {{ ref('stg__strava_activities') }}
where is_triathlon_training_activity IS TRUE
group by all
