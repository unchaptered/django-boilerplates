# 테스트 케이스 2
# @Module + @Controller / @Module + @Controller 테스트

# decorators
from decorators.injectable_decorator import Injectable
from decorators.controller_decorator import Controller
from decorators.module_decorator import Module

from decorators.http_decorator import get, post, delete


if __name__ == '__main__':
    
    @Controller('first')
    class FirstController():
        
        @get('profile')
        def getFirstProfile(self, request):
            return 'hello'
        
    @Module(controllers=[FirstController])
    class FirstModule:
        pass
    
    @Controller('second')
    class SecondController():
        
        @get('profile')
        def getFirstProfile(self, request):
            return 'hello'
        
    @Module(controllers=[SecondController])
    class SecondsModule:
        pass
    
    # print('=' * 50)
    # print(FirstModule, SecondsModule)
    # print('=' * 50)
    
    @Module(imports=[FirstModule, SecondsModule])
    class RootModule:
        pass
    
    # print(dir(RootModule))
    # print(dir(RootModule._RootModule_FirstModule))
    # print(dir(RootModule._RootModule_SecondsModule))
    print(RootModule().convertUrlPatterns())
    