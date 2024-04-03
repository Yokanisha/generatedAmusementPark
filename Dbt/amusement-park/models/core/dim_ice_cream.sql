select 
    cast(ice_cream_parlor_id as integer) as ice_cream_parlor_id,
    cast(number_of_scoops as integer) as number_of_scoops,
    cast(price as numeric) as ice_cream_price
from {{ ref('ice_cream') }}