import pytest
from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter, Cat, Dog


# enqueue
def test_animal_cat_enqueue(Animal):
    actual = Animal.enqueue(Cat('lolita'))
    expected = 'cat'
    assert actual == expected


def test_animal_dog_enqueue(Animal):
    actual = Animal.enqueue(Dog('loyid'))
    expected = 'dog'
    assert actual == expected


# dequeue
def test_animal_not_expected_dequeue(Animal):
    assert Animal.dequeue('dragon') is None


def test_animal_dog_dequeue(Animal):
    Animal.enqueue(Dog('anya'))
    Animal.enqueue(Cat('layon'))
    assert Animal.dequeue('dog').type == 'dog'


def test_animal_cat_dequeue(Animal):
    Animal.enqueue(Dog('anya'))
    Animal.enqueue(Cat('layon'))
    assert Animal.dequeue('cat').type == 'cat'


@pytest.fixture
def Animal():
    return AnimalShelter()
