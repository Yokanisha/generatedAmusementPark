select 
    cast(french_fries_id as integer) as french_fries_id,
    cast(size as string) as french_fries_size,
    cast(price as numeric) as french_fries_price
from {{ ref('french_fries') }}