import typing
from pydantic import BaseModel
from functools import cached_property


class testInterface(BaseModel):

    class testInterface2(BaseModel):

        attr1: typing.Union[str, None]
        attr2: int
        attr3: float
        attr4: bool

        def __init__(self, attr1, attr2, attr3, attr4) -> None:
            pass

        def func1(self, arg1, arg2) -> None:
            pass

        def func2(self, arg1, arg2) -> str:
            pass

    attr1: typing.Union[str, None]
    attr2: int
    attr3: float
    attr4: bool

    def __init__(self, attr1, attr2, attr3, attr4) -> None:
        pass

    def func1(self, arg1, arg2) -> None:
        pass

    def func2(self, arg1, arg2) -> str:
        pass

    @staticmethod
    def func3(arg1, arg2) -> None:
        pass

    @staticmethod
    def func4(arg1, arg2) -> None:
        pass

    @property
    def prop1(self) -> None:
        pass

    @cached_property
    def prop2(self) -> None:
        pass
