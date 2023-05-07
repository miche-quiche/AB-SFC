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

def partition(liste1, liste2):
    """ renvoie une liste de la taille de la liste 1 avec les élémens de la
    liste 2 équitablement partionné dedans """
    
    import random as random_nul
    l1 = len(liste1)
    l2 = len(liste2)
    k = l1//l2
    r = l1%l2
    new_list = l2*k + random_nul.sample(l2,r)
    random_nul.shuffle(new_list)
    
    return new_list