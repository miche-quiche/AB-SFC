#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 15:19:02 2023
"""

import agentpy as ap
import numpy as np
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
        #self.memory = ap.AgentList(self)

        
        """ Aggregated variables """
        self.unemployment = self.p.unemployment
        
        
        
        ### à ranger plus tard dans une fonction
        
        # les fonctionnaires
        memory1 = self.households.random(self.p.n_public_servants)
        memory1.employed = True
        memory1.public_servant = True
    
        #les travailleurs des cf, alogirthme trop compliqué pour ce qu'il fait...
        #ie répartir équitablement les employés dans les firmes en acceptant les cas où
        #certaines entreprises ont 1 employé de plus que d'autres
        memory1 = self.households.select([not i.employed for i in self.households])
        memory1 = memory1.random(self.p.n_cf_workers).to_list()
        memory1.employed = True
        memory1.wage = self.p.w
        memory2 = self.consumption_firms
        l1 = len(memory1)
        l2 = len(memory2)
        k,r = l1//l2, l1%l2
        for j in memory2:
            memory3 = memory1.random(k).to_list()
            for i in memory3:
                memory1.remove(i)
            j.employees_ids = list(memory3.id)
        for j in memory2.random(r):
            a = memory1.random().to_list()
            j.employees_ids.append(a.id[0])
            memory1.remove(a[0])
            
        #rebelote pour les kf
        memory1 = self.households.select([not i.employed for i in self.households])
        memory1 = memory1.random(self.p.n_kf_workers).to_list()
        memory1.employed = True
        memory1.wage = self.p.w
        memory2 = self.capital_firms
        l1 = len(memory1)
        l2 = len(memory2)
        k,r = l1//l2, l1%l2
        for j in memory2:
            memory3 = memory1.random(k).to_list()
            for i in memory3:
                memory1.remove(i)
            j.employees_ids = list(memory3.id)
        for j in memory2.random(r):
            a = memory1.random().to_list()
            j.employees_ids.append(a.id[0])
            memory1.remove(a[0])
            
        del memory1, memory2, memory3
            
        
        for i in self.consumption_firms:
            print(i.id, i.employees_ids, type(i))
        for i in self.capital_firms:
            print(i.id, i.employees_ids, type(i))
        for i in self.households:
            print(i.id, i.employed, i.public_servant)



    def step(self):
        """ Call a method for every agent. """
        pass

    def update(self):
        """ Record a dynamic variable. """
        self.unemployment = np.array([not i.employed for i in self.households]).mean()
        pass

    def end(self):
        """ Repord an evaluation measure. """
        self.report('my_measure', 1)
        print(self.unemployment)


parameters = {'n_cf':3, 'n_kf':2, 'n_b':10, 
              'n_households':15, 'steps':10,
              'n_public_servants': 1, 'n_cf_workers':7 , 'n_kf_workers':4 , 'w':5,
              'my_parameter':10, 'unemployment': 0.8}


model = Economy(parameters)
results = model.run()