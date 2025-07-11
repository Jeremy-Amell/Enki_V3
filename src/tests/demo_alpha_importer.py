#!/usr/bin/env python3
"""
Quick demo of AlphaImporter interactive mode.
"""

import sys
from pathlib import Path

# Add src directory to path
current_dir = Path(__file__).parent.parent
src_dir = current_dir
sys.path.insert(0, str(src_dir))

from alpha_importer import AlphaImporter

def quick_demo():
    print("🎯 Quick Demo: Loading a harmonic transformation file")
    print("="*55)
    
    importer = AlphaImporter()
    
    # Find a harmonic file for demo
    files = importer.list_available_files()
    harmonic_file = None
    
    for file in files:
        if "harmonic" in file:
            harmonic_file = file
            break
    
    if harmonic_file:
        print(f"📂 Loading harmonic transformation: {harmonic_file}")
        if importer.load_file(harmonic_file):
            importer.display_transformed_dataframe()
            print("\n" + "="*60)
            print("🎵 This data is ready for musical encoding!")
            print("   Next step: Map these integer arrays to musical parameters")
        else:
            print("❌ Failed to load file")
    else:
        print("❌ No harmonic transformation files found")

if __name__ == "__main__":
    quick_demo()
