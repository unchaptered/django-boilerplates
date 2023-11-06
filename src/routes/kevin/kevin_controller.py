
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from routes.dynamic_decorator import Controller, BaseController, get, put, patch, delete, post

@Controller('kevin')
class KevinController(BaseController):
    
    @get('sign-up/')
    def signup(self, request: HttpRequest):
        return JsonResponse({
            'result': 'API 호출 : signup'
        })
    
    @get('sign-up/')
    def signin(self, request: HttpRequest):
        return JsonResponse({
            'result': 'API 호출 : 으악!'
        })
        
    @get('logout/')
    def logout(self, request: HttpRequest):
        return JsonResponse({
            'result': 'API 호출 : LogOut🤔'
        })
        
    @get('logout/')
    def logout(self, request: HttpRequest):
        return JsonResponse({
            'result': 'API 호출 : LogOut🤔'
        })
    
    # @csrf_exempt
    @post('profile/')
    def postProfile(self, request: HttpRequest):
        print('끄약')
        
        return JsonResponse({
            'result': 'API 호출 : profile'
        })
    
    # @csrf_exempt
    @get('profile/')
    def getProfile(self, request: HttpRequest):
        return JsonResponse({
            'result': 'API 호출 : get profile'
        })
    
@Controller('users')
class ExampleController(BaseController):
    pass