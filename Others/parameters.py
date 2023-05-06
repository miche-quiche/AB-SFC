#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 15:26:38 2023

See appendice B p. 405 - 406.
"""

import pandas as pd
import numpy as np

"""
Table 1: Aggregate balance sheet (initial situation).

Abbreviation:
    - cf for consumption firms
    - kf for capital firms
    - cb for central bank


Attention, j'ai suivi la convention usuelle pour les dataframes de ranger
les individus par ligne à l'opposé de la notation usuelle pour les matrices
stock-flux (dont j'ai en revanche respecté la convention sur les signes + et -)

"""

agent_names = ['households', 'cf', 'kf', 'banks',
               'governement', 'cb']
stock_names = ['deposits', 'loans', 'c_good', 'k_goods', 'bonds',
                 'reserves', 'advances']
init_stock = np.array([[80704.1, 0, 0, 0, 0, 0, 0],
                       [25000, -52194.4, 2997.4, 53863.6, 0, 0, 0],
                       [5000, -1298, 0, 500, 0, 0, 0],
                       [-110704, 53492.5, 0, 0, 38273.5,  28564.6, 0],
                       [0, 0, 0, 0,  -66838.1, 0, 0],
                       [80704.1, 0, 0, 0, 28564.6, -28564.6, 0]
                       ])

init_stock_df = pd.DataFrame(init_stock, index = agent_names, columns = stock_names)


 
"""
Table 2: Aggregate transaction flow matrix (initial situation).
"""


agent_names = ['households', 'cf_ca', 'cf_ka', 'kf_ca', 'kf_ka', 'banks_ca',
               'banks_ka', 'governement', 'cb_ca', 'cb_ka']

flux_names = ['consumption', 'wages', 'dole', 'cg_inv', 'investiments',
              'k_amortization', 'taxes', 'i_dep', 'i_bonds', 'i_loans',
              'i_advances', 'profits', 'cb_profits','d_deposits', 'd_advances',
              'd_reserves', 'd_bonds', 'd_loans']

init_flux = np.array([[-32971.4,36800,1280,0,0,0,-7084.7,200.3,0,0,0,2367.6,0,-600.8,0,0,0,0],
                      [32971.4,-25000,0,22.3,0,-4974,-484.8,62,0,-388.5,0,-2208.4,0,0,0,0,0,0],
                      [0,0,0,-22.3,-5375,4974,0,0,0,0,0,220.8,0,-186.1,0,0,0,388.5],
                      [0,-5000,0,3.7,5375,0,-68.7,12.4,0,-9.7,0,-312.8,0,0,0,0,0,0],
                      [0,0,0,-3.7,0,0,0,0,0,0,0,31.3,0,-37.2,0,0,0,9.7],
                      [0,0,0,0,0,0,-39.3,-274.7,95,398.2,0,-179.1,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,71.7,0,824.1,0,-212.6,-284.9,-398.2],
                      [0,-6800,-1280,0,0,0,7677.4,0,-165.9,0,0,0,70.9,0,0,0,497.6,0],
                      [0,0,0,0,0,0,0,0,70.9,0,0,0,-70.9,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,212.6,-212.6,0]
                      ])

init_flux_df = pd.DataFrame(init_flux, index = agent_names, columns = flux_names)



"""
Table 3: Parameters

Abbreviation:
    - k for capital
    - c for consumption
    - f for firm
    - l for labor
    - b for bank
    - n for number
    - dep for depot
    - cred for credit/loan
    - i for interest rates
"""

init_param = {'g': 0.0075, #Nominal rate of growth in the steady state (SS)
              'n_households': 8000, #Number of households
              'n_cf': 100, #Number of consumption firms
              'n_kf': 20, #Number of capital firms
              'n_b': 10, #Number of banks
              'n_public_servant': 1360, #Number of public servants (constant)
              'n_cf_workers': 4000, #Consumption firms' initial workers
              'n_kf_workers': 1000, #Kapital firms' initial workers
              'unemployment': 0.08, #Initial unemployment rate
              'k_l_productivity': 2, #Productivity of labor in K sector
              'k_productivity': 1, #Productivity of K
              'kl_ratio' : 6.4, #Capital/labor ratio
              'x_c': 5, #Number of potential partners on C ajd K goods mkts
              'x_k': 5,
              'x_depot': 3, #Number of potential partners on deposit-credit mkts
              'x_cred': 3,
              'x_n': 10, #Number of potential partners on labor mkt (for each vacant job)
              'e_dep': 4.62098, #Intensity of choice in deposit-credit mkts
              'e_cred': 4.62098,
              'e_c': 3.46574, #Intensity of choice in C and K goods mkts
              'e_k': 3.46574,
              'inventory_target': 0.1, #Firms' inventories target share
              'lambda': 0.25, #Adaptive expectations parameter
              'turnover': 0.05, #Labor turnover ratio
              'mark-up_cf': 0.318857, #Initial mark-up on ULC for C firms
              'mark-up_kf': 0.075, #Initial mark-up on ULC for K firms
              'variance': 0.0094, #Normal Distribution parameters
              'profit_tax': 0.18, #Profit tax rates
              'income_tax': 0.18, #Income tax rates
              'cred_duration': 20, #Loans duration
              'k_goods_duration': 20,
              'target_profit': 0.04345, #Target profit rate (Investment function)
              'target_capu': 0.8, #Target capacity utilization (Investment function)
              'y_profit': 0.01, #Profit rate weight (Investment function)
              'y_capu': 0.02, #Capacity utilization rate weight (Investment function)
              'precautionary_dep_f': 1, #Firms' precautionary deposits as share of WB
              'div_cf': 0.9, #Firms' profits' share distributed as dividends
              'div_kf': 0.9, #Firms' profits' share distributed as dividends
              'div_b': 0.6, #Banks' profit share distributed as dividends
              'i_cred': 0.0075, #Initial interest rate on loans
              'i_dep': 0.0025, #Initial interest rate on deposits
              'capital_ratio_t': 0.17996, #Initial banks' target capital ratio
              'liquidity_ratio_t': 0.258026342, #Initial banks' target capital ratio
              'risk_b_cf': 3.92245, #Banks' risk aversion towards C firms
              'risk_b_kf': 21.51335, #Banks' risk aversion towards K firms
              'key_rates': 0.005, #Central bank interest rates on advances
              'haircut': 0.5, #Haircut on defaulted firms' capital value
              'w': 5, #Initial wages
              'w_share': 0.4, #Dole (share of average wages)
              'u_threshold': 0.08, #Unemployment threshold in wage revision function
              'a_income': 0.38581, #Propensity to consume out of income
              'a_wealth': 0.25, #Propensity to consume out of wealth
              'i_bonds': 0.0025, #Bonds interest rate
              'p_bonds': 1, #Bonds price

              'steps':10,
              }


parameters = init_param