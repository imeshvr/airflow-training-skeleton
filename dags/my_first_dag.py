# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""My First DAG."""

from datetime import timedelta

import airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator

args = {
    'owner': 'Thibaut',
    'start_date': airflow.utils.dates.days_ago(2)
}

dag = DAG(
    dag_id='my_first_dag',
    default_args=args,
    schedule_interval=None,
    dagrun_timeout=timedelta(minutes=60)
)

t1 = BashOperator(
    task_id='task_one',
    bash_command='echo 1',
    dag=dag
)

t2 = BashOperator(
    task_id='task_two',
    bash_command='echo 1',
    dag=dag
)

t3 = BashOperator(
    task_id='task_three',
    bash_command='echo 1',
    dag=dag
)

t4 = BashOperator(
    task_id='task_four',
    bash_command='echo 1',
    dag=dag
)

t5 = DummyOperator(
    task_id='run_this_last',
    dag=dag,
)

t1 >> t2
t2 >> t3
t2 >> t4
t3 >> t5
t4 >> t5
