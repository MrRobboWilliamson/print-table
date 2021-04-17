#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 12:24:04 2021

@author: rob
"""
from ordered_set import OrderedSet

class PrintTable():
    """
    Takes some loosly defined tables and prints them out nice
    """    
    def __init__(self, data, headers=None, labels=None, left_pad=1,
                 right_pad=1,  col_sep="|", hdr_sep="-", rounding=0):        
        
        # check that the input type is correct
        if type(data) is not dict:
            raise TypeError("Data must be a dictionary")

        # get the index as a list of keys
        self.index = list(data.keys())
        
        # check that keys are tuples
        if type(self.index[0]) is not tuple:
            raise TypeError("Dict must contain 2-tuple keys")
        
        # check that tuples are 2-tuples
        if len(self.index[0]) != 2:
            raise TypeError("Key must be 2 dimensional")

        # initiate parameters
        self.col_size = dict() # to track the column sizes
        self.nrows, self.ncols = self.get_dims()

        # if the headers are not provided, use the column indecies
        if headers:
            # check that the lables are list
            if type(headers) is not list:
                raise TypeError("Headers must be a list")
            # check the length matches the number of columns
            if len(headers) != self.ncols:
                raise ValueError("Expected header list of length", self.ncols)            
            self.headers = headers
        elif headers is None:
            self.headers = [str(hdr) for hdr in self.get_idxvals()[1]]

        # if labels are provided treat as extra 0th column
        if labels:
            # check that the lables are list
            if type(labels) is not list:
                raise TypeError("Labels must be a list")
            # check the length matches the number of columns
            if len(labels) != self.nrows:
                raise ValueError("Expected label list of length", self.nrows)            

            # convert the labels to strings
            self.labels = [str(lbl) for lbl in labels]
        elif labels is None:
            self.labels = [str(lbl) for lbl in self.get_idxvals()[0]]

        # self.index = self.create_index(data.keys())
        self.rounding = rounding
        self.data = data # as a dict with tuple index
        self.left_pad = left_pad
        self.right_pad = right_pad
        self.col_sep = col_sep
        self.hdr_sep = hdr_sep
        self.cell_base = r"{{:.{}f}}".format(self.rounding)
                    
        # need to know what size the columns are
        self.col_size[0] = max([len(lbl) for lbl in self.labels])
        self.col_start = 1
        self.headers.insert(0, "")
        self.size_cols()
        self.row_base = self.construct_rowbase()
        self.header_row = self.construct_header()
        self.table = self.construct_table()

    def get_idxvals(self):
        """
        from the keys get the unique row and column labels
        """
        input_rows = list()
        input_cols = list()
        for key in self.index:
            input_rows.append(key[0])
            input_cols.append(key[1])

        return list(OrderedSet(input_rows)), list(OrderedSet(input_cols))
    
    def get_dims(self):
        """
        from the keys in the data, let's workout the dims     
        """
        row_lbl, col_lbl = self.get_idxvals()
        return len(row_lbl), len(col_lbl)
        
    def size_cols(self):
        """
        Sizes the cols to be the bigger of the header
        or the column data
        """
        # initial is the header requirement
        for c, hdr in enumerate(self.headers):
            self.col_size[c+self.col_start] = len(str(hdr))
            
        # go through the rows and check the column sizing to find the max
        row_lbls, col_lbls = self.get_idxvals()
        for rlbl in row_lbls:
            for c, clbl in enumerate(col_lbls):
                self.col_size[c+self.col_start] = max(
                    self.col_size[c+self.col_start],
                    len(self.cell_base.format(self.data[rlbl,clbl]))
                    )
        
    def construct_rowbase(self):
        """
        Builds up the base to write the row data to
        """
        
        # build out the format string to enter the strings into
        row_bse = [r"{}{{: >{}}}{}".format(
            " "*self.left_pad,
            str(self.col_size[c]),
            " "*self.right_pad) for c in range(self.ncols+self.col_start)]
        return row_bse        
    
    def construct_header(self):
        """
        Enters data into the row_base for the headers
        """        
        
        # create the individual labels
        hdr_bits = [hb.format(hdr) for hb, hdr in zip(self.row_base, self.headers)]
                
        # stick it all together and return with hdr_sep underneath
        hdr_str = f"|{'|'.join(hdr_bits)}|\n"
        return hdr_str + self.hdr_sep * (len(hdr_str)-1) + "\n"
    
    def construct_row(self, ridx, row_data):
        """
        Enters data into the row base for a give set of data
        """
        
        # construct the row bits
        row_bits = [self.row_base[0].format(self.labels[ridx])]
        for cidx in range(self.ncols):
            data_str = self.cell_base.format(row_data[cidx])
            cell_str = self.row_base[cidx+self.col_start].format(data_str)
            row_bits.append(cell_str)       
            
        # stick it all together and return
        row_str = f"|{'|'.join(row_bits)}|\n"
        return row_str
    
    def construct_table(self):
        """
        put it all together
        """
        table_str = self.header_row
        row_lbls, col_lbls = self.get_idxvals()
        for r,rlbl in enumerate(row_lbls):
            row_data = [self.data[rlbl,clbl] for clbl in col_lbls]
            table_str += self.construct_row(r, row_data)
            
        return table_str
    
    def __repr__(self):
        return self.table
            
            
        
        
        
        
        
        
        
        
        