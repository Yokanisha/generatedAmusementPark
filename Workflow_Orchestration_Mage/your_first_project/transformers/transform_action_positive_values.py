if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    columnList = ['identification_card_id', 'ice_cream_parlor', 'french_fries', 'drink', 'souvenir']
    positive_data = data[data[columnList].apply(lambda x: x >= 0).all(axis=1)]
    
    return positive_data
