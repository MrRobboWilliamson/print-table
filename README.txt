===================
Print Table Module
===================

The primary purpose of this package is to print out Gurobi variables in the console
as tables.

The PrintTable class takes data as a dictionary with a 2-tuple key, (row_label, col_label).

Run the following command to install
> pip install git+https://github.com/MrRobboWilliamson/print-table.git#egg=printtable

Usage:
>>> from printable.prnt_tbls import PrintTable
print(PrintTable(data))

Optional arguments for column labels (headers) and row labels (labels)

To Do:
Allow other input types:
  - pandas.DataFrame, list, list[list]
