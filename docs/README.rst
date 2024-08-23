
Simple DDL Parser
-----------------


.. image:: https://img.shields.io/pypi/v/simple-ddl-parser-2
   :target: https://img.shields.io/pypi/v/simple-ddl-parser-2
   :alt: badge1

.. image:: https://img.shields.io/pypi/l/simple-ddl-parser-2
   :target: https://img.shields.io/pypi/l/simple-ddl-parser-2
   :alt: badge2

.. image:: https://img.shields.io/pypi/pyversions/simple-ddl-parser-2
   :target: https://img.shields.io/pypi/pyversions/simple-ddl-parser-2
   :alt: badge3

.. image:: https://github.com/xnuinside/simple-ddl-parser/actions/workflows/main.yml/badge.svg
   :target: https://github.com/xnuinside/simple-ddl-parser/actions/workflows/main.yml/badge.svg
   :alt: workflow


Build with ply (lex & yacc in python). A lot of samples in 'tests/.

Is it Stable?
^^^^^^^^^^^^^

Yes, this is a project based on https://github.com/xnuinside/simple-ddl-parser

How does it work?
^^^^^^^^^^^^^^^^^

Parser supports:


* SQL
* HQL (Hive)
* MSSQL dialec
* Oracle dialect
* MySQL dialect
* PostgreSQL dialect
* BigQuery
* Redshift
* Snowflake
* SparkSQL
* IBM DB2 dialect

You can check dialects sections after ``Supported Statements`` section to get more information that statements from dialects already supported by parser. If you need to add more statements or new dialects - feel free to open the issue.

How to install
^^^^^^^^^^^^^^

.. code-block:: bash


       pip install simple-ddl-parser

How to use
----------

Extract additional information from HQL (& other dialects)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In some dialects like HQL there is a lot of additional information about table like, fore example, is it external table, STORED AS, location & etc. This property will be always empty in 'classic' SQL DB like PostgreSQL or MySQL and this is the reason, why by default this information are 'hidden'.
Also some fields hidden in HQL, because they are simple not exists in HIVE, for example 'deferrable_initially'
To get this 'hql' specific details about table in output please use 'output_mode' argument in run() method.

example:

.. code-block:: python


       ddl = """
       CREATE TABLE IF NOT EXISTS default.salesorderdetail(
           SalesOrderID int,
           ProductID int,
           OrderQty int,
           LineTotal decimal
           )
       PARTITIONED BY (batch_id int, batch_id2 string, batch_32 some_type)
       LOCATION 's3://datalake/table_name/v1'
       ROW FORMAT DELIMITED
           FIELDS TERMINATED BY ','
           COLLECTION ITEMS TERMINATED BY '\002'
           MAP KEYS TERMINATED BY '\003'
       STORED AS TEXTFILE
       """

       result = DDLParser(ddl).run(output_mode="hql")
       print(result)

And you will get output with additional keys 'stored_as', 'location', 'external', etc.

.. code-block:: python


       # additional keys examples
     {
       ...,
       'location': "'s3://datalake/table_name/v1'",
       'map_keys_terminated_by': "'\\003'",
       'partitioned_by': [{'name': 'batch_id', 'size': None, 'type': 'int'},
                           {'name': 'batch_id2', 'size': None, 'type': 'string'},
                           {'name': 'batch_32', 'size': None, 'type': 'some_type'}],
       'primary_key': [],
       'row_format': 'DELIMITED',
       'schema': 'default',
       'stored_as': 'TEXTFILE',
       ...
     }

If you run parser with command line add flag '-o=hql' or '--output-mode=hql' to get the same result.

Possible output_modes: ['redshift', 'spark_sql', 'mysql', 'bigquery', 'mssql', 'databricks', 'sqlite', 'vertics', 'ibm_db2', 'postgres', 'oracle', 'hql', 'snowflake', 'sql']

From python code
^^^^^^^^^^^^^^^^

.. code-block:: python

       from simple_ddl_parser_2 import DDLParser


       parse_results = DDLParser("""create table dev.data_sync_history(
           data_sync_id bigint not null,
           sync_count bigint not null,
           sync_mark timestamp  not  null,
           sync_start timestamp  not null,
           sync_end timestamp  not null,
           message varchar(2000) null,
           primary key (data_sync_id, sync_start)
       ); """).run()

       print(parse_results)

To parse from file
^^^^^^^^^^^^^^^^^^

.. code-block:: python


       from simple_ddl_parser_2 import parse_from_file

       result = parse_from_file('tests/sql/test_one_statement.sql')
       print(result)

From command line
^^^^^^^^^^^^^^^^^

simple-ddl-parser is installed to environment as command **sdp**

.. code-block:: bash


       sdp path_to_ddl_file

       # for example:

       sdp tests/sql/test_two_tables.sql

You will see the output in **schemas** folder in file with name **test_two_tables_schema.json**

If you want to have also output in console - use **-v** flag for verbose.

.. code-block:: bash


       sdp tests/sql/test_two_tables.sql -v

If you don't want to dump schema in file and just print result to the console, use **--no-dump** flag:

.. code-block:: bash


       sdp tests/sql/test_two_tables.sql --no-dump

You can provide target path where you want to dump result with argument **-t**\ , **--target**\ :

.. code-block:: bash


       sdp tests/sql/test_two_tables.sql -t dump_results/

Get Output in JSON
^^^^^^^^^^^^^^^^^^

If you want to get output in JSON in stdout you can use argument **json_dump=True** in method **.run()** for this

.. code-block:: python

       from simple_ddl_parser_2 import DDLParser


       parse_results = DDLParser("""create table dev.data_sync_history(
           data_sync_id bigint not null,
           sync_count bigint not null,
       ); """).run(json_dump=True)

       print(parse_results)

Output will be:

.. code-block:: json

   [{"columns": [{"name": "data_sync_id", "type": "bigint", "size": null, "references": null, "unique": false, "nullable": false, "default": null, "check": null}, {"name": "sync_count", "type": "bigint", "size": null, "references": null, "unique": false, "nullable": false, "default": null, "check": null}], "primary_key": [], "alter": {}, "checks": [], "index": [], "partitioned_by": [], "tablespace": null, "schema": "dev", "table_name": "data_sync_history"}]

More details
^^^^^^^^^^^^

``DDLParser(ddl).run()``
.run() method contains several arguments, that impact changing output result. As you can saw upper exists argument ``output_mode`` that allow you to set dialect and get more fields in output relative to chosen dialect, for example 'hql'. Possible output_modes: ['redshift', 'spark_sql', 'mysql', 'bigquery', 'mssql', 'databricks', 'sqlite', 'vertics', 'ibm_db2', 'postgres', 'oracle', 'hql', 'snowflake', 'sql']

Also in .run() method exists argument ``group_by_type`` (by default: False). By default output of parser looks like a List with Dicts where each dict == one entity from ddl (table, sequence, type, etc). And to understand that is current entity you need to check Dict like: if 'table_name' in dict - this is a table, if 'type_name' - this is a type & etc.

To make work little bit easy you can set group_by_type=True and you will get output already sorted by types, like:

.. code-block:: python


       {
           'tables': [all_pasrsed_tables],
           'sequences': [all_pasrsed_sequences],
           'types': [all_pasrsed_types],
           'domains': [all_pasrsed_domains],
           ...
       }

For example:

.. code-block:: python


       ddl = """
       CREATE TYPE "schema--notification"."ContentType" AS
           ENUM ('TEXT','MARKDOWN','HTML');
           CREATE TABLE "schema--notification"."notification" (
               content_type "schema--notification"."ContentType"
           );
       CREATE SEQUENCE dev.incremental_ids
           INCREMENT 10
           START 0
           MINVALUE 0
           MAXVALUE 9223372036854775807
           CACHE 1;
       """

       result = DDLParser(ddl).run(group_by_type=True)

       # result will be:

       {'sequences': [{'cache': 1,
                       'increment': 10,
                       'maxvalue': 9223372036854775807,
                       'minvalue': 0,
                       'schema': 'dev',
                       'sequence_name': 'incremental_ids',
                       'start': 0}],
       'tables': [{'alter': {},
                   'checks': [],
                   'columns': [{'check': None,
                               'default': None,
                               'name': 'content_type',
                               'nullable': True,
                               'references': None,
                               'size': None,
                               'type': '"schema--notification"."ContentType"',
                               'unique': False}],
                   'index': [],
                   'partitioned_by': [],
                   'primary_key': [],
                   'schema': '"schema--notification"',
                   'table_name': '"notification"'}],
       'types': [{'base_type': 'ENUM',
                   'properties': {'values': ["'TEXT'", "'MARKDOWN'", "'HTML'"]},
                   'schema': '"schema--notification"',
                   'type_name': '"ContentType"'}]}

ALTER statements
^^^^^^^^^^^^^^^^

Right now added support only for ALTER statements with FOREIGEIN key

For example, if in your ddl after table definitions (create table statements) you have ALTER table statements like this:

.. code-block:: sql


   ALTER TABLE "material_attachments" ADD FOREIGN KEY ("material_id", "material_title") REFERENCES "materials" ("id", "title");

This statements will be parsed and information about them putted inside 'alter' key in table's dict.
For example, please check alter statement tests - **tests/test_alter_statements.py**

More examples & tests
^^^^^^^^^^^^^^^^^^^^^

You can find in **tests/** folder.

Dump result in json
^^^^^^^^^^^^^^^^^^^

To dump result in json use argument .run(dump=True)

You also can provide a path where you want to have a dumps with schema with argument .run(dump_path='folder_that_use_for_dumps/')

Raise error if DDL cannot be parsed by Parser
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default Parser does not raise the error if some statement cannot be parsed - and just skip & produce empty output.

To change this behavior you can pass 'silent=False' argumen to main parser class, like:

.. code-block::

   DDLParser(.., silent=False)


Normalize names
^^^^^^^^^^^^^^^

Use DDLParser(.., normalize_names=True)flag that change output of parser:
If flag is True (default 'False') then all identifiers will be returned without '[', '"' and other delimiters that used in different SQL dialects to separate custom names from reserved words & statements.
For example, if flag set 'True' and you pass this input:

CREATE TABLE [dbo].\ `TO_Requests <[Request_ID] [int] IDENTITY(1,1>`_ NOT NULL,
    [user_id] [int]

In output you will have names like 'dbo' and 'TO_Requests', not '[dbo]' and '[TO_Requests]'.

Supported Statements
--------------------


*
  CREATE [OR REPLACE] TABLE [ IF NOT EXISTS ] + columns definition, columns attributes: column name + type + type size(for example, varchar(255)), UNIQUE, PRIMARY KEY, DEFAULT, CHECK, NULL/NOT NULL, REFERENCES, ON DELETE, ON UPDATE,  NOT DEFERRABLE, DEFERRABLE INITIALLY, GENERATED ALWAYS, STORED, COLLATE

*
  STATEMENTS: PRIMARY KEY, CHECK, FOREIGN KEY in table definitions (in create table();)

*
  ALTER TABLE STATEMENTS: ADD CHECK (with CONSTRAINT), ADD FOREIGN KEY (with CONSTRAINT), ADD UNIQUE, ADD DEFAULT FOR, ALTER TABLE ONLY, ALTER TABLE IF EXISTS; ALTER .. PRIMARY KEY; ALTER .. USING INDEX TABLESPACE; ALTER .. ADD; ALTER .. MODIFY; ALTER .. ALTER COLUMN; etc

*
  PARTITION BY statement

*
  CREATE SEQUENCE with words: INCREMENT [BY], START [WITH], MINVALUE, MAXVALUE, CACHE

*
  CREATE TYPE statement:  AS TABLE, AS ENUM, AS OBJECT, INTERNALLENGTH, INPUT, OUTPUT

*
  LIKE statement (in this and only in this case to output will be added 'like' keyword with information about table from that we did like - 'like': {'schema': None, 'table_name': 'Old_Users'}).

*
  TABLESPACE statement

*
  COMMENT ON statement

*
  CREATE SCHEMA [IF NOT EXISTS] ... [AUTHORIZATION] ...

*
  CREATE DOMAIN [AS]

*
  CREATE [SMALLFILE | BIGFILE] [TEMPORARY] TABLESPACE statement

*
  CREATE DATABASE + Properties parsing

SparkSQL Dialect statements
^^^^^^^^^^^^^^^^^^^^^^^^^^^


* USING

HQL Dialect statements
^^^^^^^^^^^^^^^^^^^^^^


* PARTITIONED BY statement
* ROW FORMAT, ROW FORMAT SERDE
* WITH SERDEPROPERTIES ("input.regex" =  "..some regex..")
* STORED AS (AVRO, PARQUET, etc), STORED AS INPUTFORMAT, OUTPUTFORMAT
* COMMENT
* LOCATION
* FIELDS TERMINATED BY, LINES TERMINATED BY, COLLECTION ITEMS TERMINATED BY, MAP KEYS TERMINATED BY
* TBLPROPERTIES ('parquet.compression'='SNAPPY' & etc.)
* SKEWED BY
* CLUSTERED BY

MySQL
^^^^^


* ON UPDATE in column without reference

MSSQL
~~~~~


* CONSTRAINT [CLUSTERED]... PRIMARY KEY
* CONSTRAINT ... WITH statement
* PERIOD FOR SYSTEM_TIME in CREATE TABLE statement
* ON [PRIMARY] after CREATE TABLE statement (sample in test files test_mssql_specific.py)
* WITH statement for TABLE properties
* TEXTIMAGE_ON statement
* DEFAULT NEXT VALUE FOR in COLUMN DEFAULT

MSSQL / MySQL/ Oracle
^^^^^^^^^^^^^^^^^^^^^


* type IDENTITY statement
* FOREIGN KEY REFERENCES statement
* 'max' specifier in column size
* CONSTRAINT ... UNIQUE, CONSTRAINT ... CHECK, CONSTRAINT ... FOREIGN KEY, CONSTRAINT ... PRIMARY KEY
* CREATE CLUSTERED INDEX
* CREATE TABLE (...) ORGANIZATION INDEX

Oracle
^^^^^^


* ENCRYPT column property [+ NO SALT, SALT, USING]
* STORAGE column property

PotgreSQL
^^^^^^^^^


* INHERITS table statement - https://postgrespro.ru/docs/postgresql/14/ddl-inherit

AWS Redshift Dialect statements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* ENCODE column property
* SORTKEY, DISTSTYLE, DISTKEY, ENCODE table properties
*
  CREATE TEMP / TEMPORARY TABLE

*
  syntax like with LIKE statement:

  ``create temp table tempevent(like event);``

Snowflake Dialect statements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* CREATE .. CLONE statements for table, database and schema
* CREATE TABLE [or REPLACE] [ TRANSIENT | TEMPORARY ] .. CLUSTER BY ..
* CONSTRAINT .. [NOT] ENFORCED
* COMMENT = in CREATE TABLE & CREATE SCHEMA statements
* WITH MASKING POLICY
* WITH TAG, including multiple tags in the same statement.
* DATA_RETENTION_TIME_IN_DAYS
* MAX_DATA_EXTENSION_TIME_IN_DAYS
* CHANGE_TRACKING

BigQuery
^^^^^^^^


* OPTION in CREATE SCHEMA statement
* OPTION in CREATE TABLE statement
* OPTION in column definition statement

Parser settings
^^^^^^^^^^^^^^^

Logging
~~~~~~~


#. Logging to file

To get logging output to file you should provide to Parser 'log_file' argument with path or file name:

.. code-block:: console


       DDLParser(ddl, log_file='parser221.log').run(group_by_type=True)


#. Logging level

To set logging level you should provide argument 'log_level'

.. code-block:: console


       DDLParser(ddl, log_level=logging.INFO).run(group_by_type=True)

