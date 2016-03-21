__author__ = '2131905K'
import os
import test_trec
import populate_trec
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'treceval.settings')
from trec_eval_app.models import Track, Task, UserProfile, Run

import django
django.setup()

from trec_eval_app.models import Track, Task, UserProfile, Run

#add_run(rID, name, task, desc, automated, qType, fbType):

for i in os.listdir("./evaluator/participants/robust"):
    scores = test_trec.getScores("./evaluator/data/robust/aq.trec2005.qrels", i)
    populate_trec.add_run(i[5:], i[5:], populate_trec.Robust2005Track, "Placeholder description",
                          False, "d", Run.feedTypeR, scores[0], scores[1], scores[2])