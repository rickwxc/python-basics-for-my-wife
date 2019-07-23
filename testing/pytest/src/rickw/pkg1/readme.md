my_package/
├── CHANGELOG.rst
├── LICENSE
├── MANIFEST.in
├── README.rst
├── setup.py
├── src
│ └── tasks
│ ├── __init__.py
│ ├── api.py
│ ├── cli.py
│ ├── config.py
│ ├── tasksdb_pymongo.py
│ └── tasksdb_tinydb.py
└── tests
├── conftest.py
├── pytest.ini
├── func
│ ├── __init__.py
│ ├── test_add.py
│ └── ...
└── unit
├── __init__.py
├── test_task.py
└── ...

Functional and unit tests are separated into their own directories. 
separate functional and unit tests separate:
functional tests should only break if we are intentionally changing functionality of the system, 
unit tests could break during a refactoring or an implementation change.
