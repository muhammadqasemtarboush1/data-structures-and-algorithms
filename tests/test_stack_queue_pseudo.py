import pytest
from stack_queue_pseudo.stack_queue_pseudo import PseudoQueue,EmptyQueueException


def test_enqueue(new_queue):
    new_queue.enqueue(20)
    print(new_queue.pseudo_queue.top.value,"top")
    actual = new_queue.__str__()
    expected = '20 -> 4 -> 3 -> 2 -> 1 -> '
    assert actual == expected

def test_enqueue_one():
    new_queue= PseudoQueue()
    new_queue.enqueue(20)
    actual = new_queue.__str__()
    expected = '20 -> '
    assert actual == expected


def test_enqueue_more_than_one(new_queue):
    new_queue.enqueue(20)
    new_queue.enqueue(40)
    new_queue.enqueue(60)
    actual = new_queue.__str__()
    expected = '60 -> 40 -> 20 -> 4 -> 3 -> 2 -> 1 -> '
    assert actual == expected


def test_dequeue(new_queue):
    # new_queue.dequeue()
    actual = new_queue.dequeue()
    expected = 1
    assert actual == expected

def test_dequeue_more_than_one(new_queue):
    new_queue.dequeue()
    new_queue.dequeue()
    new_queue.dequeue()
    actual = new_queue.__str__()
    expected = '4 -> '
    assert actual == expected

def test_dequeue_more_than_one_and_raise_error(new_queue):
    new_queue.dequeue()
    new_queue.dequeue()
    new_queue.dequeue()
    new_queue.dequeue()
    with pytest.raises(EmptyQueueException) as err:
        new_queue.dequeue()
        new_queue.peek()
    expected = 'Empty Queue'
    assert str(err.value) == expected


def test_dequeue_empty_queue():
    new_queue = PseudoQueue()
    with pytest.raises(EmptyQueueException) as err:
        new_queue.dequeue()
    expected = 'Empty Queue'
    assert str(err.value) == expected

@pytest.fixture
def new_queue():
    new_queue = PseudoQueue()
    new_queue.enqueue(1)
    new_queue.enqueue(2)
    new_queue.enqueue(3)
    new_queue.enqueue(4)
    return new_queue
