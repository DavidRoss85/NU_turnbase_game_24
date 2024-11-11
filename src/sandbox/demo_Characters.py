
from src.character.Character import Character

me=Character("David",1,100,100,1,1)
cpu=Character("CPU",1,100,100,1,1)


print(f"Available moves: {me.get_move_list()}")
print(f"CPU HP: {cpu.get_curr_hp()}")
me.set_target(cpu)
me.attack()
print("You Attack")
print(f"CPU HP: {cpu.get_curr_hp()}")

me.execute_move("Attack")
print("You Attack again")
print(f"CPU HP: {cpu.get_curr_hp()}")