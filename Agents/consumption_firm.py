#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 19:38:31 2023

@author: marjan van frommmaj
"""

from agentpy import Agent
from os import chdir
chdir("..")

from Others.utils import expectation
#from Others.parameters import *


import random as random


class Consumption_firm(Agent):
    
    def setup(self):
        
        #Contracts with others agents
        self.employees_ids = [] #warning: to access the wage, the firm has to ask the worker
        self.deposits = [(0,0.)] #(bank_id, amount)
        self.loans =[(0,0.)] #same
        
        #Memory
        self.sales = 0
        self.real_k = 0
        self.inventory = 0
        
        #Strategy
        self.expected_sales = 0
        self.desired_output = 0
        self.desired_margins = 0
        self.l_needs = 0
        
        
        
    def step1(self):
        '''
        Production planning: consumption and capital firms compute their
        desired output level.
        '''
        self.expected_sales = expectation(self.sales, self.expected_sales)
        self.desired_output = self.expected_sales*(1+self.p.inventory_target) - self.inventory


    
    def step2(self):
        '''
        Firms' labor demand: firms evaluate the number of workers needed to 
        produce.
        '''
        
        #calcul du taux d'utilisation désiré
        u = min (1,self.desired_output/(self.real_k * self.p.k_productivity))
        #calcul des besoins de main d'oeuvre pour ce taux d'utilisation
        self.l_needs = u * self.real_capital / self.p.k_l_ratio

        #suppression de postes si main d'oeuvre excédentaire
        r = round(self.l_needs)
        l = len(self.unique_ids)
        if r < l:
            s = self.model.sample(self.employees_ids,l-r)
            for i in s:
                self.employees_ids.remove(i)
                self.model.fire(i)
        
        #turnover à rajouter plus tard
    
    def step3(self):
        '''
        Prices, interest, and Wages: consumption and capital firms set the 
        price of their output; banks determine the interest rate on loans and 
        deposits. Workers adaptively revise their reservation wages.

        '''
        random.normalvariate(mu=0.0, sigma=1.0)
        pass
    
    def step4(self):
        '''
        Investment in capital accumulation: consumption firms' determine their 
        desired rate of capacity growth and, as a consequence, their real 
        demand for capital goods.
        '''
        pass
    
    def step5(self):
        '''
        Capital good market (1): consumption firms choose their capital
        supplier.
        '''
        pass
    
    def step6(self):
        '''
        Credit demand: Firms assess their demand for credit and select the
        lending bank.
        '''
        pass
    
    def step7(self):
        '''
        Credit supply: Banks evaluate loan requests and supply credit
        accordingly.
        '''
        pass
       
    def step8(self):
        '''
        Labor market: unemployed workers interact with firms on the labor 
        market.
        '''
        pass
       
    def step9(self):
        '''
        Production: capital and consumption firms produce their output.
        '''
        pass
    
    def step10(self):
        '''
        Capital goods market (2): consumption firms purchase capital from their
        supplier. New machineries are employed in the production process 
        starting from the next period.
        '''
        pass
    
    def step11(self):
        '''
        Consumption goods market: households interact with consumption firms 
        and consume.
        '''
        pass
    
    def step12(self):
        '''
        Interest, bonds and loans repayment: firms pay interests on loans and 
        repay a (constant) share of each loan principal. The government repays
        bonds and interest to bonds' holders. Banks pay interest on deposits.
        Cash advances and related interests, when present, are repaid.
        '''
        pass
    
    def step13(self):
        '''
        Wages and dole: wages are paid. Unemployed workers receive a dole from
        the government.
        '''
        pass
    
    def step14(self):
        '''
        Taxes: taxes on profits and income are paid to the government.
        '''
        pass
    
    def step15(self):
        '''
        Dividends: dividends are distributed to households.
        '''
        pass
    
    def step16(self):
        '''
        Deposit market interaction: households an firms select their deposit
        bank.
        '''
        pass
    
    def step17(self):
        '''
        Bond purchases: banks and the Central Bank purchase newly issued bonds.
        '''
        pass
    
    def step18(self):
        '''
        Cash Advances: the Central Bank accommodates cash advances requests by
        private banks.
        '''
        pass
 












       
       
       