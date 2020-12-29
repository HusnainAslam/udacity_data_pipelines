from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class DataQualityOperator(BaseOperator):
    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id='',
                 tests={},
                 *args, **kwargs):
        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.tests = tests

    def execute(self, context):
        self.log.info('Connect Redshift')
        redshift = PostgresHook(self.redshift_conn_id)

        for test in self.tests:
            self.log.info('Run test query.')
            result = redshift.get_records(test['query'])

            self.log.info('Sanity checks on returned result set.')
            if len(result) == 0 or len(result[0]) == 0:
                raise ValueError('No result returned by test query. Data quality test failed.')
            count = result[0][0]

            self.log.info('Check expected results.')
            if count != test['expected_result']:
                raise ValueError('Returned count: {}. Data quality test failed.'.format(count))
        self.log.info('Data quality checks passed.')
