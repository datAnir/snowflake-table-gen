# snowflake-table-gen
A quick method of generating a table from a CSV in Snowflake and uploading the data

Usage: 
1) Clone this repo
2) Set up a Python virtualenv
3) pip install the requirements.txt file
4) Fill out the parameters.py file
5) Run the script! 

Essentially this is super simple - we set up a connection to Snowflake using the Snowflake SQLAlchemy driver,  read the CSV with Pandas, and then pass the connection to Pandas to create the table. Pandas actually does the magic of sampling the table to establish datatypes, generates the SQL statement (with SQL Alchemy), and creates the table.

The only things we do here are:
1) Set the chunk-size to 16000. This is because Snowflake has a maximum number of rows that can be inserted in a single statement.
2) Set index to False - because Snowflake doesn't use indexes.

Note: I do _not_ recommend using this to do large loads, as under the hood Pandas is using an INSERT statement, which doesn't leverage Snowflake's COPY command. COPY is much faster for bulk data loads. This is just a speedy way of generating the DDL and auto-running it.


TODOs/Caveats/Open questions:
- I'm not certain how far Pandas goes to get optimal DDL - I highly recommend using the generated DDL as a start point and editing it.
- Ideally this would be easier to use, but honestly you can probably just use the interactive interpreter.