'''
Created on Mar 26, 2018

@author: awon
'''

from tastypie.resources import ModelResource
from api.models import QuestionAnswer


class QuestionAnswerResource(ModelResource):
    class Meta:
        queryset = QuestionAnswer.objects.all()
        resource_name = 'qa'
