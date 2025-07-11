#!/usr/bin/env python3
"""
Example usage of the refactored Enki system.
This demonstrates the separation of data generation and transformation.
"""

from enki_class_v2 import Enki_V3
from alpha_transformer import AlphaTransformer


def main():
    """Example of how to use the refactored system."""
    
    # Step 1: Generate alpha data using Enki_V3
    print("="*60)
    print("ENKI V3 - DATA GENERATION")
    print("="*60)
    
    enki = Enki_V3()
    alpha_data = enki.run_pipeline()
    
    if alpha_data is None:
        print("Data generation was cancelled or failed.")
        return
    
    # Step 2: Transform the data using AlphaTransformer
    print("\n" + "="*60)
    print("ALPHA TRANSFORMATION")
    print("="*60)
    
    # Create transformer with default mod table
    transformer = AlphaTransformer(mod_table_version="default")
    
    # Transform the alpha data
    transformed_data = transformer.transform_alpha_dataframe(
        alpha_data['alpha_phorms_dataframe']
    )
    
    # Export the transformed data
    output_file = transformer.export_transformed_data(
        N=alpha_data['N'],
        phi_=alpha_data['phi_'],
        filename_suffix="_refactored"
    )
    
    print(f"\nProcess complete! Output saved to: {output_file}")
    
    # Future: You could easily add different transformation types
    # transformer.apply_music_theory_transform(transformed_data, "harmonic")
    # transformer.apply_decision_tree_transform(transformed_data, decision_rules)


def demonstrate_flexibility():
    """Demonstrates the flexibility of the new architecture."""
    
    # You can now easily test different transformation approaches
    enki = Enki_V3()
    
    # For testing, you could skip the UI and set values directly
    enki.N = 8
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
    
    # Now test different transformation approaches
    transformer1 = AlphaTransformer(mod_table_version="default")
    transformer2 = AlphaTransformer(mod_table_version="alternative")  # If you have one
    
    result1 = transformer1.transform_alpha_dataframe(enki.alpha_phorms_dataframe)
    # result2 = transformer2.transform_alpha_dataframe(enki.alpha_phorms_dataframe)
    
    print("Flexible transformation testing complete!")


if __name__ == "__main__":
    main()
    # demonstrate_flexibility()
