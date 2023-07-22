from animals import Cat, Dog, Bird
class AnimalFabric:
    def make_animal(self, animal_type: str, *args, **kwargs):
        new_animal = self._get_maker(animal_type)
        return new_animal(*args, **kwargs)
    def _get_maker(self, animal_type: str):
        types = {"dog": Dog, "cat": Cat, "bird": Bird}
        return types[animal_type.lower()]
if __name__ == '__main__':
    fabric = AnimalFabric()
    animal_from_fabric = fabric.make_animal("dog", "Sharik", "Spaniel")
    animal_from_fabric.commands = ["сидеть", "лежать"]
    print(animal_from_fabric)