import pytest
from src.mythical_creatures.ogre import Ogre, Human


@pytest.fixture
def ogre():
    ogre = Ogre('Brak')
    return ogre


@pytest.fixture
def human():
    human = Human('Jane')
    return human


def test_it_has_a_name(ogre):
    assert ogre.name == 'Brak'


def test_it_has_a_default_home(ogre):
    assert ogre.home == 'swamp'


def test_it_can_have_a_different_name():
    ogre = Ogre('Shrek', 'The Ritz')
    assert ogre.name == 'Shrek'


def test_it_doesnt_have_to_live_in_a_swamp():
    ogre = Ogre('Shrek', 'The Ritz')
    assert ogre.home == 'The Ritz'


def test_it_can_meet_humans(ogre, human):
    assert human.name == 'Jane'
    ogre.encounter(human)
    assert ogre.encounter_counter == 1


def test_it_can_swing_at_human_after_3_encounters(ogre, human):
    ogre.encounter(human)
    assert ogre.encounter_counter == 1
    assert ogre.swing(human) == False
    ogre.encounter(human)
    assert ogre.encounter_counter == 2
    assert ogre.swing(human) == False
    ogre.encounter(human)
    assert ogre.encounter_counter == 3
    assert ogre.swing(human) == True


def test_human_is_knocked_out_after_ogre_swings(ogre, human):
    assert human.knocked_out == False
    for x in range(3):
        ogre.encounter(human)
    ogre.swing(human)
    assert human.knocked_out == True


def test_human_wake_up_after_ogre_apologizes(ogre, human):
    for x in range(3):
        ogre.encounter(human)
    ogre.swing(human)
    ogre.apologize(human)
    assert human.knocked_out == False

