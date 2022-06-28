from stack_and_queue.stack_and_queue import Queue, EmptyQueueException


class AnimalShelter:
    def __init__(self):
        self.dog = Queue()
        self.cat = Queue()

    def enqueue(self, animal_obj):
        if animal_obj.type.lower() == 'cat':
            self.cat.enqueue(animal_obj)
        elif animal_obj.type.lower() == 'dog':
            self.dog.enqueue(animal_obj)
        return animal_obj.type

    def dequeue(self, pref):
        if pref == 'cat':
            return self.cat.dequeue()
        elif pref == 'dog':
            return self.dog.dequeue()
        else:
            return None

class Cat:
    def __init__(self, name):
        self.name = name
        self.type = 'cat'


class Dog:
    def __init__(self, name):
        self.name = name
        self.type = 'dog'
