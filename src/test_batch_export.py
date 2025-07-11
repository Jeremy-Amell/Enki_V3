#!/usr/bin/env python3
"""
Comprehensive test of the new multiple transformation feature
This creates a full batch export demonstration
"""

import sys
from pathlib import Path

# Add the src directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

from enki_class_v2 import Enki_V3
from alpha_transformer import AlphaTransformer

def test_batch_transformations():
    """Test multiple transformations with automatic export."""
    
    print("🎯 Testing Batch Transformations")
    print("="*50)
    
    # Create test data
    enki = Enki_V3()
    enki.N = 7  # Medium complexity
    
    # Run pipeline steps
    print("Generating source data...")
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
    
    print(f"Generated source data: N={enki.N}, phi={enki.phi_}")
    
    # Test multiple transformations
    selected_mod_tables = ["harmonic", "modal", "rhythmic", "octave"]  # Musical transformations
    
    print(f"\n🎵 Processing {len(selected_mod_tables)} musical transformations...")
    print("-" * 50)
    
    successful_exports = []
    
    for i, mod_table_name in enumerate(selected_mod_tables, 1):
        print(f"\n🔄 Processing {i}/{len(selected_mod_tables)}: {mod_table_name.upper()}")
        
        # Create transformer
        transformer = AlphaTransformer(
            mod_table_version=mod_table_name,
            output_dir="F:/Enki_V3/data/alpha_output"
        )
        
        # Transform data
        result = transformer.transform_alpha_dataframe(enki.alpha_phorms_dataframe)
        
        if result is not None:
            print(f"   ✅ Transformation completed! Shape: {result.shape}")
            
            # Export
            output_file = transformer.export_transformed_data(
                N=enki.N,
                phi_=enki.phi_
            )
            
            if output_file:
                filename = output_file.split('/')[-1]
                print(f"   ✅ Export successful: {filename}")
                successful_exports.append((mod_table_name, filename))
            else:
                print(f"   ❌ Export failed!")
        else:
            print(f"   ❌ Transformation failed!")
    
    print(f"\n🎉 Batch Processing Complete!")
    print("="*50)
    print(f"✅ Successfully created {len(successful_exports)} files:")
    for mod_table_name, filename in successful_exports:
        print(f"   ✓ {mod_table_name.upper()}: {filename}")
    
    print(f"\n📁 All files saved to: F:/Enki_V3/data/alpha_output/")
    print("🎵 Each file contains the same source data transformed using different musical approaches!")

if __name__ == "__main__":
    test_batch_transformations()
