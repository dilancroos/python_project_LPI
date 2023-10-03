from unittest import TestCase
from backEnd.utils import calories_counter
# from backEnd.constants import calories, combos  

class CalCounterTestCase(TestCase):
    def individual_items(self):
        oneItem = ['Hamburger']
        assert calories_counter(oneItem) == '600'