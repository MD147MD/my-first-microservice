from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id','owner_id','title','body')


class QuestionCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('owner_id','title','body')


class QuestionEditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('title','body')
