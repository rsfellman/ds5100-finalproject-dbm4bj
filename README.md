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
    
   - faces: NumPy array of the faces for a die.
    
Methods defined here:
 
-**__init__(self, N)**
    
   - Initializer. 
   - It sets up the die with a given number of sides and adds a weight of 1 for each side of the die.

inputs:
 
   - N: Faces for a die.  
        N must be a NumPy array with unique values. 
        This method will return errors if those conditions are not met.
outputs:None

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

 **get_current_state(self)**
 - Prints a data frame with the sides of the die as an index and the assigned weights for each side as the data.

inputs: none
outputs:
 - die_df_index: data frame with the faces of the die as an index and a single column with the assigned weights for each face.
  
 **roll_dice(self, nrolls=1)**
 - Calculates the probability for each side of the die from the assigned weights.
 - Next, takes a sample of the sides using the calculated probabilities, and prints the results of the rolls as a list.

inputs:
- nrolls: Default set to one unless the user reassigns it. 
        Nrolls should be an integer.
outputs:
 - results: a python list of the results of the rolls

---




