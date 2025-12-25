{% macro clean_strings(column_name) %}
    UPPER(TRIM(TRY_CAST({{ column_name }} as VARCHAR)))
{% endmacro %}