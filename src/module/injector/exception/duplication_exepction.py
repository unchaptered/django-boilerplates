from typing import List

class DuplicationControllerException(Exception):
    
    def __init__(self, messages: List[str]) -> None:
        if isinstance(messages, List):
            messages.insert(0, 'Controller.__name__ must be unique')
        elif isinstance(messages, str):
            messages = [ 'Controller.__name__ must be unique', messages ]
        else:
            raise AssertionError(f'{self.__name__}.__init__.messages must be List[str] or str')
        
        super().__init__(messages)

class DuplicationProviderException(Exception):
    
    def __init__(self, messages: List[str]) -> None:
        if isinstance(messages, List):
            messages.insert(0, 'Controller.__name__ must be unique')
        elif isinstance(messages, str):
            messages = [ 'Controller.__name__ must be unique', messages ]
        else:
            raise AssertionError(f'{self.__name__}.__init__.messages must be List[str] or str')
        
        super().__init__(messages)