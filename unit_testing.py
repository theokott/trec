__author__ = '2146734s'

from populate_trec import *

import unittest

from trec_eval_app.models import Track, Task, UserProfile, Run


class TestTrecEvaluator(unittest.TestCase):

    def test_add_track(self):
        self.assertEqual((add_track(0,"testTrack1","First unit test: this Track tests the method add_track")).name,"testTrack1")



if __name__ == '__main__':
    unittest.main()