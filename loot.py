class Loot():
    """class Loot represents bag of loot with childrens presents"""
    def __init__(self):
        self.all_loot = []


    def add_loot_and_child_to_bag(self, child, loot):
        self.child = child
        self.loot = loot
        loot_child = (self.child, self.loot)
        self.all_loot.append(loot_child)

    def remove_loot(self, child, loot):
        self.child_and_loot = [child, loot]
        for x in self.all_loot:
            if (self.child_and_loot):
                self.all_loot.remove(self.child_and_loot)

    def list_children(self):
        for x in self.all_loot:
            return self.all_loot
        # return "list of children"

    def delivered_loot(self):
        return "loot delivered to child"
















