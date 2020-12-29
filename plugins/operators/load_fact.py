from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class LoadFactOperator(BaseOperator):
    ui_color = '#F98866'

    __INSERT_SQL__ = """
        INSERT INTO {}
        {}
    """

    __DELETE_SQL__ = """
        DELETE FROM {}
    """

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 table="",
                 select_sql="",
                 append_mode=True,
                 *args, **kwargs):
        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.select_sql = select_sql
        self.append_mode = append_mode

    def execute(self, context):
        self.log.info('Connect Redshift.')
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)

        self.log.info('Delete existing records if append mode is disabled.')
        if not self.append_mode:
            redshift.run(self.__DELETE_SQL__.format(self.table))

        insert_sql = self.__INSERT_SQL__.format(self.table, self.select_sql)

        self.log.info('Run insert SQL statement.')
        redshift.run(insert_sql)
