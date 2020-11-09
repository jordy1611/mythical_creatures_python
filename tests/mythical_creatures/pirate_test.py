import pytest
from src.mythical_creatures.pirate import Pirate


@pytest.fixture
def pirate():
    pirate = Pirate('Jack')
    return pirate


def test_it_has_a_name(pirate):
    assert pirate.name == 'Jack'


def test_it_is_a_scally_wag_by_default(pirate):
    assert pirate.job == 'scallywag'


def test_it_is_not_always_a_scallywag():
    pirate = Pirate('Jack', 'cook')
    assert pirate.job == 'cook'


def test_it_is_not_cursed_by_default(pirate):
    assert pirate.is_cursed() == False


def test_becomes_cursed_after_enough_heinous_acts(pirate):
    assert pirate.is_cursed() == False
    pirate.commit_heinous_act()
    assert pirate.is_cursed() == False
    pirate.commit_heinous_act()
    assert pirate.is_cursed() == False
    pirate.commit_heinous_act()
    assert pirate.is_cursed() == True


def test_a_pirate_has_no_booty(pirate):
    assert pirate.booty == 0


def test_pirate_gets_100_booty_for_robbing_a_ship(pirate):
    assert pirate.booty == 0
    pirate.robs_ship()
    assert pirate.booty == 100