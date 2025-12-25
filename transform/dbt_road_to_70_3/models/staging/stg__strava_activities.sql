SELECT 
    id as activity_id,
    {{ clean_strings('name') }} as activity_name,
    TRY_CAST(distance as FLOAT) as activity_distance,
    TRY_CAST(moving_time as INTEGER) as activity_moving_time,
    TRY_CAST(elapsed_time as INTEGER) as activity_elapsed_time,
    TRY_CAST(total_elevation_gain as FLOAT) as activity_total_elevation_gain,
    {{ clean_strings('type') }} as activity_type,
    IF({{ clean_strings('type') }} in ('RUN', 'RIDE', 'SWIM'), TRUE, FALSE) as is_triathlon_activity,
    IF({{ clean_strings('type') }} in ('RUN', 'RIDE', 'SWIM', 'WORKOUT'), TRUE, FALSE) as is_triathlon_training_activity,
    TRY_CAST(start_date as TIMESTAMP) as activity_start_date,
    TRY_CAST(average_speed as FLOAT) as activity_average_speed,
    TRY_CAST(max_speed as FLOAT) as activity_max_speed,
    TRY_CAST(average_heartrate as FLOAT) as activity_average_heartrate,
    TRY_CAST(max_heartrate as FLOAT) as activity_max_heartrate,
    TRY_CAST(ingestion_at_ts as TIMESTAMP) as source_ingestion_at_ts,
    current_localtimestamp() as ingestion_at_ts
FROM {{ source('strava_raw', 'strava_activities') }}