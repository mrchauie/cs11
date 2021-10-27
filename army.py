class Warrior:    
    def __init__(self, health, attack, is_alive, name):
        self.health = health
        self.attack = attack
        self.is_alive = is_alive
        self.name = name
   
class Knight(Warrior):
    def __init__(self, health, attack, is_alive, name):
        super().__init__(health, attack, is_alive, name)

class Army():
    def __init__(self):
        self.units = []

    def add_units(self, unit, count):
        for x in range(count):
            self.units.append(unit)

class Battle():
    def fight(self, army1, army2):
        while len(army1.units) > 0 and len(army2.units) > 0:
            self.unitFight(army1.units[0], army2.units[0])
            if army1.units[0].is_alive != True:
                army1.units.pop(0)
                print('army 1 unit died next fight')
            if army2.units[0].is_alive != True:
                army2.units.pop(0)
                print('army 2 unit died next fight')
        return len(army1.units) > 0
       
    def unitFight(self, unit_1, unit_2):
        p1Turn = True
        while unit_1.is_alive and unit_2.is_alive:
            if p1Turn:
                unit_2.health -= unit_1.attack
                if unit_2.health <= 0:
                    unit_2.is_alive = False
                    print('unit 2 is dead')
                    return True
                p1Turn = False
            else:
                unit_1.health -= unit_2.attack
                if unit_1.health < 1:
                    unit_1.is_alive = False
                    print('unit 1 is dead')

                    return False
                p1Turn = True
               
def fight(unit_1, unit_2):
    p1Turn = True
    while unit_1.is_alive and unit_2.is_alive:
        if p1Turn == True:
            unit_2.health -= unit_1.attack
            if unit_2.health <=0:
                unit_2.is_alive= False
                return True
            p1Turn = False
        else:
            unit_1.health -= unit_2.attack
            if unit_1.health <1:
                unit_1.is_alive = False
                return False
            p1Turn = True



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
   
    #fight tests
    chuck = Warrior(50, 5, True, 'chuck')
    bruce = Warrior(50, 5, True, 'bruce')
    carl = Knight(50, 7, True, 'carl')
    dave = Warrior(50, 5, True, 'dave')
    mark = Warrior(50, 5, True, 'mark')

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    #battle tests
    my_army = Army()
    my_army.add_units(Knight(50, 7, True, 'carl'), 3)
   
    enemy_army = Army()
    enemy_army.add_units(Warrior(50, 5, True, 'chuck'), 3)

    army_3 = Army()
    army_3.add_units(Warrior(50, 5, True, 'chuck'), 20)
    army_3.add_units(Knight(50, 7, True, 'carl'), 5)
   
    army_4 = Army()
    army_4.add_units(Warrior(50, 5, True, 'chuck'), 30)

    battle = Battle()
    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")

	
	
	
