import unittest
import new_word_ladder
class TestWordLadder(unittest.TestCase):

    def setUp(self):
        print("                                        Setup   ")
        print('Try wrong dictionary name')
        self.wrong_name = new_word_ladder.initialise('sdfnjkdhdfnks.txt')  # a garbage name
        
        print("Initialise")
        new_word_ladder.initialise('dictionary.txt')
        
        print('Setup start and target such that they are not in dictionary !')
        self.word_not_in_dic1 = new_word_ladder.solution('asdd','lead',[])
        self.word_not_in_dic2 = new_word_ladder.solution('asd','lsd',[])
        self.word_not_in_dic3 = new_word_ladder.solution('lead','lsdd',[])

        print('Setup start and target of different lengths')
        self.different_len_start_and_target1 = new_word_ladder.solution('load','aa',[])
        self.different_len_start_and_target2 = new_word_ladder.solution('god','load',[])

        print('Setup same start and target')
        self.start_equalto_target = new_word_ladder.solution('load','load',[])
        
        

        print('Setup no path condition')
        self.nopath = new_word_ladder.solution('abamp','abash',[])

        print('Setup Input as (lead,gold) and (hide,seek) to complete in 3 and 6 steps as opposed to 481 and 434 steps')
        self.program_steps1 = new_word_ladder.solution('lead','gold',[])
        self.program_steps2 = new_word_ladder.solution('hide','seek',[])

        print('\n\n ######## Done Setup ########')
        
        
    def tearDown(self):
        print('\n\n')
        print("                                       Cleanup ")
        print('Delete all variables created')
        del self.word_not_in_dic1
        del self.word_not_in_dic2
        del self.word_not_in_dic3
        del self.different_len_start_and_target1
        del self.different_len_start_and_target2
        del self.start_equalto_target

        del new_word_ladder.all_words
        del new_word_ladder.in_dic
        del self.wrong_name
        del self.program_steps1
        del self.program_steps2

        print('\n\n ######## Done Cleaning ########')
        

    def test_input(self):

        self.assertEqual(self.word_not_in_dic1,'Start or target not found in given dictionary')
        self.assertEqual(self.word_not_in_dic2,'Start or target not found in given dictionary')
        self.assertEqual(self.word_not_in_dic3,'Start or target not found in given dictionary')

        self.assertEqual(self.different_len_start_and_target1,'Start and Target are of different length')
        self.assertEqual(self.different_len_start_and_target2,'Start and Target are of different length')

        self.assertTrue(self.start_equalto_target.startswith('1'))

        self.assertEqual(self.wrong_name,0)
        self.assertEqual(self.nopath,'No path found')

        self.assertTrue(self.program_steps1.startswith('3'))
        self.assertTrue(self.program_steps2.startswith('6'))
    
if __name__=="__main__":
    unittest.main()
