# Alpha Transformer Class
# Handles all transformations of alpha data using phorms mod tables
# This class is designed to be extensible for music theory and decision tree expansions

import pandas as pd
import numpy as np
import os
from phorms_mod_table import phorms_mod_table


class AlphaTransformer:
    """
    Handles transformation of alpha data using various mod tables and transformation rules.
    Designed to be extensible for music theory applications and decision trees.
    """
    
    def __init__(self, mod_table_version: str = "default", output_dir: str = "F:/Enki_V3/data/alpha_output"):
        self.mod_table_version = mod_table_version
        self.output_dir = output_dir
        self.phorms_mod_table_df = None
        self.transphormed_alpha_dataframe = None
        os.makedirs(self.output_dir, exist_ok=True)
    
    def load_mod_table(self):
        """Generate the Phorms Mod Table using the external function."""
        self.phorms_mod_table_df = phorms_mod_table(self.mod_table_version)
        return self.phorms_mod_table_df
    
    def transform_alpha_dataframe(self, alpha_phorms_dataframe, max_value=9):
        """
        Transforms the alpha_phorms_dataframe using the phorms_mod_table_df and creates a new DataFrame.
        Ensures all values in the resulting arrays are integers.
        
        Args:
            alpha_phorms_dataframe: DataFrame containing alpha values to transform
            max_value: Maximum value for modulo operations (default: 9)
            
        Returns:
            DataFrame: Transformed alpha data
        """
        if alpha_phorms_dataframe is None:
            print("Error: alpha_phorms_dataframe is not defined.")
            return None

        # Ensure the mod table is loaded
        if self.phorms_mod_table_df is None:
            self.load_mod_table()

        # Create a copy to avoid modifying the original
        alpha_phorms_dataframe = alpha_phorms_dataframe.copy()
        
        # Initialize a dictionary to store the transformed outputs
        transformed_data = {}

        # Iterate through each row in the alpha_phorms_dataframe
        for index, row in alpha_phorms_dataframe.iterrows():
            # Extract the values
            A_Root = [int(x) for x in row['A_Root']]
            A_Root_Copy = [int(x) for x in row['A_Root_Copy']]
            Alpha_PV_Mod = [int(x) for x in row['Alpha_PV_Mod']]
            Repeater = int(row['Repeater'])

            # Initialize with the original A_Root
            modified_versions = [A_Root]

            # Apply transformations for each mod value
            for mod in Alpha_PV_Mod:
                if mod in self.phorms_mod_table_df.index:
                    transformed_row = [
                        int((self.phorms_mod_table_df.loc[mod, 'Transformation'](value) % (max_value + 1)))
                        if self.phorms_mod_table_df.loc[mod, 'Transformation'](value) >= 0
                        else max_value
                        for value in A_Root_Copy
                    ]
                    modified_versions.append(transformed_row)

            # Handle repetition based on the Repeater value
            if Repeater == 0:
                repeated_rows = modified_versions
            else:
                repeated_rows = modified_versions * Repeater

            # Validate the structure
            self._validate_structure(repeated_rows, index)

            # Store the result
            transformed_data[f"alpha_phormed_{index.split('_')[-1]}"] = [repeated_rows]

        # Create the transformed DataFrame
        self.transphormed_alpha_dataframe = pd.DataFrame.from_dict(
            transformed_data, orient='index', columns=['Alpha_Phormed']
        )

        print("\nTransformed Alpha DataFrame created.")
        print(self.transphormed_alpha_dataframe)
        return self.transphormed_alpha_dataframe
    
    def _validate_structure(self, repeated_rows, index):
        """Validate that repeated_rows has the correct structure."""
        for array in repeated_rows:
            if not isinstance(array, list):
                raise ValueError(f"Invalid structure: Expected a list, got {type(array)}")
            if not all(isinstance(x, int) for x in array):
                raise ValueError(f"Invalid data type: All elements must be integers. Found: {array}")
    
    def export_transformed_data(self, N, phi_):
        """
        Export the transformed DataFrame to a pickle file.
        
        Args:
            N: The N value used in generation
            phi_: The phi array used in generation
        """
        if self.transphormed_alpha_dataframe is None:
            print("No data to export. The DataFrame is empty or undefined.")
            return None
            
        # Define the output file path with mod table suffix
        phi_str = '_'.join(map(str, phi_))
        filename = f"alpha_transphormed_N{N}_phi_{phi_str}_{self.mod_table_version}.pkl"
        output_file = os.path.join(self.output_dir, filename)

        try:
            self.transphormed_alpha_dataframe.to_pickle(output_file)
            print(f"\nTransformed Alpha DataFrame exported to '{output_file}'.")
            return output_file
        except Exception as e:
            print(f"Error exporting DataFrame: {e}")
            return None
    
    # Future expansion methods for music theory and decision trees
    def apply_music_theory_transform(self, alpha_data, theory_type="harmonic"):
        """
        Placeholder for future music theory transformations.
        
        Args:
            alpha_data: The alpha data to transform
            theory_type: Type of music theory to apply
        """
        # This is where you would implement specific music theory transformations
        print(f"Applying {theory_type} music theory transformation...")
        # Implementation would go here
        pass
    
    def apply_decision_tree_transform(self, alpha_data, decision_rules):
        """
        Placeholder for future decision tree transformations.
        
        Args:
            alpha_data: The alpha data to transform
            decision_rules: Rules for the decision tree
        """
        # This is where you would implement decision tree logic
        print("Applying decision tree transformation...")
        # Implementation would go here
        pass
