import requests
import json

class QuestionClient:
    
    def __init__(self):
        self.url = 'http://localhost:8001/api/'
        self.user_url = 'http://localhost:8002/api/'

    def get_all_questions(self):
        res = requests.get(self.url + 'all/')
        questions = json.loads(res.text)
        return questions

    def get_single_question(self,pk):
        res = requests.get(self.url + f'get/{pk}/')
        question = json.loads(res.text)
        if 'error' in question.keys():
            return None
        owner_id = question['owner_id']
        user_res = requests.get(self.user_url + f'get/{owner_id}/')
        owner = json.loads(user_res.text)
        if 'error' in owner.keys():
            return None
        question['full_name'] = owner['full_name']
        question['email'] = owner['email']
        return question
    
    def create_question(self,data):
        res = requests.post(self.url + 'create/',data)
        if res.status_code == 201:
            return True
        return json.loads(res.text)

    def remove_question(self,pk):
        res = requests.delete(self.url + 'remove/' + str(pk) + '/')
        if res.status_code == 204:
            return True
        return json.loads(res.text)


class UserClient():
    
    def __init__(self):
        self.url = 'http://localhost:8002/api/'

    def create_user(self,data):
        res = requests.post(self.url + 'create/',data)
        return json.loads(res.text)

    def get_token(self,data):
        res = requests.post(self.url + 'token/',data)
        if res.status_code != 200:
            return "error"
        return json.loads(res.text)
    
    def is_authenticated(self,request):
        if 'access' not in request.session.keys():
            return False
        token = request.session['access']
        if token:
            res = requests.post(self.url + 'token/verify/',{'token':token})
            if res.status_code == 200:
                return True
        return False

    def get_current_user(self,request):
        if self.is_authenticated(request):
            token = request.session['access']
            res = requests.get(self.url + 'get-user-from-token/',headers={'Authorization':'Bearer ' + token})
            return json.loads(res.text)
        return None
    

user_manager = UserClient()
question_manager = QuestionClient()


