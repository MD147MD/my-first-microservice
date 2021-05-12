from django.shortcuts import redirect, render
from django.views import View
from .clients import question_manager,user_manager


class HomePage(View):

    def get(self,request):
        questions = question_manager.get_all_questions()
        return render(request,'home/home-page.html',{'questions':questions})


class QuestionDetail(View):

    def dispatch(self,request,pk):
            if not user_manager.is_authenticated(request):
                return redirect('accounts:login')
            return self.get(request,pk)

    def get(self,request,pk):
        question = question_manager.get_single_question(pk)
        if not question:
            return redirect('core:home')
        current_user = user_manager.get_current_user(request)
        is_owner_of_question = current_user['id'] == question['owner_id']
        print(question)
        return render(request,'question-detail/question-detail-page.html',{'question':question,'is_owner_of_question':is_owner_of_question})
