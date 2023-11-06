
from django.http import HttpRequest
# from django.views.decorators.csrf import csrf_exempt
from routes.dynamic_decorator import Controller, BaseController, get, put, patch, delete, post

# def get(subpath):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print('오잉')
#             instance = args[0]  # 클래스 인스턴스
#             if instance.__path__ is None:
#                 instance.__path__ = subpath
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator

@Controller('auth')
class SampleController(BaseController):
    
    # @csrf_exempt
    @get('sign-up')
    def signup(self, request: HttpRequest):
        # print('API 호출 : signup')
        return 'API 호출 : signup'
    
    # @csrf_exempt
    @get('sign-in')
    def signin(self, request: HttpRequest):
        return 'API 호출 : signin'
    
    # @csrf_exempt
    @post('profile/')
    def postProfile(self, request: HttpRequest):
        print('끄약')
        
        return 'API 호출 : signin'
    
    # @csrf_exempt
    @get('profile/')
    def getProfile(self, request: HttpRequest):
        return 'API 호출 : signin'
    
    # @put('putAuth')
    # def putAuth(self, request: HttpRequest):
    #     return 'API 호출 : signin'
    
    # @patch('patchAuth')
    # def patchAuth(self, request: HttpRequest):
    #     return 'API 호출 : signin'
    
    # @delete('deleteAuth')
    # def deleteAuth(self, request: HttpRequest):
    #     return 'API 호출 : signin'

@Controller('users')
class ExampleController(BaseController):
    pass