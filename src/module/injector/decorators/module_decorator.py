from django.urls import path
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from typing import Optional, TypedDict, Type, List

# Type
import type.injector_type as ijType
import type.path_type as pathType
import type.router_type as routerType

# Inject
from inject import injectController, injectProvider, injectExport, injectModule
from exception.invalid_controller_exception import InvalidControllerException

class ModuleParamTypedDict(TypedDict):
    controllers: Optional[List[Type]]
    imports: Optional[List[Type]]
    providers: Optional[List[Type]]
    exports: Optional[List[Type]]

def concatPath(parentPath: str, childrenPath: str):
    
    if parentPath is None:
        return childrenPath
    else:
        return parentPath + '/' + childrenPath
    

def convertUrlPatterns(self):
    urlpattern = []
    
    for key in dir(self):
        attr = getattr(self, key, None)
        
        isPublicAttr = attr is not None
        isClassType = isinstance(attr, type)
        
        if (isPublicAttr and isClassType):
            
            InnerClass = attr
            
            ijValue = getattr(InnerClass, ijType.KEY)
            
            # [CASE A] 클래스인 경우
            isController = ijValue == ijType.INJECTOR_CONTROLLER
            if isController:
                
                # [STEP 1] 데코레이터 태깅 생성 (최초 1회 호출 필요)
                ctl = InnerClass()
                ctlMethodNameList = [ m for m in dir(ctl) if ( callable(getattr(ctl, m)) and not m.startswith("_") ) ]
                for ctlMethodName in ctlMethodNameList:    
                    ctlMethod = getattr(ctl, ctlMethodName)
                    ctlMethod('This method is interrupted')
                # print('✅ : ', dir(ctl))
                
                # [STEP 2] childrenPathDict['path'] 를 키로가지는 Mapper 생성
                parentPath = getattr(ctl, pathType.PARENT_PATH, None)
                childrenPathDictList = getattr(ctl, pathType.CHILDREN_PATH_LIST, [])
                
                ctlUrlFormatDictList = {}
                for key in childrenPathDictList:
                    
                    childrenPathDict = childrenPathDictList[key]
                    
                    childrenPath = childrenPathDict['path']
                    childrenMethod = childrenPathDict['method']
                    childrenCallable = childrenPathDict['callable']
                    
                    # print(" childrenPathDict['path'] : " , childrenPathDict['path'])
                    # print(" childrenPathDict['method'] : " , childrenPathDict['method'])
                    # print(" childrenPathDict['callable'] : " , childrenPathDict['callable'])
                    
                    hasChildrenPath = childrenPath in ctlUrlFormatDictList
                    if hasChildrenPath:
                        ctlUrlFormatDictList[childrenPath].append(childrenPathDict)
                    else:
                        ctlUrlFormatDictList[childrenPath] = [ childrenPathDict ]
                
                # [STEP 3] childrenPathDict['path'] 를 가지는 Mapper 로 urlPattern 생성
                ctlUrlPattern = []
                for key in ctlUrlFormatDictList:
                    
                    dynamicFuncDict = {}
                    for ctlUrlFormatDict in ctlUrlFormatDictList[key]:
                        # print('DD : ', ctlUrlFormatDict)
                        
                        dynamicFuncDict[ctlUrlFormatDict['method']] = ctlUrlFormatDict['callable']
                    DynamicView = type(key, (View, ), dynamicFuncDict)
                    ctlUrlPattern.append(
                        path(
                            route=concatPath(parentPath, ctlUrlFormatDict['path']),
                            view=DynamicView.as_view(),
                            name=ctlUrlFormatDict['path']+'-view'
                        )
                    )
                
                urlpattern.extend(ctlUrlPattern)
            
            # [CASE B] 모듈인 경우
            isModule = ijValue == ijType.INJECTOR_MODULE
            isNotRootModule = key != '__class__'
            if isModule and isNotRootModule:
                
                ModuleClass = getattr(self, key)
                moduleClass = ModuleClass()
                moduleUrlPatterns = moduleClass.convertUrlPatterns()
                urlpattern.extend(moduleUrlPatterns)
                
    return urlpattern    

def Module(**kwargs: ModuleParamTypedDict):
    # print('@Module')
    
    def moduleDecorator(targetCls: type):
        # print('@Module.moduleDecorator')
        setattr(targetCls, ijType.KEY, ijType.INJECTOR_MODULE)
        
        injectController(targetCls, kwargs.get('controllers', []))
        injectProvider(targetCls, kwargs.get('providers', []))
        injectExport(targetCls, kwargs.get('exports', []))
        injectModule(targetCls, kwargs.get('imports', []))
        
        setattr(targetCls, routerType.KEY, convertUrlPatterns)
        
        return targetCls

    return moduleDecorator