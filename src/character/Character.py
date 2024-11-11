import random

#Declare constants for game tuning
ATTACK_DICE = 6
DEFEND_DICE = 2

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
        self.__messenger=self
        self.__attack_move=self._Skill("Punch","physical",self.__base_stats.strength,0,"none")
        self.__move_list={
            "Attack":self.attack,
            "Defend":self.defend,
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
        #Set HP:
        self.__battle_stats.hp=hp
        #Health shouldn't dip below 0:
        if self.__battle_stats.hp<0:
            self.__battle_stats.hp=0
        #Ensure health doesn't go above max
        if self.__battle_stats.hp>self.__base_stats.hp:
            self.__battle_stats.hp=self.__base_stats.hp

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
        self.__attack_move.dmg= self.__battle_stats.strength * roll_die(ATTACK_DICE)
        self.deliver_message(self.__messenger,f"{self.__name} attacks with {self.__attack_move.name} for {self.__attack_move.dmg}!")
        self.__target.receive_attack(self.__attack_move)

    def defend(self):
        self.deliver_message(self.__messenger,f"{self.__name} guards themself.")
        self.__condition.shield_up=True

    def receive_attack(self,attack):
        is_heal=False   #Check if "Attack heals"
        final_dmg=attack.dmg    #Final damage starts at attack damage

        #Roll dice to determine defense against attack:
        defense=self.__battle_stats.strength * roll_die(DEFEND_DICE)
        #Shield doubles defense:
        if self.__condition.shield_up:
            defense*=2
        #Total damage is reduced by defense:
        final_dmg = max(final_dmg-defense,0)

        #Check for affinities:
        if (self.__condition.affinities.get(attack.s_type) is not None and
            self.__condition.affinities.get(attack.s_type) is True):

            #Update message
            self.deliver_message(self.__messenger,f"{self.__name} is resistant to {attack.name} attack.")
            #Affinities only deliver half damage
            final_dmg=int(final_dmg/2)

        # Check for aversions:
        if (self.__condition.aversions.get(attack.s_type) is not None and
                self.__condition.affinities.get(attack.s_type) is True):
            # Update message
            self.deliver_message(self.__messenger, f"{attack.name} is very effective!")
            # Aversions do double damage:
            final_dmg = int(final_dmg *2)

        #Check for healing:
        if (self.__condition.heal_affinity.get(attack.s_type) is not None and
                self.__condition.affinities.get(attack.s_type) is True):
            # Update message
            self.deliver_message(self.__messenger, f"HP UP")
            # Healers give health:
            is_heal=True

        if is_heal:
            # Update message
            self.deliver_message(self.__messenger, f"{self.__name} is healed for {final_dmg} points of health.")
            # Add to health:
            self.set_curr_hp(self.__battle_stats.hp+final_dmg)
        else:
            #Update message
            self.deliver_message(self.__messenger,f"{self.__name} receives {final_dmg} points of damage.")
            #Subtract final damage from health:
            self.set_curr_hp(self.__battle_stats.hp-final_dmg)


    def execute_move(self,command):
        self.__condition.shield_up=False
        self.__move_list[command]()

    def stub_command(self):
        pass

    def deliver_message(self, messenger, message):
        #stub
        print(message)

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
            self.aversions={"magic":False}
            self.heal_affinity={"life":True}

