from django.db import models
#from djongo import models


class ReferenceTable(models.Model):
	CodeSnippetsID = models.AutoField(primary_key = True)
	GuidelineName = models.TextField()
	Tag = models.TextField()
	Description = models.TextField()
	Code = models.TextField()
	OptChar = models.TextField()
	OptInt = models.IntegerField()
	Company = models.TextField()
# ReferenceTable is name of the model with following attributes. While sending post request, there is no need to send CodeSnippetsID with the data. It will be taken care of automatically.

