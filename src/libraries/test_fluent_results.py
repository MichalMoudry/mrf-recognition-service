"""
Module with tests for fluent results module.
"""
from .fluent_results import *


def test_ok():
    """
    This test covers a basic scenario where Result object is created with an Ok result.
    """
    result = Result(True, "Test value")
    assert isinstance(result.value, str) is True
    assert result.value == "Test value"
    assert result.is_success is True


def test_fail():
    """
    This test cover a basic scenario where Result object is created with a failed result.
    """


def test_err_messages():
    """
    This test covers a failed result with multiple fails.
    """
    msg = "This task has failed"
    msg2 = "This task has failed 2"
    result = Result(False).with_error(msg).with_error(msg2)
    assert len(result.errors) == 2
    assert (msg in result.errors) is True
    assert (msg2 in result.errors) is True
    assert len(result.successes) == 0


def test_success_messages():
    """
    This test covers a successful result with multiple successes.
    """
    msg = "This task has finished"
    msg2 = "This task has finished 2"
    result = Result(True).with_success(msg).with_success(msg2)
    assert len(result.successes) == 2
    assert (msg in result.successes) is True
    assert (msg2 in result.successes) is True
    assert len(result.errors) == 0
