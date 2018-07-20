import unittest
import sys
from loot import Loot

class TestLoot(unittest.TestCase):
    def test_class_loot_exists (self):
        loot = Loot()
        self.assertTrue(True, loot)

    def test_child_and_loot_adds_to_bag(self):
        bag = Loot()
        bag.add_loot_and_child_to_bag('Matt', 'YoYo')
        result = bag.all_loot[0]
        expected = ('Matt', 'YoYo')
        self.assertEqual(expected, result)

    def test_remove_child_and_loot_from_bag(self):
        bag = Loot()
        bag.add_loot_and_child_to_bag('Matt', 'YoYo')
        bag.remove_loot('Matt', 'YoYo')
        result = len(bag.all_loot)
        expected = 0
        self.assertEqual(expected, result)

    # def test_list_children_receiving_toy(self):
    #     bag = Loot()
    #     bag.add_loot_and_child_to_bag('Matt', 'YoYo')
    #     bag.add_loot_and_child_to_bag('Pat', 'Bike')
    #     bag.list_children()
    #     self.assertEqual(('Matt', 'Pat'), bag.list_children())

    def test_if_loot_delivered_to_child(self):
        bag = Loot()
        self.assertEqual("loot delivered to child", bag.delivered_loot())




if __name__ == '__main__':
    unittest.main()

    # lootBag = Bag()
    # lootBag.add_toy_for_child("kite", "suzy");
    # self.assertEqual("kite", lootBag.child_items("suzy")[0]);