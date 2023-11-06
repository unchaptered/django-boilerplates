# decorators
from decorators.injectable_decorator import Injectable
from decorators.controller_decorator import Controller
from decorators.module_decorator import Module

from decorators.http_decorator import get, post, delete

@Controller('power')
class PowerController():
    
    @get('charge')
    def getCharge(self, request):
        # print('hello')
        return 'hi'
    
    @post('charge')
    def postCharge(self, request):
        # print('hello')
        return 'hi'
    
    @delete('profile')
    def deleteHi(self, request):
        # print('hello')
        return 'hi'
    
@Controller('auth')
class AuthController():
    
    @get('sign-in')
    def getHello(self, request):
        # print('hello')
        return 'hi'
    
    @post('sign-in')
    def postHello(self, request):
        # print('hello')
        return 'hi'
    
    @delete('profile')
    def deleteHi(self, request):
        # print('hello')
        return 'hi'

@Injectable()
class AuthService():
    pass

if __name__ == '__main__':
    
    @Module(controllers=[AuthController, PowerController],
            providers=[AuthService])
    class SampleModule:
        def hello(self):
            print('🤔: ', dir(self))
            
    # print("SampleModule() : ", SampleModule())
    # print("SampleModule().convertUrlPattern() : ", )
    for url in SampleModule().convertUrlPattern():
        print(url)