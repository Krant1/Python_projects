import site
class Entity:
    def __init__(self,health,damage,stats):
        self.health=health
        self.damage=damage
        self.stats=stats

    def attack(self,attacker,target):
        return target.health-attacker.damage
        
    def show_stats(self):
        return self.stats

class Hyena(Entity):
    def __init__(self):
        self.name='Hyena'
        super().__init__(30, 10, None)

    def attack(self,attacker,target):
        return super().attack(attacker,target)

class Crocodile(Entity):
    def __init__(self):
        self.name='Crocodile'
        super().__init__(40,15,None)
    
    def attack(self,attacker,target):
        return super().attack(attacker,target)

class Witch(Entity):
    def __init__(self):
        self.name='Witch Of Belgarfurst'
        super().__init__(50,20,None)
    
    def attack(self,attacker,target):
        return super().attack(attacker,target)
    
    
class Player_Stats(Entity):
    def __init__(self):
        super().__init__(100,0,['speed','strength','agility'])
    
    def show_stats(self):
        self.abilities=','.join(self.stats)
        print(f'''
        Your health is {self.health}
        Your abilities are : {self.abilities}''')

    def choose_weapon(self,weapon_choice):
        self.weapon_choice=weapon_choice
        self.weapon_dict={'A':['Hammer',15],'B':['Arrow',10],'C':['Staff',10],'D':['Sword',20]}
        return self.weapon_dict.get(self.weapon_choice)

    def use_potion(self):
        self.health += 30
        print(f'Your health is now rejuvenated.It\'s at {self.health}')
    
    def player_attack(self,weapon_damage,target):
        self.weapon_damage=weapon_damage
        return int(target.health)-self.weapon_damage

class AdventuresOfEden():
    def __init__(self):
        self.player_stats=Player_Stats()
        self.hyena=Hyena()
        self.crocodile=Crocodile()
        self.witch=Witch()

    def combat(self,enemy):
        self.enemy=enemy
        self.no_of_attacks=int(input(f'How many times do you hit the {self.enemy.name}? '))
        for hit in range(self.no_of_attacks):
            self.player_health_left=self.enemy.attack(self.enemy,self.player_stats)
            self.player_stats.health=self.player_health_left
            print(f'Oh no! {self.enemy.name} has attacked you, your health has decreased by 10')
            print(f'Your health remaining: {self.player_stats.health}')
            self.enemy_health_left=self.player_stats.player_attack(self.weapon[1],self.enemy)
            self.enemy.health=self.enemy_health_left
            if self.enemy_health_left<=0:
                print(f'You killed the {self.enemy.name}')
                break
            print(f'{self.enemy.name}\'s health remaining: {self.enemy.health}') 
            if self.player_health_left<=0:
                print('You have died')
                print('Restart the game')
                exit()
            print('------*--------')

    def game(self):
        print('------*------')
        print('''
        Welcome, you are, Eden, a young ambitious mercenary on his way to his family
        You have to travel through jungles, grasslands, mountains to reach Engardia, the city where your family lives
        Your path is filled with creatures and obstacles, but your will is strong''')
        print('------*------')
        self.ask_question=input('Do you want to see your stats? ')

        if self.ask_question.lower()[:1]=='y':
            self.player_stats.show_stats()
        else:
            print('You seem very confident, Eden.But remember, the land doesn\'t treat those too well who take pride in themselves')
        print('------*------')
        print('''
        You move along the trodden path.The paved bricks now stained yellow and show years of exposure to the wrath of weather
        You come across a hut, the hut belongs to Balrug, the famed weapons-master.
        Balrug is known to be a giver.He sees you, smiles and invites to his hut
        Inside the hut, there are 4 boxes with A,B,C,D written on them.You look at Balrug with confusion
        Balrug smiles and says,'Under each of theses boxes, lies a weapon that will help you in your journey,
        but the choice of weapon is based solely on your luck,so choose, my child'
        You are confused but you know that your old weapons would be of no use against magical creatures.With a sigh, you look at the boxes...
        ''')
        print('------*------')
        self.ask_weapon=input('Which one of the boxes do you choose: A,B,C or D? ')
        self.weapon=self.player_stats.choose_weapon(self.ask_weapon)
        print(f'You get {self.weapon[0]} with a damage causing ability of {self.weapon[1]}')
        print('------*------')
        print('''
        With the new weapon in hand, you thank Balrug and take his leave
        You travel for days and nights, taking rest under the shade of trees and quenching your hunger with berries from trees
        One cloudy and gloomy day, you come across a bridge which seemed to be older than time itself.
        The weather gives the bridge a more menancing look.Under the bridge is the shallow remanants of once mighty river 
        You have two options, either you can waddle across the river, your you can go through the bridge.
        You know that you have a difficult choice to make
         ''')
        print('------*------')
        self.ask_path=input('Which path do you choose: Bridge or River? ')
        if self.ask_path.lower()[:1]=='b':
            print(f'''
            Ever so cautiously, you walk on the stone bridge, expectant of the danger that lies ahead.
            You hear a growl, with a figure yet to be identified running toward you
            You ready your {self.weapon[0]} with sweat drippin from your brows.Your weapon can deal a damage of {self.weapon[1]}
            It's a hyena! It looks hungry and is ready for a fight.According to your book of creatures, Hyena has a health of {self.hyena.health}
            ''')
            print('------*--------') 
            self.combat(self.hyena)
        elif self.ask_path.lower()[:1]=='r':
            print(f'''
            Cautiously, you waddle across the river, praying to the gods above that nothing snatches you from under the muddy waters
            Amongst the muddy waters, you see a shadow with two golden dots, to your horror, the dots seem to move forward
            You ready your {self.weapon[0]} with sweat drippin from your brows.Your weapon can deal a damage of {self.weapon[1]}
            It's a crocodile! It looks hungry and is ready for a fight.According to your book of creatures, Crocodile has a health of {self.hyena.health}
            ''')
            print('------*--------') 
            self.combat(self.crocodile)
            print('------*--------')
        print('''
        Wary of the battle, you take a rest near a tree.You seem to have taken some damage
        The damage seems repairable, but can be fatal if left untreated
        You remember your vial of life, a potion that could restore your health by 30 points''')   
        self.take_potion=input('Do you take the potion?: ')
        if self.take_potion.lower()[:1]=='y':
            self.player_stats.use_potion()
            if self.player_stats.health>100:
                print('Your health is now fully restored')
            elif self.player_stats.health<=100:
                print(f'You seem refreshed after taking the vial. Your health is now {self.player_stats.health}')
        else:
            print('It\'s a brave choice Eden, but remember, there is a long road and along that road you may encounter various creatures')
        print('------*--------')
        print('''
        After being refreshed, you travel along the path.
        As you walk, you find the colour of the road's bricks changing, the weather dampening and you can feel something wrong
        You see a hut, a sole hut in middle of jungle.The moonlight gives it an eerie look
        You have no choice but to take shelter in the hut as the weather worsens
        You knock once,twice,thrice....but no one answers.Reluctantly, you enter the hut
        To your shock, the hut is much larger on the inside with everything inside made of marble.
        You cannot believe your eyes as they look at this magnificent sight.
        Your eyes jump from te marble furnitures to strange souvenirs from foreign lands
        Then....you see it, a strange symbol, you cannot believe it, you remember this symbol from a time long ago
        The symbol is of Witch Of Belgarfurst, who is known to be from the dark side
        You try to turn away, but are hit with a stench, a stench emanating from.....the witch herself
        'You', she screams, 'How dare you enter my hut? You shall face my wrath'.She begins to cast spell after spell, and you parry it with your weapon
        After some time, the witch seems tired, now might be your chance.........
        ''')
        self.combat(self.witch)
        print('------*--------')
        print('''
        You have done it....you killed the Witch Of Belgarfurst.
        You are still in disbelief, adrenalin coursing through your veins.You think this is all a dream, but the witch's lifeless body says otherwise
        Suddenly, you see her body disintegrating, and somehow all that's left of her is her necklace
        The necklace is made of pure emerald, and thought to be one of the most expensive items in the land
        You take the necklace from the pile of ash, and leave the hut
        This journey has brought you many blows, but it also gave you this necklace.
        Now, you won\'t have to travel far away,your wife won't have to wrk as a help in noble's houses.
        You can all live a great life now.
        As you are thinking of this, you see a distant light, the sun has risen and with it's sunlight, you're able to see your city,home is not far away,after all....''')
        print('------*--------')
        print('THE END')

player_1=AdventuresOfEden()
player_1.game()


