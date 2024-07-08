# Monte Carlo Simulator

## Metadata  
### Name: Rachel Fellman
### Project: Monte Carlo Simulator - DS5100 Final Project


## Synopsis
### Installing & Importing the package
If you have access to this package it can be easily installed using the following code.

    pip install montecarlo

Next the package can be imported using the `import` function.  
    
    import montecarlo.montecarlo
The user can just import montecarlo, but I would suggest importing the module as well to make using this package easier.

### Creating Dice
Dice are created using the `Die` class. The user must create a numpy array which consists of the faces they want on their die. Below is an example:  
    
    die1 = np.array([1,2,3,4,5,6])   
    mydie = montecarlo.Die(die_arr)

From the instance of the `Die` class created, the weights of the faces of the die can be changed using the `change_weights` method. By default, the weight of each face of the die is set to 1.

The current weights and side of the die can be seen using the `get_current_state` method.

This `Die` class also gives the user the ability to roll the die a given number of times with the `roll_dice` method.

### Playing a Game
A game is created using the `Game` class. The `Game` class takes an input of a list of dice. The dice in the list should be objects created from the `Die` class explained above. All of the dice in this list should have the same number of sides and associated faces. See the game created below with 2 of the same dice:

    mygame = montecarlo.Game([mydie,mydie])

From this instance of the `Game` class the user can use the play method to roll the dice. With the play method, an input of the number of rolls for the game is required. In the example below, I will use 10 rolls. 

    mygame.play(10)

The results from this game can be seen using the `show_last_play` method, which returns a dataframe detailing the outcome of each roll.

### Analyzing a Game
A game is analyzed using the `Analyzer` class. The input for this class is a game object like the one created above. See below for an example of the `Analyzer` class:  
    
    myanalyzer = montecarlo.Analyzer(mygame)


The analyzer class has the following methods available: `count_jackpots`, `count_faces`, `combo_count`, and `permutation_count`. Below is an example of using the `count_jackpots` method which returns an integer.

    myanalyzer.count_jackpots() 


## API Descirption
This package includes one module: montecarlo. Within the montecarlo module there are 3 classes: Die, Game, and Analyzer. Below are the docstrings for each class. These can also be accessed by using the `help()` function.




### Die Class 

Create a die with the ability to change the weights of select faces of said die and roll the die, taking into account the weights.

Methods:

   -  **__init__**:   This is the initializer.
             The user must input a numpy array with faced for the die.
  
  -  **change_weight**: Changes the weight of one face of the die.
      
  
  -  **roll_die**:   Rolls the die a given number of times.
                The results for roll_die will change as if the weights for the die are changed.
  
  
   - **get_current_state**: Prints a data frame with the sides of the die as an index and the assigned weights for each side as the data.

Attributes: 
    
   - **faces**: NumPy array of the faces for a die.
    
Methods defined here:

---
 
**__init__(self, N)**
    
   - Initializer. 
   - It sets up the die with a given number of sides and adds a weight of 1 for each side of the die.

inputs:
 
   - N: Faces for a die.  
        N must be a NumPy array with unique values. 
        This method will return errors if those conditions are not met.
outputs:None

---

**change_weight(self, face, new_weight)**

   - Changes the weight of one specified side of the die by assigning the new weight to the data frame.

 inputs:
 
   - face:   The face from your die that you want to change the weight of.
            This must be in the initial NumPy array N.
            This method will throw an error if the face listed is not in the original numpy array N.
     
   - new_weight: This is the new weight you are assigning to a side. 
                This must be an integer or a float. 
                An error will be returned if it does not meet those conditions.
outputs: None

---

 **get_current_state(self)**
 - Prints a data frame with the sides of the die as an index and the assigned weights for each side as the data.

inputs: none
outputs:
 - die_df_index: data frame with the faces of the die as an index and a single column with the assigned weights for each face.
 
 ---
  
 **roll_dice(self, nrolls=1)**
- Takes a sample of the sides using the assigned weights, and prints the results of the rolls as a list.

inputs:
- nrolls: Default set to one unless the user reassigns it. 
        Nrolls should be an integer.
outputs:
 - results: a python list of the results of the rolls





### Game Class

Gives the user the ability to roll one or more similar die. 
The die should have the same number of sides and associated faces.
Game is initialized with a python list of one or more dice created from the die class.
Game gives the user the ability to "roll" the inputed dice a given number of times.

Methods:
- **__init__**:   Initializer. It takes an input of a python list of dice.
  
- **play**:   The user calls this method to "roll" the die. The user is able to specify the number of rolls.
            The die are sampled, taking into account the given weights, for the number of rolls specified and the output is stored in a private dataframe.

- **show_last_play**: Method to see the results of their most recent play.
                    A dataframe of the results is returned.
 
Attributes:

- **die_list**: Python list of dice, where each element of the list is a single die.
 
 
 Methods defined here:
 
 ---
 **__init__(self, dielist)**
- Initializer for the Game class
inputs:
- dielist:   Python list of dice created using the Die class.
            The die in die list should have the same number of sides and associated faces.
outputs:
- dielist: Python list of dice, where each element of the list is a single die.

---

**play(self, rolls)**
 - Allows user to "roll" the die.
- Samples the faces of the die for a given number of rolls based on the given weights and saves the result in a private dataframe.

inputs:
 - **rolls**:  Integer
                Specifies how many time the die should be "rolled"/sampled.
outputs:none

---

**show_last_play(self, format='wide')**
- Used to see the results of the most recent play. 
- Returns dataframe created by data in the play class.
- The data can be returned in 'narrow' or 'wide' format and an error will be raised if a different format is supplied by the user.

inputs:
- format: "narrow" or "wide"
    Format defaults to wide but the user can choose to have the data presented in narrow format by entering "narrow".
 outputs:
 - last_play:  Dataframe of the results of the most recent play. 
         Can be in either wide or narrow format.





### Analyzer Class

Takes the results of a game played via the Game class and computes statistics about said game.

Methods:
 - **__init__**:   Initializer. It takes in an instance of the Game class.
                 If the input is not an instance of the Game class, a ValueError will be raised.
                 A dataframe named data is created. Data holds the information for the last play from the game class. 
- **count_jackpots**: A jackpot is when all the faces for a given roll are the same.
                    The count_jackpots method counts the number of times a game resulted in a jackpot and returns an integer.
 
 - **count_faces**:    Calculates the number of times a given face is returned for a roll.
             A dataframe of the results is returned.
  
 - **combo_count**:    Counts the number of distinct combinations among the rolls.
         A distinct combination is order-independent and can included repetitions.
        A data frame of the combinations and associated counts is returned.
 
 - **permutation_count**:  Counts the number of disinct permutations among the rolls.
         A distinct permutation is order-dependent and can include repetitions.
         A data frame of the permutations and counts is returned.

Attributes:
- **data**: a data frame of the last play.
  
  
Methods defined here:
 
**__init__(self, game)**
- Initializer. Takes in a an instance of the Game class. 
- From the input of the game class the method show_last_play is called to create a data frame of the the last play.

Inputs:
- game:   A Game object/instnace of the game class.
         If game is not a Game object, a ValueError will be raised.
 Outputs: 
  - data: Data frame of the last play.
 
--- 
 
**count_combos(self)**
 - This method calculates the distinct combination of faces rolled and their counts.
 - A distinct combination is not dependent on order and may have repetitions.

Inputs: none
Outputs: 
- combo_count_df: Dataframe with a MultiIndex of distinct combinations and a single column for the associated counts.

 ---
 
**count_faces(self)**
- Counts the number of times a given face appears in one roll using the value_counts() method with a lambda function.
- The lambda function is the applied across the data frame to calculate the face counts for each roll.

inputs: none
outputs: 
- face_count: Data frame with roll number as the index, faces as the columns and counts for each face appearance as the data.

---

***count_jackpots(self)***
- Calculates the number of times a game resulted in a jackpot and returns and integer.
- A jackpot is when all the races for a given roll are the same.
- For each row of the data, this method finds the number of unique values. If the number of unique values is greater than 1, that roll was not a jackpot.
- For each row where the number of unique values is equal to one, the jackpot count goes up by one.

inputs:none
outputs: 
- jack_count: integer, the number of jackpots

---

***count_permutations(self)***
- Calculates the distinct permutations of faces rolled in a game and their counts.
- A permutaiton is dependent on order and may contain repetitions.

inputs:none
outputs:
- perm_count_df: Datareame with a MultiIndex of distinct permutations and a column for the associated counts.
