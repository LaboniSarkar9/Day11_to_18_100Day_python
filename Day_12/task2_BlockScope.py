#There is no Block Scope in python
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
'''
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)
'''
def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)
