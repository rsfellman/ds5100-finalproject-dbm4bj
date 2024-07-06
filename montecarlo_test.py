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
    This tests to make sure the Game class is functioning as expected.
    ---
    methods:
    test_05_initializer: This tests to make sure our initializer creates and attribute which is equal to out input for an instance of the Game class.
    test_06_play: This tests to see if the play method correctly sampled the dice for a given number of rolls.
    test_07_show_last_play: This tests to make sure the output of the show_last_play method is a dataframe.
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
    '''
    The AnalyzerTestSuite has a series of unittests to make sure the Analyzer class from the montecarlo simulation is functioning as expected.
    ---
    methods:
    test_08_initializer: This tests that the attribute data created is a dataframe.
    test_09_count_jackpots: This tests that the number of jackpots is counted correctly and returned as an integer.
    test_10_count_faces: This tests if the count_faces method correctly counts the number of faces.
    test_11_count_combos: This tests to see if the output of the count_combos method is a dataframe with a MultiIndex by calculating the numbers of levels in the index.
    test_12_count_permutations: This tests the the output of the count_permutations method is a dataframe with a MultiIndex.

    
    '''
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
        '''
        This tests that the number of jackpots is counted correctly and returned as an integer.
        This test will set every die to have one face so every roll should be a jackpot.
        For the purpose of this test we ignore the fact that it is imposible to have a one sided die unless it is a mobius strip of some sort.
        '''
        dice = [1]
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
        self.assertTrue((myanalyzer.count_jackpots() == nrolls) & (isinstance(myanalyzer.count_jackpots(), int)))


    def test_10_count_faces(self):
        '''
        This tests if the count_faces method correctly counts the number of faces.
        Ignoring reality once again, we will have one sided dice, so the face count for each roll should be equal to the number of dice rolled, in this case 4.
        This test will also confirm that the output is a dataframe.
        '''
        dice = [1]
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
        num_dice = 4
        face_counts = myanalyzer.count_faces().loc[0].tolist()
        self.assertTrue((face_counts[0]== num_dice) & (isinstance(myanalyzer.count_faces(), pd.DataFrame)))

    def test_ll_count_combos(self):
        '''
        This tests to see if the output of the count_combos method is a dataframe with a MultiIndex by calculating the numbers of levels in the index.
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
        mycombos = myanalyzer.count_combos()
        self.assertTrue((mycombos.index.nlevels > 1) & isinstance(mycombos, pd.DataFrame))


    def test_12_count_permutations(self):
        '''
        This tests the the output of the count_permutations method is a dataframe with a MultiIndex.
        The MultiIndex is tested by counding the number of levels in the index.
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
        mypermutations = myanalyzer.count_permutations()
        self.assertTrue((mypermutations.index.nlevels > 1) & isinstance(mypermutations, pd.DataFrame))


if __name__ == '__main__':
    unittest.main()