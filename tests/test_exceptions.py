from unittest import TestCase

from backEnd.utils import calories_counter, comp_cal_counter, comp_cal_counter2
from backEnd.exceptions import BigMealException

class test_exceptions_TestCase(TestCase):
    def calories_counter_exception(self):
        with self.assertRaises(BigMealException) as e:
            calories_counter('Cheesy Combo', 'Cheesy Combo', 'Cheesy Combo')
            self.assertEqual(
                e.exception.message,
                "Meal has 3210 calories, which is too much!",
                "wrong exception message"
            )
            
    def comp_cal_counter_exception(self):
        with self.assertRaises(BigMealException) as e:
            comp_cal_counter('combo-1', 'combo-1', 'combo-1')
            self.assertEqual(
                e.exception.message,
                "Meal has 3210 calories, which is too much!",
                "wrong exception message"
            )

    def comp_cal_counter2_exception(self):
        with self.assertRaises(BigMealException) as e:
            comp_cal_counter2('combo-1', 'combo-1', 'combo-1')
            self.assertEqual(
                e.exception.message,
                "Meal has 3210 calories, which is too much !",
                "wrong exception message"
            )