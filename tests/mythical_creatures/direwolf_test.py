import pytest
from src.mythical_creatures.direwolf import Direwolf, Stark


@pytest.fixture

def direwolf():
    direwolf = Direwolf('Nymeria')
    return direwolf


def test_it_has_a_name(direwolf):
    assert direwolf.name == 'Nymeria'


def test_it_can_have_another_name():
    wolf = Direwolf('Lady')
    assert wolf.name == 'Lady'


def test_default_home_is_beyond_the_wall_and(direwolf):
    direwolf.home == 'Beyond the Wall'


def test_default_size_is_massive():
    wolf = Direwolf('Ghost')
    assert wolf.size == 'Massive'
    assert wolf.name == 'Ghost'


def test_it_can_have_another_home_or_size():
    wolf = Direwolf('Shaggydog', 'Winterfell', 'Smol Pupper')

    assert wolf.name == 'Shaggydog'
    assert wolf.home =='Winterfell'
    assert wolf.size == 'Smol Pupper'


def test_starks_are_in_winterfell_by_default():
    wolf = Direwolf('Summer', 'Winterfell')
    stark = Stark('Bran')

    assert wolf.home == 'Winterfell'
    assert stark.name == 'Bran'
    assert stark.location == 'Winterfell'


def test_starts_off_with_no_Starks_to_protect(direwolf):
    stark = Stark('Arya')

    assert direwolf.starks_to_protect == []
    assert stark.name == 'Arya'
    assert stark.location == 'Winterfell'
    assert direwolf.home == 'Beyond the Wall'


def test_protects_stark_kids():
    wolf = Direwolf('Nymeria', 'Riverlands')
    stark = Stark('Arya', 'Riverlands')

    wolf.protects(stark)

    assert wolf.starks_to_protect[0].name == 'Arya'
    assert stark.location == 'Riverlands'
    assert wolf.home == 'Riverlands'


def test_can_only_protect_stark_kids_if_home_and_location_match():
    wolf = Direwolf('Ghost')
    stark = Stark('John', "King's Landing")

    wolf.protects(stark)

    assert wolf.home == 'Beyond the Wall'
    assert stark.location == "King's Landing"
    assert wolf.starks_to_protect == []


# def test_direwolf_can_only_protect_two_starks_at_a_time():
#     summer_wolf = Direwolf('Summer', 'Winterfell')
#     lady_wolf = Direwolf('Lady', 'Winterfell')
#     sansa_stark = Stark('Sansa')
#     john_stark = Stark('John')
#     rob_stark = Stark('Rob')
#     bran_stark = Stark('Bran')
#     arya_stark = Stark('Arya')

#     summer_wolf.protects(sansa_stark)
#     summer_wolf.protects(john_stark)
#     lady_wolf.protects(rob_stark)
#     lady_wolf.protects(bran_stark)
#     lady_wolf.protects(arya_stark)

#     assert summer_wolf.starks_to_protect[0] == sansa_stark
#     assert summer_wolf.starks_to_protect[1] == john_stark
#     assert lady_wolf.starks_to_protect[0] == rob_stark
#     assert lady_wolf.starks_to_protect[1] == bran_stark
#     assert lady_wolf.starks_to_protect[0] != arya_stark
#     assert lady_wolf.starks_to_protect[1] != arya_stark


# def test_starks_start_off_unsafe():
#     stark = Stark('John', 'The Wall')

#     assert stark.is_safe() == False


# def test_default_house_words():
#     stark = Stark('John', 'The Wall')
#     assert stark.house_words == 'Winter is Coming'


# def test_protected_status_changes_once_protected():
#     wolf = Direwolf('Nymeria', 'Winterfell')
#     arya_stark = Stark('Arya')
#     sansa_stark = Stark('Sansa')

#     wolf.protects(arya_stark)

#     assert arya_stark.is_safe == True
#     assert sansa_stark.is_safe == False
#     assert arya_stark.house_words == 'The North Remembers'
#     assert sansa_stark.house_words == 'Winter is Coming'


# def test_hunts_white_walkers():
#     wolf = Direwolf('Nymeria', 'Winterfell')

#     assert wolf.hunts_white_walkers == True


# def test_hunts_white_walkers_but_not_if_protecting_starks():
#     wolf = Direwolf('Nymeria', 'Winterfell')
#     stark = Stark('Sansa')

#     wolf.protects(stark)
#     wolf.hunts_white_walkers == False


# def test_wolves_can_leave_and_stop_protecting_starks():
#     summer_wolf = Direwolf('Summer', 'Winterfell')
#     lady_wolf = Direwolf('Lady', 'Winterfell')
#     sansa_stark = Stark('Sansa')
#     arya_stark = Stark('Arya')

#     summer_wolf.protects(arya_stark)
#     lady_wolf.protects(sansa_stark)
#     summer_wolf.leaves(arya_stark)

#     assert summer_wolf.starks_to_protect == []
#     assert lady_wolf.starks_to_protect[0].name == 'Sansa'
#     assert type(lady_wolf.starks_to_protect) is list
#     assert arya_stark.is_safe == False


# def test_if_stark_not_protected_when_direwolf_leaves_then_that_stark_is_the_return_value():
#     summer_wolf = Direwolf('Summer', 'Winterfell')
#     lady_wolf = Direwolf('Lady', 'Winterfell')
#     sansa_stark = Stark('Sansa')
#     arya_stark = Stark('Arya')
#     rickon_stark = Stark('Rickon')

#     summer_wolf.protects(arya_stark)
#     lady_wolf.protects(sansa_stark)
#     summer_wolf.leaves(arya_stark)

#     expected = lady_wolf.leaves(rickon_stark)

#     assert expected.name == 'Rickon'
