import random


def roll_die(sides):
    return random.randint(1,sides)


class Character:
    def __init__(self,name,level,hp,mp,strength,intel):
        self.__name=name
        self.__level = level
        self.__base_stats=self._Stats(hp,mp,strength,intel)
        self.__battle_stats=self._Stats(hp,mp,strength,intel)
        self.__condition=self._Condition()
        self.__target=self
        self.__attack_move=self._Skill("Attack","physical",self.__curr_str,0,"none")
        self.__move_list={
            "Attack":self.attack,
            "Defend":self.stub_command,
        }



    #Getters:
    def get_name(self):
        return self.__name

    def get_max_hp(self):
        return self.__base_stats.hp

    def get_curr_hp(self):
        return self.__battle_stats.hp

    def get_max_mp(self):
        return self.__base_stats.mp

    def get_curr_mp(self):
        return self.__battle_stats.mp

    def get_base_strength(self):
        return self.__base_stats.strength

    def get_battle_strength(self):
        return self.__battle_stats.strength

    def get_base_intel(self):
        return self.__base_stats.intel

    def get_battle_intel(self):
        return self.__battle_stats.intel

    def get_level(self):
        return self.__level

    def get_move_list(self):
        return list(self.__move_list.keys())

    def get_target(self):
        return self.__target

    def get_battle_effect(self):
        return self.__battle_stats.effect


    #Setters
    def set_name(self,name):
        self.__name=name

    def set_max_hp(self,hp):
        self.__base_stats.hp=hp
    def set_curr_hp(self,hp):
        self.__battle_stats.hp=hp

    def set_max_mp(self,mp):
        self.__base_stats.mp=mp

    def set_curr_mp(self,mp):
        self.__battle_stats.mp=mp

    def set_base_strength(self,strength):
        self.__base_stats.strength=strength

    def set_battle_strength(self,strength):
        self.__battle_stats.strength=strength

    def set_base_intel(self,intel):
        self.__base_stats.intel=intel

    def set_battle_intel(self,intel):
        self.__battle_stats.intel=intel

    def set_level(self,level):
        self.__level=level

    def set_target(self,target):
        self.__target=target

    # def set_move_list(self):
    #     return self.__move_list

    def attack(self):
        self.__attack_move.dmg= self.__battle_stats.strength * roll_die(6)
        self.__target.receive_attack(self.__attack_move)

    def defend(self):
        self.__condition.shield_up=True

    def receive_attack(self,attack):
        final_dmg=attack.dmg
        final_dmg-= self.__battle_stats.strength * roll_die(2)
        if (self.__condition.affinities.get(attack.s_type) is not None and
            self.__condition.affinities.get(attack.s_type) is True):
            final_dmg=int(final_dmg/2)
        self.__battle_stats.hp-=final_dmg

    def execute_move(self,command):
        self.__condition.shield_up=False
        self.__move_list[command]()

    def stub_command(self):
        pass
    #----------------------Skill-------------------------------
    class _Skill:
        """
        This is a class to hold skill properties
        """
        def __init__(self, name,s_type,dmg,cost,effect):
            self.name = name
            self.s_type=s_type
            self.dmg=dmg
            self.cost=cost
            self.effect=effect
    #-----------------------Base Stats---------------------------
    class _Stats:
        def __init__(self,hp,mp,strength, intel):
            self.hp = hp  #health
            self.mp = mp  # magic points
            self.strength = strength  # determines physical attributes
            self.intel=intel    #determines ability aptitude
            self.effect="" #status effects

    #----------------------Condition-------------------------------
    class _Condition:
        def __init__(self):
            self.shield_up=False
            self.affinities= {"physical":False}
