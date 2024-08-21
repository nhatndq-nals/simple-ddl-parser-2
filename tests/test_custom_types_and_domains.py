from simple_ddl_parser_2 import DDLParser


def test_custom_enum():
    ddl = """
    CREATE TYPE "schema--notification"."ContentType" AS
    ENUM ('TEXT','MARKDOWN','HTML');
    CREATE TABLE "schema--notification"."notification" (
        content_type "schema--notification"."ContentType"
    );
    """

    result = DDLParser(ddl).run()
    expected = [
        {
            "base_type": "ENUM",
            "properties": {"values": ["'TEXT'", "'MARKDOWN'", "'HTML'"]},
            "schema": '"schema--notification"',
            "type_name": '"ContentType"',
        },
        {
            "alter": {},
            "checks": [],
            "columns": [
                {
                    "check": None,
                    "default": None,
                    "name": "content_type",
                    "nullable": True,
                    "references": None,
                    "size": None,
                    "type": '"schema--notification"."ContentType"',
                    "unique": False,
                }
            ],
            "index": [],
            "partitioned_by": [],
            "primary_key": [],
            "schema": '"schema--notification"',
            "table_name": '"notification"',
            "tablespace": None,
        },
    ]
    assert expected == result


def test_custom_enum_wihtout_schema():
    ddl = """
    CREATE TYPE "ContentType" AS
    ENUM ('TEXT','MARKDOWN','HTML');
    CREATE TABLE "schema--notification"."notification" (
        content_type "ContentType"
    );
    """

    result = DDLParser(ddl).run()
    expected = [
        {
            "base_type": "ENUM",
            "properties": {"values": ["'TEXT'", "'MARKDOWN'", "'HTML'"]},
            "schema": None,
            "type_name": '"ContentType"',
        },
        {
            "alter": {},
            "checks": [],
            "columns": [
                {
                    "check": None,
                    "default": None,
                    "name": "content_type",
                    "nullable": True,
                    "references": None,
                    "size": None,
                    "type": '"ContentType"',
                    "unique": False,
                }
            ],
            "index": [],
            "partitioned_by": [],
            "primary_key": [],
            "schema": '"schema--notification"',
            "table_name": '"notification"',
            "tablespace": None,
        },
    ]
    assert expected == result


def test_create_type_as_object():
    ddl = """
    CREATE OR REPLACE TYPE addr_obj_typ AS OBJECT (
        street          VARCHAR2(30),
        city            VARCHAR2(20),
        state           CHAR(2),
        zip             NUMBER(5)
    );
    """

    result = DDLParser(ddl).run(group_by_type=True)
    expected = {
        "sequences": [],
        "ddl_properties": [],
        "domains": [],
        "schemas": [],
        "tables": [],
        "types": [
            {
                "base_type": "OBJECT",
                "properties": {
                    "attributes": [
                        {"name": "street", "size": 30, "type": "VARCHAR2"},
                        {"name": "city", "size": 20, "type": "VARCHAR2"},
                        {"name": "state", "size": 2, "type": "CHAR"},
                        {"name": "zip", "size": 5, "type": "NUMBER"},
                    ]
                },
                "schema": None,
                "type_name": "addr_obj_typ",
            }
        ],
    }
    assert expected == result


def test_create_type_with_input_properties():
    ddl = """
    CREATE TYPE box (
        INTERNALLENGTH = 16,
        INPUT = my_box_in_function,
        OUTPUT = my_box_out_function
    );
    """

    result = DDLParser(ddl).run(group_by_type=True)

    expected = {
        "sequences": [],
        "ddl_properties": [],
        "domains": [],
        "schemas": [],
        "tables": [],
        "types": [
            {
                "base_type": None,
                "properties": {
                    "INPUT": "my_box_in_function",
                    "INTERNALLENGTH": "16",
                    "OUTPUT": "my_box_out_function",
                },
                "schema": None,
                "type_name": "box",
            }
        ],
    }

    assert expected == result


def test_as_table():
    ddl = """
    CREATE TYPE dbo.T_LCT_SLIPS AS TABLE (
    hashKY varbinary(48),
    numContratoGF bigint
    );
    """
    result = DDLParser(ddl).run(group_by_type=True)
    expected = {
        "ddl_properties": [],
        "domains": [],
        "schemas": [],
        "sequences": [],
        "tables": [],
        "types": [
            {
                "base_type": None,
                "properties": {
                    "columns": [
                        {
                            "check": None,
                            "default": None,
                            "name": "hashKY",
                            "nullable": True,
                            "primary_key": False,
                            "references": None,
                            "size": 48,
                            "type": "varbinary",
                            "unique": False,
                        },
                        {
                            "check": None,
                            "default": None,
                            "name": "numContratoGF",
                            "nullable": True,
                            "primary_key": False,
                            "references": None,
                            "size": None,
                            "type": "bigint",
                            "unique": False,
                        },
                    ]
                },
                "schema": "dbo",
                "type_name": "T_LCT_SLIPS",
            }
        ],
    }
    assert result == expected
