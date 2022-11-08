import ast
import typing
import os


class InterfaceCreator:

    def __init__(
            self,
            filePath,
            targetPath,
            ignoreDecorators,
            enforcedDecorators,
            formatSource,
            skipLocalImports) -> None:
        pass

    def _create_class_interface(self, cls, indent) -> str:
        pass

    def _create_imports(self) -> str:
        pass

    @staticmethod
    def format_source(source) -> str:
        pass

    def create(self) -> str:
        pass

    @classmethod
    def createInterface(
            cls,
            sourcePath,
            targetPath,
            ignoreDecorator,
            enforcedDecorators,
            formatSource,
            skipLocalImports) -> None:
        pass
