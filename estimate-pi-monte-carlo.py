# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 20:51:42 2019

@author: Christian
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.patches import Circle as Circle

class EstimatePi:
    def __init__(self):
        self.current = pd.DataFrame(columns =['current_estimate'])
        self.coordinates = pd.DataFrame(columns =['x','y'])
        self.circle = 0
        
    def generate_points(self): 

        for sim in range(self.n_sims):
            sim += 1
            x = np.random.uniform(-1,1)
            y = np.random.uniform(-1,1)
            r_squared = np.square(x) + np.square(y)

            self.coordinates = self.coordinates.append({'x': x , 'y': y}, ignore_index = True)
            
            if r_squared <= 1:
                self.circle += 1
            
            estimate = self.calc_estimate(sim)
            self.current= self.current.append({'current_estimate': estimate}, ignore_index = True)

    def calc_estimate(self, n_sims):
        pi = 4*self.circle/n_sims
        
        return pi

    def estimate(self, n_sims):
        self.n_sims = n_sims
        self.generate_points()
        
        print(pi.current['current_estimate'].iloc[-1])
 
    def plot_sim(self):
        y = self.coordinates['x']
        x = self.coordinates['y']
        
        fig, ax = plt.subplots(figsize = (5,5))
        ax.scatter(x,y)
        ax.add_patch(Circle((0, 0), 1, color='b', fill=False)) 
        ax.set_title('Area Plot')
        fig

        current = self.current['current_estimate']
        n_sims = range(self.n_sims)
        
        fig, ax = plt.subplots(figsize = (5,5))
        ax.plot(n_sims,current, '-o')   
        ax.set_title('Running Estimate')
        ax.set_ylabel('Pi Estimate')
        ax.set_xlabel('Num Simulations')
        fig
        
        
pi = EstimatePi()
pi.estimate(500)
pi.plot_sim()
pi.current['current_estimate'].iloc[-1]
