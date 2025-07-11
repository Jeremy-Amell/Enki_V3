# Imports
### If repeated is zero, the root and root_copy are included in the output, however polority seems to not be included in the current version. Need to fix the code so PVs are applied, but then that transform row is not repeated. 

import numpy as np
import pandas as pd
import random
import os
from IPython.display import clear_output
from phorms_mod_table import phorms_mod_table

# Enki class definition
class Enki_V3:
    def __init__(self, output_dir: str = "F:/Enki_V3/data/alpha_output", mod_table_version: str = "default"):

        self.N = None
        self.phi_ = None
        self.roots_list_ = None
        self.kappa_roots_ = None
        self.kappa_total = None
        self.data_triangle_roots = None
        self.data_triangle_roots_w_theta = None
        self.data_triangle_roots_w_lambda = None
        self.data_triangle_roots_w_epsilon = None
        self.data_triangle_roots_w_kappa_roots = None
        self.combined_values_of_data_triangle = None
        self.pva_array = None
        self.pva_length = None
        self.DT_df = None
        self.PVA_Mods = None
        self.PVA_Mods_df = None
        self.alpha_roots_pre_pivot = None
        self.alpha_roots_post_pivot = None
        self.combined_alpha_roots = None
        self.alpha_roots_df = None
        self.alpha_values = None
        self.alpha_phorms_dataframe = None
        self.phorms_mod_table_df = None
        self.transphormed_alpha_dataframe = None
        self.output_dir = output_dir
        self.mod_table_version = mod_table_version
        os.makedirs(self.output_dir, exist_ok=True)

    # User input declaration: Value for n
    def get_user_input(self) -> int:
        while True:
            try:
                clear_output(wait=True)
                user_input = input(
                    "Enki: Welcome...I am Enki."
                    "\nEnki: Enter an integer for n (6-15) or 'q' to quit: \n"
                ).strip().lower()
                if user_input == 'q':
                    return None
                n = int(user_input)
                if 6 <= n <= 15:
                    return n
            except ValueError:
                pass

    # This function is the main user interface that interacts with the user
    def Enki_User_Interface(self):
        clear_output(wait=True)
        while True:
            n = self.get_user_input()
            if n is not None:
                user_response = input(" \nEnter 'y' to continue or 'q' to quit and start over: ").strip().lower()
                if user_response == 'y':
                    return n
                elif user_response == 'q':
                    continue
                else:
                    continue
            else:
                break

    # Step 2: Create the base array (phi_)
    def create_base(self):
        self.phi_ = np.array([random.randint(0, 9) for _ in range(self.N)])
        return self.phi_

    # Step 3: Create a list of root arrays
    def root_arrays(self):
        self.roots_list_ = [
            ("chi_root", np.array([], dtype=int)),
            ("theta_root", np.array([], dtype=int)),
            ("lambda_root", np.array([], dtype=int)),
            ("epsilon_root", np.array([], dtype=int)),
        ]
        return self.roots_list_

    # Step 4: Create kappa root arrays
    def create_kappa_root_arrays(self):
        self.kappa_total = self.N - 4
        self.kappa_roots_ = [(f"kappa_root_{i}", np.array([], dtype=int)) for i in range(self.kappa_total)]
        return self.kappa_roots_, self.kappa_total

    # Step 5: Create data triangle roots
    def create_data_triangle_roots(self):
        for i, root in enumerate(self.roots_list_):
            if root[0] == "chi_root":
                self.roots_list_[i] = ("chi_root", self.phi_.copy())
                break
        self.data_triangle_roots = self.roots_list_ + self.kappa_roots_
        return self.data_triangle_roots

    # Step 6: Update data triangle roots (w/ theta)
    def update_theta_root(self):
        chi_root = None
        for name, array in self.data_triangle_roots:
            if name == "chi_root":
                chi_root = array
                break
        if chi_root is None:
            raise ValueError("chi_root not found in data_triangle_roots")
        theta_root_values = np.abs(np.diff(chi_root))
        for i, (name, array) in enumerate(self.data_triangle_roots):
            if name == "theta_root":
                self.data_triangle_roots[i] = ("theta_root", theta_root_values)
                break
        return self.data_triangle_roots

    # Step 7: Update data triangle roots (w/ lambda)
    def update_lambda_root(self):
        theta_root = None
        for name, array in self.data_triangle_roots:
            if name == "theta_root":
                theta_root = array
                break
        if theta_root is None:
            raise ValueError("theta_root not found in data_triangle_roots")
        lambda_root_values = np.abs(np.diff(theta_root))
        for i, (name, array) in enumerate(self.data_triangle_roots):
            if name == "lambda_root":
                self.data_triangle_roots[i] = ("lambda_root", lambda_root_values)
                break
        return self.data_triangle_roots

    # Step 8: Update data triangle roots (w/ epsilon)
    def update_epsilon_root(self):
        lambda_root = None
        for name, array in self.data_triangle_roots:
            if name == "lambda_root":
                lambda_root = array
                break
        if lambda_root is None:
            raise ValueError("lambda_root not found in data_triangle_roots")
        epsilon_root_values = np.abs(np.diff(lambda_root))
        for i, (name, array) in enumerate(self.data_triangle_roots):
            if name == "epsilon_root":
                self.data_triangle_roots[i] = ("epsilon_root", epsilon_root_values)
                break
        return self.data_triangle_roots

    # Step 9: Update data triangle roots (w/ kappa_roots_)
    def update_kappa_roots(self):
        epsilon_root = None
        for name, array in self.data_triangle_roots:
            if name == "epsilon_root":
                epsilon_root = array
                break
        if epsilon_root is None:
            raise ValueError("epsilon_root not found in data_triangle_roots")
        kappa_root_0_values = np.abs(np.diff(epsilon_root))
        for i, (name, array) in enumerate(self.data_triangle_roots):
            if name == "kappa_root_0":
                self.data_triangle_roots[i] = ("kappa_root_0", kappa_root_0_values)
                break
        for kappa_index in range(self.kappa_total - 1):
            current_kappa_name = f"kappa_root_{kappa_index}"
            current_kappa = None
            for name, array in self.data_triangle_roots:
                if name == current_kappa_name:
                    current_kappa = array
                    break
            if current_kappa is None:
                raise ValueError(f"{current_kappa_name} not found in data_triangle_roots")
            next_kappa_values = np.abs(np.diff(current_kappa))
            next_kappa_name = f"kappa_root_{kappa_index + 1}"
            for i, (name, array) in enumerate(self.data_triangle_roots):
                if name == next_kappa_name:
                    self.data_triangle_roots[i] = (next_kappa_name, next_kappa_values)
                    break
        return self.data_triangle_roots

    # Step 10: Combine all values of Data Triangle
    def combine_all_values_DT(self):
        max_length = max(len(array) for _, array in self.data_triangle_roots)
        padded_data = {name: np.pad(array, (0, max_length - len(array)), constant_values=-99) for name, array in self.data_triangle_roots}
        combined_array = []
        for row_index in range(max_length):
            for name in padded_data:
                value = padded_data[name][row_index]
                if value != -99:
                    combined_array.append(value)
        self.combined_values_of_data_triangle = np.array(combined_array)
        return self.combined_values_of_data_triangle

    # Step 11: Create PVA array
    def create_pva_array(self):
        self.pva_array = []
        for i in range(len(self.combined_values_of_data_triangle) - 1):
            if self.combined_values_of_data_triangle[i + 1] > self.combined_values_of_data_triangle[i]:
                self.pva_array.append(1)
            elif self.combined_values_of_data_triangle[i + 1] < self.combined_values_of_data_triangle[i]:
                self.pva_array.append(0)
            else:
                self.pva_array.append(2)
        self.pva_array.append(3)
        self.pva_array = np.array(self.pva_array)
        self.pva_length = len(self.pva_array)
        return self.pva_array, self.pva_length

    # Step 12: Create DataFrame for data triangle
    def create_DT_dataframe(self):
        max_length = max(len(array) for _, array in self.data_triangle_roots)
        padded_data = {name: np.pad(array, (0, max_length - len(array)), constant_values=-99) for name, array in self.data_triangle_roots}
        self.DT_df = pd.DataFrame(padded_data)
        return self.DT_df

    # Step 13: Create PVA Mods
    def create_PVA_Mods(self):
        """Create and initialize the PVA_Mods attribute."""
        if self.pva_array is None:
            raise ValueError("pva_array is not initialized. Call create_pva_array first.")
        self.PVA_Mods = []
        array_length = len(self.pva_array)
        current_index = 0
        for _ in range(self.N):
            new_array = []
            for _ in range(self.N):
                new_array.append(self.pva_array[current_index])
                current_index = (current_index + 1) % array_length
            self.PVA_Mods.append(new_array)
        self.PVA_Mods = np.array(self.PVA_Mods)
        return self.PVA_Mods

    # Step 14: Create PVA Mods DF
    def create_PVA_Mods_dataframe(self):
        self.PVA_Mods_df = pd.DataFrame(self.PVA_Mods)
        self.PVA_Mods_df.index = [f"alpha_{i}_PV_mod" for i in range(len(self.PVA_Mods))]
        return self.PVA_Mods_df

    # Step 15: Create Alpha Roots Rows
    def create_alpha_roots_rows(self):
        output_rows = [row[row != -99] for row in self.DT_df.iloc[0:(self.N - 3)].values]
        self.alpha_roots_pre_pivot = {"Output Rows": output_rows}
        return self.alpha_roots_pre_pivot

    # Step 16: Create Alpha Roots Post Pivot
    def create_alpha_roots_post_pivot(self):
        epsilon_index = self.DT_df.columns.get_loc("epsilon_root")
        num_rows = len(self.DT_df)
        self.alpha_roots_post_pivot = {}
        start_index = len(self.alpha_roots_pre_pivot["Output Rows"])
        for col_index in range(epsilon_index, len(self.DT_df.columns)):
            column_name = self.DT_df.columns[col_index]
            anti_diagonal = []
            for i in range(min(num_rows, col_index + 1)):
                anti_diagonal.append(self.DT_df.iloc[i, col_index - i])
            self.alpha_roots_post_pivot[f"alpha_{start_index}"] = anti_diagonal[::-1]
            start_index += 1
        return self.alpha_roots_post_pivot

    # Step 17: Combine Alpha Roots
    def combine_alpha_roots(self):
        self.combined_alpha_roots = {}
        for i, row in enumerate(self.alpha_roots_pre_pivot["Output Rows"]):
            self.combined_alpha_roots[f"alpha_root_{i}"] = list(row)
        offset = len(self.alpha_roots_pre_pivot["Output Rows"])
        for key, value in self.alpha_roots_post_pivot.items():
            self.combined_alpha_roots[f"alpha_root_{offset}"] = value
            offset += 1
        return self.combined_alpha_roots

    # Step 18: Create Alpha Roots DataFrame
    def create_alpha_roots_dataframe(self):
        self.alpha_roots_df = pd.DataFrame.from_dict(self.combined_alpha_roots, orient='index')
        self.alpha_roots_df = self.alpha_roots_df.fillna(-99).astype(int)
        return self.alpha_roots_df

    # Step 19: Create Alpha Values
    def create_alpha(self):
        self.alpha_values = {}
        all_repeater_values = self.alpha_roots_df.iloc[:, 4:].replace(-99, np.nan).stack().dropna().astype(int).tolist()
        for index, row in self.alpha_roots_df.iterrows():
            A_Root = [int(x) for x in row.iloc[:4].tolist()]
            valid_repeater_values = row.iloc[4:][row.iloc[4:] != -99]
            Repeater = int(valid_repeater_values.sum())
            if Repeater == 0:
                Repeater = int(np.random.choice(all_repeater_values)) if all_repeater_values else -1
            adjusted_index = index.replace("alpha_root", "alpha") + "_PV_mod"
            if adjusted_index in self.PVA_Mods_df.index:
                alpha_PV_mod = [int(x) for x in self.PVA_Mods_df.loc[adjusted_index].tolist()]
            else:
                alpha_PV_mod = [int(x) for x in self.PVA_Mods_df.sample(n=1).iloc[0].tolist()]
            self.alpha_values[f"{index}"] = {
                "A_Root": A_Root,
                "A_Root_Copy": A_Root.copy(),
                "Alpha_PV_Mod": alpha_PV_mod,
                "Repeater": Repeater
            }
        return self.alpha_values

    # Step 20: Create Alpha Phorms DataFrame
    def create_alpha_phorms_dataframe(self):
        self.alpha_phorms_dataframe = pd.DataFrame.from_dict(self.alpha_values, orient='index')
        return self.alpha_phorms_dataframe

    # Step 21: Apply Phorms Mod Table DF
    def phorms_mod_table(self):
        """
        Generate the Phorms Mod Table using the external function.
        """
        self.phorms_mod_table_df = phorms_mod_table(self.mod_table_version)
        return self.phorms_mod_table_df

# Step 22: Transphorm Alpha Dataframe
    def transphorm_alpha_dataframe(self, max_value=9):
        """
        Transforms the alpha_phorms_dataframe using the phorms_mod_table_df and creates a new DataFrame.
        Ensures all values in the resulting arrays are integers.
        """
        if self.alpha_phorms_dataframe is None:
            print("Error: alpha_phorms_dataframe is not defined.")
            self.transphormed_alpha_dataframe = None
            return None

        # Ensure the mod table is generated
        if self.phorms_mod_table_df is None:
            self.phorms_mod_table()

        # Create a copy of the alpha_phorms_dataframe to avoid modifying the original
        alpha_phorms_dataframe = self.alpha_phorms_dataframe.copy()

        # Initialize a dictionary to store the transformed outputs
        transformed_data = {}

        # Iterate through each row in the alpha_phorms_dataframe
        for index, row in alpha_phorms_dataframe.iterrows():
            # Extract the A_Root, A_Root_Copy, Alpha_PV_Mod, and Repeater values
            A_Root = [int(x) for x in row['A_Root']]
            A_Root_Copy = [int(x) for x in row['A_Root_Copy']]
            Alpha_PV_Mod = [int(x) for x in row['Alpha_PV_Mod']]
            Repeater = int(row['Repeater'])

            # Initialize a list to store all modified versions of A_Root_Copy
            modified_versions = [A_Root]  # Start with the original A_Root

            # Apply the transformation using the Mod Table for each value in Alpha_PV_Mod
            for mod in Alpha_PV_Mod:
                if mod in self.phorms_mod_table_df.index:
                    # Apply the transformation to each value in A_Root_Copy
                    transformed_row = [
                        int((self.phorms_mod_table_df.loc[mod, 'Transformation'](value) % (max_value + 1)))
                        if self.phorms_mod_table_df.loc[mod, 'Transformation'](value) >= 0
                        else max_value  # If the result is negative, set it to max_value
                        for value in A_Root_Copy
                    ]
                    # Add the transformed row to the list of modified versions
                    modified_versions.append(transformed_row)

            # Handle repetition based on the Repeater value
            if Repeater == 0:
                # If Repeater is zero, do not repeat the list of modified versions
                repeated_rows = modified_versions
            else:
                # Repeat all modified versions based on the Repeater value
                repeated_rows = modified_versions * Repeater

            # Validate that repeated_rows is a list of arrays and all elements are integers
            for array in repeated_rows:
                if not isinstance(array, list):
                    raise ValueError(f"Invalid structure: Expected a list, got {type(array)}")
                if not all(isinstance(x, int) for x in array):
                    raise ValueError(f"Invalid data type: All elements must be integers. Found: {array}")

            # Store the result in the dictionary
            transformed_data[f"alpha_phormed_{index.split('_')[-1]}"] = [repeated_rows]

        # Create a new DataFrame from the transformed data with a single column
        self.transphormed_alpha_dataframe = pd.DataFrame.from_dict(transformed_data, orient='index', columns=['Alpha_Phormed'])

        print("\nTransformed Alpha DataFrame created.")
        print(self.transphormed_alpha_dataframe)

        return self.transphormed_alpha_dataframe

    # Run the pipeline for the Enki class
    def run_pipeline(self):
        # Step 1: Get user input for N
        self.N = self.Enki_User_Interface()
        if self.N is None:
            return
        print(f"\nN: {self.N}")  # Print the value of N

        # Step 2: Create the base array (phi_)
        self.create_base()
        print(f"\nphi_: {self.phi_}")  # Print the value of phi_

        # Step 3: Create a list of root arrays
        self.root_arrays()

        # Step 4: Create kappa root arrays
        self.create_kappa_root_arrays()

        # Step 5: Create data triangle roots
        self.create_data_triangle_roots()

        # Step 6: Update roots w/ (theta)
        self.update_theta_root()

        # Step 7: Update roots w/ (lambda)
        self.update_lambda_root()

        # Step 8: Update roots w/ (epsilon)
        self.update_epsilon_root()

        # Step 9: Update roots w/ (kappa_roots_)
        self.update_kappa_roots()

        # Step 10: Combine all values of Data Triangle
        self.combine_all_values_DT()

        # Step 11: Create PVA array
        self.create_pva_array()
        print(f"\nPVA Array: {self.pva_array}")

        # Step 12: Create DataFrame for data triangle
        self.create_DT_dataframe()
        print(f"\nData Triangle DataFrame:\n{self.DT_df}")

        # Step 13: Create PVA Mods
        self.create_PVA_Mods()
        print(f"\nPVA Mods:\n{self.PVA_Mods}")

        # Step 14: Create PVA Mods DF
        self.create_PVA_Mods_dataframe()
        print(f"\nPVA Mods DataFrame:\n{self.PVA_Mods_df}")

        # Step 15: Create Alpha Roots Rows
        self.create_alpha_roots_rows()

        # Step 16: Create Alpha Roots Post Pivot
        self.create_alpha_roots_post_pivot()

        # Step 17: Combine Alpha Roots
        self.combine_alpha_roots()

        # Step 18: Create Alpha Roots DataFrame
        self.create_alpha_roots_dataframe()
        print(f"\nAlpha Roots DataFrame:\n{self.alpha_roots_df}")

        # Step 19: Create Alpha Values
        self.create_alpha()

        # Step 20: Create Alpha Phorms DataFrame
        self.create_alpha_phorms_dataframe()
        print(f"\nAlpha DataFrame (Phorms) :\n{self.alpha_phorms_dataframe}")

        # Step 21: Apply Phorms Mod Table DF
        self.phorms_mod_table()
        print(f"\nPhorms Mod Table ({self.mod_table_version} version):")
        print(self.phorms_mod_table_df)

        # Step 22: Transphorm Alpha Dataframe
        self.transphorm_alpha_dataframe()

        # Ensure the directory exists
        output_dir = r"F:/Enki_V3/data/alpha_output"
        os.makedirs(output_dir, exist_ok=True)
        self.output_dir = output_dir

        # Validate the structure of transphormed_alpha_dataframe
        if self.transphormed_alpha_dataframe is not None:
            for index, row in self.transphormed_alpha_dataframe.iterrows():
                alpha_phormed = row['Alpha_Phormed']

                # Check if the row is a list
                if not isinstance(alpha_phormed, list):
                    raise ValueError(f"Invalid structure at index {index}: Expected a list, got {type(alpha_phormed)}")

                # Check each array in the list
                for array_index, array in enumerate(alpha_phormed):
                    if not isinstance(array, list):
                        raise ValueError(f"Invalid structure in row {index}, array {array_index}: Expected a list, got {type(array)}")
                    if not all(isinstance(x, int) for x in array):
                        raise ValueError(f"Invalid data type in row {index}, array {array_index}: All elements must be integers. Found: {array}")

        # Define the output file path
        self.output_file = os.path.join(self.output_dir, f"alpha_transphormed_N{self.N}_phi_{'_'.join(map(str, self.phi_))}.pkl")

        # Export the DataFrame
        try:
            if self.transphormed_alpha_dataframe is not None:
                self.transphormed_alpha_dataframe.to_pickle(self.output_file)
                print(f"\nTransformed Alpha DataFrame exported to '{self.output_file}'.")
            else:
                print("No data to export. The DataFrame is empty or undefined.")
        except Exception as e:
            print(f"Error exporting DataFrame: {e}")

        print("\nEnki: Export completed successfully.")


if __name__ == "__main__":
    enki = Enki_V3()
    enki.run_pipeline()
