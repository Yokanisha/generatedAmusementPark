import pandas as pd

from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_file(*args, **kwargs):

    url = r'https://github.com/Yokanisha/generatedAmusementPark/raw/main/Data/action_output.csv.gz'

    visitor_dtypes = {
        'identification_card_id': pd.Int64Dtype(),
        'ice_cream_parlor': pd.Int64Dtype(),
        'french_fries': pd.Int64Dtype(),
        'drink': pd.Int64Dtype(),
        'souvenir': pd.Int64Dtype()
    }

    df = pd.read_csv(url, sep=",", dtype=visitor_dtypes, dayfirst=True)

    return df