"""
Contains classes and functions for all the collectibles in the game
"""


from gameplay import slowprint, exit_game
from questions import YesNo
from emojis import Emoji


emoji_choices = Emoji()
inventory = []


class Wand:
    """
    Wand class
    """
    def __init__(self, owner, length, wood, core, characteristic):
        """
        Creates an instance of Wand
        """
        self.owner = owner
        self.length = length
        self.wood = wood
        self.core = core
        self.characteristic = characteristic

    def description(self):
        """
        Describes the wand
        """
        return (
            f"'This wand is {self.length} long, "
            f"is made with {self.wood} wood, "
            f"has a(n) {self.core} core, "
            f"and is {self.characteristic}!'"
        )

    def add_wand_to_inventory(self):
        """
        Adds wand to the player's inventory
        """
        inventory.append({self.owner})
        return (
            f"{self.owner} was added to your inventory."
        )


class Pet:
    """
    Pet class
    """
    def __init__(self, kind, skill):
        """
        Creates an instance of Pet
        """
        self.kind = kind
        self.skill = skill

    def choice_confirmation(self):
        """
        Confirms pet choice
        """
        return f"'Great choice! You'll love your {self.kind}!'"

    def description(self):
        """
        Describes the pet
        """
        return (
            f"'{self.kind.capitalize()}s are known for their impressive "
            f"{self.skill} skills. Use this wisely!'"
        )

    def add_pet_to_inventory(self):
        """
        Adds pet to the player's inventory
        """
        inventory.append(str({self.kind}))
        return f"Your {self.kind} was added to your inventory."


def collect_key_backstory():
    """
    Runs backstory on player collecting key from chest
    """
    slowprint(
        "Nice work, now you can reach the chest and get the key!" +
        emoji_choices.key_emoji()
    )
    add_to_inventory("key")


def unlock_door_request():
    """
    Asks the player if they want to unlock the door or not
    """
    unlock_door_responses = YesNo(
        "Of course you do! Here we go...",
        "Unusual choice, but it's your decision..."
        )

    use_key_input = input(
        "Do you want to use the key to unlock the door? (y/n) \n"
        )

    print("\n")

    if use_key_input == "y":
        slowprint(
            unlock_door_responses.yes_response() +
            emoji_choices.happy_emoji()
        )
    elif use_key_input == "n":
        slowprint(
            unlock_door_responses.no_response() +
            emoji_choices.neutral_emoji()
        )
        exit_game()
    else:
        slowprint(
            unlock_door_responses.other_response() +
            emoji_choices.neutral_emoji()
        )
        unlock_door_request()


def add_to_inventory(item):
    """
    Adds the collectible found by the player to their inventory
    """
    inventory.append(str({item}))

    slowprint(
        f"The {item} was added to your inventory." +
        emoji_choices.backpack_emoji()
    )


def key_main():
    """
    Runs the key backstory, adds it to the player's inventory,
    and asks the player if they want to unlock the door
    """
    collect_key_backstory()
    unlock_door_request()
