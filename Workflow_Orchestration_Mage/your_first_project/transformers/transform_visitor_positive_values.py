if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    
    positive_data = data[data[['entry_id', 'identification_card_id']].apply(lambda x: x > 0).all(axis=1)]
    
    return positive_data

