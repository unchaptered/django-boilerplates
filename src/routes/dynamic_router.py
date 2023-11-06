from django.urls import path
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from typing import List, Type
from routes.dynamic_decorator import BaseController

class DynamicRouter:
    
    controllers: List[BaseController] = []
    
    def __init__(self,
                 controllers: List[Type[BaseController]]) -> None:
        for controller in controllers:
            self.__injectController__(controllerClsType=controller)
        
        self.__injectControllerMethod__()    
        self.__validateController__()
    
    def __injectController__(self, controllerClsType: Type[BaseController]):
        self.controllers.append(controllerClsType())
    
    def __injectControllerMethod__(self):
        for controller in self.controllers:
            # methods = [m for m in dir(controller) if callable(getattr(controller, m))]
            controllerMethodStrs =[
                m
                for m
                in dir(controller)
                if (
                    callable(getattr(controller, m))
                    and not m.startswith("_")
                )
            ]
            for controllerMethodStr in controllerMethodStrs:
                controllerMethod = getattr(controller, controllerMethodStr)
                controllerMethod('This method is interrupted')
                    
    def __validateController__(self):
        parentPathSet = set()
        for controller in self.controllers:
            print('__validateController__ : ', controller.__parentPath__)
            
            hasParentPath = controller.__parentPath__ in parentPathSet
            if hasParentPath:
                raise ReferenceError([
                    'BaseController.child.prototype.__path__ is overlapped the other BaseController.child.prototype.__path__',
                    'Please change the @Controller("path")'
                ])
            
            parentPathSet.add(controller.__parentPath__)
        return True
    
    def convertUrlpattenrs(self):
        urlpattern = []
        
        for controller in self.controllers:
            for childPath in controller.__childPathDictList__:
                
                injectedMethods = {}
                for childPathDict in controller.__childPathDictList__[childPath]:
                    injectedMethod = childPathDict['method']
                    injectedFunction = childPathDict['callable']
                    
                    injectedMethods[injectedMethod] = injectedFunction
                
                controller.__childPathDictList__[childPath]
                DynamicView: type[BaseController] = type(childPath, (View, ), injectedMethods)
                urlpattern.append(
                    path(childPath, DynamicView.as_view(), name=f'{childPath}-view')
                )
                
        return urlpattern