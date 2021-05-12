from django.shortcuts import render,redirect
from django.views import View
from core.clients import user_manager,question_manager
from .forms import QuestionCreationForm
from django.contrib import messages




class CreateQuestion(View):
    form_class = QuestionCreationForm
    template_name = 'question-creation/question-creation-page.html'

    def dispatch(self,request):
            if not user_manager.is_authenticated(request):
                return redirect('accounts:login')
            if request.method == 'POST':
                return self.post(request)
            return self.get(request)

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            current_user_id = user_manager.get_current_user(request)['id']
            question_owner = {'owner_id':current_user_id}
            cd.update(question_owner)
            res = question_manager.create_question(cd)
            if res == True:
                messages.success(request,'Your Question has been Successfully Created','success')
                return redirect('core:home')
            messages.error(request,res['error'],'danger')

        return render(request,self.template_name,{'form':form})


class RemoveQuestion(View):

    def dispatch(self,request,pk):
        if not user_manager.is_authenticated(request):
            return redirect('accounts:login')
        return self.get(request,pk)
    
    def get(self,request,pk):
        question = question_manager.get_single_question(pk)
        current_user = user_manager.get_current_user(request)
        if not question or int(question['owner_id']) != int(current_user['id']):
            return redirect('core:home')
        res = question_manager.remove_question(question['id'])
        if not res:
            messages.error(request,res['error'],'danger')
        else:
            messages.success(request,'Your Question is Successfully Been Removed','success')
        return redirect('core:home')