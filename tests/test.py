import typing
from pydantic import BaseModel
from functools import cached_property
from InterfaceCreator.cli import *
import InterfaceCreator

class testInterface(BaseModel, frozen=True):
    attr1 : typing.Union[str, None]
    attr2 : int
    attr3 : float
    attr4 : bool
    
    class testInterface2(BaseModel, frozen=True):
        attr1 : typing.Union[str, None]
        attr2 : int
        attr3 : float
        attr4 : bool
        
        def __init__(self, attr1, attr2, attr3, attr4):
            pass

        def func1(self, arg1, arg2) -> None:
            pass

        def func2(self, arg1, arg2) -> str:
            pass
    
    def __init__(self, attr1, attr2, attr3, attr4):
        pass
    
    def func1(self, arg1, arg2) -> None:
        pass
    
    def func2(self, arg1, arg2) -> str:
        pass
    
    @staticmethod
    def func3(arg1, arg2):
        pass
    
    @staticmethod
    def func4(arg1, arg2):
        pass
    
    @property
    def prop1(self):
        pass
    
    @cached_property
    def prop2(self):
        pass