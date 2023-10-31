from unittest import TestCase

from backEnd.utils import calories_counter, comp_cal_counter, comp_cal_counter2, price_counter
from backEnd.jsonUtils import comp_cal_counter_json, price_counter_json

class calories_counterTestCase(TestCase):
    def test_calaries_simple(self):
        result = calories_counter('Hamburger','Salad','Iced Tea')
        self.assertEqual(result, 685, f"Expected 685, got {result}") 

    def test_calaries_combo(self):
        result = calories_counter('Cheesy Combo')
        self.assertEqual(result, 1070, f"Expected 1070, got {result}")

    def test_mix(self):
        result = calories_counter('Hamburger', 'Cheesy Combo')
        self.assertEqual(result, 1670, f"Expected 1670, got {result}")

    def test_calaries_complex_id(self):
        result = comp_cal_counter('meal-1', 'meal-2', 'meal-3')
        self.assertEqual(result, 1750, f"Expected 1750, got {result}")

    def test_calaries_complex_name(self):
        result = comp_cal_counter('hamburger','salad','iced tea')
        self.assertEqual(result, 685, f"Expected 685, got {result}")

    # Complex loop through method

    def test_calaries_combo_complex_id2(self):
        result = comp_cal_counter('combo-1', 'combo-2')
        self.assertEqual(result, 1770, f"Expected 1770, got {result}")

    def test_calaries_combo_complex_name2(self):
        result = comp_cal_counter('cheesy combo', 'veggie combo')
        self.assertEqual(result, 1770, f"Expected 1770, got {result}")

    def test_calaries_complex_mix_id2(self):
        result = comp_cal_counter('meal-1', 'combo-2')
        self.assertEqual(result, 1300, f"Expected 1300, got {result}")

    def test_calaries_complex_mix_name2(self):
        result = comp_cal_counter('hamburger', 'veggie combo')
        self.assertEqual(result, 1300, f"Expected 1300, got {result}")

    # Complex dict method

    def test_calaries_combo_complex_id(self):
        result = comp_cal_counter2('combo-1', 'combo-2')
        self.assertEqual(result, 1770, f"Expected 1770, got {result}")

    def test_calaries_combo_complex_name(self):
        result = comp_cal_counter2('cheesy combo', 'veggie combo')
        self.assertEqual(result, 1770, f"Expected 1770, got {result}")

    def test_calaries_complex_mix_id(self):
        result = comp_cal_counter2('meal-1', 'combo-2')
        self.assertEqual(result, 1300, f"Expected 1300, got {result}")

    def test_calaries_complex_mix_name(self):
        result = comp_cal_counter2('hamburger', 'veggie combo')
        self.assertEqual(result, 1300, f"Expected 1300, got {result}")

class price_counterTestCase(TestCase):
    
    def test_price_complex_id(self):
        result = price_counter('meal-1', 'meal-2', 'meal-3')
        self.assertEqual(result, 18, f"Expected 18, got {result}")

    def test_price_complex_name(self):
        result = price_counter('hamburger','salad','iced tea')
        self.assertEqual(result, 11, f"Expected 11, got {result}")

class json_fileTestCase(TestCase):

    def test_json_calaries_combo_complex_id(self):
        result = comp_cal_counter_json('combo-1', 'combo-2')
        self.assertEqual(result, 1770, f"Expected 1770, got {result}")

    def test_json_calaries_combo_complex_name(self):
        result = comp_cal_counter_json('cheesy combo', 'veggie combo')
        self.assertEqual(result, 1770, f"Expected 1770, got {result}")

    def test_json_calaries_complex_mix_id(self):
        result = comp_cal_counter_json('meal-1', 'combo-2')
        self.assertEqual(result, 1300, f"Expected 1300, got {result}")

    def test_json_calaries_complex_mix_name(self):
        result = comp_cal_counter_json('hamburger', 'veggie combo')
        self.assertEqual(result, 1300, f"Expected 1300, got {result}")

    def test_json_price_complex_id(self):
        result = price_counter_json('meal-1', 'meal-2', 'meal-3')
        self.assertEqual(result, 18, f"Expected 18, got {result}")

    def test_json_price_complex_name(self):
        result = price_counter_json('hamburger','salad','iced tea')
        self.assertEqual(result, 11, f"Expected 11, got {result}")