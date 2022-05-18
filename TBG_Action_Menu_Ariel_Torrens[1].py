# TBG Action Menu - Ariel Torrens
# May 18, 2022

# This code creates an action menu
# for my TBG.

name = input("What is your name? ") + (": ")
print((name) + "Perhaps I should call him...")

def scene_1():
    print("What do you do?")
    print("""> Call him
> Sit and wait for him
> Order another drink""")
    s1_input = input()
    
    if s1_input == "call him":
        print("""Your hand starts to sweat as you pick up your phone.
You start to dial in his number and pause before you do. Your thumb
hovers over the screen and you start to type in his phone number""")
        print("""\nJoe doesn't pick up his phone. The waiter comes and asks
you if you want to order another drink""")
        scene_2()
    elif s1_input == "sit and wait for him":
        print("""You rest your hands on the table in front of you and start to
fiddle with the straw twisting, twirling and stirring your drink.
Thinking of what happened to Joe terrifies you.""")
        print("""The waiter comes and asks you if you want to order another drink""")
        scene_2()
    elif s1_input  == "order another drink":
        print("""You wave to one of the waiters. You see a handsome young guy in
his mid twenties start to walk over to you""")
        scene_2()
    else:
        print("Invalid input. Re-enter your choice")
        scene_1()
        
def scene_2():
    print((name) + "I would like to order a...")
    print("""> Glass of wine
> Glass of water
> Shot of vodka""")
    s2_input = input()
    
    if s2_input == "glass of wine":
        print(f"I'll bring a {s2_input} right away")
    elif s2_input == "glass of water":
        print(f"I'll bring a {s2_input} right away")
    elif s2_input == "shot of vodka":
        print(f"I'll bring a {s2_input} right away")
    else:
        print("Waiter: Sorry, we don't have that on the menu.")
        scene_2()

scene_1()
