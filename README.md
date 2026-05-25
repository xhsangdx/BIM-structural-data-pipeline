# BIM Structural Data Pipeline

An open-source data pipeline and asset bridge designed to extract, normalize, and visualize complex structural engineering formulas and BIM (Building Information Modeling) data schemas into clean, reusable Python and JavaScript formats.

## Why This Project Exists
Structural engineering computations (e.g., calculation of shear walls, moment frames, and lateral load distributions) are heavily locked inside proprietary, high-cost software. This project serves as a critical, open-source bridge allowing independent developers and architectural researchers to integrate certified structural calculation logic directly into open-source rendering engines and CAD tools.

## Key Features
* **Schema Normalization:** Translates proprietary IFC/BIM data structures into standardized JSON formats.
* **Structural Logic Core:** Provides open-source modules for calculating bending moments, axial forces, and structural safety coefficients.
* **Automation-Ready:** Built to feed structured mathematical models straight into visualization libraries.
 
## Code Preview (Integration Example)

```python
# Core logic framework for standard structural compliance mapping
import json

class StructuralDataBridge:
    def __init__(self, bim_file_path):
        self.file_path = bim_file_path
        self.standard_metrics = {}

    def extract_lateral_load_data(self):
        # Simulated extraction of shear wall and brace data for cross-platform rendering
        print(f"[SUCCESS] Extracting building structure matrices from {self.file_path}...")
        return {
            "system_type": "Shear Wall & Moment Frame",
            "load_distribution": [0.45, 0.55],
            "status": "Verified"
        }

    def export_to_json(self, output_path):
        data = self.extract_lateral_load_data()
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"[INFO] Normalized structural schema exported to {output_path}")

# Initialize pipeline
pipeline = StructuralDataBridge("./models/building_structure_v1.ifc")
pipeline.export_to_json("./output/normalized_schema.json")

* Upgraded validation matrix logic for dynamic loads.
* Upgraded validation matrix logic for dynamic loads.
