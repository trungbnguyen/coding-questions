# An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis.
# People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
# They cannot select which specific animal they would like. Create the data structures to maintain this system and
# implement operations such as enqueue, dequeue_any, dequeue_dog, and dequeue_cat.
# You may use the built-in Linked list data structure.


class Animal:
    def __init__(self, animal_type=None, animal_name=None, next=None):
        self.animal_type = animal_type
        self.animal_name = animal_name
        self.next = next
        self.timestamp = 0


class AnimalShelter:
    def __init__(self):
        self.dog_head = None
        self.dog_tail = None
        self.cat_head = None
        self.cat_tail = None
        self.animal_number = 0

    def enqueue(self, animal_type, animal_name):
        self.animal_number += 1
        new_animal = Animal(animal_type, animal_name)
        new_animal.timestamp = self.animal_number

        if animal_type == "dog":
            if not self.dog_head:
                self.dog_head = new_animal
            elif self.dog_tail:
                self.dog_tail.next = new_animal
            self.dog_tail = new_animal
        elif animal_type == "cat":
            if not self.cat_head:
                self.cat_head = new_animal
            elif self.cat_tail:
                self.cat_tail.next = new_animal
            self.cat_tail = new_animal

    def dequeue_dog(self):
        if self.dog_head:
            new_animal = self.dog_head
            self.dog_head = new_animal.next
            return str(new_animal.animal_name)
        else:
            return "No more dog left"

    def dequeue_cat(self):
        if self.cat_head:
            new_animal = self.cat_head
            self.cat_head = new_animal.next
            return str(new_animal.animal_name)
        else:
            return "No more cat left"

    def dequeue_any(self):
        if self.dog_head and not self.cat_head:
            return self.dequeue_dog()
        elif not self.dog_head and self.cat_head:
            return self.dequeue_cat()
        elif self.dog_head:
            if self.dog_head.timestamp < self.cat_head.timestamp:
                return self.dequeue_dog()
            else:
                return self.dequeue_cat()
        else:
            return "No more animal left"

    def display(self):
        print("Dogs list:")
        dogs = self.dog_head
        dog_count = 1
        while dogs is not None:
            print(f"{dog_count}: {dogs.animal_name}")
            dogs = dogs.next
            dog_count += 1

        print("\nCats list:")
        cats = self.cat_head
        cat_count = 1
        while cats is not None:
            print(f"{cat_count}: {cats.animal_name}")
            cats = cats.next
            cat_count += 1


def main():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue("dog", "Angela")
    animal_shelter.enqueue("cat", "Garfield")
    animal_shelter.enqueue("dog", "Eddie")
    animal_shelter.enqueue("dog", "Lyly")
    animal_shelter.enqueue("cat", "Tom")
    animal_shelter.enqueue("cat", "Lotion")
    animal_shelter.enqueue("cat", "Bot")
    animal_shelter.display()
    print("\nSelect a cat:")
    print(animal_shelter.dequeue_cat())
    print("\nSelect a dog:")
    print(animal_shelter.dequeue_dog())
    print("\nSelect a random animal:")
    print(animal_shelter.dequeue_any())
    animal_shelter.display()


if __name__ == "__main__":
    main()
