class Fish:
    def __init__(self, species, position, weight, health, food_capacity):
        self.species = species
        self.position = position
        self.weight = weight
        self.health = health
        self.food_capacity = food_capacity

    def swim(self):
        pass

    def eat(self):
        pass

    def take_damage(self, damage):
        self.health -= damage


class Marlin(Fish):
    def __init__(self, position, weight, health, food_capacity):
        super().__init__("Marlin", position, weight, health, food_capacity)

    def special_ability(self):
        pass  # 可以定义马林鱼特有的能力或行为