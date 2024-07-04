import pandas as pd
import numpy as np
        

        
class Die:

    '''
    Create a weighted die with the option to roll it.
    ---
    
    Methods:
    ---
    __init__:   This is the initializer.
                The user must input a numpy array with faced for the die.
    
    change_weight: changes the weight of one face of the die.
        

    roll_die:   This rolls the die a given number of times.
                The results for roll_die will change as if the weights for the die are changed.
    
    
    get_current_state: prints a data frame with the sides of the die as an index and the assigned weights for each side as the data.
 
    '''

    def __init__(self, N):
        '''
        This is the initializer. It sets up the die with a given number of sides and adds a weight of 1 for each side of the die.
        A private dataframe is also created. This dataframe has the sides of the die as an index and the weights as the data in a column.

        ---
        inputs:
        N:  N is the number of faces for a die.  
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
        This changes the weight of one specified side of the die by assigning the new wieght to the data frame.
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
        Roll_die calculates the probability for each side of the die from the assigned weights.
        It then takes a sample of the sides using the calculated probabilities, and prints the results of the rolls as a list.
        ---
        inputs:
        nrolls: This is set to one unless the user reassigns it. 
                Nrolls should be an integer.
        outputs:
        results: a python list of the results of the rolls
        '''
        
        results = []
        die_probs = [i/sum(self.__die_df['weights']) for i in self.__die_df['weights']]
        for i in range(nrolls):
            result = self.__die_df.side.sample(weights=die_probs).values[0].tolist()
            results.append(result)
        print(results)
    
    def get_current_state(self):
        '''
        get_current_state prints a data frame with the sides of the die as an index and the assigned weights for each side as the data.
        ---
        inputs: none
        outputs:
        die_df_index: a data frame with the faces of the die as an index and a single column with the assigned weights for each face.
        '''
        
        return self.__die_df_index
    

    
    
class Game:
    '''
    The Game class gives the user the ability to roll one or more similar die. The die should have the same number of sides and associated faces.
    The game is initialized with a python list of one or more dice created from the die class.
    Game gives the user the ability to "roll" the inputed dice a given number of times.
    ---
    Methods:
    __init__:   This is the initializer. It takes an input of a python list of dice.

    play:   The user calls this method to "roll" the die. The user is able to specify the number of rolls.
            Play calculates the probability of each face based on the weights assigned to each side of the die.
            The die are sampled for the number of rolls specified and the output is stored in a private dataframe.

    show_last_play:  The user calls this method to see the results of their most recent play.
                    A dataframe of the results is returned.
    '''
    def __init__(self, die_list):
        '''
        This is the initializer for the Game class
        ---
        inputs:
        die_list:   die_list is a python list of dice created using the Die class.
                    The die in die list should have the same number of sides and associated faces.
        outputs:
        die_list: a python list of dice, where each element of the list is a single die.
        '''
        self.die_list = die_list
    
    def play (self, rolls):
        '''
        This method allows the user to "roll" the die. The probability of each face is calculated using the weights given in the die_list.
        The play method samples the faces of the die for a given number of rolls based on the calculated probabilites and saves the result in a private dataframe.
        ---
        inputs:
        rolls:  integer
                rolls is an integer that specified how many time the die should be "rolled"/sampled.
        outputs:none
        '''
        die_probs = list(range(len(self.die_list)))
        for x in range(0,len(self.die_list)):
            die_probs[x] = [i/sum(self.die_list[x]['weights']) for i in self.die_list[x]['weights']]

        newlist= list(range(len(self.die_list)))
        for y in range(len(self.die_list)):
            newlist[y] = pd.DataFrame({'side':self.die_list[y].index.tolist(),
                               'die_probs':die_probs[y]})   

        results=  list(range(len(dielist)))
        for k in range(len(dielist)):
            test = newlist[k]
            results[k] = [test.side.sample(weights=die_probs[k]).values[0].tolist() for i in range(rolls)]
    
        self.__outcome = pd.DataFrame(columns = list(range(len(dielist))),
                                index= list(range(rolls)),
                                data = []
                                 )
        length =  len(self.__outcome.columns)
        for col in range(length):
            self.__outcome[col] = results[col]
        self.__outcome.index.name = 'roll_number'

    def show_last_play (self, format = "wide"):
        ''' 
        show_last_play is used to see the results of the most recent play. This method returns the private dataframe created by the play class.
        The data can be returned in 'narrow' or 'wide' format and an error will be raised if a differnt format is supplied by the user.
        ---
        inputs:
        format: "narrow" or "wide"
                format defaults to wide but the user can choose to have the data presented in narrow format by entering "narrow".
        outputs:
        last_play:  a dataframe of the results of the most recent play. 
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
    The Analyzer class takes the results of a game played via the Game class and computes statistics about said game.
    ---
    methods:
    __init__:   this is the initializer. It takes in an instance of the Game class.
                If the input is not an instance of the Game class, a ValueError will be raised.
                A dataframe named data is created. Data holds the information for the last play from the game class.

    count_jackpots: A jackpot is when all the faces for a given roll are the same.
                    The count_jackpots method counts the number of times a game resulted in a jackpot and returns an integer.

    count_faces:    This calculates the number of times a given face is returned for a roll.
                    A dataframe of the resutls is returned.

    combo_count:    This counts the number of distinct combinations among the rolls.
                    A distinct combination is order-independent and can included repetitions.
                    A data frame of the combinations and associated counts is returned.

    permutation_count:  This method counts the number of disinct permutations among the rolls.
                        A distinct permutation is order-dependent and can include repetitions.
                        A data frame of the permutations and counts is returned.

    '''  
    def __init__(self, game):
        ''' 
        This is the initializer. It takes in a an instance of the Game class. 
        From the input of the game class the method show_last_play is called to create a data frame of the the last play.
        ---
        inputs:
        game:   a Game object/instnace of the game class.
                If game is not a Game object, a ValueError will be raised.
        outputs: 
        attributes: data: a data frame of the last play.
        '''
        if not isinstance(game, Game):
            raise ValueError("This is not a Game object. Please input a Game object.")
        else:
            self.data = game.show_last_play()

    def count_jackpots(self):
        ''' 
        The count_jackpots method calculated the numbe rof times a game resulted in a jackpot and returns and integer.
        A jackpot is when all the races for a given roll are the same.
        For each row of the data, this method finds the number of unique values. If the number of unique values is greater than 1, that roll was not a jackpot.
        For each row where the number of unique values is equal to one, the jackpot count goes up by one.
        ---
        inputs:none
        outputs: 
        integer
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
        The count_faces method counts the number of times a given face appears in one roll using the value_counts() method with a lambda function.
        The lambda function is the applied across the data frame to calculate the face counts for each roll.
        ---
        inputs: none
        outputs: 
        face_count: data frame with roll number as the index, faces as the columns and counts for each face appearance as the data.
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
        combo_count_df: a dataframe with a MultiIndex of distinct combinations and a single column for the associated counts.
        '''
        row_combos = self.data.apply(lambda row: tuple(sorted(row)), axis = 1)
        combo_count = row_combos.value_counts()
        combo_count_df = pd.DataFrame(combo_count)
        combo_count_df.index.name = "combinations"
        return combo_count_df
    
    def count_permutations(self):
        ''' 
        count_permutations calculates the distinct permutations of faces rolled in a game and their counts.
        A permutaiton is dependent on order and may contain repetitions.
        ---
        inputs:none
        outputs:
        perm_count_df: a datareame with a MultiIndex of distinct permutations and a column for the associated counts.
        '''
        row_perm = x.apply(lambda row: tuple(row), axis = 1)
        perm_count = row_perm.value_counts()
        perm_count_df = pd.DataFrame(perm_count)
        perm_count_df.index.name = "permutaions"
        return perm_count_df