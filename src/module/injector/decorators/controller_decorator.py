import re

# Type
import type.path_type as pathType
import type.injector_type as ijType

def Controller(path: str):
    
    # print('@Controller')
    
    incorrectPathStrs = re.findall('[^a-zA-Z\-]', path)
    if len(incorrectPathStrs) > 0:
        raise ReferenceError('path must contain a-zA-Z')
    
    def moduleDecorator(targetCls: type):
        # print('@Controller.moduleDecorator')
        
        substitutePath = re.sub('[^a-zA-Z]', '', path)
        
        setattr(targetCls, ijType.KEY, ijType.INJECTOR_CONTROLLER)
        setattr(targetCls, pathType.PARENT_PATH, substitutePath)
        setattr(targetCls, pathType.CHILDREN_PATH_LIST, {})
        
        return targetCls
    
    return moduleDecorator