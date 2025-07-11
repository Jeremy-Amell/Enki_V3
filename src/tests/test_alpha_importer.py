#!/usr/bin/env python3
"""
Test script for AlphaImporter - demonstrates functionality by automatically selecting and displaying a file.
"""

import sys
from pathlib import Path

# Add src directory to path
current_dir = Path(__file__).parent
src_dir = current_dir
sys.path.insert(0, str(src_dir))

from alpha_importer import AlphaImporter

def test_alpha_importer():
    """Test the AlphaImporter with automatic file selection."""
    
    print("🧪 Testing AlphaImporter functionality...")
    print("="*50)
    
    # Create importer instance
    importer = AlphaImporter()
    
    # Get available files
    files = importer.list_available_files()
    
    if not files:
        print("❌ No files available for testing.")
        return False
    
    # Display available files
    importer.display_available_files()
    
    # Automatically select the first file for testing
    test_file = files[0]
    print(f"\n🔄 Automatically selecting first file for testing: {test_file}")
    
    # Load the file
    if not importer.load_file(test_file):
        print("❌ Failed to load test file.")
        return False
    
    # Display the transformed dataframe
    print("\n" + "="*60)
    print("TESTING: Display Transformed Dataframe")
    print("="*60)
    importer.display_transformed_dataframe()
    
    # Display metadata
    print("\n" + "="*60)
    print("TESTING: Display Metadata")
    print("="*60)
    importer.display_metadata()
    
    # Test getter methods
    print("\n" + "="*60)
    print("TESTING: Getter Methods")
    print("="*60)
    
    df = importer.get_dataframe()
    if df is not None:
        print(f"✅ get_dataframe() successful - Shape: {df.shape}")
    else:
        print("❌ get_dataframe() returned None")
    
    metadata = importer.get_metadata()
    print(f"✅ get_metadata() successful - Keys: {list(metadata.keys())}")
    
    print("\n🎉 AlphaImporter test completed successfully!")
    return True

if __name__ == "__main__":
    test_alpha_importer()
