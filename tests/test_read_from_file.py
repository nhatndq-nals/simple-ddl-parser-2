import os

from simple_ddl_parser_2 import parse_from_file


def test_parse_from_file_one_table():
    expected = [
        {
            "columns": [
                {
                    "name": '"id"',
                    "type": "SERIAL",
                    "size": None,
                    "nullable": False,
                    "default": None,
                    "check": None,
                    "unique": False,
                    "references": None,
                },
                {
                    "name": '"name"',
                    "type": "varchar",
                    "size": 160,
                    "nullable": True,
                    "default": None,
                    "check": None,
                    "unique": False,
                    "references": None,
                },
                {
                    "name": '"created_at"',
                    "type": "timestamp",
                    "size": None,
                    "nullable": True,
                    "default": None,
                    "check": None,
                    "unique": False,
                    "references": None,
                },
                {
                    "name": '"updated_at"',
                    "type": "timestamp",
                    "size": None,
                    "nullable": True,
                    "default": None,
                    "check": None,
                    "unique": False,
                    "references": None,
                },
                {
                    "name": '"country_code"',
                    "type": "int",
                    "size": None,
                    "nullable": True,
                    "default": None,
                    "check": None,
                    "unique": False,
                    "references": None,
                },
                {
                    "name": '"default_language"',
                    "type": "int",
                    "size": None,
                    "nullable": True,
                    "default": None,
                    "check": None,
                    "unique": False,
                    "references": None,
                },
            ],
            "primary_key": ['"id"'],
            "index": [],
            "table_name": '"users"',
            "tablespace": None,
            "schema": None,
            "partitioned_by": [],
            "alter": {},
            "checks": [],
        }
    ]
    current_path = os.path.dirname(os.path.abspath(__file__))
    assert expected == parse_from_file(
        os.path.join(current_path, "sql", "test_one_table.sql")
    )


def test_parse_from_file_generated_by_default():
    expected = [
        {
            "alter": {},
            "checks": [],
            "columns": [
                {
                    "check": None,
                    "default": None,
                    "generated": {
                        "always": True,
                        "as": "IDENTITY(INCREMENT BY 1 MINVALUE 1 "
                        "MAXVALUE 9223372036854775807 START 1 CACHE "
                        "1 NO CYCLE)",
                        "stored": False,
                    },
                    "name": '"id"',
                    "nullable": False,
                    "references": None,
                    "size": None,
                    "type": "int8",
                    "unique": False,
                },
                {
                    "check": None,
                    "default": None,
                    "name": '"name"',
                    "nullable": False,
                    "references": None,
                    "size": 255,
                    "type": "varchar",
                    "unique": False,
                },
                {
                    "check": None,
                    "default": None,
                    "name": '"description"',
                    "nullable": True,
                    "references": None,
                    "size": None,
                    "type": "varchar",
                    "unique": False,
                },
                {
                    "check": None,
                    "default": None,
                    "name": '"created_at"',
                    "nullable": True,
                    "references": None,
                    "size": None,
                    "type": "timestamp",
                    "unique": False,
                },
                {
                    "check": None,
                    "default": None,
                    "name": '"updated_at"',
                    "nullable": True,
                    "references": None,
                    "size": None,
                    "type": "timestamp",
                    "unique": False,
                },
            ],
            "index": [],
            "partitioned_by": [],
            "primary_key": [],
            "schema": None,
            "table_name": '"city_new"',
            "tablespace": None,
        },
        {
            "alter": {},
            "checks": [
                {"constraint_name": "authority_order_check", "statement": "order >= 0"}
            ],
            "columns": [
                {
                    "check": None,
                    "default": None,
                    "name": '"id"',
                    "nullable": False,
                    "references": None,
                    "size": None,
                    "type": "bigserial",
                    "unique": False,
                },
                {
                    "check": None,
                    "default": None,
                    "name": '"created_at"',
                    "nullable": False,
                    "references": None,
                    "size": None,
                    "type": "timestamptz",
                    "unique": False,
                },
                {
                    "check": None,
                    "default": None,
                    "name": '"updated_at"',
                    "nullable": True,
                    "references": None,
                    "size": None,
                    "type": "timestamptz",
                    "unique": False,
                },
                {
                    "check": None,
                    "default": None,
                    "name": '"app_div"',
                    "nullable": False,
                    "references": None,
                    "size": None,
                    "type": "int4",
                    "unique": False,
                },
                {
                    "check": None,
                    "default": None,
                    "name": '"name"',
                    "nullable": False,
                    "references": None,
                    "size": 50,
                    "type": "varchar",
                    "unique": False,
                },
                {
                    "check": None,
                    "default": None,
                    "name": '"key"',
                    "nullable": False,
                    "references": None,
                    "size": 50,
                    "type": "varchar",
                    "unique": False,
                },
                {
                    "check": None,
                    "default": None,
                    "name": '"order"',
                    "nullable": False,
                    "references": None,
                    "size": None,
                    "type": "int4",
                    "unique": False,
                },
            ],
            "constraints": {
                "checks": [
                    {
                        "constraint_name": "authority_order_check",
                        "statement": "order >= 0",
                    }
                ],
                "primary_keys": [
                    {"columns": ['"id"'], "constraint_name": "authority_pkey"}
                ],
            },
            "index": [],
            "partitioned_by": [],
            "primary_key": ['"id"'],
            "schema": "public",
            "table_name": "authority",
            "tablespace": None,
        },
    ]
    current_path = os.path.dirname(os.path.abspath(__file__))

    assert expected == parse_from_file(
        os.path.join(current_path, "sql", "test_generated_by_default.sql")
    )


def test_parse_from_file_two_statements():
    expected = [
        {
            "columns": [
                {
                    "name": '"id"',
                    "type": "SERIAL",
                    "size": None,
                    "nullable": False,
                    "default": None,
                    "check": None,
                    "unique": False,
                    "references": None,
                },
                {
                    "name": '"name"',
                    "type": "varchar",
                    "size": None,
                    "nullable": True,
                    "default": None,
                    "check": None,
                    "unique": False,
                    "references": None,
                },
                {
                    "name": '"created_at"',
                    "type": "timestamp",
                    "size": None,
                    "nullable": True,
                    "default": None,
                    "check": None,
                    "unique": False,
                    "references": None,
                },
                {
                    "name": '"updated_at"',
                    "type": "timestamp",
                    "size": None,
                    "nullable": True,
                    "default": None,
                    "check": None,
                    "unique": False,
                    "references": None,
                },
                {
                    "name": '"country_code"',
                    "type": "int",
                    "size": None,
                    "nullable": True,
                    "default": None,
                    "check": None,
                    "unique": False,
                    "references": None,
                },
                {
                    "name": '"default_language"',
                    "type": "int",
                    "size": None,
                    "nullable": True,
                    "default": None,
                    "check": None,
                    "unique": False,
                    "references": None,
                },
            ],
            "primary_key": ['"id"'],
            "index": [],
            "table_name": '"users"',
            "tablespace": None,
            "schema": None,
            "partitioned_by": [],
            "alter": {},
            "checks": [],
        },
        {
            "columns": [
                {
                    "name": '"id"',
                    "type": "int",
                    "size": None,
                    "nullable": False,
                    "default": None,
                    "check": None,
                    "unique": False,
                    "references": None,
                },
                {
                    "name": '"code"',
                    "type": "varchar",
                    "size": 2,
                    "nullable": False,
                    "default": None,
                    "check": None,
                    "unique": False,
                    "references": None,
                },
                {
                    "name": '"name"',
                    "type": "varchar",
                    "size": None,
                    "nullable": False,
                    "default": None,
                    "check": None,
                    "unique": False,
                    "references": None,
                },
            ],
            "primary_key": ['"id"'],
            "index": [],
            "table_name": '"languages"',
            "tablespace": None,
            "schema": None,
            "partitioned_by": [],
            "alter": {},
            "checks": [],
        },
    ]
    # expected = [{"data": []}]
    current_path = os.path.dirname(os.path.abspath(__file__))
    assert expected == parse_from_file(
        os.path.join(current_path, "sql", "test_two_tables.sql")
    )


def test_parse_from_file_encoding():
    expected = [
        {
            "columns": [
                {
                    "name": "`entry`",
                    "type": "mediumint unsigned",
                    "size": 8,
                    "references": None,
                    "unique": False,
                    "nullable": False,
                    "default": "'0'",
                    "check": None,
                },
                {
                    "name": "`content_default`",
                    "type": "text",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": False,
                    "default": None,
                    "check": None,
                },
                {
                    "name": "`content_loc1`",
                    "type": "text",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
                {
                    "name": "`content_loc2`",
                    "type": "text",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
                {
                    "name": "`content_loc3`",
                    "type": "text",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
                {
                    "name": "`content_loc4`",
                    "type": "text",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
                {
                    "name": "`content_loc5`",
                    "type": "text",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
                {
                    "name": "`content_loc6`",
                    "type": "text",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
                {
                    "name": "`content_loc7`",
                    "type": "text",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
                {
                    "name": "`content_loc8`",
                    "type": "text",
                    "size": None,
                    "references": None,
                    "unique": False,
                    "nullable": True,
                    "default": None,
                    "check": None,
                },
            ],
            "primary_key": ["`entry`"],
            "alter": {},
            "checks": [],
            "index": [],
            "partitioned_by": [],
            "tablespace": None,
            "if_not_exists": True,
            "schema": None,
            "table_name": "`mangos_string`",
        },
        {"name": "'IP:", "value": "%s\\"},
        {
            "comments": [
                "!40101 SET @OLD_CHARACTER_SET_CLIENT = @@CHARACTER_SET_CLIENT */;",
                "!40101 SET NAMES utf8 */;",
                "!40014 SET @OLD_FOREIGN_KEY_CHECKS = @@FOREIGN_KEY_CHECKS ,  FOREIGN_KEY_CHECKS = 0 */;",
                "!40101 SET @OLD_SQL_MODE = @@SQL_MODE ,  SQL_MODE = 'NO_AUTO_VALUE_ON_ZERO' */;",
                "!40000 ALTER TABLE `mangos_string` DISABLE KEYS */;",
                "!40000 ALTER TABLE `mangos_string` ENABLE KEYS */;",
                "!40101 SET SQL_MODE = IFNULL ( @OLD_SQL_MODE ,  '' )  */;",
                "!40014 SET FOREIGN_KEY_CHECKS = IF ( @OLD_FOREIGN_KEY_CHECKS IS NULL ,  1 ,  "
                "@OLD_FOREIGN_KEY_CHECKS )  */;",
                "!40101 SET CHARACTER_SET_CLIENT = @OLD_CHARACTER_SET_CLIENT */;",
            ]
        },
    ]

    current_path = os.path.dirname(os.path.abspath(__file__))
    result = parse_from_file(
        os.path.join(current_path, "sql", "mangos_encoding_test.sql")
    )
    assert expected == result
