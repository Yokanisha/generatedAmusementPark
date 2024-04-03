select 
    cast(souvenir_id as integer) as souvenir_id,
    cast(item as string) as souvenir_item,
    cast(price as numeric) as souvenir_price
from {{ ref('souvenir') }}