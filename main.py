from random import choice
class Game():

    step={'r':'камень','p':'бумага','s':'ножницы'}
    save_step_pc=0
    save_step_player=0

    def pc_action(self):
        global save_step_pc
        self.pcaction=choice(['r','p','s'])
        for x,y in self.step.items():
            if self.pcaction==x:
                self.save_step_pc=x
                self.pcaction=y
                return f'Компьютер бросил {self.pcaction}! \n'



    def player_action(self):
        global save_step_player
        self.player_throw=input(str('Вы бросаете : ')).lower()
        for x,y in self.step.items():
            if self.player_throw==y:
                self.save_step_player=x
                return f'Вы бросили {self.player_throw}! \n'
        if self.save_step_player!=self.player_throw:
            print('Вы должны бросить камень, ножницы или бумагу!')
            return self.player_action()



    def start_game(self):
            print('Начинаем игру... ',end='\n')
            print(self.player_action())
            print(self.pc_action())
            if self.save_step_player == self.save_step_pc:
                return 'Ничья!\n'
            elif (self.save_step_player == 'r' and self.save_step_pc=='s') or (self.save_step_player=='s' and self.save_step_pc=='p') or (self.save_step_player== 'p' and self.save_step_pc=='r'):
                return 'Вы выиграли! \n'
            else:
                return 'Вы проиграли!\n'
play=Game()
while True:
    print(play.start_game())
    ask=input(str('Ещё одну игру? пиши "да" если хочешь реванш : ')).lower()
    if ask!='да':
        print('Пока!')
        break


