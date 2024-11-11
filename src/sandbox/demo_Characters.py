
from src.character.Character import Character

me=Character("David",1,1000,100,6,2)
cpu=Character("CPU",1,1000,100,6,1)


print(f"Available moves: {me.get_move_list()}")
print(f"CPU HP: {cpu.get_curr_hp()}")
me.set_target(cpu)
cpu.set_target(me)

my_input=""
while my_input=="":

    cpu.execute_move("Defend")

    me.attack()
    print(f"CPU HP: {cpu.get_curr_hp()}\n")

    cpu.execute_move("Attack")
    print(f"David HP: {me.get_curr_hp()}\n")

    me.execute_move("Attack")
    print(f"CPU HP: {cpu.get_curr_hp()}\n")

    me.execute_move("Attack")
    print(f"CPU HP: {cpu.get_curr_hp()}\n")

    my_input=input("Keep going?")