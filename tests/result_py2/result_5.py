('test_precisely',
 [('E128', 9, 12, 'continuation line under-indented for visual indent',
   "    Column('id', Integer, primary_key=True),\n"),
  ('E251', 16, 20, 'unexpected spaces around keyword / parameter equals',
   '        data = {"key1": "value1", "key2": "value2"}\n'),
  ('E251', 16, 22, 'unexpected spaces around keyword / parameter equals',
   '        data = {"key1": "value1", "key2": "value2"}\n'),
  ('F821', 8, 21, "undefined name 'Table'", "data_table = Table('data_table', metadata,\n"),
  ('F821', 8, 41, "undefined name 'metadata'", "data_table = Table('data_table', metadata,\n"),
  ('F821', 9, 12, "undefined name 'Column'", "    Column('id', Integer, primary_key=True),\n"),
  ('F821', 9, 25, "undefined name 'Integer'", "    Column('id', Integer, primary_key=True),\n"),
  ('F821', 10, 12, "undefined name 'Column'", "    Column('data', JSONB)\n"),
  ('F821', 10, 27, "undefined name 'JSONB'", "    Column('data', JSONB)\n"),
  ('F821', 13, 13, "undefined name 'engine'", 'with engine.connect() as conn:\n')],
 {'logical lines': 3, 'physical lines': 10, 'tokens': 68})
