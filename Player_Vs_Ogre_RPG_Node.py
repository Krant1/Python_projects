from random import randint,choice
game_decision=[]
class DecisionNode:
    def __init__(self,title,description,menu_a,menu_b,node_a,node_b):
        self.title=title
        self.description=description
        self.menu_a=menu_a
        self.menu_b=menu_b
        self.node_a=node_a
        self.node_b=node_b

    def process(self):
        self.node_pointer=None
        print(f'''
        {self.title}:{self.description}
        A) {self.menu_a}
        B) {self.menu_b}
        ''')
        self.choose_option=input('Which one do you choose? ')
        if self.choose_option.upper()=='A':
            self.node_pointer=self.node_a
        elif self.choose_option.upper()=='B':
            self.node_pointer=self.node_b
        else:
            print('Invalid input, please enter between A) and B)')
        return self.node_pointer

class Character:
    def __init__(self,name,health,strength):
        self.name=name
        self.health=health
        self.strength=strength

    def fight(self,enemy):
        self.fight_option=choice(['hit','miss'])
        if self.fight_option=='hit':
            enemy.health=enemy.health-self.strength
            print(f'{self.name} hits {enemy.name}')
            print(f'''
            {self.name}  : Health Remaining ={self.health} 
            {enemy.name} : Health Remaining ={enemy.health}''')
        else:
            print(f'{self.name} misses {enemy.name}')

player=Character('player', 50, 10)
ogre=Character('ogre', 50, 10)

class CombatNode:
    def __init__(self,player,enemy,description,win_node,lose_node):
        self.player=player
        self.enemy=enemy
        self.description=description
        self.win_node=win_node
        self.lose_node=lose_node

    def process(self):
        print(self.description)
        while True:
            player.fight(ogre)
            if ogre.health<=0 :
                self.result=self.win_node
                break
            ogre.fight(player)
            if player.health<=0 :
                self.result=self.lose_node
                break
        return self.result

def sample_game():
    game_decision.append(DecisionNode('start','You see a monster','fight','run',1,2))
    game_decision.append(CombatNode(player,ogre,'Fight the ogre',3,4))
    game_decision.append(DecisionNode('Dead','Monster chased you and killed you','start over','quit',0,5))
    game_decision.append(DecisionNode('Win','You killed the monster','start over','quit',0,5))
    game_decision.append(DecisionNode('Lose','Monster killed you','start over','quit',0,5))
    game_decision.append(DecisionNode('game over','','','',0,0))

def game():
    quit_node=5
    node_pointer=0
    while node_pointer!=quit_node:
        current_node=game_decision[node_pointer]
        node_pointer=current_node.process()
        current_node=game_decision[node_pointer]

def main():
    sample_game()
    game()
    print(game_decisions)

if __name__ == "__main__":
  main()

