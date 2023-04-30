#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 15:07:38 2023

@author: marjan van frommmaj
"""

import mesa
import numpy as np
import matplotlib.pyplot as plt
import math


def compute_shannon(model):
    """ Calcul l'indice de Shannon-Weaver """
    n_Prey = model.num_agents
    n_Predator = 0
    n_tot = model.num_agents
    p = []
    p_Prey = n_Prey / n_tot
    if p_Prey > 0:
        p.append(p_Prey)
    p_Predator = n_Predator / n_tot
    if p_Predator > 0:
        p.append(p_Predator)
    if len(p)>0:
        H = 0
        for i in p:
            H -= i*math.log(i)
        return H
    else:
        return -1
    

class Animal(mesa.Agent):
    """ A random animal """
    
    species = ("Prey", "Predator")
    
    def __init__(self, unique_id, model, specie = "Prey"):
        super().__init__(unique_id, model)
        self.specie = specie
        
        
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=True
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
        
    def interact(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = self.random.choice(cellmates)
            print(other.unique_id)
            self.model.death(other)
            print("Arg")
        
    def step(self):
        self.move()
        self.interact()
        

class Ecosystem(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)

        # Create agents
        for i in range(self.num_agents):
            a = Animal(i, self)
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))
            
        # Pour collecter des données
        self.datacollector = mesa.DataCollector(model_reporters={
            "Shannon": compute_shannon}, 
            agent_reporters={"Identité": "unique_id"}
        )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
        
    def death(self,a):
        self.schedule.remove(a)
               
    def count(self):
              self.num_agents = self.get_agent_count()      
      
        
model = Ecosystem(3, 10, 10)
for i in range(20):
    model.step()
    
gini = model.datacollector.get_model_vars_dataframe()
gini.plot()
        
"""
agent_counts = np.zeros((model.grid.width, model.grid.height))
for cell in model.grid.coord_iter():
    cell_content, x, y = cell
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count
plt.imshow(agent_counts, interpolation="nearest")
plt.colorbar()
plt.show()
"""

