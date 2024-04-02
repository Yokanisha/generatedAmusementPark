{{
    config(
        materialized='table'
    )
}}

with action_join_dim as (
    select 
        identification_card_id,
        drink_size,
        drink_price,
        french_fries_size,
        french_fries_price,
        number_of_scoops,
        ice_cream_price,
        souvenir_item,
        souvenir_price
     from {{ ref('action') }}
),

visitor_join_dim as (
    select
        visitor_date,
        country,
        identification_card_id,
        person,
        entry_price
    from {{ ref('visitor') }}
)

select

        v.visitor_date,
        v.country,
        v.person,
        v.entry_price,

        a.drink_size,
        a.drink_price,
        a.french_fries_size,
        a.french_fries_price,
        a.number_of_scoops,
        a.ice_cream_price,
        a.souvenir_item,
        a.souvenir_price

from action_join_dim as a
inner join visitor_join_dim as v
on a.identification_card_id = v.identification_card_id