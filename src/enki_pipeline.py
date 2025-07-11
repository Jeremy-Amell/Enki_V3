#!/usr/bin/env python3
r"""
Enki V3 Pipeline Script
This script provides a complete pipeline for Enki data generation and transformation.
Demonstrates the separation of data generation and transformation using the refactored architecture.

Features:
- Interactive data generation with user input for N value
- Musical parameter generation: Chi (durations), Theta (pitches), Lambda (octaves), Epsilon (modifiers)
- Mod table selection with musically-aware transformations
- Multiple run modes for different use cases
- Clean separation between data generation and transformation

To run this script:
1. Navigate to the src directory: cd f:\Enki_V3\src
2. Run: python enki_pipeline.py

OR to run from anywhere:
python f:\Enki_V3\src\enki_pipeline.py

Available modes:
- python enki_pipeline.py        # Full interactive pipeline
- python enki_pipeline.py test   # Quick automated test
- python enki_pipeline.py demo   # Demonstrate flexibility
- python enki_pipeline.py help   # Show help
"""

# Standard library imports
import sys
import os
from pathlib import Path

# Add the src directory to Python path so we can import our modules
# This ensures the script can find enki_class_v2 and alpha_transformer
current_dir = Path(__file__).parent
src_dir = current_dir
sys.path.insert(0, str(src_dir))

# Now import our custom modules
from enki_class_v2 import Enki_V3
from alpha_transformer import AlphaTransformer

# Optional: Import these if you want to work with the data directly
import pandas as pd
import numpy as np


def choose_mod_table():
    """
    Interactive function to let users choose their preferred mod table version.
    
    Returns:
        str: The selected mod table version
    """
    print("\n" + "="*60)
    print("SELECT MOD TABLE VERSION")
    print("="*60)
    
    mod_table_options = {
        "1": {
            "name": "default",
            "description": "Standard transformations (subtract 1, add 1, add 2, add 3)"
        },
        "2": {
            "name": "increment", 
            "description": "Incremental transformations (add 0, add 2, add 4, add 6)"
        },
        "3": {
            "name": "custom",
            "description": "Custom transformations (multiply by 2, square, subtract 3, add 5)"
        },
        "4": {
            "name": "chromatic",
            "description": "Chromatic transformations (12-tone pitch mapping) - General Theta focus"
        },
        "5": {
            "name": "rhythmic",
            "description": "Rhythmic transformations (note durations, tempo shifts, subdivisions) - Chi focus"
        },
        "6": {
            "name": "harmonic",
            "description": "Harmonic transformations (chord building, root/3rd/5th/7th) - Theta focus"
        },
        "7": {
            "name": "modal",
            "description": "Modal transformations (major, minor, phrygian scales) - Theta variations"
        },
        "8": {
            "name": "octave",
            "description": "Octave transformations (register shifts, inversions) - Lambda focus"
        }
    }
    
    print("Available mod table versions:")
    for key, info in mod_table_options.items():
        print(f"   {key}. {info['name'].upper()}")
        print(f"      └─ {info['description']}")
    
    while True:
        try:
            print(f"\nPlease choose a mod table version (1-{len(mod_table_options)}):", end=" ")
            choice = input().strip()
            
            if choice in mod_table_options:
                selected = mod_table_options[choice]
                print(f"✅ Selected: {selected['name'].upper()}")
                print(f"   Description: {selected['description']}")
                
                # Confirm choice
                confirm = input(f"\nConfirm selection of '{selected['name']}' mod table? (y/n): ").strip().lower()
                if confirm in ['y', 'yes', '']:
                    return selected['name']
                else:
                    print("Selection cancelled. Please choose again.")
                    continue
            else:
                print(f"❌ Invalid choice '{choice}'. Please enter a number between 1 and {len(mod_table_options)}.")
                
        except KeyboardInterrupt:
            print("\n❌ Selection cancelled by user.")
            return None
        except Exception as e:
            print(f"❌ Error during selection: {e}")
            return None


def main():
    """Example of how to use the refactored system."""
    
    print("Starting Enki V3 Data Generation and Transformation Pipeline...")
    print("Working directory:", os.getcwd())
    print("Script location:", __file__)
    
    try:
        # Step 1: Generate alpha data using Enki_V3
        print("\n" + "="*60)
        print("ENKI V3 - DATA GENERATION")
        print("="*60)
        
        # Initialize the data generator
        enki = Enki_V3()
        
        # Run the complete data generation pipeline
        alpha_data = enki.run_pipeline()
        
        if alpha_data is None:
            print("❌ Data generation was cancelled or failed.")
            return False
        
        print("✅ Data generation completed successfully!")
        print(f"   - N value: {alpha_data['N']}")
        print(f"   - Phi array: {alpha_data['phi_']}")
        print(f"   - Alpha phorms shape: {alpha_data['alpha_phorms_dataframe'].shape}")
        
        # Step 2: Choose mod table version
        selected_mod_table = choose_mod_table()
        if selected_mod_table is None:
            print("❌ Mod table selection was cancelled.")
            return False
        
        # Step 3: Transform the data using AlphaTransformer
        print("\n" + "="*60)
        print("ALPHA TRANSFORMATION")
        print("="*60)
        
        # Create transformer with selected mod table
        transformer = AlphaTransformer(
            mod_table_version=selected_mod_table,
            output_dir="F:/Enki_V3/data/alpha_output"
        )
        
        print("Transformer initialized with:")
        print(f"   - Mod table version: {transformer.mod_table_version}")
        print(f"   - Output directory: {transformer.output_dir}")
        
        # Transform the alpha data
        print("\nStarting transformation process...")
        transformed_data = transformer.transform_alpha_dataframe(
            alpha_data['alpha_phorms_dataframe']
        )
        
        if transformed_data is not None:
            print("✅ Transformation completed successfully!")
            print(f"   - Transformed data shape: {transformed_data.shape}")
            
            # Export the transformed data
            print("\nExporting transformed data...")
            output_file = transformer.export_transformed_data(
                N=alpha_data['N'],
                phi_=alpha_data['phi_']
            )
            
            if output_file:
                print(f"✅ Export completed successfully!")
                print(f"   - File saved to: {output_file}")
                print(f"   - File size: {os.path.getsize(output_file)} bytes")
            else:
                print("❌ Export failed!")
                return False
        else:
            print("❌ Transformation failed!")
            return False
        
        print("\n" + "="*60)
        print("🎉 PIPELINE COMPLETED SUCCESSFULLY! 🎉")
        print("="*60)
        print("\nSummary:")
        print(f"✓ Generated data for N={alpha_data['N']}")
        print(f"✓ Processed {len(alpha_data['alpha_values'])} alpha values")
        print(f"✓ Applied transformations using '{selected_mod_table.upper()}' mod table")
        print(f"✓ Exported results to: {output_file}")
        
        # Future: You could easily add different transformation types
        print("\n🎵 Musical transformations now available!")
        print("   ✓ Rhythmic: Focus on Chi values (note durations, tempo)")
        print("   ✓ Harmonic: Focus on Theta values (pitch relationships, chords)")
        print("   ✓ Modal: Focus on Theta variations (scales, modes)")
        print("   ✓ Octave: Focus on Lambda values (register, transposition)")
        print("\n📋 Future expansion possibilities:")
        print("   - transformer.apply_epsilon_modifiers(transformed_data, 'dynamics_articulations')")
        print("   - transformer.apply_musical_forms(transformed_data, 'sonata_form')")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error occurred during pipeline execution:")
        print(f"   Error type: {type(e).__name__}")
        print(f"   Error message: {str(e)}")
        print(f"   Check that all required files are present:")
        print(f"   - enki_class_v2.py")
        print(f"   - alpha_transformer.py") 
        print(f"   - phorms_mod_table.py")
        return False


def demonstrate_flexibility():
    """Demonstrates the flexibility of the new architecture for testing/development."""
    
    print("\n" + "="*60)
    print("DEMONSTRATING FLEXIBLE ARCHITECTURE")
    print("="*60)
    
    try:
        # You can now easily test different approaches without the UI
        print("Creating Enki instance for programmatic testing...")
        enki = Enki_V3()
        
        # For testing, skip the UI and set values directly
        print("Setting test parameters (N=8)...")
        enki.N = 8
        
        # Run the pipeline steps programmatically
        print("Running data generation steps...")
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
        
        print("✅ Data generation completed programmatically!")
        print(f"   - Generated phi: {enki.phi_}")
        print(f"   - Alpha phorms shape: {enki.alpha_phorms_dataframe.shape}")
        
        # Now test different transformation approaches
        print("\nTesting multiple transformation approaches...")
        
        # Test all available mod tables programmatically
        mod_tables = ["default", "increment", "custom", "chromatic", "rhythmic", "harmonic", "modal", "octave"]
        
        for mod_table in mod_tables:
            print(f"\n   Testing '{mod_table}' mod table...")
            transformer = AlphaTransformer(mod_table_version=mod_table)
            result = transformer.transform_alpha_dataframe(enki.alpha_phorms_dataframe)
            
            if result is not None:
                print(f"   ✅ '{mod_table}' transformation successful! Shape: {result.shape}")
            else:
                print(f"   ❌ '{mod_table}' transformation failed!")
        
        print("✅ Flexible transformation testing complete!")
        return True
        
    except Exception as e:
        print(f"❌ Error in flexibility demonstration: {e}")
        return False


def quick_test_run():
    """Quick test without user interaction - useful for development."""
    
    print("\n" + "="*60)
    print("QUICK TEST RUN (NO USER INPUT)")
    print("="*60)
    
    try:
        # Create and configure Enki for automated testing
        enki = Enki_V3()
        enki.N = 6  # Minimum valid value for quick testing
        
        # Run abbreviated pipeline for testing
        print("Running quick test with N=6...")
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
        
        # Quick transformation test
        transformer = AlphaTransformer()
        result = transformer.transform_alpha_dataframe(enki.alpha_phorms_dataframe)
        
        if result is not None:
            print("✅ Quick test successful!")
            print(f"   - Generated data for N={enki.N}")
            print(f"   - Phi: {enki.phi_}")
            print(f"   - Transformation result shape: {result.shape}")
            return True
        else:
            print("❌ Quick test transformation failed!")
            return False
            
    except Exception as e:
        print(f"❌ Quick test failed: {e}")
        return False


if __name__ == "__main__":
    """
    Main execution block - runs when script is executed directly.
    
    Usage options:
    1. python enki_pipeline.py              # Full interactive pipeline
    2. python enki_pipeline.py test         # Quick automated test
    3. python enki_pipeline.py demo         # Demonstrate flexibility
    """
    
    # Check command line arguments for different run modes
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
        
        if mode == "test":
            print("🚀 Running in QUICK TEST mode...")
            success = quick_test_run()
            
        elif mode == "demo":
            print("🚀 Running in DEMONSTRATION mode...")
            success = demonstrate_flexibility()
            
        elif mode == "help":
            print("📖 ENKI V3 Usage Help:")
            print("   python enki_pipeline.py        # Full interactive pipeline")
            print("   python enki_pipeline.py test   # Quick automated test")
            print("   python enki_pipeline.py demo   # Demonstrate flexibility")
            print("   python enki_pipeline.py help   # Show this help")
            sys.exit(0)
            
        else:
            print(f"❓ Unknown mode: {mode}")
            print("   Use 'help' for usage options")
            sys.exit(1)
    else:
        # Default: run the full interactive pipeline
        print("🚀 Running FULL INTERACTIVE pipeline...")
        success = main()
    
    # Exit with appropriate code
    if success:
        print("\n🎉 All operations completed successfully!")
        sys.exit(0)
    else:
        print("\n❌ Some operations failed!")
        sys.exit(1)
