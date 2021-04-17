from printable.prnt_tbls import PrintTable


# create some test data
inputs = {
     ('rob',0): 2.0,
      ('jane',0): 3.5,
      ('rob',1): 4.9,
      ('jane',1): 12.6      
      }

print(inputs)
print("\nPrintTable:")
print(PrintTable(inputs,headers=['start', 'end'], labels=[2,3,4]))
