
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression  
import itertools
import copy
import warnings
import time
import pickle
from tabulate import tabulate

#loading strings here never uncomment unless we need to store new string --> load string first!
"""
with open('stringlist.pkl', 'wb') as f:
       #pickle.dump(stringlist, f)
"""
#with open('stringlist.pkl', 'rb') as f:
      #stringlist = pickle.load(f)

s1 =""" 

  I'm programmed for etiquette, not destruction.                                         
  You may want to consider setting appropriate bounds to                                           
  find a solution in a reasoable time!
  
               \  .-.                                
                 /_ _\                               
                 |o^o|                               
                 \ _ /                               
                .-'-'-.              BLEEP BOOP BLOOP
              /`)  .  (`\            (THIS MEANS YES)
             / /|.-'-.|\ \         /                 
             \ \| (_) |/ /  .-""-.                   
              \_'-.-'/_/   /[] _ _\                  
              /_/ \_/ \_\ _|_o_LII|_                 
                |'._.'|  / | ==== | \                
                |  |  |  |_| ==== |_|                
                 \_|_/    ||" ||  ||                 
                 |-|-|    ||LI  o ||                 
                 |_|_|    ||'----'||                 
                /_/ \_\  /__|    |__\                

"""

s2 ="""


Input data must be of type pandas Dataframe ( ་ ⍸ ་ )


"""

s3 ="""


"Bounds must be integers! ಠ_ಠ



"""

s4 = """


adjusted_r2 needs to be boolean: True or False (ノಠ益ಠ)ノ




"""

s5 = """
Used to be Yoda
"""

s6 = """

____ ____ _  _ ____ _  _ ____ _  _    ____ ___ ____ ___ _ ____ ___ _ ____ ____ 
|    |__| |  | |___ |\/| |__| |\ |    [__   |  |__|  |  | [__   |  | |    [__  
|___ |  |  \/  |___ |  | |  | | \|    ___]  |  |  |  |  | ___]  |  | |___ ___] 

 Version 1.0                                            © Geoffrey Kasenbacher                                                                  


"""

stringlist = []
stringlist.append(s1)
stringlist.append(s2)
stringlist.append(s3)
stringlist.append(s4)
stringlist.append(s5)
stringlist.append(s6)
        
## this will solve all combinations of Y and X - linear regressions and return the one with highest R^2

class ExhaustiveSearch: 
    
    def __init__(self, data, remove, lowerbound, upperbound, adjusted_R2):
        self.data = data
        self.remove = remove
        self.lowerbound = lowerbound
        self.upperbound = upperbound
        self.adjusted_R2 = adjusted_R2
        
        ## Raising Expections and Warnings here
        if not isinstance(self.data, pd.DataFrame):   
            raise TypeError(stringlist[1])
        if not isinstance(self.remove, list):
            raise TypeError('This must be a list :-(')
        if not isinstance(self.lowerbound, int):
            raise TypeError(stringlist[2])
        if not isinstance(self.upperbound, int):
            raise TypeError(stringlist[2])
        if not isinstance(self.adjusted_R2, bool):
            raise TypeError(stringlist[3])
        if len(list(self.data)) > 15:
            warnings.warn(stringlist[0], Warning)
    
    def subset(self, X):
        _set = self.powerset(X)
        subset = []
        for i in _set:
            if self.upperbound >= len(i) >= self.lowerbound:
                subset.append(i)
        return subset
        
    def assign(self):
        XX = list(self.data)
        dic = {}
        for i in XX:
            Y = i
            #X = self.powerset([x for x in XX if x != Y])
            X = self.subset([x for x in XX if x != Y])
            dic[Y] = X
            if self.remove != None:
                for k in self.remove:
                    dic.pop(k, None)     
        return dic

    def powerset(self, X):
        target = []
        def combinations(target,X):
            for i in range(len(X)):
                new_target = copy.copy(target)
                new_data = copy.copy(X)
                new_target.append(X[i])
                new_data = X[i+1:]
                pp.append(new_target)
                combinations(new_target,new_data)
        pp = []
        combinations(target, X)
        return pp
    
    def regress(self, X, Y, data):
        regressor = LinearRegression()
        R = regressor.fit(self.data[X],self.data[Y])
        
        # Calculate R^2
        r2 = regressor.score(self.data[X], self.data[Y])
        
        # Calculate Adjusted R^2 
        n = len(self.data)
        k = len(list(self.data[X]))
        adj_r2 = (1 - ( ((1 - r2)*(n - 1))/(n - k - 1) ))
        
        if self.adjusted_R2 == True:
            return adj_r2
        else:
            return r2
    
    def search(self):
        dic = self.assign()
        newdic = {}
        for y in dic:
            for x in dic[y]:
                newdic[self.regress(x, y, data)] = y, x
        new={}
        sd = sorted(newdic.items(), reverse=True)
        for k,v in sd:
            new[k] = v
        return new
    
    def output(self,results):
        headers = ['Best Models', 'Y (Dependant Variable)', ' X (Explanatoy Variables)', 'R^2']
        R_2 =[]
        for i in range(10):
            R_2.append(list(results.keys())[i])

        ##get variables from tuples
        content = []
        for index,i in enumerate(R_2):
            y, x = results[i]
            row = []
            row.append('# {:<10}'.format(1+index))
            row.append(y)
            row.append(x)
            row.append(i)
            content.append(row)

        table = tabulate(content, headers,tablefmt='orgtbl')
        return table

    def solve(self):
        results = self.search()
        table = self.output(results)
        
        highest_R2 = list(results.keys())[0]
        best_vars = results[highest_R2]
        
        yvar, xvar = best_vars

        print('{} \n \n \n{}'.format(stringlist[5], table ))
        #print(table)
        return best_vars, results
    
## BruteForce Solves all models for a specified Y

class BruteForce: 
    
    def __init__(self, data, Y, lowerbound, upperbound, adjusted_R2):
        self.data = data
        self.Y = Y
        self.lowerbound = lowerbound
        self.upperbound = upperbound
        self.adjusted_R2 = adjusted_R2
        
        #warnings and exceptions
        if not isinstance(self.data, pd.DataFrame):   
            raise TypeError(stringlist[1])
        if not isinstance(self.Y, str):
            raise TypeError('This must be a string :D')
        if not isinstance(self.lowerbound, int):
            raise TypeError(stringlist[2])
        if not isinstance(self.upperbound, int):
            raise TypeError(stringlist[2])
        if not isinstance(self.adjusted_R2, bool):
            raise TypeError(stringlist[3])
        if len(list(self.data)) > 15:
            warnings.warn(stringlist[0], Warning)
            
        datalist = list(self.data)
        self.X = [x for x in datalist if x != Y]
        
    def subset(self, X):
        _set = self.powerset(X)
        subset = []
        for i in _set:
            if self.upperbound >= len(i) >= self.lowerbound:
                subset.append(i)
        return subset
   
    def powerset(self, X):
        target = []
        def combinations(target,X):
            for i in range(len(X)):
                new_target = copy.copy(target)
                new_data = copy.copy(X)
                new_target.append(X[i])
                new_data = X[i+1:]
                pp.append(new_target)
                #print(new_target)
                combinations(new_target,new_data)
        pp = []
        combinations(target, X)
        return pp
    
    def regress(self, X, Y, data):
        regressor = LinearRegression()
        R = regressor.fit(data[X],data[Y])  
        
        #returns R^2
        r2 = regressor.score(data[X], data[Y])
        
        # Calculates adjusted R^2
        n = len(data)
        k = len(self.X)
        adj_r2 = ( 1 - (( (1-r2)*(n-1) )/ (n - k -1)) )
        
        if self.adjusted_R2 == True:
            return adj_r2
        else:
            return r2
    
    def search(self):
        solutions = []
        combos = self.subset(self.X)
        for i in combos:
            solutions.append(self.regress(i, self.Y, self.data))  
        t = dict(zip(solutions, combos))
        
        results = {}
        sd = sorted(t.items(), reverse=True)
        for k,v in sd:
            results[k] = v
        return results
    
    def output(self,results):
        headers = ['Best Models', 'Y (Dependant Variable)', ' X (Explanatoy Variables)', 'R^2']
        R_2 =[]
        for i in range(10):
            R_2.append(list(results.keys())[i])

        ##get variables from tuples
        content = []
        for index,i in enumerate(R_2):
            x = results[i]
            row = []
            row.append('# {:<10}'.format(1+index))
            row.append(self.Y)
            row.append(x)
            row.append(i)
            content.append(row)
        table = tabulate(content, headers,tablefmt='orgtbl')
        return table
    
    def solve(self):
        results = self.search()
        table = self.output(results)
        
        highest_R2 = list(results.keys())[0]
        best_vars = results[highest_R2]
        
        #highest_R2 = combos[np.argmax(sol)]
        #R2 = max(sol)
        
        print('{} \n \n \n{}'.format(stringlist[5], table ))
        return best_vars, results

