import re
import injector
from typing import Type, List

class BaseController:
    __parentPath__: str
    __childPathDictList__ = {}
    
    def __init__(self) -> None:
        if self.__parentPath__ is None:
            raise NotImplementedError('BaseController.__path__ need Controller Decorator')

def Controller(path):
    incorrectPathStrs = re.findall('[^a-zA-Z\-\/]', path)
    if len(incorrectPathStrs) > 0:
        raise ReferenceError('path must contain a-zA-Z')

    def decorator(cls: BaseController):
        print('@Controller.decorator')
        
        subPath = re.sub('[^a-zA-Z]', '', path)
        cls.__parentPath__ = subPath
        return cls  # 클래스 그대로 반환
    
    return decorator  # 데코레이터 함수 반환

def get(path):
    
    incorrectPathStrs = re.findall('[^a-zA-Z\-\/]', path)
    if len(incorrectPathStrs) > 0:
        raise ReferenceError('path must contain a-zA-Z')
    
    def decorator(fn):
        
        print('🐈🐈')
        def wrapper(self: Type[BaseController], *args, **kwargs):
            print('🎊🎊')
            if path not in self.__childPathDictList__:
                concatPath = '/'.join([self.__parentPath__, path])
                isAlreadyInjectedPath = concatPath in self.__childPathDictList__
                if isAlreadyInjectedPath:
                    self.__childPathDictList__[concatPath].append({
                        'method': 'get',
                        'callable': fn
                    })    
                else:
                    self.__childPathDictList__[concatPath] = [{
                        'method': 'get',
                        'callable': fn
                    }]
            
            print('✅ : ',args)
            print('✅ : ',kwargs)
            
            return fn(self, *args, **kwargs)
        return wrapper
    
    return decorator

def put(path):
    
    incorrectPathStrs = re.findall('[^a-zA-Z\-\/]', path)
    if len(incorrectPathStrs) > 0:
        raise ReferenceError('path must contain a-zA-Z')
    
    def decorator(fn):
        
        def wrapper(self: Type[BaseController], *args, **kwargs):
            if path not in self.__childPathDictList__:
                concatPath = '/'.join([self.__parentPath__, path])
                isAlreadyInjectedPath = concatPath in self.__childPathDictList__
                if isAlreadyInjectedPath:
                    self.__childPathDictList__[concatPath].append({
                        'method': 'put',
                        'callable': fn
                    })    
                else:
                    self.__childPathDictList__[concatPath] = [{
                        'method': 'put',
                        'callable': fn
                    }]
                return None
                
            return fn(self, *args, **kwargs)
        return wrapper
    
    return decorator

def post(path):
    
    incorrectPathStrs = re.findall('[^a-zA-Z\-\/]', path)
    if len(incorrectPathStrs) > 0:
        raise ReferenceError('path must contain a-zA-Z')
    
    def decorator(fn):
        
        def wrapper(self: Type[BaseController], *args, **kwargs):
            if path not in self.__childPathDictList__:
                concatPath = '/'.join([self.__parentPath__, path])
                isAlreadyInjectedPath = concatPath in self.__childPathDictList__
                if isAlreadyInjectedPath:
                    self.__childPathDictList__[concatPath].append({
                        'method': 'post',
                        'callable': fn
                    })    
                else:
                    self.__childPathDictList__[concatPath] = [{
                        'method': 'post',
                        'callable': fn
                    }]
                
            return fn(self, *args, **kwargs)
        return wrapper
    
    return decorator

def patch(path):
    
    incorrectPathStrs = re.findall('[^a-zA-Z\-\/]', path)
    if len(incorrectPathStrs) > 0:
        raise ReferenceError('path must contain a-zA-Z')
    
    def decorator(fn):
        
        def wrapper(self: Type[BaseController], *args, **kwargs):
            if path not in self.__childPathDictList__:
                concatPath = '/'.join([self.__parentPath__, path])
                isAlreadyInjectedPath = concatPath in self.__childPathDictList__
                if isAlreadyInjectedPath:
                    self.__childPathDictList__[concatPath].append({
                        'method': 'patch',
                        'callable': fn
                    })    
                else:
                    self.__childPathDictList__[concatPath] = [{
                        'method': 'patch',
                        'callable': fn
                    }]
                
            return fn(self, *args, **kwargs)
        return wrapper
    
    return decorator

def delete(path):
    
    incorrectPathStrs = re.findall('[^a-zA-Z\-\/]', path)
    if len(incorrectPathStrs) > 0:
        raise ReferenceError('path must contain a-zA-Z')
    
    def decorator(fn):
        
        def wrapper(self: Type[BaseController], *args, **kwargs):
            if path not in self.__childPathDictList__:
                concatPath = '/'.join([self.__parentPath__, path])
                isAlreadyInjectedPath = concatPath in self.__childPathDictList__
                if isAlreadyInjectedPath:
                    self.__childPathDictList__[concatPath].append({
                        'method': 'delete',
                        'callable': fn
                    })    
                else:
                    self.__childPathDictList__[concatPath] = [{
                        'method': 'delete',
                        'callable': fn
                    }]
            
            return fn(self, *args, **kwargs)
        return wrapper
    
    return decorator
