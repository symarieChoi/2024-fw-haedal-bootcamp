class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, damage):
        try:
            self.health -= damage
            if self.health <= 0:
                raise ValueError("Game Over")
            print(f"{self.name}의 남은 체력: {self.health}")
        except ValueError as e:
            print(e)

warrior = Player("Warrior", 100)
warrior.attack(50)
warrior.attack(60)