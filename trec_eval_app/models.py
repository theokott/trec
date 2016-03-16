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

    user = models.OneToOneField(User)
    university = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    ##dateOfRegistration = models.DateField


class Task(models.Model):

##NEED TO ADD:
##   Judgement path?
##   Path?

    taskID = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=1024)
    ##dateCreated = models.DateField
    track = models.ForeignKey(Track)

    def __unicode__(self):
        return self.name


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
    ##dateSubmitted = models.DateField
    task = models.ForeignKey(Task)
    description = models.CharField(max_length=1024)
    isFullyAutomated = models.BooleanField()
    queryType = models.CharField(max_length=1, choices=queryTypeChoices, default=test)

    def __unicode__(self):
        return self.name





