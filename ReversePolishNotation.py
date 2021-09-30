from collections.abc import Callable
import inspect


class RpnCalculator:

    def __init__(self) -> None:
        """
        Initialize object.

        self.operations contains default mathematical operations with lambda's functions.
        """
        self.operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y
        }

    def operation_add(self, label: str, function: Callable, overwrite: bool = False) -> None:
        """
        Adds operation to current operations dictionary.
        :param label: operation key to be added
        :param function: operation definition as a Python function/lambda
        :param overwrite: allow overwriting existing operation, overwriting disabled by default
        :return: None
        """
        if overwrite or not self.operations.get(label):
            self.operations[label] = function

    def operation_remove(self, label: str) -> None:
        """
        Remove operation based on label key
        :param label: key of operations to remove
        :return: None
        """
        if self.operations.get(label):
            del self.operations[label]

    def calculate(self, definition: str, split_by: str = ' ') -> float:
        """
        Calculate result of Reverse Polish Notation (RPN) clause.
        RPN details can be found here: https://pl.wikipedia.org/wiki/Odwrotna_notacja_polska

        :param definition: string, contains RPN calculation definiton. Definition can be splitted into elements
         by space sign. Elements contain numbers (integers) and mathematical or custom function names.
        :param split_by: string, delimiter of elements in definition
        :return: float, result of calculation
        """

        definition_elements = definition.split(split_by)

        results = list()

        for element in definition_elements:
            if (func := self.operations.get(element)) is not None:
                func_args = inspect.signature(func).parameters
                element_args = []
                for _ in range(len(func_args)):
                    element_args.insert(0, results.pop())
                results.append(func(*element_args))
            else:
                try:
                    results.append(float(element))
                except ValueError:
                    raise ValueError(f'Element {element} not found in operations, neither is not a number')

        if len(results) > 1:
            raise ValueError(f'RPN definition cant be resolved to float, definition: {definition}, result: {results}')

        return results.pop()
