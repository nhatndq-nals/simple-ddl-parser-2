from simple_ddl_parser import DDLParser


def test_several_indexes_types():
    ddl = """
    CREATE TABLE sqlserverlist (

    id INT IDENTITY (1,1) PRIMARY KEY, -- NOTE THE IDENTITY
    company_id BIGINT ,
    primary_id INT FOREIGN KEY REFERENCES Persons(PersonID), -- ADD THIS COLUMN FOR THE FOREIGN KEY
    age TINYINT NULL UNIQUE,
    days_active SMALLINT NOT NULL,
    user_origin_of_birth char(255),
    user_account VARCHAR(8000) NOT NULL,
    birth_date DATE NOT NULL,
    time_of_birth TIME(7),
    enrollment_date SMALLDATETIME,
    delete_date DATETIME NULL,
    create_date DATETIME2(7) NOT NULL,
    user_time_zone DATETIMEOFFSET(7),
    oder_date date DEFAULT GETDATE(), -- added to demonstrate sql sever Defaults
    country varchar(255) DEFAULT 'Sandnes', -- added to demonstrate sql sever Defaults
    active bit NULL,
    home_size GEOMETRY, -- Sql Server Defaults to Null
    user_photo IMAGE, -- Sql Server Defaults to Null
    --UNIQUE (id),
    CONSTRAINT UC_sqlserverlist_last_name UNIQUE (company_id,user_last_name),
    CONSTRAINT CHK_Person_Age_under CHECK (days_active<=18 AND user_city='New York'),
    FOREIGN KEY (id) REFERENCES Persons(PersonID),
    CONSTRAINT FK_Person_Age_under  FOREIGN KEY (id)REFERENCES Persons(PersonID)
    );

    CREATE INDEX i1 ON sqlserverlist (extra_funds);
    CREATE CLUSTERED INDEX i2 ON sqlserverlist  (delete_date,create_date); --- This line is commented
    CREATE UNIQUE INDEX i3 ON sqlserverlist (delete_date DESC, create_date ASC, ending_funds  DESC);
    CREATE INDEX test2_info_nulls_low ON sqlserverlist (info NULLS FIRST);
    CREATE INDEX test3_desc_index ON sqlserverlist (id DESC NULLS LAST);
    """

    result = DDLParser(ddl).run(group_by_type=True, output_mode="mssql")
    expected = {
        "comments": [
            " NOTE THE IDENTITY",
            " ADD THIS COLUMN FOR THE FOREIGN KEY",
            " added to demonstrate sql sever Defaults",
            " added to demonstrate sql sever Defaults",
            " Sql Server Defaults to Null",
            " Sql Server Defaults to Null",
            "- This line is commented",
        ],
        "sequences": [],
        "ddl_properties": [],
        "domains": [],
        "schemas": [],
        "tables": [
            {
                "alter": {},
                "checks": [
                    {
                        "constraint_name": "CHK_Person_Age_under",
                        "statement": "days_active<=18 AND user_city = 'New York'",
                    }
                ],
                "columns": [
                    {
                        "check": None,
                        "default": None,
                        "name": "id",
                        "nullable": False,
                        "references": {
                            "column": "PersonID",
                            "deferrable_initially": None,
                            "on_delete": None,
                            "on_update": None,
                            "schema": None,
                            "table": "Persons",
                        },
                        "size": None,
                        "identity": (1, 1),
                        "type": "INT",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "company_id",
                        "nullable": True,
                        "references": None,
                        "size": None,
                        "type": "BIGINT",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "primary_id",
                        "nullable": True,
                        "references": {
                            "column": "PersonID",
                            "deferrable_initially": None,
                            "on_delete": None,
                            "on_update": None,
                            "schema": None,
                            "table": "Persons",
                        },
                        "size": None,
                        "type": "INT",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "age",
                        "nullable": True,
                        "references": None,
                        "size": None,
                        "type": "TINYINT",
                        "unique": True,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "days_active",
                        "nullable": False,
                        "references": None,
                        "size": None,
                        "type": "SMALLINT",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "user_origin_of_birth",
                        "nullable": True,
                        "references": None,
                        "size": 255,
                        "type": "char",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "user_account",
                        "nullable": False,
                        "references": None,
                        "size": 8000,
                        "type": "VARCHAR",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "birth_date",
                        "nullable": False,
                        "references": None,
                        "size": None,
                        "type": "DATE",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "time_of_birth",
                        "nullable": True,
                        "references": None,
                        "size": 7,
                        "type": "TIME",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "enrollment_date",
                        "nullable": True,
                        "references": None,
                        "size": None,
                        "type": "SMALLDATETIME",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "delete_date",
                        "nullable": True,
                        "references": None,
                        "size": None,
                        "type": "DATETIME",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "create_date",
                        "nullable": False,
                        "references": None,
                        "size": 7,
                        "type": "DATETIME2",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "user_time_zone",
                        "nullable": True,
                        "references": None,
                        "size": 7,
                        "type": "DATETIMEOFFSET",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": "GETDATE()",
                        "name": "oder_date",
                        "nullable": True,
                        "references": None,
                        "size": None,
                        "type": "date",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": "'Sandnes'",
                        "name": "country",
                        "nullable": True,
                        "references": None,
                        "size": 255,
                        "type": "varchar",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "active",
                        "nullable": True,
                        "references": None,
                        "size": None,
                        "type": "bit",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "home_size",
                        "nullable": True,
                        "references": None,
                        "size": None,
                        "type": "GEOMETRY",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "user_photo",
                        "nullable": True,
                        "references": None,
                        "size": None,
                        "type": "IMAGE",
                        "unique": False,
                    },
                ],
                "constraints": {
                    "checks": [
                        {
                            "constraint_name": "CHK_Person_Age_under",
                            "statement": "days_active<=18 AND "
                            "user_city = 'New York'",
                        }
                    ],
                    "references": [
                        {
                            "columns": ["PersonID"],
                            "constraint_name": "FK_Person_Age_under",
                            "deferrable_initially": None,
                            "name": "id",
                            "on_delete": None,
                            "on_update": None,
                            "schema": None,
                            "table": "Persons",
                        }
                    ],
                    "uniques": [
                        {
                            "columns": ["company_id", "user_last_name"],
                            "constraint_name": "UC_sqlserverlist_last_name",
                        }
                    ],
                },
                "index": [
                    {
                        "clustered": False,
                        "columns": ["extra_funds"],
                        "detailed_columns": [
                            {"name": "extra_funds", "nulls": "LAST", "order": "ASC"}
                        ],
                        "index_name": "i1",
                        "index_type": None,
                        "unique": False,
                    },
                    {
                        "clustered": True,
                        "columns": ["delete_date", "create_date"],
                        "detailed_columns": [
                            {"name": "delete_date", "nulls": "LAST", "order": "ASC"},
                            {"name": "create_date", "nulls": "LAST", "order": "ASC"},
                        ],
                        "index_name": "i2",
                        "index_type": None,
                        "unique": False,
                    },
                    {
                        "clustered": False,
                        "columns": ["delete_date", "create_date", "ending_funds"],
                        "detailed_columns": [
                            {"name": "delete_date", "nulls": "LAST", "order": "DESC"},
                            {"name": "create_date", "nulls": "LAST", "order": "ASC"},
                            {"name": "ending_funds", "nulls": "LAST", "order": "DESC"},
                        ],
                        "index_name": "i3",
                        "index_type": None,
                        "unique": True,
                    },
                    {
                        "clustered": False,
                        "columns": ["info"],
                        "detailed_columns": [
                            {"name": "info", "nulls": "FIRST", "order": "ASC"}
                        ],
                        "index_name": "test2_info_nulls_low",
                        "index_type": None,
                        "unique": False,
                    },
                    {
                        "clustered": False,
                        "columns": ["id"],
                        "detailed_columns": [
                            {"name": "id", "nulls": "LAST", "order": "DESC"}
                        ],
                        "index_name": "test3_desc_index",
                        "index_type": None,
                        "unique": False,
                    },
                ],
                "partitioned_by": [],
                "primary_key": ["id"],
                "schema": None,
                "table_name": "sqlserverlist",
                "tablespace": None,
            }
        ],
        "types": [],
    }
    assert result == expected


def test_clustered_index():
    ddl = """
   CREATE TABLE sqlserverlist (

   id INT IDENTITY (1,1) PRIMARY KEY, -- NOTE
   company_id BIGINT ,
   primary_id INT FOREIGN KEY REFERENCES Persons(PersonID), -- ADD THIS COLUMN FOR THE FOREIGN KEY
   age TINYINT NULL UNIQUE,
   days_active SMALLINT NOT NULL,
   user_origin_of_birth char(255),
   user_account VARCHAR(8000) NOT NULL,
   birth_date DATE NOT NULL,
   time_of_birth TIME(7),
   enrollment_date SMALLDATETIME,
   delete_date DATETIME NULL,
   create_date DATETIME2(7) NOT NULL,
   user_time_zone DATETIMEOFFSET(7),
   oder_date date DEFAULT GETDATE(), -- added to demonstrate sql sever Defaults
   country varchar(255) DEFAULT 'Sandnes', -- added to demonstrate sql sever Defaults
   active bit NULL,
   home_size GEOMETRY, -- Sql Server Defaults to Null
   user_photo IMAGE, -- Sql Server Defaults to Null
   --UNIQUE (id),
   CONSTRAINT UC_sqlserverlist_last_name UNIQUE (company_id,user_last_name),
   CONSTRAINT CHK_Person_Age_under CHECK (days_active<=18 AND user_city='New York'),
   FOREIGN KEY (id) REFERENCES Persons(PersonID),
   CONSTRAINT FK_Person_Age_under  FOREIGN KEY (id)REFERENCES Persons(PersonID)
   );

   CREATE INDEX i1 ON sqlserverlist (extra_funds);
   CREATE CLUSTERED INDEX i2 ON sqlserverlist  (delete_date,create_date); --- This
   --CREATE UNIQUE INDEX i1 ON t1 (delete_date DESC, create_date ASC, ending_funds  DESC); --- This

   """

    result = DDLParser(ddl).run(group_by_type=True, output_mode="mssql")
    expected = {
        "comments": [
            " NOTE",
            " ADD THIS COLUMN FOR THE FOREIGN KEY",
            " added to demonstrate sql sever Defaults",
            " added to demonstrate sql sever Defaults",
            " Sql Server Defaults to Null",
            " Sql Server Defaults to Null",
            "- This",
        ],
        "sequences": [],
        "domains": [],
        "schemas": [],
        "tables": [
            {
                "alter": {},
                "checks": [
                    {
                        "constraint_name": "CHK_Person_Age_under",
                        "statement": "days_active<=18 AND user_city = 'New York'",
                    }
                ],
                "columns": [
                    {
                        "check": None,
                        "default": None,
                        "name": "id",
                        "nullable": False,
                        "references": {
                            "column": "PersonID",
                            "deferrable_initially": None,
                            "on_delete": None,
                            "on_update": None,
                            "schema": None,
                            "table": "Persons",
                        },
                        "size": None,
                        "identity": (1, 1),
                        "type": "INT",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "company_id",
                        "nullable": True,
                        "references": None,
                        "size": None,
                        "type": "BIGINT",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "primary_id",
                        "nullable": True,
                        "references": {
                            "column": "PersonID",
                            "deferrable_initially": None,
                            "on_delete": None,
                            "on_update": None,
                            "schema": None,
                            "table": "Persons",
                        },
                        "size": None,
                        "type": "INT",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "age",
                        "nullable": True,
                        "references": None,
                        "size": None,
                        "type": "TINYINT",
                        "unique": True,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "days_active",
                        "nullable": False,
                        "references": None,
                        "size": None,
                        "type": "SMALLINT",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "user_origin_of_birth",
                        "nullable": True,
                        "references": None,
                        "size": 255,
                        "type": "char",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "user_account",
                        "nullable": False,
                        "references": None,
                        "size": 8000,
                        "type": "VARCHAR",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "birth_date",
                        "nullable": False,
                        "references": None,
                        "size": None,
                        "type": "DATE",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "time_of_birth",
                        "nullable": True,
                        "references": None,
                        "size": 7,
                        "type": "TIME",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "enrollment_date",
                        "nullable": True,
                        "references": None,
                        "size": None,
                        "type": "SMALLDATETIME",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "delete_date",
                        "nullable": True,
                        "references": None,
                        "size": None,
                        "type": "DATETIME",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "create_date",
                        "nullable": False,
                        "references": None,
                        "size": 7,
                        "type": "DATETIME2",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "user_time_zone",
                        "nullable": True,
                        "references": None,
                        "size": 7,
                        "type": "DATETIMEOFFSET",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": "GETDATE()",
                        "name": "oder_date",
                        "nullable": True,
                        "references": None,
                        "size": None,
                        "type": "date",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": "'Sandnes'",
                        "name": "country",
                        "nullable": True,
                        "references": None,
                        "size": 255,
                        "type": "varchar",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "active",
                        "nullable": True,
                        "references": None,
                        "size": None,
                        "type": "bit",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "home_size",
                        "nullable": True,
                        "references": None,
                        "size": None,
                        "type": "GEOMETRY",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "user_photo",
                        "nullable": True,
                        "references": None,
                        "size": None,
                        "type": "IMAGE",
                        "unique": False,
                    },
                ],
                "constraints": {
                    "checks": [
                        {
                            "constraint_name": "CHK_Person_Age_under",
                            "statement": "days_active<=18 AND "
                            "user_city = 'New York'",
                        }
                    ],
                    "references": [
                        {
                            "columns": ["PersonID"],
                            "constraint_name": "FK_Person_Age_under",
                            "deferrable_initially": None,
                            "name": "id",
                            "on_delete": None,
                            "on_update": None,
                            "schema": None,
                            "table": "Persons",
                        }
                    ],
                    "uniques": [
                        {
                            "columns": ["company_id", "user_last_name"],
                            "constraint_name": "UC_sqlserverlist_last_name",
                        }
                    ],
                },
                "index": [
                    {
                        "clustered": False,
                        "columns": ["extra_funds"],
                        "detailed_columns": [
                            {"name": "extra_funds", "nulls": "LAST", "order": "ASC"}
                        ],
                        "index_name": "i1",
                        "index_type": None,
                        "unique": False,
                    },
                    {
                        "clustered": True,
                        "columns": ["delete_date", "create_date"],
                        "detailed_columns": [
                            {"name": "delete_date", "nulls": "LAST", "order": "ASC"},
                            {"name": "create_date", "nulls": "LAST", "order": "ASC"},
                        ],
                        "index_name": "i2",
                        "index_type": None,
                        "unique": False,
                    },
                ],
                "partitioned_by": [],
                "primary_key": ["id"],
                "schema": None,
                "table_name": "sqlserverlist",
                "tablespace": None,
            }
        ],
        "types": [],
        "ddl_properties": [],
    }
    assert result == expected


def test_indexes_in_table_wint_no_schema():
    parse_results = DDLParser(
        """
    drop table if exists pipeline ;
    CREATE table pipeline (
            job_id               decimal(21) not null
        ,pipeline_id          varchar(100) not null default 'none'
        ,start_time           timestamp not null default now()
        ,end_time             timestamp not null default now()
        ,exitcode             smallint not null default 0
        ,status               varchar(25) not null
        ,elapse_time          float not null default 0
        ,message              varchar(1000) not null default 'none'
        ) ;
    create unique index pipeline_pk on pipeline (job_id) ;
    create index pipeline_ix2 on pipeline (pipeline_id, elapse_time, status) ;
    """
    ).run()
    expected = [
        {
            "columns": [
                {
                    "name": "job_id",
                    "type": "decimal",
                    "size": 21,
                    "references": None,
                    "unique": False,
                    "nullable": False,
                    "default": None,
                    "check": None,
                },
                {
                    "name": "pipeline_id",
                    "type": "varchar",
                    "size": 100,
                    "references": None,
                    "unique": False,
                    "nullable": False,
                    "default": "'none'",
                    "check": None,
                },
                {
                    "name": "start_time",
                    "type": "timestamp",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": False,
                    "default": "now()",
                    "check": None,
                },
                {
                    "name": "end_time",
                    "type": "timestamp",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": False,
                    "default": "now()",
                    "check": None,
                },
                {
                    "name": "exitcode",
                    "type": "smallint",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": False,
                    "default": 0,
                    "check": None,
                },
                {
                    "name": "status",
                    "type": "varchar",
                    "size": 25,
                    "references": None,
                    "unique": False,
                    "nullable": False,
                    "default": None,
                    "check": None,
                },
                {
                    "name": "elapse_time",
                    "type": "float",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": False,
                    "default": 0,
                    "check": None,
                },
                {
                    "name": "message",
                    "type": "varchar",
                    "size": 1000,
                    "references": None,
                    "unique": False,
                    "nullable": False,
                    "default": "'none'",
                    "check": None,
                },
            ],
            "primary_key": [],
            "alter": {},
            "checks": [],
            "index": [
                {
                    "index_name": "pipeline_pk",
                    "index_type": None,
                    "unique": True,
                    "columns": ["job_id"],
                    "detailed_columns": [
                        {"name": "job_id", "nulls": "LAST", "order": "ASC"}
                    ],
                },
                {
                    "index_name": "pipeline_ix2",
                    "index_type": None,
                    "unique": False,
                    "columns": ["pipeline_id", "elapse_time", "status"],
                    "detailed_columns": [
                        {"name": "pipeline_id", "nulls": "LAST", "order": "ASC"},
                        {"name": "elapse_time", "nulls": "LAST", "order": "ASC"},
                        {"name": "status", "nulls": "LAST", "order": "ASC"},
                    ],
                },
            ],
            "table_name": "pipeline",
            "tablespace": None,
            "schema": None,
            "partitioned_by": [],
        }
    ]
    assert expected == parse_results


def test_indexes_in_table():
    parse_results = DDLParser(
        """
    drop table if exists dev.pipeline ;
    CREATE table dev.pipeline (
            job_id               decimal(21) not null
        ,pipeline_id          varchar(100) not null default 'none'
        ,start_time           timestamp not null default now()
        ,end_time             timestamp not null default now()
        ,exitcode             smallint not null default 0
        ,status               varchar(25) not null
        ,elapse_time          float not null default 0
        ,message              varchar(1000) not null default 'none'
        ) ;
    create unique index pipeline_pk on dev.pipeline (job_id) ;
    create index pipeline_ix2 on dev.pipeline (pipeline_id, elapse_time, status) ;
    create index pipeline_ix3 ON dev.pipeline USING btree (pipeline_id);
    """
    ).run()
    expected = [
        {
            "columns": [
                {
                    "name": "job_id",
                    "type": "decimal",
                    "size": 21,
                    "references": None,
                    "unique": False,
                    "nullable": False,
                    "default": None,
                    "check": None,
                },
                {
                    "name": "pipeline_id",
                    "type": "varchar",
                    "size": 100,
                    "references": None,
                    "unique": False,
                    "nullable": False,
                    "default": "'none'",
                    "check": None,
                },
                {
                    "name": "start_time",
                    "type": "timestamp",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": False,
                    "default": "now()",
                    "check": None,
                },
                {
                    "name": "end_time",
                    "type": "timestamp",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": False,
                    "default": "now()",
                    "check": None,
                },
                {
                    "name": "exitcode",
                    "type": "smallint",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": False,
                    "default": 0,
                    "check": None,
                },
                {
                    "name": "status",
                    "type": "varchar",
                    "size": 25,
                    "references": None,
                    "unique": False,
                    "nullable": False,
                    "default": None,
                    "check": None,
                },
                {
                    "name": "elapse_time",
                    "type": "float",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": False,
                    "default": 0,
                    "check": None,
                },
                {
                    "name": "message",
                    "type": "varchar",
                    "size": 1000,
                    "references": None,
                    "unique": False,
                    "nullable": False,
                    "default": "'none'",
                    "check": None,
                },
            ],
            "primary_key": [],
            "alter": {},
            "checks": [],
            "index": [
                {
                    "index_name": "pipeline_pk",
                    "index_type": None,
                    "unique": True,
                    "detailed_columns": [
                        {"name": "job_id", "nulls": "LAST", "order": "ASC"}
                    ],
                    "columns": ["job_id"],
                },
                {
                    "index_name": "pipeline_ix2",
                    "index_type": None,
                    "unique": False,
                    "columns": ["pipeline_id", "elapse_time", "status"],
                    "detailed_columns": [
                        {"name": "pipeline_id", "nulls": "LAST", "order": "ASC"},
                        {"name": "elapse_time", "nulls": "LAST", "order": "ASC"},
                        {"name": "status", "nulls": "LAST", "order": "ASC"},
                    ],
                },
                {
                    "columns": ["pipeline_id"],
                    "detailed_columns": [
                        {"name": "pipeline_id", "nulls": "LAST", "order": "ASC"}
                    ],
                    "index_name": "pipeline_ix3",
                    "index_type": "btree",
                    "unique": False,
                },
            ],
            "table_name": "pipeline",
            "tablespace": None,
            "schema": "dev",
            "partitioned_by": [],
        }
    ]
    assert expected == parse_results


def test_index_as_key():
    """
    Tests that CREATE TABLE with KEY statements properly create the index
    for that table.
    """
    ddl = """
    /*!50503 SET character_set_client = utf8mb4 */;
    CREATE TABLE "test_with_key" (
    "criteria_id" int unsigned NOT NULL,
    "super_category" tinyint unsigned NOT NULL COMMENT 'Da category',
    "currency_id" int unsigned DEFAULT '1',

    PRIMARY KEY ("criteria_id","super_category"),
    KEY "currency_ibfk" ("currency_id"),
    CONSTRAINT "currency_ibfk" FOREIGN KEY ("currency_id") REFERENCES "currency" ("id"),
    CONSTRAINT "criteria_ibfk" FOREIGN KEY ("criteria_id") REFERENCES "criteria" ("id")
);
    /*!40101 SET character_set_client = @saved_cs_client */;
    """
    result = DDLParser(ddl).run(group_by_type=True, output_mode="mysql")
    expected = {
        "tables": [
            {
                "columns": [
                    {
                        "name": '"criteria_id"',
                        "type": "int unsigned",
                        "size": None,
                        "references": None,
                        "unique": False,
                        "nullable": False,
                        "default": None,
                        "check": None,
                    },
                    {
                        "name": '"super_category"',
                        "type": "tinyint unsigned",
                        "size": None,
                        "references": None,
                        "unique": False,
                        "nullable": False,
                        "default": None,
                        "check": None,
                        "comment": "'Da category'",
                    },
                    {
                        "name": '"currency_id"',
                        "type": "int unsigned",
                        "size": None,
                        "references": None,
                        "unique": False,
                        "nullable": True,
                        "default": "'1'",
                        "check": None,
                    },
                ],
                "primary_key": ['"criteria_id"', '"super_category"'],
                "alter": {},
                "checks": [],
                "index": [
                    {
                        "clustered": False,
                        "columns": ['"currency_id"'],
                        "detailed_columns": [
                            {"name": '"currency_id"', "nulls": "LAST", "order": "ASC"}
                        ],
                        "index_name": '"currency_ibfk"',
                        "unique": False,
                    },
                ],
                "partitioned_by": [],
                "tablespace": None,
                "constraints": {
                    "references": [
                        {
                            "table": '"currency"',
                            "columns": ['"id"'],
                            "schema": None,
                            "name": '"currency_id"',
                            "on_delete": None,
                            "on_update": None,
                            "deferrable_initially": None,
                            "constraint_name": '"currency_ibfk"',
                        },
                        {
                            "table": '"criteria"',
                            "columns": ['"id"'],
                            "schema": None,
                            "name": '"criteria_id"',
                            "on_delete": None,
                            "on_update": None,
                            "deferrable_initially": None,
                            "constraint_name": '"criteria_ibfk"',
                        },
                    ]
                },
                "schema": None,
                "table_name": '"test_with_key"',
            }
        ],
        "types": [],
        "sequences": [],
        "domains": [],
        "schemas": [],
        "ddl_properties": [],
        "comments": [
            "!50503 SET character_set_client = utf8mb4 */;",
            "!40101 SET character_set_client = @saved_cs_client */;",
        ],
    }
    assert result == expected
