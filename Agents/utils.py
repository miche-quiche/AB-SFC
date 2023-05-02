#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 20:44:09 2023
"""

def expectation(past, expected_past, l = 0.5):
    return expected_past + l*(past-expected_past)