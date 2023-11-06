import type.injector_type as ijType

def Injectable():
    
    # print('@Injectable')
    
    def moduleDecorator(targetCls: type):
        # print('@Injectable.moduleDecorator')
        setattr(targetCls, ijType.KEY, ijType.INJECTOR_PROVIDER)
        return targetCls
    
    return moduleDecorator
        
