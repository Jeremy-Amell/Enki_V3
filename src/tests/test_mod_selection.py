#!/usr/bin/env python3
"""
Quick test script to demonstrate the mod table selection feature
without running the full pipeline.
"""

import sys
from pathlib import Path

# Add the src directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Import the mod table selection function
from enki_pipeline import choose_mod_table

if __name__ == "__main__":
    print("🧪 Testing Mod Table Selection Feature")
    print("This will show you the interactive mod table selection.")
    print("Press Ctrl+C to cancel at any time.\n")
    
    selected = choose_mod_table()
    
    if selected:
        print(f"\n✅ You selected: {selected.upper()}")
        print("This selection would be used in the full pipeline.")
    else:
        print("\n❌ No mod table was selected.")
