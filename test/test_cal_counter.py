from unittest import TestCase
# import backEnd.utils as utils
# import backEnd.constants as constants

import backEnd.classes as classes


class OrderMaking(TestCase):
    def count_cals(self):
        order = Order(['Hamburger'])
        assert order.calories == 600


# class CalCounterTestCase(TestCase):
#     def individual_items(self):
#         oneItem = ['Hamburger']
#         assert calories_counter(oneItem) == '600'
