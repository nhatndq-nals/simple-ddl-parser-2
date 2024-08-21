from simple_ddl_parser_2 import DDLParser


def test_unique_statement_in_columns():
    ddl = """

    CREATE TABLE "steps" (
    "id" int UNIQUE,
    "title" varchar unique,
    "description" varchar(160),
    "created_at" timestamp,
    "updated_at" timestamp
    );
    """
    expected = [
        {
            "columns": [
                {
                    "name": '"id"',
                    "type": "int",
                    "size": None,
                    "references": None,
                    "unique": True,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
                {
                    "name": '"title"',
                    "type": "varchar",
                    "size": None,
                    "references": None,
                    "unique": True,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
                {
                    "name": '"description"',
                    "type": "varchar",
                    "size": 160,
                    "references": None,
                    "unique": False,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
                {
                    "name": '"created_at"',
                    "type": "timestamp",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
                {
                    "name": '"updated_at"',
                    "type": "timestamp",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
            ],
            "primary_key": [],
            "index": [],
            "alter": {},
            "checks": [],
            "table_name": '"steps"',
            "tablespace": None,
            "schema": None,
            "partitioned_by": [],
        }
    ]
    assert DDLParser(ddl).run() == expected


def test_unique_statement_separate_line():
    ddl = """

    CREATE TABLE "steps" (
    "id" int,
    "title" varchar,
    "description" varchar(160),
    "created_at" timestamp,
    "updated_at" timestamp,
    unique ("id", "title")
    );
    """
    expected = [
        {
            "columns": [
                {
                    "name": '"id"',
                    "type": "int",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
                {
                    "name": '"title"',
                    "type": "varchar",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
                {
                    "name": '"description"',
                    "type": "varchar",
                    "size": 160,
                    "references": None,
                    "unique": False,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
                {
                    "name": '"created_at"',
                    "type": "timestamp",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
                {
                    "name": '"updated_at"',
                    "type": "timestamp",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
            ],
            "primary_key": [],
            "index": [],
            "alter": {},
            "checks": [],
            "constraints": {
                "uniques": [
                    {
                        "columns": ['"id"', '"title"'],
                        "constraint_name": 'UC_"id"_"title"',
                    }
                ],
            },
            "table_name": '"steps"',
            "tablespace": None,
            "schema": None,
            "partitioned_by": [],
        }
    ]

    assert DDLParser(ddl).run() == expected


def test_unique_key_statement():
    """
    Verifies that UNIQUE KEY statements are properly parsed.  If they are simple,
    one column keys, then add unique=True to the column, if they are compound
    keys, then create a constraint
    """
    ddl = """

    CREATE TABLE "steps" (
    "id" int,
    "title" varchar,
    "description" varchar(160),
    "created_at" timestamp,
    "updated_at" timestamp,
    UNIQUE KEY "id_uk" ("id"),
    UNIQUE KEY "title_uk" ("title"),
    UNIQUE KEY "compound_uk" ("created_at", "updated_at")
    );
    """
    expected = [
        {
            "columns": [
                {
                    "name": '"id"',
                    "type": "int",
                    "size": None,
                    "references": None,
                    "unique": True,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
                {
                    "name": '"title"',
                    "type": "varchar",
                    "size": None,
                    "references": None,
                    "unique": True,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
                {
                    "name": '"description"',
                    "type": "varchar",
                    "size": 160,
                    "references": None,
                    "unique": False,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
                {
                    "name": '"created_at"',
                    "type": "timestamp",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
                {
                    "name": '"updated_at"',
                    "type": "timestamp",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
            ],
            "primary_key": [],
            "index": [],
            "alter": {},
            "checks": [],
            "constraints": {
                "uniques": [
                    {
                        "columns": ['"created_at"', '"updated_at"'],
                        "constraint_name": '"compound_uk"',
                    }
                ],
            },
            "table_name": '"steps"',
            "tablespace": None,
            "schema": None,
            "partitioned_by": [],
        }
    ]
    assert DDLParser(ddl).run() == expected


def test_unique_alter_sql():
    ddl = """
    CREATE TABLE "participations"(
        "user_id" BIGINT NOT NULL,
        "project_id" BIGINT NOT NULL,
        "team_id" BIGINT NOT NULL,
    );
    ALTER TABLE
        "participations" ADD CONSTRAINT "participations_team_id_user_id_unique" UNIQUE("team_id", "user_id");
    """

    result = DDLParser(ddl).run()
    expected = [
        {
            "alter": {
                "uniques": [
                    {
                        "columns": ['"team_id"', '"user_id"'],
                        "constraint_name": '"participations_team_id_user_id_unique"',
                    }
                ]
            },
            "checks": [],
            "columns": [
                {
                    "check": None,
                    "default": None,
                    "name": '"user_id"',
                    "nullable": False,
                    "references": None,
                    "size": None,
                    "type": "BIGINT",
                    "unique": False,
                },
                {
                    "check": None,
                    "default": None,
                    "name": '"project_id"',
                    "nullable": False,
                    "references": None,
                    "size": None,
                    "type": "BIGINT",
                    "unique": False,
                },
                {
                    "check": None,
                    "default": None,
                    "name": '"team_id"',
                    "nullable": False,
                    "references": None,
                    "size": None,
                    "type": "BIGINT",
                    "unique": False,
                },
            ],
            "index": [],
            "partitioned_by": [],
            "primary_key": [],
            "schema": None,
            "table_name": '"participations"',
            "tablespace": None,
        }
    ]
    assert expected == result


def test_unique_key():
    ddl = """
    CREATE TABLE `posts`(
        `integer_column__unique` INT NOT NULL AUTO_INCREMENT UNIQUE,
        `integer_column__unique_key` INT NOT NULL AUTO_INCREMENT UNIQUE KEY
    );
    """

    result = DDLParser(ddl).run()
    expected = [
        {
            "alter": {},
            "checks": [],
            "columns": [
                {
                    "autoincrement": True,
                    "check": None,
                    "default": None,
                    "name": "`integer_column__unique`",
                    "nullable": False,
                    "references": None,
                    "size": None,
                    "type": "INT",
                    "unique": True,
                },
                {
                    "autoincrement": True,
                    "check": None,
                    "default": None,
                    "name": "`integer_column__unique_key`",
                    "nullable": False,
                    "references": None,
                    "size": None,
                    "type": "INT",
                    "unique": True,
                },
            ],
            "index": [],
            "partitioned_by": [],
            "primary_key": [],
            "schema": None,
            "table_name": "`posts`",
            "tablespace": None,
        }
    ]
    assert expected == result
