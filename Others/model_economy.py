#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 15:19:02 2023
"""

import agentpy as ap
#from agents import *

from os import chdir
chdir("..")

#from Agents.generical_agent import Agent_name
#from Agents.households import Households
from Agents.household import Household
from Agents.consumption_firm import Consumption_firm
from Agents.capital_firm import Capital_firm
from Agents.bank import Bank
from Agents.state import Central_bank
from Agents.state import Government

class Economy(ap.Model):
    
    def setup(self):
        """ Initiate the lists of agents according to their class """
        self.consumption_firms = ap.AgentList(self, self.p.n_cf, Consumption_firm)
        self.capital_firms = ap.AgentList(self, self.p.n_kf, Capital_firm)
        self.banks = ap.AgentList(self, self.p.n_b, Bank)
        self.households = ap.AgentList(self, self.p.n_households, Household)
        self.central_bank = Central_bank(self)
        self.government = Government(self)
        
        """ List for the management of agents """
        self.memory = ap.AgentList(self)
        
        """ Aggregated variables """
        self.unemployment = 0
        
    def fire(self, identity):
        """ Method for firing an agent/resign a contract """
        pass
        
    def hire(self, identity):
        """ Method for hiring an agent/sign a contract """
        pass


    def step(self):
        """ Call a method for every agent. """
        pass

    def update(self):
        """ Record a dynamic variable. """
        pass

    def end(self):
        """ Repord an evaluation measure. """
        self.report('my_measure', 1)


parameters = {'n_cf':10, 'n_kf':10, 'n_b':10, 
              'n_households':10, 'steps':10,
              'my_parameter':10}


model = Economy(parameters)
results = model.run()