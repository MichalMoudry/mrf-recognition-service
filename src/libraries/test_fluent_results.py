"""
Module with tests for fluent results module.
"""
from .fluent_results import *


def test_ok():
    """
    This test covers a basic scenario where Result object is created with an Ok result.
    """
    result = Result(True, "Test value")
    assert result.value == "Test value"
    assert result.is_success is True


def test_fail():
    """
    This test cover a basic scenario where Result object is created with a failed result.
    """


def test_empty_ok():
    """
    This test covers a basic scenario where Result object is created with an Ok result. This time with an empty value.
    """
    result = Result(True)
    assert result.is_success is True
    assert result.has_value() is False


def test_message_join():
    """
    This test covers a failed result with multiple fails.
    """
    msg = "This task has failed"
