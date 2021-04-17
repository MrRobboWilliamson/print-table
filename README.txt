===================
Print Table Module
===================

The primary purpose of this package is to print as neat tables, 2D numerical data stored as a dictionary with 2-tuple keys.

The PrintTable constructor takes data as a dictionary with a 2-tuple key, (row_label, col_label).

Run the following command to install
> pip install git+https://github.com/MrRobboWilliamson/print-table.git#egg=printtable

Usage:
Here data is extracted from Gurobi variables and printed to the console with custom headers and labels
>>> from printable.prnt_tbls import PrintTable as pt
>>> data = { (r,c):X[r,c].x for r in rows for c in cols }
>>> print(pt(data,headers,labels))
|    | G28 | G1 | G43 | G46 | G32 |
-----------------------------------
| D0 |  85 |  5 |   0 |  73 |   0 |
| D1 | 100 | 27 |   0 | 100 |   0 |
| D2 | 100 | 41 |   4 | 100 | 100 |
| D3 | 100 | 66 |  11 | 100 | 100 |
| D4 | 100 | 98 |  21 | 100 | 100 |
| D5 | 100 | 64 |  12 | 100 | 100 |

Optional arguments:
 - headers: for custom column labels
 - labels: for custom row labels
 - left_pad: control padding on the left, default=1
 - right_pad: control padding on the right, default=1
 - col_sep: character to separate the columns, default="|" 
 - hdr_sep: character to separate the header row, default="-"
 - rounding: control the precision of the numbers, default=0   

To Do:
Allow other input types:
  - pandas.DataFrame, list, list[list]
