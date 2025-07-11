#!/usr/bin/env python3
"""
Test script to demonstrate the new encoding option in AlphaImporter.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from alpha_importer import AlphaImporter

def test_encoding_option():
    """
    Demonstrate the encoding option functionality.
    """
    print("🧪 Testing AlphaImporter Encoding Option")
    print("="*50)
    
    # Initialize importer
    importer = AlphaImporter()
    
    # Load a specific file directly
    filename = "alpha_transphormed_N7_phi_5_8_9_0_9_5_5_harmonic.pkl"
    print(f"📂 Loading test file: {filename}")
    
    if importer.load_file(filename):
        print("\n🎵 Testing encoding functionality...")
        importer.encode_to_musicxml()
    else:
        print("❌ Could not load test file.")
        print("   Make sure the data directory contains alpha output files.")

if __name__ == "__main__":
    test_encoding_option()
