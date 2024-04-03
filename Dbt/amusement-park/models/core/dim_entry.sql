select 
    cast(entry_id as integer) as entry_id,
    cast(persons as string) as person,
    cast(price as numeric) as entry_price
from {{ ref('entry') }}