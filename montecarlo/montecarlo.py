import pandas as pd
import numpy as np
        

        
class Die:

    '''
    Create a die with the ability to change the weights of select faces of said die and roll the die, taking into account the weights.
    ---
    
    Methods:
    ---
    __init__:   This is the initializer.
                The user must input a numpy array with faced for the die.
    
    change_weight: Changes the weight of one face of the die.
        

    roll_die:   Rolls the die a given number of times.
                The results for roll_die will change as if the weights for the die are changed.
    
    
    get_current_state: Prints a data frame with the sides of the die as an index and the assigned weights for each side as the data.
    
    ---
    Attributes: 
    faces: NumPy array of the faces for a die.
 
    '''

    def __init__(self, N):
        '''
        Initializer. 
        It sets up the die with a given number of sides and adds a weight of 1 for each side of the die.
        A private dataframe is also created. 
        The private dataframe has the sides of the die as an index and the weights as the data in a column.

        ---
        inputs:
        N:  Faces for a die.  
            N must be a NumPy array with unique values. 
            This method will return errors if those conditions are not met.
        outputs:None
        
        '''
        
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
        self.__die_df_index = self.__die_df.set_index(['side'])

    def change_weight(self, face, new_weight):
        '''
        Changes the weight of one specified side of the die by assigning the new weight to the data frame.
        ---
        inputs:
        face:   The face from your die that you want to change the weight of.
                This must be in the initial NumPy array N.
                This method will throw an error if the face listed is not in the original numpy array N.

        new_weight: This is the new weight you are assigning to a side. 
                    This must be an integer or a float. 
                    An error will be returned if it does not meet those conditions.
        outputs: None
        '''
        
        if face not in self.faces:
            raise IndexError("The face for which the weight is altered needs to be one of the existing faces")
        if not isinstance(new_weight,(float,int)):
            raise TypeError("The new weight must be a float or integer")
        else:
            self.__die_df_index.loc[face]= new_weight

    def roll_dice(self, nrolls=1):
        '''
        Calculates the probability for each side of the die from the assigned weights.
        Next, takes a sample of the sides using the calculated probabilities, and prints the results of the rolls as a list.
        ---
        inputs:
        nrolls: Default set to one unless the user reassigns it. 
                Nrolls should be an integer.
        outputs:
        results: a python list of the results of the rolls
        '''
        
        results = []
        die_probs = [i/sum(self.__die_df['weights']) for i in self.__die_df['weights']]
        for i in range(nrolls):
            result = self.__die_df.side.sample(weights=die_probs).values[0].tolist()
            results.append(result)
        return results
    
    def get_current_state(self):
        '''
        Prints a data frame with the sides of the die as an index and the assigned weights for each side as the data.
        ---
        inputs: none
        outputs:
        die_df_index: data frame with the faces of the die as an index and a single column with the assigned weights for each face.
        '''
        
        return self.__die_df_index
    

    
    
class Game:
    '''
    Gives the user the ability to roll one or more similar die. 
    The die should have the same number of sides and associated faces.
    Game is initialized with a python list of one or more dice created from the die class.
    Game gives the user the ability to "roll" the inputed dice a given number of times.
    ---
    Methods:
    __init__:   Initializer. It takes an input of a python list of dice.

    play:   The user calls this method to "roll" the die. The user is able to specify the number of rolls.
            Calculates the probability of each face based on the weights assigned to each side of the die.
            The die are sampled for the number of rolls specified and the output is stored in a private dataframe.

    show_last_play: Method to see the results of their most recent play.
                    A dataframe of the results is returned.
    ---
    attributes:
    die_list: Python list of dice, where each element of the list is a single die.
    '''
    def __init__(self, dielist):
        '''
        Initializer for the Game class
        ---
        inputs:
        dielist:   Python list of dice created using the Die class.
                    The die in die list should have the same number of sides and associated faces.
        outputs:
        dielist: Python list of dice, where each element of the list is a single die.
        '''
        die_list = list(range(len(dielist)))
        for i in range(len(dielist)):
            die_list[i] = dielist[i].get_current_state()
        
        self.die_list = die_list
    
    def play (self, rolls):
        '''
        Allows user to "roll" the die.
        Probability of each face being rolled is calculated using the weights given in the die_list.
        Samples the faces of the die for a given number of rolls based on the calculated probabilites and saves the result in a private dataframe.
        ---
        inputs:
        rolls:  Integer
                Specifies how many time the die should be "rolled"/sampled.
        outputs:none
        '''
        die_probs = list(range(len(self.die_list)))
        for x in range(0,len(self.die_list)):
            die_probs[x] = [i/sum(self.die_list[x]['weights']) for i in self.die_list[x]['weights']]

        newlist= list(range(len(self.die_list)))
        for y in range(len(self.die_list)):
            newlist[y] = pd.DataFrame({'side':self.die_list[y].index.tolist(),
                               'die_probs':die_probs[y]})   

        results=  list(range(len(self.die_list)))
        for k in range(len(self.die_list)):
            test = newlist[k]
            results[k] = [test.side.sample(weights=die_probs[k]).values[0].tolist() for i in range(rolls)]
    
        self.__outcome = pd.DataFrame(columns = list(range(len(self.die_list))),
                                index= list(range(rolls)),
                                data = []
                                 )
        length =  len(self.__outcome.columns)
        for col in range(length):
            self.__outcome[col] = results[col]
        self.__outcome.index.name = 'roll_number'

    def show_last_play (self, format = "wide"):
        ''' 
        Used to see the results of the most recent play. 
        Returns the private dataframe created by the play class.
        The data can be returned in 'narrow' or 'wide' format and an error will be raised if a different format is supplied by the user.
        ---
        inputs:
        format: "narrow" or "wide"
                Format defaults to wide but the user can choose to have the data presented in narrow format by entering "narrow".
        outputs:
        last_play:  Dataframe of the results of the most recent play. 
                    Can be in either wide or narrow format.
        '''
        if format == "wide":
            last_play = self.__outcome
            return last_play
        if format == "narrow":
            last_play = pd.DataFrame(self.__outcome.unstack())
            return last_play
        else:
            raise TypeError(f"{format} is not an acceptable format. Please enter 'narrow' or 'wide'")
             
    


class Analyzer:
    ''' 
    Takes the results of a game played via the Game class and computes statistics about said game.
    ---
    methods:
    __init__:   Initializer. It takes in an instance of the Game class.
                If the input is not an instance of the Game class, a ValueError will be raised.
                A dataframe named data is created. Data holds the information for the last play from the game class.

    count_jackpots: A jackpot is when all the faces for a given roll are the same.
                    The count_jackpots method counts the number of times a game resulted in a jackpot and returns an integer.

    count_faces:    Calculates the number of times a given face is returned for a roll.
                    A dataframe of the results is returned.

    combo_count:    Counts the number of distinct combinations among the rolls.
                    A distinct combination is order-independent and can included repetitions.
                    A data frame of the combinations and associated counts is returned.

    permutation_count:  Counts the number of disinct permutations among the rolls.
                        A distinct permutation is order-dependent and can include repetitions.
                        A data frame of the permutations and counts is returned.
    ---
    attributes:
    data: a data frame of the last play.

    '''  
    def __init__(self, game):
        ''' 
        Initializer. Takes in a an instance of the Game class. 
        From the input of the game class the method show_last_play is called to create a data frame of the the last play.
        ---
        inputs:
        game:   A Game object/instnace of the game class.
                If game is not a Game object, a ValueError will be raised.
        outputs: 
        data: Data frame of the last play.
        '''
        if not isinstance(game, Game):
            raise ValueError("This is not a Game object. Please input a Game object.")
        else:
            self.data = game.show_last_play()

    def count_jackpots(self):
        ''' 
        Calculates the number of times a game resulted in a jackpot and returns and integer.
        A jackpot is when all the races for a given roll are the same.
        For each row of the data, this method finds the number of unique values. If the number of unique values is greater than 1, that roll was not a jackpot.
        For each row where the number of unique values is equal to one, the jackpot count goes up by one.
        ---
        inputs:none
        outputs: 
        jack_count: integer, the number of jackpots
        '''
        jack_count = 0
        for i in range(len(self.data)):
            if len(self.data.iloc[i].unique()) == 1:
                jack_count += 1
            else:
                jack_count = jack_count
        return jack_count
    
    def count_faces(self):
        ''' 
        Counts the number of times a given face appears in one roll using the value_counts() method with a lambda function.
        The lambda function is the applied across the data frame to calculate the face counts for each roll.
        ---
        inputs: none
        outputs: 
        face_count: Data frame with roll number as the index, faces as the columns and counts for each face appearance as the data.
        '''
        row_count = lambda row: row.value_counts()
        face_count = self.data.apply(row_count, axis = 1).fillna(0).astype(int)
        return face_count
    
    def count_combos(self):
        ''' 
        This method calculates the distinct combination of faces rolled and their counts.
        A distinct combination is not dependent on order and may have repetitions.
        ---
        inputs: none
        outputs: 
        combo_count_df: Dataframe with a MultiIndex of distinct combinations and a single column for the associated counts.
        '''
        row_combos = self.data.apply(lambda row: tuple(sorted(row)), axis = 1)
        combo_count = row_combos.value_counts()
        combo_count_df = pd.DataFrame(combo_count)
        combo_count_df.index = pd.MultiIndex.from_tuples(combo_count_df.index)
        return combo_count_df
    
    def count_permutations(self):
        ''' 
        Calculates the distinct permutations of faces rolled in a game and their counts.
        A permutaiton is dependent on order and may contain repetitions.
        ---
        inputs:none
        outputs:
        perm_count_df: Datareame with a MultiIndex of distinct permutations and a column for the associated counts.
        '''
        row_perm = self.data.apply(lambda row: tuple(row), axis = 1)
        perm_count = row_perm.value_counts()
        perm_count_df = pd.DataFrame(perm_count)
        perm_count_df.index = pd.MultiIndex.from_tuples(perm_count_df.index)
        return perm_count_df