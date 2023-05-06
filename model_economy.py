#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 15:19:02 2023
"""

import agentpy as ap
#from agents import *

from Agents.generical_agent import Agent_name
#from Agents.households import Households
from Agents.consumption_firm import Consumption_firm
from Agents.capital_firm import Capital_firm
from Agents.bank import Bank
from Agents.state import Central_bank
from Agents.state import Governement

class Economy(ap.Model):
    
    def setup(self):
        """ Initiate the lists of agents according to their class """
        self.consumption_firms = ap.AgentList(self, self.p.n_consumption_firms, Consumption_firm)
        self.capital_firms = ap.AgentList(self, self.p.n_capital_firms, Capital_firm())
        self.banks = ap.AgentList(self, self.p.n_banks, Bank)
        #self.households = ap.AgentList(self, self.p.n_households, Households)
        self.central_bank = Central_bank(self)
        self.governement = Governement(self)
        
        """ List for the management of agents """
        self.memory = ap.AgentList(self)
        
        """ Aggregated variables """
        self.unemployment = 0
        


    def step(self):
        """ Call a method for every agent. """
        self.banques.agent_method()
        self.banques.shuffle()
        self.banques.append(Agent_name(self))

    def update(self):
        """ Record a dynamic variable. """
        self.banques.record('my_attribute')


    def end(self):
        """ Repord an evaluation measure. """
        self.report('my_measure', 1)
        print(self.banques)


parameters = {'n_consumption_firms':10, 'n_capital_firms':10, 'n_banks':10, 
              'n_households':10, 'n_households': 10, 'steps':10,
              'my_attribute':10}