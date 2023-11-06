from typing import Optional, TypedDict, Type, List

# Types
import type.injector_type as ijType
import type.module_type as moduleType

# Exceptions
from exception.duplication_exepction import DuplicationControllerException
from exception.un_matched_exception import UnMatchedControllerException


def injectController(classType: type,
                     controllers: List[Type]
) -> None:
    
    className = classType.__name__

    for ct in controllers:
        
        ctName = ct.__name__
        ctType = getattr(ct, ijType.KEY, None)
        
        isInvalidController = ctType != ijType.INJECTOR_CONTROLLER
        isDupController = hasattr(classType, ctName)
        
        if isInvalidController:
            raise UnMatchedControllerException([
                f'{ct}.{ctType} is not equal {ijType.INJECTOR_CONTROLLER}'
            ]) 
            
        if isDupController:
            raise DuplicationControllerException([
                f'{ct}.{ctType} is not unique'
            ])
            
        else:
            
            # controllerList = getattr(classType, moduleType.CONTROLLER_LIST, [])
            
            # if len(controllerList) == 0:
            #     print('✅')
            #     setattr(classType, moduleType.PROVIDER_LIST, [ct])
                
            # else:
            #     controllerList.append(ct)
            
            setattr(classType, f'_{className}__{ctName}', ct)

def injectProvider(classType: type,
                   providers: List[Type]):
    
    className = classType.__name__

    for pr in providers:
        
        prName = pr.__name__
        prType = getattr(pr, ijType.KEY, None)
        
        isInvalidProvider = prType != ijType.INJECTOR_PROVIDER
        isDupProvider = hasattr(classType, prName)
    
        if isInvalidProvider:
            raise UnMatchedControllerException([
                f'{pr}.{prType} is not equal {ijType.INJECTOR_PROVIDER}'
            ]) 
            
        if isDupProvider:
            raise DuplicationControllerException([
                f'{pr}.{prType} is not unique'
            ])
            
        else:
            
            # providerList = getattr(classType, moduleType.PROVIDER_LIST, [])
            # if len(providerList) == 0:
            #     setattr(classType, moduleType.PROVIDER_LIST, [pr])
                
            # else:
            #     providerList.append(pr)
            
            setattr(classType, f'_{className}_{prName}', pr)
            
def injectExport(classType: type,
                 exports: List[type]):
    
    for ex in exports:
        
        exName = ex.__name__
        exType = getattr(ex, ijType.KEY, None)
        
        canExport = exType == ijType.INJECTOR_PROVIDER
        isDupProvider = hasattr(classType, exType)

def injectModule(classType: type,
                 modules: List[type]):
    
    className = classType.__name__
    for md in modules:
        
        mdName = md.__name__
        mdType = getattr(md, ijType.KEY, None)
        
        # canImport = mdType == ijType.INJECTOR_MODULE
        # if canImport:
        #     print(mdName, mdType)
        #     isDupProvider = hasattr(classType, mdType)
            
        isInvalidModule = mdType != ijType.INJECTOR_MODULE
        isDupModule = hasattr(classType, mdName)
        
        if isInvalidModule:
            raise UnMatchedControllerException([
                f'{md}.{mdType} is not equal {ijType.INJECTOR_MODULE}'
            ]) 
            
        if isDupModule:
            raise DuplicationControllerException([
                f'{md}.{mdType} is not unique'
            ])
            
        else:
            
            setattr(classType, f'_{className}_{mdName}', md)
