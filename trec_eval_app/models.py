from django.db import models
from django.contrib.auth.models import User

# Create your models here.


##TO DO: FILL OUT REST OF FIELDS

class Track(models.Model):

##NEED TO ADD:
##   Measures
##   Track type
##   Path?

    trackID = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128, unique=False)
    description = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):

#One to one relationship with existing model User
#User already contains first name, last name, email, password and username fields
#Make sure that when you interact with a user you use both the User and UserProfile unless you're only
#interested in the fields from one. This means we'll need two form for registration and such

##   Is date needed when Django already tracks this?

    user = models.OneToOneField(User)
    university = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    adminPermission = models.BooleanField()
    adminPermission.default = False
    #dateOfRegistration = models.DateField()
    #dateOfRegistration.null = True


class Task(models.Model):

##NEED TO ADD:
##   Judgement path?
##   Path?
##   Is date needed when Django already tracks this?

    taskID = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=1024)
    #dateCreated = models.DateField
    track = models.ForeignKey(Track)


class Run(models.Model):

    qtTitle = "t"
    qtTitleAndDesc = "td"
    qtDesc = "d"
    qtAll = "a"
    qtOther = "o"
    queryTypeChoices = (
        (qtTitle, "Title"),
        (qtTitleAndDesc, "Title and Description"),
        (qtDesc, "Description"),
        (qtAll, "All"),
        (qtOther, "Other"),
    )

    feedTypeN = "n"
    feedTypeP = "p"
    feedTypeR = "r"
    feedTypeO = "o"
    feedbackTypeChoices = (
        (feedTypeN, "None"),
        (feedTypeP, "Pseudo"),
        (feedTypeR, "Relevance"),
        (feedTypeO, "Other"),
    )




##NEED TO ADD:
##   Feedback type
##   Results
##   Path?
##   Is date needed when Django already tracks this?

    runID = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128, unique=False)
    #dateSubmitted = models.DateField()
    #dateSubmitted.null = True
    task = models.ForeignKey(Task)
    description = models.CharField(max_length=1024)
    isFullyAutomated = models.BooleanField()
    isFullyAutomated.default = False
    queryType = models.CharField(max_length=2, choices=queryTypeChoices, default=qtTitle)
    feedbackType = models.CharField(max_length=1, choices=feedbackTypeChoices, default=feedTypeN)

    def __unicode__(self):
        return self.name





