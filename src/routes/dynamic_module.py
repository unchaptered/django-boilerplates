from typing import Optional, List

class BaseController:
    pass

class BaseProvider:
    pass

class DynamicModule:
    controllers: List[BaseController]
    imports: List[BaseProvider]
    exports: List[BaseProvider]
    
def Module(
    controllers: Optional[List[type]],
    imports: Optional[List[type]],
    providers: Optional[List[type]],
    exports: Optional[List[type]],
):
    pass
    

class IanProvider():
    pass

@Module(
    imports=[],
    providers=[IanProvider],
    exports=[IanProvider] 
)
class IanModule:
    pass