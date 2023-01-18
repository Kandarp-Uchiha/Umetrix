import imp
from django.forms import ModelChoiceField
from rest_framework import serializers
from snippetsApp.models import ReferenceTable
from rest_framework.serializers import ModelSerializer


class ReferenceTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceTable
        fields=['CodeSnippetsID', 'GuidelineName','Tag','Description','Code', 'OptChar','OptInt','Company'] # add snip here
    