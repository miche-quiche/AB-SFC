#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 20:44:09 2023
"""

def expectation(past, expected_past, l = 0.5):
    return expected_past + l*(past-expected_past)

class Contract():
    """ peut-être créer une classe pour les contrats ?"""
    
    def __init__(self,identity=int(0), amount=float(0)):
        self.identity = identity
        self.amount = amount

    pass