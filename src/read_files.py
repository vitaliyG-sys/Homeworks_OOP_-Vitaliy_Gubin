import json
import os
from typing import Any, Union


def get_json_file(path: Union[str, os.PathLike]) -> list | Any:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о товарах.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    result = []
    try:
        with open(path, "r", encoding="utf-8") as json_operations:
            result = json.load(json_operations)
    except FileNotFoundError:
        print("Файл не найден")
        return result
    except json.JSONDecodeError:
        print("Ошибка декодирования файла")
        return result
    return result
