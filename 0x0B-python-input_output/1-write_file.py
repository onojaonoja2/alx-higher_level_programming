#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 15:13:37 2022
@author: Samuel Onoja
"""


def write_file(filename="", text=""):
    """
    Writes inputed text to a utf-8 encoded file
    Arguments:
        filename (str): The name of the file to open
        text (str): The text to write in
    Return:
        A file with text written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
