from simple_ddl_parser import DDLParser


def test_partitioned_by_hql_output_mode_hql():
    ddl = """
    CREATE EXTERNAL TABLE IF NOT EXISTS database.table_name
    (
        day_long_nm     string,
        calendar_dt     date,
        source_batch_id string,
        field_qty       decimal(10, 0),
        field_bool      boolean,
        field_float     float,
        create_tmst     timestamp,
        field_double    double,
        field_long      bigint
    ) PARTITIONED BY (batch_id int);

    CREATE TABLE IF NOT EXISTS database.table_name2
    (
        day_long_nm     string,
        calendar_dt     date,
        source_batch_id string,
        field_qty       decimal(10, 0),
        field_bool      boolean,
        field_float     float,
        create_tmst     timestamp,
        field_double    double,
        field_long      bigint
    ) PARTITIONED BY (batch_id int)

    """


    result = DDLParser(ddl).run(output_mode='hql')
    
    expected = [{'columns': [{'name': 'day_long_nm', 'type': 'string', 'size': None, 'references': None, 'unique': False, 'nullable': True, 'default': None, 'check': None}, {'name': 'calendar_dt', 'type': 'date', 'size': None, 'references': None, 'unique': False, 'nullable': True, 'default': None, 'check': None}, {'name': 'source_batch_id', 'type': 'string', 'size': None, 'references': None, 'unique': False, 'nullable': True, 'default': None, 'check': None}, {'name': 'field_qty', 'type': 'decimal', 'size': (10, 0), 'references': None, 'unique': False, 'nullable': True, 'default': None, 'check': None}, {'name': 'field_bool', 'type': 'boolean', 'size': None, 'references': None, 'unique': False, 'nullable': True, 'default': None, 'check': None}, {'name': 'field_float', 'type': 'float', 'size': None, 'references': None, 'unique': False, 'nullable': True, 'default': None, 'check': None}, {'name': 'create_tmst', 'type': 'timestamp', 'size': None, 'references': None, 'unique': False, 'nullable': True, 'default': None, 'check': None}, {'name': 'field_double', 'type': 'double', 'size': None, 'references': None, 'unique': False, 'nullable': True, 'default': None, 'check': None}, {'name': 'field_long', 'type': 'bigint', 'size': None, 'references': None, 'unique': False, 'nullable': True, 'default': None, 'check': None}], 'primary_key': [], 'alter': {}, 'checks': [], 'index': [], 'partitioned_by': [{'name': 'batch_id', 'type': 'int', 'size': None}], 'external': True, 'schema': 'database', 'table_name': 'table_name'}, {'columns': [{'name': 'day_long_nm', 'type': 'string', 'size': None, 'references': None, 'unique': False, 'nullable': True, 'default': None, 'check': None}, {'name': 'calendar_dt', 'type': 'date', 'size': None, 'references': None, 'unique': False, 'nullable': True, 'default': None, 'check': None}, {'name': 'source_batch_id', 'type': 'string', 'size': None, 'references': None, 'unique': False, 'nullable': True, 'default': None, 'check': None}, {'name': 'field_qty', 'type': 'decimal', 'size': (10, 0), 'references': None, 'unique': False, 'nullable': True, 'default': None, 'check': None}, {'name': 'field_bool', 'type': 'boolean', 'size': None, 'references': None, 'unique': False, 'nullable': True, 'default': None, 'check': None}, {'name': 'field_float', 'type': 'float', 'size': None, 'references': None, 'unique': False, 'nullable': True, 'default': None, 'check': None}, {'name': 'create_tmst', 'type': 'timestamp', 'size': None, 'references': None, 'unique': False, 'nullable': True, 'default': None, 'check': None}, {'name': 'field_double', 'type': 'double', 'size': None, 'references': None, 'unique': False, 'nullable': True, 'default': None, 'check': None}, {'name': 'field_long', 'type': 'bigint', 'size': None, 'references': None, 'unique': False, 'nullable': True, 'default': None, 'check': None}], 'primary_key': [], 'alter': {}, 'checks': [], 'index': [], 'partitioned_by': [{'name': 'batch_id', 'type': 'int', 'size': None}], 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'external': False, 'schema': 'database', 'table_name': 'table_name2'}]
    
    assert expected == result