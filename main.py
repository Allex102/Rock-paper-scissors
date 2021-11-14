from random import randint
class Game():

    step={1:'камень',2:'бумага',3:'ножницы'}

    def start_game(self):
        player=str(input('Что выбросить? :'))
        self.pcaction=randint(1,3)
        for x,y in self.step.items():
            if self.pcaction==x:
                self.pcaction=y
        return self.pcaction

play=Game()
print(play.start_game())


