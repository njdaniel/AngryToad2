import sys
from angrytoad.character import Character


def main(args=None):
    """Main routine"""
    if args is None:
        args = sys.argv[1:]

    print("In main")

    # Start program here
    # 1. Start up game menu

    # 2. Select or Create character
    list_characters = []
    
    # Creating new Character by user
    new_character = Character()
    new_character.user_create_character()
    list_characters.append(new_character)
    for x in list_characters:
        print(x.name)
    player1 = input("Choose your character for player1: ")
    player2 = input("Choose your character for player2: ")

    # 3. Choose Opponent to fight

    # 4. Call algorithm for the fight/manual fight

    # 5. Display results of fight with option to: fight again, pick new opponent, or back to main menu

if __name__=='__main__':
    main()


