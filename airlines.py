# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 07:06:50 2019

@author: Prakash
"""

import seaborn as sns
import matplotlib as mlt
import random as rd
import numpy as np
from matplotlib import rcParams
import matplotlib.pyplot as plt

seat_capacity = 100;
prob_board = 0.95;

def boarding(porb_board):
    if rd.random()<=prob_board:
        return 1
    else:
        return 0

def simulate_flight(tickets_sold,prob_board):
    n=0;
    for i in range(1,tickets_sold):
        if(boarding(prob_board)):
            n = n+1
    return n
def revenue_model(tickets_sold, seat_capacity,prob_board, revenue_per_seat, voucher_cost):
    
    total_showups = simulate_flight(tickets_sold,prob_board)
  
    if (total_showups <= seat_capacity):
        return revenue_per_seat * total_showups
  
    else:
        upset_customers = total_showups - seat_capacity
     
    return (total_showups * revenue_per_seat) - (voucher_cost * upset_customers)
  
revenue_per_seat = 7000
voucher_cost = revenue_per_seat * 2
no_simulations = 10000
max_overbooking = 20
revenue = np.zeros(shape = (no_simulations,max_overbooking+1))

for tickets_overbooked in range(0,max_overbooking):
    tickets_sold = seat_capacity + tickets_overbooked
    for i in range(1,no_simulations):
        revenue[i,tickets_overbooked] = revenue_model(tickets_sold, seat_capacity,prob_board, revenue_per_seat, voucher_cost)

sns.set(rc={'figure.figsize':(10,15)})
ax = sns.boxplot(data = revenue, notch=True)
plt.xlabel("No. of Tickets Oversold")
plt.ylabel("Net Profit")
plt.ylim(33000,40500)
plt.yticks([33000,35000,36000,37000,38000,39000,40000])

        