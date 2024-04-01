import pandas as pd

from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_file(*args, **kwargs):

    url = r'https://github.com/Yokanisha/generatedAmusementPark/raw/main/Data/visitor_output.csv.gz'

    visitor_dtypes = {
        'country': pd.StringDtype(),
        'entry_id': pd.Int64Dtype(),
        'identification_card_id': pd.Int64Dtype()
    }

    parse_dates = ['entry_date']

    df = pd.read_csv(url, sep=",", dtype=visitor_dtypes, parse_dates=parse_dates, dayfirst=True)

    return df