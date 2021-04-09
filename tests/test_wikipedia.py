"""Tests of hypermodern_python/console."""
from unittest.mock import Mock

import click
import pytest

from hypermodern_python import wikipedia


def test_random_page_uses_given_language(mock_requests_get: Mock) -> None:
    """It exits with invoking with a specified language."""
    wikipedia.random_page(language="ja")
    args, _ = mock_requests_get.call_args
    assert "ja.wikipedia.org" in args[0]


def test_random_page_returns_page(mock_requests_get: Mock) -> None:
    """It exits with calling Page instance."""
    page = wikipedia.random_page()
    assert isinstance(page, wikipedia.Page)


def test_random_page_handles_validation_errors(mock_requests_get: Mock) -> None:
    """It exits with handling errors."""
    mock_requests_get.return_value.__enter__.return_value.json.return_value = None
    with pytest.raises(click.ClickException):
        wikipedia.random_page()


# def test_trigger_typeguard(mock_requests_get: Mock):
#     import json

#     data = json.loads("{'language': 1}")
#     wikipedia.random_page(language=data["language"])
