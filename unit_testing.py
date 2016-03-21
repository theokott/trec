__author__ = '2146734s'

from populate_trec import *

import unittest

from trec_eval_app.models import Track, Task, UserProfile, Run

#				Class TestTrecEvaluator
#	This class implements the unit testing methodology.
#	Two test cases are implemented on the populate_trec.py script.

class TestTrecEvaluator(unittest.TestCase):

    def test_add_track(self):  #Test testing the insertion of a track.
        self.assertEqual((add_track(0,"testTrack1","First unit test: this Track tests the method add_track")).name,"testTrack1")

    def test_add_user(self):   #Test testing the insertion of a user.
        self.assertEqual((add_user("testUser1", "test", "user", "test@test.com", "SecondUnitTest")).username,"testUser1")



if __name__ == '__main__':
    unittest.main()