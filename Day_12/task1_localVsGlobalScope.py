enemies =1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies from outside function: {enemies}")

'''
# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
print(potion_strength) # variable only accesseble inside the local scope
'''

# Globel Scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
print(player_health)