#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 15:26:38 2023

See appendice B table 3 p. 406.

Abbreviation :
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

parameters = {'g':0.0075, #Nominal rate of growth in the steady state (SS)
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
              'my_attribute':10}