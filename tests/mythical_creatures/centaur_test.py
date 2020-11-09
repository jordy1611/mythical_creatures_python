import pytest
from src.mythical_creatures.centaur import Centaur


@pytest.fixture
def centaur():
    centaur = Centaur('George', 'Palamino')
    return centaur


def test_it_has_a_name(centaur):
    assert centaur.name == 'George'


def test_it_has_a_horse_breed(centaur):
    assert centaur.breed == 'Palamino'


def test_it_has_excellent_bow_skills(centaur):
    assert centaur.shoot() == 'Twang!!!'


def test_it_makes_a_horse_sound_when_it_runs(centaur):
    assert centaur.run() == "Clop clop clop clop!!!"


def test_when_first_created_it_is_not_cranky(centaur):
    assert centaur.is_cranky() == False


def test_when_first_created_it_is_standing_up(centaur):
    assert centaur.is_standing() == True


def test_after_running_or_shooting_a_bow_three_times_it_gets_cranky(centaur):
    assert centaur.is_cranky() == False
    centaur.shoot()
    centaur.run()
    centaur.shoot()
    assert centaur.is_cranky() == True


def test_when_cranky_it_will_not_shoot_a_bow(centaur):
    for x in range(3):
        centaur.shoot()
    assert centaur.shoot() == "NO!"


def test_when_cranky_it_will_not_run(centaur):
    for x in range(3):
        centaur.shoot()
    assert centaur.run() == "NO!"


def test_when_standing_it_will_not_sleep(centaur):
    assert centaur.sleep() == "NO!"


def test_after_laying_down_it_is_not_standing(centaur):
    centaur.lay_down()
    assert centaur.is_standing() == False
    assert centaur.is_laying() == True


def test_it_can_sleep_when_laying_down(centaur):
    centaur.lay_down()
    assert centaur.sleep() == 'OK!'


def test_when_laying_down_it_cannot_shoot_a_bow(centaur):
    centaur.lay_down()
    assert centaur.shoot() == 'NO!'


def test_when_laying_down_it_cannot_run(centaur):
    centaur.lay_down()
    assert centaur.run() == 'NO!'


def test_it_can_stand_up(centaur):
    centaur.lay_down()
    centaur.stand_up()
    assert centaur.is_standing() == True


def test_after_sleeping_it_is_no_longer_cranky(centaur):
    centaur.shoot()
    centaur.run()
    centaur.shoot()
    assert centaur.is_cranky() == True
    centaur.lay_down()
    centaur.sleep()
    assert centaur.is_cranky() == False
    centaur.stand_up()
    assert centaur.shoot() == "Twang!!!"
    assert centaur.run() == "Clop clop clop clop!!!"


def test_becomes_rested_after_drinking_a_potion(centaur):
    centaur.shoot()
    centaur.run()
    centaur.shoot()
    assert centaur.is_rested() == False
    centaur.drink_potion()
    assert centaur.is_rested() == True


def test_can_only_drink_potion_while_standing(centaur):
    centaur.shoot()
    centaur.run()
    centaur.shoot()
    assert centaur.is_rested() == False
    assert centaur.is_standing() == True
    centaur.drink_potion()
    assert centaur.is_rested() == True


def test_gets_sick_if_drinks_potion_while_rested(centaur):
    assert centaur.is_rested() == True
    centaur.drink_potion()
    assert centaur.is_sick() == True
