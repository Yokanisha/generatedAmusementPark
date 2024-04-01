with 

source as (

    select * from {{ source('staging', 'action') }}

),

renamed as (

    select
        identification_card_id,
        ice_cream_parlor,
        french_fries,
        drink,
        souvenir,
        __index_level_0__

    from source

)

select * from renamed
