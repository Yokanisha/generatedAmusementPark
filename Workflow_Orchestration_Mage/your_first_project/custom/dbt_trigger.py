if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(*args, **kwargs):
    from mage_ai.services.dbt.dbt import DbtCloudClient


    client = DbtCloudClient(dict(account_id=255585, api_token='dbtu_zFlZDb80OD0otQzAkslhkAtEXhfg9MycDyq6VT7Ag-7CjJEzyA'))

    # Set poll_status=True to wait for job completion.
    # Set poll_status=False to not wait for job completion.
    client.trigger_job_run(255585, poll_status=True)

    return {}

