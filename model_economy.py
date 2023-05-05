#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 15:19:02 2023
"""

import agentpy as ap
from agents import *

class Economy(ap.Model):
    def setup(self):
        """ Initiate a list of new agents. """
        self.banques = ap.AgentList(self, self.p.banques, Agent_name)

    def step(self):
        """ Call a method for every agent. """
        self.banques.agent_method()
        self.banques.shuffle()
        self.banques.append(Agent_names(self))

    def update(self):
        """ Record a dynamic variable. """
        self.banques.record('my_attribute')


    def end(self):
        """ Repord an evaluation measure. """
        self.report('my_measure', 1)
        print(self.banques)
        