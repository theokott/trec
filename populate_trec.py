__author__ = '2131905K'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'treceval.settings')

import django
django.setup()

from django.contrib.auth.models import User
from trec_eval_app.models import Track, Task, UserProfile, Run
import evaluate_runs


def populate():
    Robust2004Track = add_track(id = "rb04", name = "Robust2004",
                                desc = "News Retrieval"
    )

    Robust2005Track = add_track(id = "rb05track", name = "Robust2005",
                                desc = "News Retrieval"
    )

    MillionQuery = add_track(id = "mq", name = "MillionQuery",
                                desc = "Million Query Track"
    )


    Terabyte = add_track(id = "tb", name = "Terabyte",
                                desc = "Terabyte Web Track"
    )

    APNewsTrack = add_track(id = "apn", name = "APNews",
                                desc = "News Retrieval Track"
    )


    Robust2005Task = add_task(id = "rb05task", desc = "For each topic find all the relevant documents",
             track = Robust2005Track)

    add_task(id = "web05", desc = "Find all the relevant web pages",
             track = Terabyte)

    add_task(id = "apn", desc = "Find all the relevant news articles",
             track = APNewsTrack)

    ASU = add_user(username = "ASU" , password = "password", fName = "", lName = "", email = "mail@ASU.com")
    add_userProfile(user = ASU, uni = "AS University", desc = "Alpha Team", adminPerm = False)

    CK = add_user(username = "CK" , password = "password", fName = "", lName = "", email = "mail@CK.com")
    add_userProfile(user = CK, uni = "CK university", desc = "Chaos and Kontrol", adminPerm = False)

    HK = add_user(username = "HK" , password = "password", fName = "", lName = "", email = "mail@HK.com")
    add_userProfile(user = HK, uni = "HK University", desc = "HongKongIR", adminPerm = False)

    ICT = add_user(username = "ICT" , password = "password", fName = "", lName = "", email = "mail@ICT.com")
    add_userProfile(user = ICT, uni = "University of ICT", desc = "ICTer", adminPerm = False)

    RIM = add_user(username = "RIM" , password = "password", fName = "", lName = "", email = "mail@RIM.com")
    add_userProfile(user = RIM, uni = "Royal Insitute of Mayhem", desc = "IRJobs", adminPerm = False)

    add_runs(Robust2005Task)

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


def add_run(rID, name, taskArg, desc, automated, qType, fbType, MAP, P10, P20):
    x = Run.objects.get_or_create(runID = rID, task = taskArg, track = taskArg.track)[0]
    x.description = desc
    x.name = name
    x.isFullyAutomated = automated
    x.queryType = qType
    x.feedbackType = fbType
    x.MAPScore = MAP
    x.P10Score = P10
    x.P20Score = P20
    x.save()
    return x


def add_user(username, fName, lName, email, password):
    x = User.objects.get_or_create(username = username)[0]
    x.username = username
    x.first_name = fName
    x.last_name = lName
    x.email = email
    x.password = password
    x.save()
    return x


def add_userProfile(user, uni, desc, adminPerm): #, pic)
    x = UserProfile.objects.get_or_create(user = user)[0]
    x.university = uni
    x.description = desc
    #x.picture = pic
    x.adminPermission = adminPerm
    x.save()
    return x

def add_runs(task):
    for i in os.listdir("./evaluator/participants/robust"):
        scores =  evaluate_runs.getScores("./evaluator/data/robust/aq.trec2005.qrels", "./evaluator/participants/robust/"+i)
        add_run(i, i[6:], task, "Placeholder description", False, "d", Run.feedTypeP, float(scores[0]), float(scores[1]), float(scores[2]))

# Start execution here!
if __name__ == '__main__':
    print "Starting trec population script..."
    populate()