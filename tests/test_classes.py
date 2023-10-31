from unittest import TestCase

from backEnd.classes import Order

class order_Making_TestCase(TestCase):
    def check_order_counter(self):
        current_counter = Order.counter
        order1 = Order([])
        self.assertEqual(order1.order_id, f"order-{current_counter}")
        order2 = Order([])
        self.assertEqual(order2.order_id, f"order-{current_counter + 1 }")
         