from unittest import TestCase
# import backEnd.utils as utils
# import backEnd.constants as constants

import backEnd.classes as classes

class calories_counterTestCase(TestCase):
    def test_calaries_simple(self):
        pass

    def test_calaries_simple_unknown(self):
        pass

    def test_calaries_combo(self):
        pass

    def test_calaries_combo_unknown(self):
        pass

    def test_mix(self):
        pass

    def test_mix_unknown(self):
        pass

    def test_calaries_complex_id(self):
        pass

    def test_calaries_complex_id_unknown(self):
        pass

    def test_calaries_complex_name(self):
        pass

    def test_calaries_complex_name_unknown(self):
        pass

    def test_calaries_combo_complex_id(self):
        pass

    def test_calaries_combo_complex_id_unknown(self):
        pass

    def test_calaries_combo_complex_name(self):
        pass

    def test_calaries_combo_complex_name_unknown(self):
        pass

    def test_calaries_complex_mix_id(self):
        pass

    def test_calaries_complex_mix_id_unknown(self):
        pass

    def test_calaries_complex_mix_name(self):
        pass

    def test_calaries_complex_mix_name_unknown(self):
        pass

    def test_price_complex_id(self):
        pass

    def test_price_complex_id_unknown(self):
        pass

    def test_price_complex_name(self):
        pass

    def test_price_complex_name_unknown(self):
        pass

    def calories_counter_exception(self):
        pass
    
    def comp_cal_counter_exception(self):
        pass

    def comp_cal_counter2_exception(self):
        pass




class OrderMakingTestCase(TestCase):
    def count_cals(self):
        order = Order(['Hamburger'])
        assert order.calories == 600


# class CalCounterTestCase(TestCase):
#     def individual_items(self):
#         oneItem = ['Hamburger']
#         assert calories_counter(oneItem) == '600'
