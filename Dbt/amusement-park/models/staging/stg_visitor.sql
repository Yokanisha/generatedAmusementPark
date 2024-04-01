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
        entry_date,
        country,
        entry_id,
        identification_card_id,
        __index_level_0__

    from source

)

select * from renamed
