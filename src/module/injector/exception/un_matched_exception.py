from typing import List
from type.injector_type import INJECTOR_CONTROLLER

class UnMatchedControllerException(Exception):
    
    def __init__(self, messages: List[str]) -> None:
        if isinstance(messages, List):
            messages.insert(0, f'Controller.__INJECTOR_TYPE__ must be {INJECTOR_CONTROLLER}')
        elif isinstance(messages, str):
            messages = [ f'Controller.__INJECTOR_TYPE__ must be {INJECTOR_CONTROLLER}', messages ]
        else:
            raise AssertionError(f'{self.__name__}.__INJECTOR_TYPE__.messages must be List[str] or str')
        
        super().__init__(messages)