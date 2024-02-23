# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def __init__(self, items):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items
        
    def test_update_quality_for_vest(self):
        # Test how the code updates a vest item
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 10, 20)]  # Initial quality and sell_in values
        gr = GildedRose(items)

        gr.update_quality()

        self.assertEqual(items[0].sell_in, 9)  # Sell-in should decrease by 1
        self.assertEqual(items[0].quality, 19)  # Quality should decrease by 1

    def test_update_quality_for_aged_brie(self):
        # Test how the code updates Aged Brie item
        aged_brie = "Aged Brie"
        items = [Item(aged_brie, 2, 0)]  # Initial quality and sell_in values
        gr = GildedRose(items)

        gr.update_quality()

        self.assertEqual(items[0].sell_in, 1)  # Sell-in should decrease by 1
        self.assertEqual(items[0].quality, 1)   # Quality should increase by 1

    def test_update_quality_for_backstage_passes(self):
        # Test how the code updates Backstage passes item
        backstage_passes = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(backstage_passes, 15, 20)]  # Initial quality and sell_in values
        gr = GildedRose(items)

        gr.update_quality()

        self.assertEqual(items[0].sell_in, 14)  # Sell-in should decrease by 1
        self.assertEqual(items[0].quality, 21)   # Quality should increase by 1

if __name__ == '__main__':
    unittest.main()
