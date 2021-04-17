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
        
        # if the headers are not provided, use the column indecies
        if headers:
            self.headers = headers
        elif headers is None:
            self.headers = [str(hdr) for hdr in self.get_idxvals(data.keys())[1]]
            
        # this line here means we need a data input type dict()
        self.nrows, self.ncols = self.get_dims(data.keys())
        # self.index = self.create_index(data.keys())
        self.rounding = rounding
        self.col_start = 0
        self.data = data # as a dict with tuple index
        self.headers = list(headers)
        self.labels = list(labels)
        self.left_pad = left_pad
        self.right_pad = right_pad
        self.col_sep = col_sep
        self.hdr_sep = hdr_sep
        self.col_size = dict()
        self.cell_base = r"{{:.{}f}}".format(self.rounding)
        
        if labels:
            self.col_start = 1
            self.ncols += 1
            self.col_size[0] = max([len(lbl) for lbl in labels])
            
        # need to know what size the columns are
        self.size_cols()
        self.row_base = self.construct_rowbase()
        self.header_row = self.construct_header()
        self.table = self.construct_table()

    def get_idxvals(self, index):
        """
        from the keys get the unique row and column labels
        """
        input_rows = list()
        input_cols = list()
        for key in index:
            input_rows.append(key[0])
            input_cols.append(key[1])

        return OrderedSet(input_rows), Orderedset(input_cols)
    
    def get_dims(self, index):
        """
        from the keys in the data, let's workout the dims     
        """
        row_lbl, col_lbl = get_idxvals(index)
        return len(row_lbl), len(col_lbl)

    # def create_index(self, index):
    #     """
    #     from the current index, lets create a 0-n index for the cols
    #     and the rows
    #     """
    #     row_lbl, col_lbl = get_idxvals(index)

    #     # enumerate the indecies and create a lookup
    #     return len(rows), len(cols)
        
    def size_cols(self):
        """
        Sizes the cols to be the bigger of the header
        or the column data
        """
        # initial is the header requirement
        for c, hdr in enumerate(self.headers):
            self.col_size[c+self.col_start] = len(str(hdr))
            
        # go through the rows and check the column sizing to find the max
        for r in range(self.nrows):
            for c in range(self.col_start, self.ncols):
                self.col_size[c] = max(
                    self.col_size[c], len(self.cell_base.format(self.data[r,c-self.col_start]))
                    )
        
    def construct_rowbase(self):
        """
        Builds up the base to write the row data to
        """
        
        # build out the format string to enter the strings into
        row_bse = [r"{}{{: >{}}}{}".format(
            " "*self.left_pad,
            str(self.col_size[c]),
            " "*self.right_pad) for c in range(self.ncols)]
        return row_bse        
    
    def construct_header(self):
        """
        Enters data into the row_base for the headers
        """        
        
        # create the individual labels
        if self.labels:
            self.headers.insert(0, "")
        hdr_bits = [hb.format(hdr) for hb, hdr in zip(self.row_base, self.headers)]
                
        # stick it all together and return with hdr_sep underneath
        hdr_str = f"|{'|'.join(hdr_bits)}|\n"
        return hdr_str + self.hdr_sep * (len(hdr_str)-1) + "\n"
    
    def construct_row(self, idx, row_data):
        """
        Enters data into the row base for a give set of data
        """
        
        if self.labels:
            row_data.insert(0, self.labels[idx])
        
        # construct the row bits
        row_bits = [self.row_base[0].format(row_data[0])] if self.labels else []
        for idx in range(self.col_start, self.ncols):
            data_str = self.cell_base.format(row_data[idx])
            cell_str = self.row_base[idx].format(data_str)
            row_bits.append(cell_str)
            
            
        # stick it all together and return
        row_str = f"|{'|'.join(row_bits)}|\n"
        return row_str
    
    def construct_table(self):
        """
        put it all together
        """
        table_str = self.header_row
        for idx in range(self.nrows):
            row_data = [self.data[idx,c-self.col_start] for c in range(self.col_start, self.ncols)]
            table_str += self.construct_row(idx, row_data)
            
        return table_str
    
    def __repr__(self):
        return self.table
            
            
        
        
        
        
        
        
        
        
        