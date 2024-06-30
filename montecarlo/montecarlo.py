import pandas as pd
import numpy as np
        
class Die:

    '''
    Roll a weighted die.
    ---
    
    Methods:
    ---
    __init__: This is the initializer.
    It sets the weight for each side of the die to 1 creates a private dataframe 
    with the sides of the die as the index and the weights as the column.
        N: N is the number of faces for a die. 
            N must be a NumPy array with unique values. 
            This method will return errors if those conditions are not met.
    
    change_weight: changes the weight of one face of the die.
        face: the face from your die that you want to change the weight of.
            This must be in the initial NumPy array N.
        new_weight: this is the new weight you are assigning to a side. 
            This must be an integer or a float. An error will be returned if it does not meet those conditions.

    roll_die: This rolls the die a given number of times.
    roll_die calculates the probability for each side of the die from the assigned weights.
    It then takes a sample of the sides using the calculated probabilities, 
    and prints the results of the rolls as a list.
        nrolls: This is set to one unless the user reassigns it. Nrolls should be an integer.
    
    get_current_state: This method has no inputs
    get_current_state prints a data frame with the sides of the die as an index and 
    the assigned weights for each side as the data.


    '''

    def __init__(self, N):
        if not isinstance (N, np.ndarray):
            raise TypeError("The N number of sides must be a NumPy array")
        if len(N) != len(np.unique(N)):
            raise ValueError("The faces must be unique values")
        else:
            self.faces = N
        weights = [1 for _ in range(len(self.faces))]
        self.__die_df = pd.DataFrame({            
            'side': [n for n in self.faces],
            'weights': weights
        })
        self.__die_df_index = die_df.set_index(['side'])

    def change_weight(self, face, new_weight):
        if face not in self.faces:
            raise IndexError("The face for which the weight is altered needs to be one of the existing faces")
        if not isinstance(new_weight,(float,int)):
            raise TypeError("The new weight must be a float or integer")
        else:
            self.__die_df_index.loc[face]= new_weight

    def roll_dice(self, nrolls=1):
        results = []
        die_probs = [i/sum(self.__die_df['weights']) for i in self.__die_df['weights']]
        for i in range(nrolls):
            result = self.__die_df.side.sample(weights=die_probs).values[0].tolist()
            results.append(result)
        print(results)
    
    def get_current_state(self):
        return self.__die_df_index

    
    
class Game:
    def __init__:
        pass

class Analyzer:
    def __init__:
        pass
    