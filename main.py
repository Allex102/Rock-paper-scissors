from random import randint
class Game():

    step={'к':'камень','p':'бумага','s':'ножницы'}
    save_step_pc=0
    save_step_player=0

    def pc_action(self):
        self.pcaction=randint(1,3)
        for x,y in self.step.items():
            if self.pcaction==x:
                global save_number_pc
                save_number_pc=x
                self.pcaction=y
                return f'Компьютер бросил {self.pcaction}!'



    def player_action(self):
        self.player_throw=input(str('Вы бросаете : ')).lower()
        for x,y in self.step.items():
            if self.player_throw==y:
                global save_step_player
                save_step_player=x
                return f'Вы бросили {self.player_throw}! \n'
        raise Exception ('Вы должны выбросить камень ножницы или бумагу!')

    def start_game(self):
        print('Начинаем игру... ',end='\n')
        print(self.player_action())
        print(self.pc_action())
        if self.save_step_player==self.save_step_pc:
            return 'Ничья!'




