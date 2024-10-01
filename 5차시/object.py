class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

        print("{0} 유닛을 생성했습니다." .format(self.name))
        print("체력 {0}, 공격력 {1}" .format(self.hp, self.damage))

soldier1 = Unit("보병", 40, 5)
soldier2 = Unit("보병", 40, 5)
tank = Unit("탱크", 150, 35)