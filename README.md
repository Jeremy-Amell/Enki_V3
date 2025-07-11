# Enki V3 Pipeline

A modular data generation and transformation pipeline designed for advanced mathematical computations and music theory applications.

## 🏗️ Architecture

The system is built with a clean separation of concerns:

- **Data Generation** (`enki_class_v2.py`) - Handles steps 1-20 of the Enki pipeline
- **Data Transformation** (`alpha_transformer.py`) - Handles all transformations and is extensible for music theory and decision trees
- **Pipeline Runner** (`enki_pipeline.py`) - Complete executable script with multiple run modes

## 🚀 Quick Start

### Interactive Pipeline (Recommended):
```powershell
# Navigate to the source directory
cd f:\Enki_V3\src

# Run the full interactive pipeline
python enki_pipeline.py         # Prompts for N value and mod table selection

# Other modes
python enki_pipeline.py test    # Quick automated test
python enki_pipeline.py demo    # Demonstrate flexibility
python enki_pipeline.py help    # Show help
```

### Features:
- **Interactive Data Generation**: User selects N value for the mathematical pipeline
- **Musical Parameter Generation**: 
  - `Chi`: Note durations/types (quarter, whole, eighth notes, etc.)
  - `Theta`: Note pitches (A, B, C, C#, D, etc.)
  - `Lambda`: Octave selection (register/pitch height)
  - `Epsilon`: Musical modifiers (ties, slurs, dynamics, articulations)
- **Musically-Aware Transformations**: Choose between transformation approaches:
  - `default`: Standard mathematical transformations
  - `increment`: Incremental mathematical transformations  
  - `custom`: Custom mathematical transformations
  - `chromatic`: Chromatic pitch mapping (12-tone scale) - General Theta focus
  - `rhythmic`: Chi-focused (note durations, tempo, subdivisions)
  - `harmonic`: Theta-focused (chord building, harmonic relationships)
  - `modal`: Theta variations (major, minor, modal scales)
  - `octave`: Lambda-focused (register shifts, octave transpositions)
- **Multiple Run Modes**: Interactive, test, demo, and help modes

### From Any Directory:
```powershell
# Run from anywhere
python f:\Enki_V3\src\enki_pipeline.py
python f:\Enki_V3\src\enki_pipeline.py test
```

## 📁 Project Structure

```
Enki_V3/
├── README.md                 # This file
├── src/
│   ├── enki_class_v2.py      # Core data generation (Steps 1-20)
│   ├── alpha_transformer.py  # Transformation engine
│   ├── enki_pipeline.py      # Main executable script
│   ├── phorms_mod_table.py   # Mod table functions
│   └── [other modules...]
├── data/
│   └── alpha_output/         # Generated output files
└── [other directories...]
```

## 🔧 Dependencies

- **Python 3.6+**
- **pandas** - Data manipulation
- **numpy** - Numerical computations
- **IPython** - Interactive features (optional)

## 📖 Usage Examples

### Basic Usage
```python
from enki_class_v2 import Enki_V3
from alpha_transformer import AlphaTransformer

# Generate data
enki = Enki_V3()
alpha_data = enki.run_pipeline()

# Transform data
transformer = AlphaTransformer()
transformed_data = transformer.transform_alpha_dataframe(alpha_data['alpha_phorms_dataframe'])
transformer.export_transformed_data(alpha_data['N'], alpha_data['phi_'])
```

### Programmatic Usage (No UI)
```python
# Set up for automated processing
enki = Enki_V3()
enki.N = 8  # Set N directly

# Run all generation steps
enki.create_base()
# ... (all other steps)
enki.create_alpha_phorms_dataframe()

# Transform the results
transformer = AlphaTransformer(mod_table_version="default")
result = transformer.transform_alpha_dataframe(enki.alpha_phorms_dataframe)
```

## 🎯 Future Expansion

The `AlphaTransformer` class is designed for easy extension:

```python
# Music theory transformations (planned)
transformer.apply_music_theory_transform(data, "harmonic")

# Decision tree transformations (planned)
transformer.apply_decision_tree_transform(data, decision_rules)
```

## 🛠️ Development

### Running Tests
```bash
python enki_pipeline.py test
```

### Architecture Benefits
- **Modular**: Clear separation between generation and transformation
- **Extensible**: Easy to add new transformation methods
- **Testable**: Components can be tested independently
- **Maintainable**: Changes to music theory only affect transformer class

## 📄 License

See LICENSE file for details.
