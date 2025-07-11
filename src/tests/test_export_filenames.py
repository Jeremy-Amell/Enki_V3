#!/usr/bin/env python3
"""
Quick test to demonstrate the new filename format with mod table suffix
"""

import sys
from pathlib import Path

# Add the src directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

from enki_class_v2 import Enki_V3
from alpha_transformer import AlphaTransformer

def test_export_with_mod_table_suffix():
    """Test the new export functionality with mod table suffix in filename."""
    
    print("🧪 Testing Export with Mod Table Suffix")
    print("="*50)
    
    # Create test data
    enki = Enki_V3()
    enki.N = 6  # Simple test case
    
    # Run pipeline steps
    print("Generating test data...")
    enki.create_base()
    enki.root_arrays()
    enki.create_kappa_root_arrays()
    enki.create_data_triangle_roots()
    enki.update_theta_root()
    enki.update_lambda_root()
    enki.update_epsilon_root()
    enki.update_kappa_roots()
    enki.combine_all_values_DT()
    enki.create_pva_array()
    enki.create_DT_dataframe()
    enki.create_PVA_Mods()
    enki.create_PVA_Mods_dataframe()
    enki.create_alpha_roots_rows()
    enki.create_alpha_roots_post_pivot()
    enki.combine_alpha_roots()
    enki.create_alpha_roots_dataframe()
    enki.create_alpha()
    enki.create_alpha_phorms_dataframe()
    
    print(f"Generated phi: {enki.phi_}")
    
    # Test different mod tables
    mod_tables_to_test = ["harmonic", "modal", "rhythmic", "octave"]
    
    for mod_table in mod_tables_to_test:
        print(f"\n📋 Testing {mod_table} transformation...")
        
        # Create transformer
        transformer = AlphaTransformer(
            mod_table_version=mod_table,
            output_dir="F:/Enki_V3/data/alpha_output"
        )
        
        # Transform data
        result = transformer.transform_alpha_dataframe(enki.alpha_phorms_dataframe)
        
        if result is not None:
            # Export with new filename format
            output_file = transformer.export_transformed_data(
                N=enki.N,
                phi_=enki.phi_
            )
            
            if output_file:
                print(f"✅ {mod_table}: {output_file.split('/')[-1]}")
            else:
                print(f"❌ {mod_table}: Export failed")
        else:
            print(f"❌ {mod_table}: Transformation failed")
    
    print("\n🎉 Export testing completed!")

if __name__ == "__main__":
    test_export_with_mod_table_suffix()
