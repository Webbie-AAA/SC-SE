class Item():
    # This is called a constructor method
    def __init__(self, item_name):
        self.name = item_name
        self.description = None

    def get_item(self):
        return self.item_name
    
    def set_Item(self, item_name):
        self.description = item_name

    def get_description(self):
        return self.description
    
    def set_description(self, item_description):
        self.description = item_description

    
