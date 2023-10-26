from unittest import TestCase

from backEnd.utils import calories_counter, comp_cal_counter, comp_cal_counter2, price_counter

import backEnd.classes as classes

class calories_counterTestCase(TestCase):
    def test_calaries_simple(self):
        result = calories_counter('Hamburger','Salad','Iced Tea')
        self.assertEqual(result, 685, f"Expected 685, got {result}") 

    def test_calaries_simple_unknown(self):
        result = calories_counter('Hamburger','Salad','Iced Tea', 'Unknown')
        self.assertEqual(result, 685, f"Expected 685, got {result}")

    def test_calaries_combo(self):
        result = calories_counter('Cheesy Combo')
        self.assertEqual(result, 1070, f"Expected 1070, got {result}")

    def test_calaries_combo_unknown(self):
        result = calories_counter('Cheesy Combo', 'Unknown')
        self.assertEqual(result, 1070, f"Expected 1070, got {result}")

    def test_mix(self):
        result = calories_counter('Hamburger', 'Cheesy Combo')
        self.assertEqual(result, 1670, f"Expected 1670, got {result}")

    def test_mix_unknown(self):
        result = calories_counter('Hamburger', 'Cheesy Combo', 'Unknown')
        self.assertEqual(result, 1670, f"Expected 1670, got {result}")

    def test_calaries_complex_id(self):
        result = comp_cal_counter('meal-1', 'meal-2', 'meal-3')
        self.assertEqual(result, 1750, f"Expected 1750, got {result}")

    def test_calaries_complex_id_unknown(self):
        result = comp_cal_counter('meal-1', 'meal-2', 'meal-3', 'Unknown')
        self.assertEqual(result, 1750, f"Expected 1750, got {result}")

    def test_calaries_complex_name(self):
        result = comp_cal_counter('hamburger','salad','iced tea')
        self.assertEqual(result, 685, f"Expected 685, got {result}")

    def test_calaries_complex_name_unknown(self):
        result = comp_cal_counter('hamburger','salad','iced tea', 'Unknown')
        self.assertEqual(result, 685, f"Expected 685, got {result}")

    # Complex loop through method

    def test_calaries_combo_complex_id2(self):
        result = comp_cal_counter('combo-1', 'combo-2')
        self.assertEqual(result, 1770, f"Expected 1770, got {result}")

    def test_calaries_combo_complex_id_unknown2(self):
        result = comp_cal_counter('combo-1', 'combo-2', 'Unknown')
        self.assertEqual(result, 1770, f"Expected 1770, got {result}")

    def test_calaries_combo_complex_name2(self):
        result = comp_cal_counter('cheesy combo', 'veggie combo')
        self.assertEqual(result, 1770, f"Expected 1770, got {result}")

    def test_calaries_combo_complex_name_unknown2(self):
        result = comp_cal_counter('cheesy combo', 'veggie combo', 'Unknown')
        self.assertEqual(result, 1770, f"Expected 1770, got {result}")

    def test_calaries_complex_mix_id2(self):
        result = comp_cal_counter('meal-1', 'combo-2')
        self.assertEqual(result, 1300, f"Expected 1300, got {result}")

    def test_calaries_complex_mix_id_unknown2(self):
        result = comp_cal_counter('meal-1', 'combo-2', 'Unknown')
        self.assertEqual(result, 1300, f"Expected 1300, got {result}")

    def test_calaries_complex_mix_name2(self):
        result = comp_cal_counter('hamburger', 'veggie combo')
        self.assertEqual(result, 1300, f"Expected 1300, got {result}")

    def test_calaries_complex_mix_name_unknown2(self):
        result = comp_cal_counter('hamburger', 'veggie combo', 'Unknown')
        self.assertEqual(result, 1300, f"Expected 1300, got {result}")

    # Complex dict method

    def test_calaries_combo_complex_id(self):
        result = comp_cal_counter2('combo-1', 'combo-2')
        self.assertEqual(result, 1770, f"Expected 1770, got {result}")

    def test_calaries_combo_complex_id_unknown(self):
        result = comp_cal_counter2('combo-1', 'combo-2', 'Unknown')
        self.assertEqual(result, 1770, f"Expected 1770, got {result}")

    def test_calaries_combo_complex_name(self):
        result = comp_cal_counter2('cheesy combo', 'veggie combo')
        self.assertEqual(result, 1770, f"Expected 1770, got {result}")

    def test_calaries_combo_complex_name_unknown(self):
        result = comp_cal_counter2('cheesy combo', 'veggie combo', 'Unknown')
        self.assertEqual(result, 1770, f"Expected 1770, got {result}")

    def test_calaries_complex_mix_id(self):
        result = comp_cal_counter2('meal-1', 'combo-2')
        self.assertEqual(result, 1300, f"Expected 1300, got {result}")

    def test_calaries_complex_mix_id_unknown(self):
        result = comp_cal_counter2('meal-1', 'combo-2', 'Unknown')
        self.assertEqual(result, 1300, f"Expected 1300, got {result}")

    def test_calaries_complex_mix_name(self):
        result = comp_cal_counter2('hamburger', 'veggie combo')
        self.assertEqual(result, 1300, f"Expected 1300, got {result}")

    def test_calaries_complex_mix_name_unknown(self):
        result = comp_cal_counter2('hamburger', 'veggie combo', 'Unknown')
        self.assertEqual(result, 1300, f"Expected 1300, got {result}")

    def test_price_complex_id(self):
        result = price_counter('meal-1', 'meal-2', 'meal-3')
        self.assertEqual(result, 18, f"Expected 18, got {result}")

    def test_price_complex_id_unknown(self):
        result = price_counter('meal-1', 'meal-2', 'meal-3', 'Unknown')
        self.assertEqual(result, 18, f"Expected 18, got {result}")

    def test_price_complex_name(self):
        result = price_counter('hamburger','salad','iced tea')
        self.assertEqual(result, 11, f"Expected 11, got {result}")

    def test_price_complex_name_unknown(self):
        result = price_counter('hamburger','salad','iced tea', 'Unknown')
        self.assertEqual(result, 11, f"Expected 11, got {result}")
