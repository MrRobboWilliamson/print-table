 ===================
Print Table Module
===================

The primary purpose of this package is to print out Gurobi variables in the console
as tables.

The PrintTable class takes data as a 2-tuple key, (row, col).

Run the following command to install
> pip install git+https://github.com/MrRobboWilliamson/print-table.git#egg=printtable

Usage:
Currently for it to work, the tuples must index from 0 to number of rows/cols -1

To Do:
Will need to interpret the type of data provided to convert to a 0 to len -1. Propose
input types are pandas DataFrame, dict, list, list[list]
