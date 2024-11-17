import pytest
import random


def test_len():
    assert len([1, 2, 3]) == 3
    assert len("") == 0
    assert len("Python") == 6

def test_sum():
    assert sum([1, 2, 3]) == 6
    assert sum([]) == 0
    assert sum([-1, 1, 0]) == 0

def test_sorted():
    assert sorted([3, 1, 2]) == [1, 2, 3]
    assert sorted([]) == []
    assert sorted(["b", "a", "c"]) == ["a", "b", "c"]

@pytest.fixture
def random_list():
    # Возвращает случайный список
    return [random.randint(1, 100) for _ in range(10)]


def test_all_even(random_list):
    # Проверяет, что все числа в списке четные
    for num in random_list:
        assert num % 2 == 0, f"{num} нечетное"

def test_all_odd(random_list):
    # Проверяет, что все числа в списке нечетные
    for num in random_list:
        assert num % 2 != 0, f"{num} четное"

@pytest.mark.basic
def test_len():
    assert len([1, 2, 3]) == 3
    assert len("") == 0
    assert len("Python") == 6

@pytest.mark.basic
def test_sum():
    assert sum([1, 2, 3]) == 6
    assert sum([]) == 0
    assert sum([-1, 1, 0]) == 0

@pytest.mark.basic
def test_sorted():
    assert sorted([3, 1, 2]) == [1, 2, 3]
    assert sorted([]) == []
    assert sorted(["b", "a", "c"]) == ["a", "b", "c"]

@pytest.mark.random
def test_all_even(random_list):
    for num in random_list:
        assert num % 2 == 0, f"{num} нечетное"

@pytest.mark.random
def test_all_odd(random_list):
    for num in random_list:
        assert num % 2 != 0, f"{num} четное"