import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator



dag = DAG(
     dag_id="dag1",
     start_date=datetime.datetime(2021, 1, 1),
     schedule=None,
     render_template_as_native_obj = True
 )


d1 = DummyOperator()

d2 = DummyOperator()

d3 = DummyOperator()

d4 = DummyOperator()

d1 >> [d2,d3] >> d4