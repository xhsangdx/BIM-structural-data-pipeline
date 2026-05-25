import unittest
from core.calculator import StructuralCalculator

class TestStructuralCalculator(unittest.TestCase):
    def setUp(self):
        # Initialize calculator with standard concrete (30 MPa) and steel (400 MPa)
        self.calc = StructuralCalculator(concrete_strength=30.0, steel_yield_strength=400.0)

    def test_shear_wall_stiffness_valid(self):
        # Test baseline stiffness for standard wall dimensions (t=0.3m, L=4.0m, H=3.5m)
        stiffness = self.calc.calculate_shear_wall_stiffness(thickness=0.3, length=4.0, height=3.5)
        self.assertGreater(stiffness, 0)

    def test_lateral_drift_ratio_safe(self):
        # Test within safe limits (0.012 drift ratio)
        result = self.calc.verify_lateral_drift_ratio(max_displacement=0.042, story_height=3.5)
        self.assertEqual(result["status"], "PASS")

    def test_lateral_drift_ratio_fail(self):
        # Test exceeding safe limits (0.025 drift ratio)
        result = self.calc.verify_lateral_drift_ratio(max_displacement=0.087, story_height=3.5)
        self.assertEqual(result["status"], "FAIL")

if __name__ == '__main__':
    unittest.main()
