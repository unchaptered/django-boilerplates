import re
from typing import Type

# Type
import type.path_type as pathType
import type.injector_type as ijType


def get(path):
    
    # print('@get ', path)
    
    incorrectPathStrs = re.findall('[^a-zA-Z\-]', path)
    if len(incorrectPathStrs) > 0:
        raise ReferenceError('path must contain a-zA-Z')
    
    def decorator(fn):
        
        # print('@get.decorator ', fn)
        
        def wrapper(targetCls: Type[type], *args, **kwargs):
            
            # print('@get.decorator.wrapper ', targetCls)
            
            childrenPathList = getattr(targetCls, pathType.CHILDREN_PATH_LIST, {})
            
            PATH_KEY = 'GET ' + path
            if PATH_KEY not in childrenPathList:
                childrenPathList[PATH_KEY] = {
                        'path': path,
                        'method': 'get',
                        'callable': fn
                }
                return fn(targetCls, *args, **kwargs)
            
            return fn(targetCls, *args, **kwargs)
        
        return wrapper
    
    return decorator

def put(path):
    
    # print('@put ', path)
    
    incorrectPathStrs = re.findall('[^a-zA-Z\-]', path)
    if len(incorrectPathStrs) > 0:
        raise ReferenceError('path must contain a-zA-Z')
    
    def decorator(fn):
        
        # print('@put.decorator ', fn)
        
        def wrapper(targetCls: Type[type], *args, **kwargs):
            
            # print('@put.decorator.wrapper ', targetCls)
            
            childrenPathList = getattr(targetCls, pathType.CHILDREN_PATH_LIST, {})
            
            PATH_KEY = 'PUT ' + path
            if PATH_KEY not in childrenPathList:
                childrenPathList[PATH_KEY] = {
                        'path': path,
                        'method': 'put',
                        'callable': fn
                }
                return fn(targetCls, *args, **kwargs)
            
            return fn(targetCls, *args, **kwargs)
        
        return wrapper
    
    return decorator

def post(path):
    
    # print('@post ', path)
    
    incorrectPathStrs = re.findall('[^a-zA-Z\-]', path)
    if len(incorrectPathStrs) > 0:
        raise ReferenceError('path must contain a-zA-Z')
    
    def decorator(fn):
        
        # print('@post.decorator ', fn)
        
        def wrapper(targetCls: Type[type], *args, **kwargs):
            
            # print('@post.decorator.wrapper ', targetCls)
            
            childrenPathList = getattr(targetCls, pathType.CHILDREN_PATH_LIST, {})
            
            PATH_KEY = 'POST ' + path
            if PATH_KEY not in childrenPathList:
                childrenPathList[PATH_KEY] = {
                        'path': path,
                        'method': 'post',
                        'callable': fn
                }
                return fn(targetCls, *args, **kwargs)
            
            return fn(targetCls, *args, **kwargs)
        
        return wrapper
    
    return decorator

def patch(path):
    
    # print('@patch ', path)
    
    incorrectPathStrs = re.findall('[^a-zA-Z\-]', path)
    if len(incorrectPathStrs) > 0:
        raise ReferenceError('path must contain a-zA-Z')
    
    def decorator(fn):
        
        # print('@patch.decorator ', fn)
        
        def wrapper(targetCls: Type[type], *args, **kwargs):
            
            # print('@patch.decorator.wrapper ', targetCls)
            
            childrenPathList = getattr(targetCls, pathType.CHILDREN_PATH_LIST, {})
            
            PATH_KEY = 'PATCH ' + path
            if PATH_KEY not in childrenPathList:
                childrenPathList[PATH_KEY] = {
                        'path': path,
                        'method': 'patch',
                        'callable': fn
                }
                return fn(targetCls, *args, **kwargs)
            
            return fn(targetCls, *args, **kwargs)
        
        return wrapper
    
    return decorator

def delete(path):
    
    # print('@delete ', path)
    
    incorrectPathStrs = re.findall('[^a-zA-Z\-]', path)
    if len(incorrectPathStrs) > 0:
        raise ReferenceError('path must contain a-zA-Z')
    
    def decorator(fn):
        
        # print('@delete.decorator ', fn)
        
        def wrapper(targetCls: Type[type], *args, **kwargs):
            
            # print('@delete.decorator.wrapper ', targetCls)
            
            childrenPathList = getattr(targetCls, pathType.CHILDREN_PATH_LIST, {})
            
            PATH_KEY = 'DELETE ' + path
            if PATH_KEY not in childrenPathList:
                childrenPathList[PATH_KEY] = {
                        'path': path,
                        'method': 'delete',
                        'callable': fn
                }
                return fn(targetCls, *args, **kwargs)
            
            return fn(targetCls, *args, **kwargs)
        
        return wrapper
    
    return decorator