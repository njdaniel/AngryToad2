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
    new_character = Character()

    # 3. Choose Opponent to fight

    # 4. Call algorithm for the fight

    # 5. Display results of fight with option to: fight again, pick new opponent, or back to main menu

if __name__=='__main__':
    main()


