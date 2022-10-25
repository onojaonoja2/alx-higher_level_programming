#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 15:13:37 2022
@author: Samuel Onoja
"""


def read_file(filename=""):
    """
    Reads the file
    Arguments:
        filename (str): The name of the file to open
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
