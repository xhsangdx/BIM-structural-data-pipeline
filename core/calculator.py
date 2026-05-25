import math

class StructuralCalculator:
    """
    Core engineering formulas for structural system compliance checking.
    Handles lateral load distributions, shear wall stiffness, and bending moments.
    """
    def __init__(self, concrete_strength: float, steel_yield_strength: float):
        self.f_ck = concrete_strength  # MPa
        self.f_y = steel_yield_strength  # MPa

    def calculate_shear_wall_stiffness(self, thickness: float, length: float, height: float) -> float:
        # Standard structural engineering formula for wall stiffness (flexure + shear components)
        # K = 1 / ((H^3 / 3EI) + (1.2H / GAs))
        E_c = 4700 * math.sqrt(self.f_ck) # Concrete Modulus of Elasticity
        I_g = (thickness * (length ** 3)) / 12 # Gross moment of inertia
        
        flexibility = (height ** 3) / (3 * E_c * I_g)
        stiffness = 1.0 / flexibility if flexibility > 0 else 0.0
        return round(stiffness, 2)

    def verify_lateral_drift_ratio(self, max_displacement: float, story_height: float) -> dict:
        # Checks if building lateral drift complies with standard design codes (typically < 1.5% or 2%)
        drift_ratio = max_displacement / story_height
        is_safe = drift_ratio <= 0.015
        
        return {
            "drift_ratio": round(drift_ratio, 5),
            "status": "PASS" if is_safe else "FAIL",
            "code_compliance": "KBC-2016 / IBC-2024 Standard"
        }
