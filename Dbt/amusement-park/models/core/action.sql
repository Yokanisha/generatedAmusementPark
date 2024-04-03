{{
    config(
        materialized='table'
    )
}}

with _action as (
    select 
        identification_card_id,
        ice_cream_parlor_id,
        french_fries_id,
        drink_id,
        souvenir_id,
        index_nr
    from {{ ref('stg_action') }}
),

drink as (
    select
        drink_id,
        drink_size,
        drink_price
    
    from {{ ref('dim_drink') }}
),

french_fries as (
    select 
        french_fries_id,
        french_fries_size,
        french_fries_price
    from {{ ref('dim_french_fries') }}
),

ice_cream as (
    select 
        ice_cream_parlor_id,
        number_of_scoops,
        ice_cream_price
    from {{ ref('dim_ice_cream') }}
),

souvenir as (
    select 
        souvenir_id,
        souvenir_item,
        souvenir_price
    from {{ ref('dim_souvenir') }}
),

action_join_dim as (
    select 
        a.identification_card_id,
        d.drink_size,
        d.drink_price,
        f.french_fries_size,
        f.french_fries_price,
        ic.number_of_scoops,
        ic.ice_cream_price,
        s.souvenir_item,
        s.souvenir_price

    from _action as a

    left join drink as d
    on a.drink_id = d.drink_id

    left join french_fries as f
    on a.french_fries_id = f.french_fries_id

    left join ice_cream as ic
    on a.ice_cream_parlor_id = ic.ice_cream_parlor_id

    left join souvenir as s
    on a.souvenir_id = s.souvenir_id
)

select * from action_join_dim

