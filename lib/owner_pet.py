class Pet:

    all = []

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
   
    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise ValueError(f"Invalid pet type '{pet_type}'. Allowed types are: {', '.join(self.PET_TYPES)}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.__class__.all.append(self)

        


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
       return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Not a valid pet!")
        pet.owner = self

    def get_sorted_pets(self):
        pets = [pet for pet in Pet.all if isinstance(pet, Pet) and pet.owner == self]
        return sorted(pets, key=lambda x: x.name)