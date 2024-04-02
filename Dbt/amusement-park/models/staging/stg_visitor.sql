{{
    config(
        materialized='view'
    )
}}

with 

source as (

    select * from {{ source('staging', 'visitor') }}

),

renamed as (

    select
        cast(entry_date AS TIMESTAMP) AS visitor_date,
        cast(country AS VARCHAR) AS country,
        cast(entry_id AS INTEGER) AS entry_id,
        cast(identification_card_id AS INTEGER) AS identification_card_id,
        cast(__index_level_0__ AS INTEGER) AS index_nr

    from source

)

select * from renamed


