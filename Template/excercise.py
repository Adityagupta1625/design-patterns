from abc import ABC

class Creature:
    def __init__(self, attack, health):
        self.health = health
        self.attack = attack

class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the _index_ of winning creature
    def combat(self, c1_index, c2_index):
        c1=self.creatures[c1_index]
        c2=self.creatures[c2_index]

        self.hit(c1,c2)
        self.hit(c2,c1)

        c1_alive=c1.health>0
        c2_alive=c2.health>0

        if (c1_alive and c2_alive):
            return -1
        elif not c1_alive and not c2_alive:
            return -1
        elif c1_alive:
            return c1_index
        else:
            return c2_index

    def hit(self, attacker, defender):
        pass  # implement this in derived classes


class TemporaryDamageCardGame(CardGame):
    def __init__(self,creature):
        super().__init__(creature)

    def hit(self,attacker,defender):
        defender_health=defender.health
        defender.health-=attacker.attack
        if defender.health > 0:
            defender.health=defender_health

class PermanentDamageCardGame(CardGame):
    def hit(self,attacker,defender):
        defender.health-=attacker.attack

