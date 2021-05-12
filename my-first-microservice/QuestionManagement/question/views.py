from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import QuestionEditionSerializer, QuestionSerializer,QuestionCreationSerializer
from .models import Question
from rest_framework import status


class GetAll(APIView):
    
    def get(self,request):
        questions = Question.objects.filter(is_removed=False)
        serialized_questions = QuestionSerializer(instance=questions,many=True)
        return Response(serialized_questions.data)


class GetQuestion(APIView):

    def get(self,request,pk):
        question = Question.objects.filter(pk=pk,is_removed=False).first()
        if question is None:
            return Response({'error':'Question Does Not Exists','success':False},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        serialized_question = QuestionSerializer(instance=question)
        return Response(serialized_question.data)


class CreateQuestion(APIView):

    def post(self,request):
        serialized_question = QuestionCreationSerializer(data=request.data)
        if serialized_question.is_valid():
            question = serialized_question.save()
            serialized_question = QuestionSerializer(instance=question)
            return Response(serialized_question.data,status=status.HTTP_201_CREATED)
        return Response(serialized_question.errors,status=status.HTTP_400_BAD_REQUEST)


class EditQuestion(APIView):

    def put(self,request,pk):
        question = Question.objects.filter(pk=pk,is_removed=False).first()
        if question is None:
            return Response({'error':'Question Does Not Exists','success':False},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        serialized_question = QuestionEditionSerializer(data=request.data,instance=question)
        if serialized_question.is_valid():
            question = serialized_question.save()
            serialized_question = QuestionSerializer(instance=question)
            return Response(serialized_question.data,status=status.HTTP_202_ACCEPTED)
        return Response(serialized_question.errors,status=status.HTTP_400_BAD_REQUEST)


class RemoveQuestion(APIView):

    def delete(self,request,pk):
        question = Question.objects.filter(pk=pk,is_removed=False).first()
        if question is None:
            return Response({'error':'Question Does Not Exists','success':False},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        question.is_removed = True
        question.save()
        return Response(status=status.HTTP_204_NO_CONTENT)