#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed

    @property
    def set_name(self):
        return self._name
    
    @set_name.setter
    def set_name(self, name):
            if len(name) < 1 or len(name) > 25:
                print("Name must be a string between 1 and 25 characters.")
            else:
                self._name = name

    @property
    def set_breed(self):
        return self._breed
    
    @set_breed.setter
    def set_breed(self, breed):
        if breed not in APPROVED_BREEDS:
            print("Breed must be in the list of approved breeds.")
        else:
            self._breed = breed
