===================
Print Table Module
===================

The primary purpose of this package is to print out Gurobi variables in the console
as tables.

The PrintTable class takes data as a dictionary with a 2-tuple key, (row_label, col_label).

Run the following command to install
> pip install git+https://github.com/MrRobboWilliamson/print-table.git#egg=printtable

Usage:
>>> from printable.prnt_tbls import PrintTable as pt
>>> data = { (r,c):X[r,c].x for r in rows for c in cols }
>>> print(pt(data))
|    | G28 | G1 | G43 | G46 | G32 |
-----------------------------------
| D0 |  85 |  5 |   0 |  73 |   0 |
| D1 | 100 | 27 |   0 | 100 |   0 |
| D2 | 100 | 41 |   4 | 100 | 100 |
| D3 | 100 | 66 |  11 | 100 | 100 |
| D4 | 100 | 98 |  21 | 100 | 100 |
| D5 | 100 | 64 |  12 | 100 | 100 |

Optional arguments for column labels (headers) and row labels (labels)

To Do:
Allow other input types:
  - pandas.DataFrame, list, list[list]
