if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    
    file_name = "trigger-2.txt"
    content = "es hat funktioniert"
    
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"Die Datei '{file_name}' wurde erfolgreich erstellt.")
    except Exception as e:
        print(f"Fehler beim Erstellen der Datei: {e}")


    



    return {}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
