with 

source as (

    select * from {{ source('staging', 'action') }}

),

renamed as (

    select
        cast(identification_card_id AS INTEGER) AS identification_card_id,
        cast(ice_cream_parlor AS INTEGER) AS ice_cream_parlor_id,
        cast(french_fries AS INTEGER) AS french_fries_id,
        cast(drink AS INTEGER) AS drink_id,
        cast(souvenir AS INTEGER) AS souvenir_id,
        cast( __index_level_0__ AS INTEGER) AS index_nr

    from source

)

select * from renamed
