import pytest

from stack_and_queue.stack_and_queue import Stack, Queue, EmptyStackException,EmptyQueueException

def test_stack_can_push(stack):
    '''
    Can successfully push onto a stack
    '''
    actual = stack.__str__()
    expected = '24 - 16 - 8 - '
    assert actual == expected


def test_stack_push_multi(stack):
    '''
    Can successfully push multiple values onto a stack
    '''
    stack.push(32)
    stack.push(40)
    actual = stack.__str__()
    expected = '40 - 32 - 24 - 16 - 8 - '
    assert actual == expected

def test_stack_pop(stack):
    '''
    Can successfully pop off the stack
    '''
    stack.pop()
    actual = stack.__str__()
    expected = '16 - 8 - '
    assert actual == expected

def test_stack_is_empty_after_multiple_pop(stack):
    '''
   Can successfully empty a stack after multiple pops
    '''
    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.is_empty()
    expected = True
    assert actual == expected

def test_stack_peek(stack):
    '''
   Can successfully peek the next item on the stack
    '''
    actual = stack.peek()
    expected = '24'
    assert str(actual) == expected

def test_stack_empty_stack():
    '''
   Can successfully instantiate an empty stack
    '''
    new_stack = Stack()
    actual = new_stack.is_empty()
    expected = True
    assert actual== expected

def test_stack_empty_stack_pop():
    '''
    Calling pop or peek on empty stack raises exception
    ref: https://www.youtube.com/watch?v=eBO2FmoeLKw&ab_channel=PyCharmbyJetBrains
    '''
    new_stack = Stack()
    # actual = new_stack.pop()
    with pytest.raises(EmptyStackException) as poped:
        actual =  new_stack.pop()
    expected = 'Nothing to pop ,Empty Stack'
    assert str(poped.value)== expected








@pytest.fixture
def stack():
    stack= Stack()
    stack.push(8)
    stack.push(16)
    stack.push(24)
    return stack

@pytest.fixture
def queue():
    queue= Queue()
    queue.enqueue(8)
    queue.enqueue(16)
    queue.enqueue(24)
    return queue