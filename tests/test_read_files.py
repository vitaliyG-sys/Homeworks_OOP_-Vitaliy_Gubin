import json
import os
from unittest.mock import mock_open, patch

from src.read_files import get_json_file


def test_get_json_file_correct_data(data_from_json: list[dict]) -> None:
    """1. Проверяет работу функции "get_json_file" с корректно введенными данными."""
    # Задаём содержимое, которое «будет» в файле.
    content = json.dumps(data_from_json)
    # Создаём mock для open, передав содержимое через read_data.
    mock_file = mock_open(read_data=content)
    # Подменяем builtins.open на наш mock
    with patch("builtins.open", mock_file):
        assert get_json_file("dummy.json") == data_from_json


def test_get_json_file_not_found() -> None:
    """2. Проверяет работу функции "get_json_file" с обработкой ошибки FileNotFoundError."""
    invalid_path = os.path.abspath("invalid_path.json")
    assert get_json_file(invalid_path) == []


def test_get_json_file_decode_error() -> None:
    """3. Проверяет работу функции "get_json_file" с обработкой ошибки json.JSONDecodeError."""
    content = '{"name": "Боб", "age": 40,}'
    mock_file = mock_open(read_data=content)
    with patch("builtins.open", mock_file):
        assert get_json_file("dummy.json") == []
