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

    user = models.OneToOneField(User)
    university = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    dateOfRegistration = models.DateField()


class Task(models.Model):

##NEED TO ADD:
##   Judgement path?
##   Path?

    taskID = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=1024)
    ##dateCreated = models.DateField
    track = models.ForeignKey(Track)


class Run(models.Model):

    test = "a"
    test2 = "b"
    queryTypeChoices = (
        (test, "example 1"),
        (test2, "example 2"),
    )

##NEED TO ADD:
##   Feedback type
##   Results
##   Path?

    runID = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128, unique=False)
    dateSubmitted = models.DateField()
    dateSubmitted.null = True
    task = models.ForeignKey(Task)
    description = models.CharField(max_length=1024)
    isFullyAutomated = models.BooleanField()
    isFullyAutomated.default = False
    queryType = models.CharField(max_length=1, choices=queryTypeChoices, default=test)

    def __unicode__(self):
        return self.name





