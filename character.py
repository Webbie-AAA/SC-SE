class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description

# ted = Character("Ted", "Talkative")

    def describe(self):
        print(f"{self.name} is in this room!")
        print(self.description)

    def set_conversation(self, conversation):
        self.set_conversation = conversation

    def talk(self):
        if self.set_conversation != None:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print(f"[{self.name} doesn't want to talk to you.]")

    def fight(self, combat_item):
        print(f"[{self.name}]: Doesn't want to fight you.")
        return True
    
class Enemy(Character):

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You have defeated {self.name} with the {self.combat_item}")
        else:
            print(f"  has defeated you")



    
