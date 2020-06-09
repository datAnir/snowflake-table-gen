#!/usr/bin/env python

import pandas
from sqlalchemy import create_engine
from parameters import user, password, account, database, schema, warehouse, role, table_name, csv_file
engine = create_engine(
    'snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse}&role={role}'.format(
        user=user,
        password=password,
        account=account,
        database=database,
        schema=schema,
        warehouse=warehouse,
        role=role
    )
)
table_name = table_name
csv_file = csv_file
with engine.connect() as connection:
    results = connection.execute('select current_version()').fetchone()
    print(results[0])
    df = pandas.read_csv(csv_file)
    df.to_sql(table_name, connection, if_exists='fail', index=False, chunksize=16000)

