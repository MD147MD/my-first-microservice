from .clients import user_manager



def main_context(request):
    return {'is_authenticated':user_manager.is_authenticated(request),'current_user':user_manager.get_current_user(request)}
