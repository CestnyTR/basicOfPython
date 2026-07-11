# Basics of Python

A single, self-contained reference file (`basic.py`) that walks through the core
building blocks of Python, organized into classes by topic. It is meant as a
learning playground / cheat sheet rather than a runnable application.

## What it covers

- **`basicsVerbs`** — variables & types, `eval`, strings, lists, dictionaries,
  tuples, sets, `map`, `enumerate`, and common string/list methods
  (`split`, `strip`, `join`, `count`, `find`, `sort`, `pop`, `insert`, …).
- **`conditionalsVerbs`** — `if/else`, `for` loops, and `while` loops.
- **`sqlliteOpp`** — basic SQLite CRUD (`SELECT`, `INSERT`, `UPDATE`) against the
  bundled `tools/db/chinook.db` sample database.

## Layout

```
basicOfPython/
├── basic.py            # the annotated reference file
└── tools/              # sample data used by the examples
    ├── db/             # chinook.db + SQLite source
    ├── module/         # small helper modules & Tkinter widget demos
    └── *.txt/.json/.xlsx/.html/.png
```

## Usage

Each topic lives in a static method. Call the ones you want to try, e.g.:

```python
from basic import basicsVerbs, conditionalsVerbs

basicsVerbs.stringsVerb()
conditionalsVerbs.forLoops()
```

## Requirements

- Python 3.x
- Standard library only (`sqlite3` is used for the database examples)
