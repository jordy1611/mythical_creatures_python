from src.mythical_creatures.unicorn import Unicorn
import pytest


@pytest.fixture
def unicorn():
    unicorn = Unicorn('Robert')
    return unicorn


def test_it_has_a_name(unicorn):
    assert unicorn.name == 'Robert'


def test_it_is_white_by_default(unicorn):
    assert unicorn.color == 'white'


def test_it_returns_true_if_white(unicorn):
    assert unicorn.is_white() == True


def test_it_can_have_another_color():
    unicorn = Unicorn('Robert', 'purple')
    assert unicorn.color == 'purple'


def test_it_returns_false_if_not_white():
    unicorn = Unicorn('Robert', 'purple')
    assert unicorn.is_white() == False


def test_it_says_sparkly_stuff(unicorn):
    assert unicorn.say('Hello, World') == '**;* Hello, World *;**'
