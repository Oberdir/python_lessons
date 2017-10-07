# 07.10.2017 - Kevin Akpomuje

import random

# class uses capital letter in beginning and for every word added
# class Mage

class Mage:
    spell_casting = True

    def __init__(self, name, spell_casting=True, **kwargs):
        self.name = name
        self.spell_casting = spell_casting

        for key, value in kwargs.items():
            setattr(self, key, value)

    def fireball(self):
        return self.spell_casting and bool(random.randint(0, 1))

    def invisible(self, light_level):
        return self.spell_casting and light_level < 10
