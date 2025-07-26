#!/usr/bin/env python3
"""
Alpha Importer Class
This class handles importing and displaying previously exported alpha data.
Allows users to select from available pickle files and view the transformed data.

Part of the Enki V3 pipeline for data encoding and analysis.
"""

import pandas as pd
import numpy as np
import pickle
import os
from pathlib import Path
from typing import Optional, Dict, List, Any


class AlphaImporter:
    """
    Handles importing and displaying previously exported alpha transformation data.
    
    This class allows users to:
    1. Browse available alpha output files
    2. Select and load a specific transformation
    3. Display the transformed alpha dataframe
    4. Access the data for further encoding operations
    """
    
    def __init__(self, input_dir: str = "F:/Enki_V3/data/alpha_output"):
        """
        Initialize the AlphaImporter.
        
        Args:
            input_dir (str): Directory containing alpha output pickle files
        """
        self.input_dir = Path(input_dir)
        self.loaded_data = None
        self.current_file = None
        
        # Ensure the input directory exists
        if not self.input_dir.exists():
            print(f"⚠️ Warning: Input directory does not exist: {self.input_dir}")
            print(f"   Please check the path or run the pipeline to generate data first.")
    
    def list_available_files(self) -> List[str]:
        """
        List all available alpha output pickle files.
        
        Returns:
            List[str]: List of available pickle file names
        """
        if not self.input_dir.exists():
            return []
        
        pickle_files = list(self.input_dir.glob("*.pkl"))
        return [f.name for f in pickle_files]
    
    def display_available_files(self) -> None:
        """
        Display available files with details for user selection.
        """
        files = self.list_available_files()
        
        if not files:
            print("❌ No alpha output files found!")
            print(f"   Directory: {self.input_dir}")
            print(f"   Make sure you've run the pipeline and generated some data first.")
            return
        
        # Find the most recently created file
        most_recent_file = None
        most_recent_time = 0
        
        for filename in files:
            file_path = self.input_dir / filename
            creation_time = file_path.stat().st_mtime
            if creation_time > most_recent_time:
                most_recent_time = creation_time
                most_recent_file = filename
        
        print(f"\n{'='*60}")
        print("AVAILABLE ALPHA OUTPUT FILES")
        print(f"{'='*60}")
        print(f"Directory: {self.input_dir}")
        print(f"Found {len(files)} file(s):")
        
        for i, filename in enumerate(files, 1):
            file_path = self.input_dir / filename
            file_size = file_path.stat().st_size
            
            # Check if this is the most recent file
            is_most_recent = (filename == most_recent_file)
            recent_marker = " 🆕 [MOST RECENT]" if is_most_recent else ""
            
            # Parse filename to extract info
            if "_transphormed_" in filename:
                parts = filename.split("_transphormed_")
                if len(parts) == 2:
                    prefix = parts[0]
                    suffix_part = parts[1].replace(".pkl", "")
                    
                    # Extract mod table type from suffix
                    if "_" in suffix_part:
                        suffix_parts = suffix_part.split("_")
                        mod_table = suffix_parts[-1]  # Last part should be mod table name
                        n_and_phi = "_".join(suffix_parts[:-1])  # Everything before mod table
                    else:
                        mod_table = "unknown"
                        n_and_phi = suffix_part
                    
                    print(f"   {i}. {filename}{recent_marker}")
                    print(f"      └─ Mod Table: {mod_table.upper()}")
                    print(f"      └─ Parameters: {n_and_phi}")
                    print(f"      └─ Size: {file_size:,} bytes")
                else:
                    print(f"   {i}. {filename}{recent_marker}")
                    print(f"      └─ Size: {file_size:,} bytes")
            else:
                print(f"   {i}. {filename}{recent_marker}")
                print(f"      └─ Size: {file_size:,} bytes")
        
        # Add a helpful note about the most recent file
        if most_recent_file:
            most_recent_index = files.index(most_recent_file) + 1
            print(f"\n💡 NOTIFICATION: File #{most_recent_index} is the most recently created file")
        
        print()
    
    def select_file_interactive(self) -> Optional[str]:
        """
        Allow user to interactively select a file to load.
        
        Returns:
            Optional[str]: Selected filename, or None if cancelled
        """
        files = self.list_available_files()
        
        if not files:
            print("❌ No files available to select.")
            return None
        
        self.display_available_files()
        
        while True:
            try:
                print(f"Please select a file (1-{len(files)}) or 'q' to quit:", end=" ")
                choice = input().strip().lower()
                
                if choice == 'q':
                    print("Selection cancelled.")
                    return None
                
                try:
                    file_index = int(choice) - 1
                    if 0 <= file_index < len(files):
                        selected_file = files[file_index]
                        print(f"✅ Selected: {selected_file}")
                        return selected_file
                    else:
                        print(f"❌ Invalid selection. Please enter a number between 1 and {len(files)}.")
                except ValueError:
                    print(f"❌ Invalid input. Please enter a number between 1 and {len(files)}.")
                    
            except KeyboardInterrupt:
                print("\n❌ Selection cancelled by user.")
                return None
            except Exception as e:
                print(f"❌ Error during selection: {e}")
                return None
    
    def load_file(self, filename: str) -> bool:
        """
        Load a specific alpha output file.
        
        Args:
            filename (str): Name of the file to load
            
        Returns:
            bool: True if loaded successfully, False otherwise
        """
        file_path = self.input_dir / filename
        
        if not file_path.exists():
            print(f"❌ File not found: {filename}")
            return False
        
        try:
            print(f"📂 Loading file: {filename}")
            
            with open(file_path, 'rb') as f:
                self.loaded_data = pickle.load(f)
            
            self.current_file = filename
            print(f"✅ Successfully loaded: {filename}")
            
            # Display basic info about the loaded data
            if isinstance(self.loaded_data, dict):
                print(f"   - Data type: Dictionary with {len(self.loaded_data)} keys")
                print(f"   - Keys: {list(self.loaded_data.keys())}")
            else:
                print(f"   - Data type: {type(self.loaded_data).__name__}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error loading file: {e}")
            self.loaded_data = None
            self.current_file = None
            return False
    
    def display_transformed_dataframe(self) -> None:
        """
        Display the transformed alpha dataframe from the loaded data.
        """
        if self.loaded_data is None:
            print("❌ No data loaded. Please load a file first.")
            return
        
        print(f"\n{'='*60}")
        print("TRANSFORMED ALPHA DATAFRAME")
        print(f"{'='*60}")
        print(f"Source file: {self.current_file}")
        
        # Extract and display mod table from filename
        mod_table = "unknown"
        if self.current_file and "_transphormed_" in self.current_file:
            parts = self.current_file.split("_transphormed_")
            if len(parts) == 2:
                suffix_part = parts[1].replace(".pkl", "")
                if "_" in suffix_part:
                    suffix_parts = suffix_part.split("_")
                    mod_table = suffix_parts[-1]  # Last part should be mod table name
        
        print(f"📋 Mod Table: {mod_table.upper()}")
        
        df = None
        
        # Handle different data formats
        if isinstance(self.loaded_data, dict):
            if 'transformed_alpha_dataframe' in self.loaded_data:
                df = self.loaded_data['transformed_alpha_dataframe']
                print(f"✅ Found transformed alpha dataframe in dictionary!")
            else:
                print("❌ No 'transformed_alpha_dataframe' found in loaded data.")
                print(f"   Available keys: {list(self.loaded_data.keys())}")
                return
        elif isinstance(self.loaded_data, pd.DataFrame):
            df = self.loaded_data
            print(f"✅ Loaded data is directly a DataFrame!")
        else:
            print(f"❌ Unsupported data format. Type: {type(self.loaded_data)}")
            print(f"   Data preview: {str(self.loaded_data)[:200]}...")
            return
        
        # Display dataframe information
        print(f"   - Columns: {list(df.columns)}")
        
        # More detailed data type analysis
        print(f"   - Data types:")
        for col in df.columns:
            dtype = df.dtypes[col]
            if dtype == 'object':
                # For object columns, check what's actually inside
                sample_value = df[col].iloc[0]
                if isinstance(sample_value, list):
                    if len(sample_value) > 0 and isinstance(sample_value[0], list):
                        print(f"     {col}: List of arrays (pandas object dtype)")
                    else:
                        print(f"     {col}: List (pandas object dtype)")
                else:
                    print(f"     {col}: {type(sample_value).__name__} (pandas object dtype)")
            else:
                print(f"     {col}: {dtype}")
        
        print(f"\n📊 Dataframe Contents:")
        print("-" * 40)
        print(df)
        
        # Show all values of the Alpha_Phormed column if it exists
        if 'Alpha_Phormed' in df.columns:
            print(f"\n🔍 Sample Alpha_Phormed Values (All Rows):")
            print("-" * 50)
            
            # Define position names and track total array count
            total_rows = len(df)
            total_array_count = 0
            
            for i, (idx, row) in enumerate(df.iterrows()):
                alpha_value = row['Alpha_Phormed']
                
                # Determine position label
                if total_rows == 1:
                    position = "ONLY"
                elif i == 0:
                    position = "FIRST"
                elif i == total_rows - 1:
                    position = "LAST"
                else:
                    # Use ordinal numbers for middle positions
                    ordinal_map = {
                        1: "SECOND", 2: "THIRD", 3: "FOURTH", 4: "FIFTH",
                        5: "SIXTH", 6: "SEVENTH", 7: "EIGHTH", 8: "NINTH", 9: "TENTH"
                    }
                    position = ordinal_map.get(i, f"{i+1}TH")
                
                print(f"   {position}: {idx}")
                if isinstance(alpha_value, list) and len(alpha_value) > 0:
                    array_count = len(alpha_value)
                    print(f"          └─ Array count: {array_count}")
                    total_array_count += array_count
                else:
                    print(f"          └─ Data type: {type(alpha_value)}")
                
                # Add spacing between entries (except after the last one)
                if i < total_rows - 1:
                    print()
            
            # Show total aggregation
            print()
            print("=" * 50)
            print(f"📊 TOTAL ARRAY COUNT: {total_array_count:,}")
            print("=" * 50)
        
        print(f"\n💡 This is the transformed alpha data ready for encoding!")
    
    def get_dataframe(self) -> Optional[pd.DataFrame]:
        """
        Get the transformed alpha dataframe for further processing.
        
        Returns:
            Optional[pd.DataFrame]: The dataframe if available, None otherwise
        """
        if self.loaded_data is None:
            return None
        
        # Handle different data formats
        if isinstance(self.loaded_data, dict) and 'transformed_alpha_dataframe' in self.loaded_data:
            return self.loaded_data['transformed_alpha_dataframe']
        elif isinstance(self.loaded_data, pd.DataFrame):
            return self.loaded_data
        
        return None
    
    def get_metadata(self) -> Dict[str, Any]:
        """
        Get metadata about the loaded transformation.
        
        Returns:
            Dict[str, Any]: Metadata including N, phi, mod_table_version, etc.
        """
        if self.loaded_data is None:
            return {}
        
        if isinstance(self.loaded_data, dict):
            return {key: value for key, value in self.loaded_data.items() 
                   if key != 'transformed_alpha_dataframe'}
        
        return {}
    
    def display_metadata(self) -> None:
        """
        Display metadata about the loaded transformation.
        """
        if self.loaded_data is None:
            print("❌ No data loaded. Please load a file first.")
            return
        
        metadata = self.get_metadata()
        
        print(f"\n{'='*60}")
        print("TRANSFORMATION METADATA")
        print(f"{'='*60}")
        print(f"Source file: {self.current_file}")
        
        if not metadata:
            print("❌ No metadata available in this file format.")
            print("   Note: This appears to be a dataframe-only export.")
            
            # Try to extract info from filename
            if self.current_file:
                print(f"\n📋 Information from filename:")
                if "_transphormed_" in self.current_file:
                    parts = self.current_file.replace(".pkl", "").split("_")
                    for part in parts:
                        if part.startswith("N"):
                            print(f"   - N value: {part[1:]}")
                        elif part == "phi":
                            # Find phi values (numbers after "phi" until next named part)
                            phi_idx = parts.index("phi")
                            phi_values = []
                            for i in range(phi_idx + 1, len(parts)):
                                if parts[i].isdigit():
                                    phi_values.append(parts[i])
                                else:
                                    break
                            if phi_values:
                                print(f"   - Phi values: {phi_values}")
            return
        
        print("✅ Found metadata:")
        for key, value in metadata.items():
            if isinstance(value, np.ndarray):
                print(f"   {key}: {value} (shape: {value.shape})")
            else:
                print(f"   {key}: {value}")
    
    def encode_to_musicxml(self) -> None:
        """
        Encode the loaded alpha data to MusicXML format.
        This is a placeholder method for the encoding pipeline.
        """
        if self.loaded_data is None:
            print("❌ No data loaded. Please load a file first.")
            return
        
        df = self.get_dataframe()
        if df is None:
            print("❌ Could not retrieve dataframe for encoding.")
            return
        
        print(f"\n{'='*60}")
        print("🎵 ENCODING TO MUSICXML")
        print(f"{'='*60}")
        print(f"Source file: {self.current_file}")
        
        # Extract and display mod table from filename  
        mod_table = "unknown"
        if self.current_file and "_transphormed_" in self.current_file:
            parts = self.current_file.split("_transphormed_")
            if len(parts) == 2:
                suffix_part = parts[1].replace(".pkl", "")
                if "_" in suffix_part:
                    suffix_parts = suffix_part.split("_")
                    mod_table = suffix_parts[-1]  # Last part should be mod table name
        
        print(f"📋 Mod Table: {mod_table.upper()}")
        
        # Calculate total arrays for encoding
        total_arrays = 0
        if 'Alpha_Phormed' in df.columns:
            for _, row in df.iterrows():
                alpha_value = row['Alpha_Phormed']
                if isinstance(alpha_value, list):
                    total_arrays += len(alpha_value)
        
        print(f"Total arrays to encode: {total_arrays:,}")
        print()
        print("🚧 ENCODING PIPELINE STATUS:")
        print("   ✅ Alpha data loaded and ready")
        print("   🔄 Moving to encoding stage...")
        print("   ⏳ Encoding mapper class: [TO BE IMPLEMENTED]")
        print("   ⏳ Integer-to-musical parameter mapping: [TO BE IMPLEMENTED]")
        print("   ⏳ MusicXML generation: [TO BE IMPLEMENTED]")
        print()
        print("💡 Next development steps:")
        print("   1. ✅ PHASE TRANSITION: Moving to cryptographic development")
        print("   2. 🔐 Extract mathematical primitives from musical algorithms")
        print("   3. 🔒 Implement revolutionary musical cryptography engine")
        print("   4. 📋 Document algorithms for patent filing")
        print("   5. ⚖️  File patent applications before any public disclosure")
        print(f"{'='*60}")
        print("🔐 CONFIDENTIAL: Ready for cryptographic implementation!")
        print("⚠️  PATENT PENDING - KEEP DEVELOPMENT CONFIDENTIAL")

    def extract_cryptographic_primitives(self) -> None:
        """
        CONFIDENTIAL: Extract mathematical primitives from musical algorithms for cryptographic use.
        
        This method begins the transformation from musical intelligence to cryptographic strength.
        DO NOT EXPOSE PUBLICLY UNTIL PATENT PROTECTION IS SECURED.
        """
        if self.loaded_data is None:
            print("❌ No data loaded. Please load a file first.")
            return
        
        print(f"\n{'='*60}")
        print("🔐 EXTRACTING CRYPTOGRAPHIC PRIMITIVES")
        print(f"{'='*60}")
        print("⚠️  CONFIDENTIAL DEVELOPMENT - PATENT PENDING")
        print(f"Source file: {self.current_file}")
        
        # Import crypto core (keep import local for security)
        try:
            from enki_crypto_core import EnkiCryptoCore
            
            # Initialize crypto engine with our alpha data
            df = self.get_dataframe()
            crypto_engine = EnkiCryptoCore(df)
            
            # Extract mathematical foundation
            print("\n🔬 Extracting mathematical foundation from musical algorithms...")
            crypto_primitives = crypto_engine.extract_mathematical_foundation()
            
            print("✅ Cryptographic primitives extracted successfully!")
            print(f"   - Chi mathematics: {len(crypto_primitives.get('chi_mathematics', {}))} components")
            print(f"   - Theta mathematics: {len(crypto_primitives.get('theta_mathematics', {}))} components") 
            print(f"   - Lambda mathematics: {len(crypto_primitives.get('lambda_mathematics', {}))} components")
            print(f"   - Epsilon mathematics: {len(crypto_primitives.get('epsilon_mathematics', {}))} components")
            print(f"   - Mod table context: Available")
            
            print(f"\n💡 Mathematical primitives ready for encryption implementation!")
            print("🔐 KEEP CONFIDENTIAL - PATENT PENDING")
            
            return crypto_primitives
            
        except ImportError as e:
            print(f"❌ Error importing crypto core: {e}")
            print("   Make sure enki_crypto_core.py is in the src directory")
        except Exception as e:
            print(f"❌ Error extracting cryptographic primitives: {e}")

    def test_encryption_decryption(self) -> None:
        """
        CONFIDENTIAL: Test encryption and decryption using musical algorithm intelligence.
        
        This method demonstrates the revolutionary cryptographic capabilities.
        DO NOT EXPOSE PUBLICLY UNTIL PATENT PROTECTION IS SECURED.
        """
        if self.loaded_data is None:
            print("❌ No data loaded. Please load a file first.")
            return
        
        print(f"\n{'='*60}")
        print("🔐 TESTING MUSICAL CRYPTOGRAPHY ENGINE")
        print(f"{'='*60}")
        print("⚠️  CONFIDENTIAL DEVELOPMENT - PATENT PENDING")
        print(f"Source file: {self.current_file}")
        
        try:
            from enki_crypto_core import EnkiCryptoCore
            
            # Initialize crypto engine
            df = self.get_dataframe()
            crypto_engine = EnkiCryptoCore(df)
            
            # Get test message from user
            test_message = input("\n🔤 Enter message to encrypt (or press Enter for default): ").strip()
            if not test_message:
                test_message = "Revolutionary musical cryptography test message!"
            
            print(f"\n📝 Original message: '{test_message}'")
            
            # Encrypt the message
            print("\n🔒 Encrypting using musical algorithm intelligence...")
            encrypted_data = crypto_engine.encrypt_message(test_message)
            print(f"✅ Encryption complete!")
            print(f"   - Original length: {len(test_message)} characters")
            print(f"   - Encrypted length: {len(encrypted_data)} bytes")
            
            # Decrypt the message
            print("\n🔓 Decrypting using musical algorithm intelligence...")
            decrypted_message = crypto_engine.decrypt_message(encrypted_data)
            print(f"✅ Decryption complete!")
            print(f"📝 Decrypted message: '{decrypted_message}'")
            
            # Verify integrity
            if test_message == decrypted_message:
                print("\n✅ ENCRYPTION/DECRYPTION TEST SUCCESSFUL!")
                print("🔐 Musical cryptography engine is operational!")
            else:
                print("\n❌ ENCRYPTION/DECRYPTION TEST FAILED!")
                print("🔧 Algorithm implementation needs refinement.")
            
            print(f"\n💡 Revolutionary musical cryptography demonstrated!")
            print("🔐 KEEP CONFIDENTIAL - PATENT PENDING")
            
        except ImportError as e:
            print(f"❌ Error importing crypto core: {e}")
        except Exception as e:
            print(f"❌ Error during encryption/decryption test: {e}")

    def run_interactive_session(self) -> None:
        """
        Run an interactive session to select and display alpha data.
        """
        print("🚀 Alpha Importer - Interactive Session")
        print("="*50)
        
        # Select file
        filename = self.select_file_interactive()
        if filename is None:
            return
        
        # Load file
        if not self.load_file(filename):
            return
        
        # Check if metadata is available to determine menu options
        has_metadata = False
        if isinstance(self.loaded_data, dict) and len(self.get_metadata()) > 0:
            has_metadata = True
        
        # Display options
        while True:
            print(f"\n{'='*60}")
            print("DISPLAY OPTIONS")
            print(f"{'='*60}")
            print("Current file:", self.current_file)
            print()
            print("1. Display transformed dataframe")
            if has_metadata:
                print("2. Display metadata")
                print("3. Extract cryptographic primitives")
                print("4. Test encryption/decryption")
                print("5. Select different file")
                print("6. Quit")
                max_choice = 6
            else:
                print("2. Extract cryptographic primitives")
                print("3. Test encryption/decryption")
                print("4. Select different file")
                print("5. Quit")
                max_choice = 5
            
            try:
                choice = input(f"\nSelect option (1-{max_choice}): ").strip()
                
                if choice == '1':
                    self.display_transformed_dataframe()
                elif choice == '2':
                    if has_metadata:
                        self.display_metadata()
                    else:
                        # Option 2 is "Extract cryptographic primitives" when no metadata
                        self.extract_cryptographic_primitives()
                elif choice == '3':
                    if has_metadata:
                        # Option 3 is "Extract cryptographic primitives" when metadata available
                        self.extract_cryptographic_primitives()
                    else:
                        # Option 3 is "Test encryption/decryption" when no metadata
                        self.test_encryption_decryption()
                elif choice == '4':
                    if has_metadata:
                        # Option 4 is "Test encryption/decryption" when metadata available
                        self.test_encryption_decryption()
                    else:
                        # Option 4 is "Select different file" when no metadata
                        filename = self.select_file_interactive()
                        if filename:
                            if self.load_file(filename):
                                # Re-check metadata availability for new file
                                has_metadata = isinstance(self.loaded_data, dict) and len(self.get_metadata()) > 0
                elif choice == '5':
                    if has_metadata:
                        # Option 5 is "Select different file" when metadata available
                        filename = self.select_file_interactive()
                        if filename:
                            if self.load_file(filename):
                                # Re-check metadata availability for new file
                                has_metadata = isinstance(self.loaded_data, dict) and len(self.get_metadata()) > 0
                    else:
                        # Option 5 is "Quit" when no metadata
                        print("\n👋 Goodbye!\n")
                        break
                elif choice == '6' and has_metadata:
                    print("\n👋 Goodbye!\n")
                    break
                else:
                    print(f"❌ Invalid choice. Please select 1-{max_choice}.")
                    
            except KeyboardInterrupt:
                print("\n👋 Session ended by user.")
                break
            except Exception as e:
                print(f"❌ Error: {e}")


def main():
    """
    Main function to demonstrate AlphaImporter functionality.
    """
    print("🔍 Alpha Importer - Standalone Mode")
    print("="*50)
    
    importer = AlphaImporter()
    importer.run_interactive_session()


if __name__ == "__main__":
    main()
