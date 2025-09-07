class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"


def process_sound(sound_object):
    print(sound_object.make_sound())

dog = Dog()
cat = Cat()

process_sound(dog)
process_sound(cat)
