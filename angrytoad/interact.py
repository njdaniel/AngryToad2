def user_create_character(new_character):
    print("Please help finish")
    get_name = input("Please enter name: ")
    new_character.set_name(get_name)
    print("You have %d points to spend on Attributes:" % (new_character.points))

    # Distributing the points
    while True:
        CHARACTER_POINTS_COMMANDS = ['add_points', 'remove_points', 'reset_points']
        new_character._attributes = {'Strength': new_character.strength, 'Dexterity': new_character.dexterity,
                                     'Constitution': new_character.constitution,
                                     'Intelligence': new_character.intelligence, 'Wisdom': new_character.wisdom,
                                     'Charisma': new_character.charisma}
        new_character.print_attributes()

        command = input("Enter command to alter points"
                        "(ex. <add,remove>, <attribute>, <amount>"
                        "OR <clear> to reset attributes "
                        "OR <confirm> to finalize character: ")

        numbers_inlist = [x for x in command if x.isdigit()]
        if numbers_inlist:
            amount = int(''.join(numbers_inlist))
        attribute_to_alter = ''
        for key in new_character._attributes.items():
            if key[0].lower() in command:
                attribute_to_alter = key[0].lower()
        if 'clear' in command.lower():
            new_character.reset_points()
            new_character.print_attributes()
        elif 'add' in command.lower():
            new_character.add_points(amount, attribute_to_alter)
            new_character.print_attributes()
        elif 'remove' in command.lower():
            new_character.remove_points(amount, attribute_to_alter)
            new_character.print_attributes()
        elif 'confirm' in command.lower():
            new_character.print_attributes()
            confirmation = input("Are you sure?[y/n] ")
            if confirmation is 'y':
                break
            else:
                continue

# Print for loops
    def print_attributes(character):
        for key, value in character._attributes.items():
            print(key, value)
    def print_commands(character, commands):
        for command in commands:
            print(command, end='')