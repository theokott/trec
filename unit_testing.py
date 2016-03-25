__author__ = '2146734s'

from populate_trec import *

import unittest

from trec_eval_app.models import Track, Task, UserProfile, Run

#                Class TestTrecEvaluator
#    This class implements the unit testing methodology.
#    Two test cases are implemented on the populate_trec.py script.

class TestTrecEvaluator(unittest.TestCase):

    def test_add_track(self):  #Test testing the insertion of a track.
        testTrack = add_track(0,"testTrack1","First unit test: this Track tests the method add_track")  #All the attributes of the new track are checked.
        self.assertEqual(testTrack.name,"testTrack1")
        self.assertEqual(testTrack.desc,"First unit test: this Track tests the method add_track")
        

    def test_add_user(self):   #Test testing the insertion of a user.
        testUser = add_user("testUser1", "test", "user", "test@test.com", "SecondUnitTest")  #All the attributes of the new user are checked.
        self.assertEqual(testUser.username,"testUser1")
        self.assertEqual(testUser.first_name,"test")
        self.assertEqual(testUser.last_name,"user")
        self.assertEqual(testUser.email,"test@test.com")
        self.assertEqual(testUser.password,"SecondUnitTest")

        



if __name__ == '__main__':  #This testing script has to be called by console to test the functionalities.
    unittest.main()