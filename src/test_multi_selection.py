#!/usr/bin/env python3
"""
Test the new multiple mod table selection functionality
"""

import sys
from pathlib import Path

# Add the src directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

from enki_pipeline import choose_mod_table

def test_multi_selection():
    """Test the multiple mod table selection feature."""
    
    print("🧪 Testing Multiple Mod Table Selection")
    print("="*50)
    print("This demonstrates the new multi-selection options:")
    print("• Single: Enter '6' for harmonic only")
    print("• Multiple: Enter '6,7' for harmonic and modal")
    print("• All musical: Enter 'music' for all musical transformations")
    print("• All options: Enter 'all' for every transformation")
    print("\nPress Ctrl+C to cancel at any time.\n")
    
    selected = choose_mod_table()
    
    if selected:
        print(f"\n✅ You selected {len(selected)} transformation(s):")
        for i, mod_table in enumerate(selected, 1):
            print(f"   {i}. {mod_table.upper()}")
        print("\nThese would all be processed in the full pipeline!")
    else:
        print("\n❌ No mod tables were selected.")

if __name__ == "__main__":
    test_multi_selection()
