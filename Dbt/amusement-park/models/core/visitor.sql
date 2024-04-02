{{
    config(
        materialized='table'
    )
}}

with visitor as (
    select 
        visitor_date,
        country,
        entry_id AS entry_id_fk,
        identification_card_id,
        index_nr
     from {{ ref('stg_visitor') }}
),

entry as (
    select 
        entry_id as entry_id_pk,
        person,
        entry_price
    from  {{ ref('dim_entry') }}
),

action_join_dim as (
    select * from visitor
    left join entry
    on visitor.entry_id_fk = entry.entry_id_pk
)

select 
    visitor_date,
    country,
    identification_card_id,
    person,
    entry_price

 from action_join_dim