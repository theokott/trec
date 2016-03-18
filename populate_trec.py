__author__ = '2131905K'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'treceval.settings')

import django
django.setup()

from trec_eval_app.models import Track, Task, UserProfile, Run
import datetime


def populate():
    microblog_track = add_track(id = "1", name = "Microblog Track",
                                desc = "Description of the microblog track"
    )

    session_track = add_track(id = "2", name = "Session Track",
                                desc = "Description of the session track"
    )

    microTask = add_task(id = "mb1", desc = "This task a for the microblog track",
             track = microblog_track)

    sessTask = add_task(id = "s1", desc = "This task a for the session track",
             track = session_track)

    add_run(id = "a", name = "example run", task = microTask, desc = "Run for the task mb1",
            date = datetime.date.today(), automated=False, qType = "t", fbType = Run.feedTypeR)

    add_run(id = "b", name = "example run2", task = sessTask, desc = "Run for the task s1",
            date = datetime.date.today(), automated=False, qType = "d", fbType = Run.feedTypeP)

    for tr in Track.objects.all():
        for ta in Task.objects.filter(track = tr):
            for run in Run.objects.filter(task = ta):
                print "- {0} - {1}".format(str(tr), ta.taskID)
                print run.runID + " - " + run.name + " - " + run.description +  " - " + run.queryType + " - " + run.feedbackType
                print ""


def add_track(id, name, desc):
    x = Track.objects.get_or_create(trackID = id)[0]
    x.name = name
    x.desc = desc
    x.save()
    return x

def add_task(id, desc, track):
    x = Task.objects.get_or_create(track = track, taskID = id)[0]
    x.description = desc
    x.save()
    return x

def add_run(id, name, task, desc, date, automated, qType, fbType):
    x = Run.objects.get_or_create(runID = id, task = task)[0]
    x.description = desc
    x.name = name
    x.date = date
    x.isFullyAutomated = automated
    x.queryType = qType
    x.feedbackType = fbType
    x.save()
    return x

# Start execution here!
if __name__ == '__main__':
    print "Starting trec population script..."
    populate()