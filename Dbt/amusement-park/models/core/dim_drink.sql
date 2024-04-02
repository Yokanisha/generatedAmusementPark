select 
    cast(drink_id as integer) as drink_id,
    cast(size as numeric) as drink_size,
    cast(price as numeric) as drink_price
from {{ ref('drink') }}