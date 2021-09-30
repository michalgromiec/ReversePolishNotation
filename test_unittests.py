import pytest
from ReversePolishNotation import RpnCalculator


@pytest.fixture()
def obj():
    return RpnCalculator()


def test_object_initialized_with_defaults(obj):
    assert hasattr(obj, 'operations')
    assert len(obj.operations.keys()) == 4
    assert len({'+', '-', '*', '/'}.difference(obj.operations.keys())) == 0


def test_calculator_basic_operations_test(obj):
    assert obj.calculate('6 2 +') == 8
    assert obj.calculate('6 2 -') == 4
    assert obj.calculate('6 2 *') == 12
    assert obj.calculate('6 2 /') == 3


def test_calculator_wikipedia_examples(obj):
    assert obj.calculate('12 2 3 4 * 10 5 / + * +') == 40
    assert obj.calculate('5 1 2 + 4 * + 3 -') == 14


def test_unresolved_definition(obj):
    with pytest.raises(ValueError):
        obj.calculate('2 3 4 5 +')


def test_dividing_by_zero(obj):
    with pytest.raises(ZeroDivisionError):
        obj.calculate('1 0 /')
    with pytest.raises(ZeroDivisionError):
        obj.calculate('3 4 4 - /')


def test_unknown_operation_in_definition(obj):
    with pytest.raises(ValueError):
        obj.calculate('3 multiply 2')


def test_custom_function_added_to_operations(obj):
    obj.operation_add('test', lambda x: x)
    assert hasattr(obj, 'operations')
    assert obj.operations.get('test') is not None


def test_results_calculated_correctly_on_definition_with_custom_function_added(obj):
    obj.operation_add('multiply', lambda x, y: x * y)
    assert obj.calculate('2 3 multiply') == 6


def test_results_calculated_correcly_definition_with_custom_function_with_one_arg(obj):
    obj.operation_add('square', lambda x: x ** 2)
    assert obj.calculate('2 3 + square') == 25

    obj.operation_add('root', lambda x: x ** (1 / 2))
    assert obj.calculate('25 root') == 5
    assert obj.calculate('3 3 3 + + root') == 3


def test_results_calculated_correctly_definition_with_custom_function_with_more_than_one_arg(obj):
    obj.operation_add('multiple_3_elements', lambda x, y, z: x * y * z)
    assert obj.calculate('2 3 5 multiple_3_elements') == 30


def test_custom_function_removed_from_operations(obj):
    obj.operation_remove('+')
    assert hasattr(obj, 'operations')
    assert len(obj.operations.keys()) == 3
    assert {'+', '-', '*', '/'}.difference(obj.operations.keys()) == {'+'}
