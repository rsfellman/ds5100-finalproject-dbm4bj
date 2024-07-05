import pandas as pd
import numpy as np
from montecarlo.montecarlo import Die
from montecarlo.montecarlo import Game
from montecarlo.montecarlo import Analyzer
import unittest

class DieTestSuite(unittest.TestCase):
    '''
    This module tests the methods in the die class unsing unittest.

    Methods:
    test_01_initializer: This tests if a numpy array of the faces is created/stored
    test_02_change_weight: checks to see if the new weight is stored in the data frame with the correct side.
    test_03_roll_die:Tests if the results are a list containing faces of the die.
        This is done using the all method to see if the results are in our originial list of die faces and isinstance to make sure it is a list. 
    test_04_get_current_state: This tests if the outcome of this method is a dataframe with a column for wieghts.
    '''
    def test_01_initializer(self):
        '''
        This tests if a numpy array of the faces is created/stored
        '''
        die1 = [1,2,3,4,5,6]
        die_arr = np.array(die1)
        mydie = Die(die_arr)
        self.assertIsInstance(mydie.faces, np.ndarray)

    def test_02_change_weight(self):
        '''
        checks to see if the new weight is stored in the data frame with the correct side.
        '''
        die1 = [1,2,3,4,5,6]
        die_arr = np.array(die1)
        mydie = Die(die_arr)
        face = 2
        weight = 100
        mydie.change_weight(face,weight)
        die_weight = mydie.get_current_state()
        self.assertEqual(100, die_weight.loc[face, 'weights'])

    def test_03_roll_dice(self):
        '''
        Tests if the results are a list containing faces of the die.
        This is done using the all method to see if the results are in our originial list of die faces and isinstance to make sure it is a list.
        '''
        die1 = [1,2,3,4,5,6]
        die_arr = np.array(die1)
        mydie = Die(die_arr)
        myroll = mydie.roll_dice(10)
        self.assertTrue(all(e in die1 for e in myroll)& isinstance(myroll,list))

    def test_04_get_current_state(self):
        '''
        This tests if the outcome of this method is a dataframe with a column for wieghts.
        '''
        die1 = [1,2,3,4,5,6]
        die_arr = np.array(die1)
        mydie = Die(die_arr)
        current_die = mydie.get_current_state()
        self.assertTrue(isinstance(current_die,pd.DataFrame) & (current_die.columns == 'weights'))


class GameTestSuite(unittest.TestCase):
    '''
    This test to make sure the Game class is functioning as expected
    '''
    def test_05_initializer(self):
        '''
        This tests to make sure our initializer creates and attribute which is equal to out input for an instance of the Game class.
        '''
        dice = [1,2,3,4]
        dice_arr = np.array(dice)
        die1 = Die(dice_arr)
        die2 = Die(dice_arr)
        die3 = Die(dice_arr)
        die4 = Die(dice_arr)
        die1_state = die1.get_current_state()
        die2_state = die2.get_current_state()
        die3_state = die3.get_current_state()
        die4_state = die4.get_current_state()
        dice_list = [die1_state, die2_state, die3_state, die4_state]
        mygame = Game(dice_list)
        self.assertEqual(dice_list, mygame.die_list)

    def test_06_play(self):
        '''
        this tests to see if the play method correctly sampled the dice for a given number of rolls.
        '''
        dice = [1,2,3,4]
        dice_arr = np.array(dice)
        die1 = Die(dice_arr)
        die2 = Die(dice_arr)
        die3 = Die(dice_arr)
        die4 = Die(dice_arr)
        die1_state = die1.get_current_state()
        die2_state = die2.get_current_state()
        die3_state = die3.get_current_state()
        die4_state = die4.get_current_state()
        dice_list = [die1_state, die2_state, die3_state, die4_state]
        mygame = Game(dice_list)
        nrolls = 10
        mygame.play(nrolls)
        self.assertTrue(nrolls == len(mygame.show_last_play()))
    
    def test_07_show_last_play(self):
        '''
        This tests to make sure the output of the show_last_play method is a dataframe.
        '''
        dice = [1,2,3,4]
        dice_arr = np.array(dice)
        die1 = Die(dice_arr)
        die2 = Die(dice_arr)
        die3 = Die(dice_arr)
        die4 = Die(dice_arr)
        die1_state = die1.get_current_state()
        die2_state = die2.get_current_state()
        die3_state = die3.get_current_state()
        die4_state = die4.get_current_state()
        dice_list = [die1_state, die2_state, die3_state, die4_state]
        mygame = Game(dice_list)
        nrolls = 10
        mygame.play(nrolls)
        myplay = mygame.show_last_play()
        self.assertIsInstance(myplay, pd.DataFrame)


class AnalyzerTestSuite(unittest.TestCase):

    def test_08_initializer(self):
        '''
        this tests that the attribute data created is a dataframe.
        '''
        dice = [1,2,3,4]
        dice_arr = np.array(dice)
        die1 = Die(dice_arr)
        die2 = Die(dice_arr)
        die3 = Die(dice_arr)
        die4 = Die(dice_arr)
        die1_state = die1.get_current_state()
        die2_state = die2.get_current_state()
        die3_state = die3.get_current_state()
        die4_state = die4.get_current_state()
        dice_list = [die1_state, die2_state, die3_state, die4_state]
        mygame = Game(dice_list)
        nrolls = 10
        mygame.play(nrolls)
        myanalyzer = Analyzer(mygame)
        mydata = myanalyzer.data
        self.assertIsInstance(mydata, pd.DataFrame)

    def test_09_count_jackpots(self):

if __name__ == '__main__':
    unittest.main()
 