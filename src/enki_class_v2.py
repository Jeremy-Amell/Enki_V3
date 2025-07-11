# Imports
### If repeated is zero, the root and root_copy are included in the output, however polority seems to not be included in the current version. Need to fix the code so PVs are applied, but then that transform row is not repeated. 

import numpy as np
import pandas as pd
import random
import os
from IPython.display import clear_output

# Enki class definition
class Enki_V3:
    def __init__(self, output_dir: str = "F:/Enki_V3/data/alpha_output"):

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
        self.output_dir = output_dir
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

    # Step 1. This function is the main user interface that interacts with the user
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

    # Step 3: Create a list of root arrays. They are empty at this point.
    # This will be used to store the roots of the data triangle.
    def root_arrays(self):
        self.roots_list_ = [
            ("chi_root", np.array([], dtype=int)),
            ("theta_root", np.array([], dtype=int)),
            ("lambda_root", np.array([], dtype=int)),
            ("epsilon_root", np.array([], dtype=int)),
        ]
        return self.roots_list_

    # Step 4: Create kappa root arrays. They are empty at this point.
    # This will be used to store the kappa roots of the data triangle.
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

    # Step 13: Create PVA Mods. Creates an Array of PVA Mods based on the pva_array.
    # This is a 2D array where each row corresponds to a PVA Mod.
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

    def get_alpha_data(self):
        """
        Returns the generated alpha data for use with external transformers.
        
        Returns:
            dict: Dictionary containing all generated data
        """
        return {
            'N': self.N,
            'phi_': self.phi_,
            'alpha_phorms_dataframe': self.alpha_phorms_dataframe,
            'alpha_values': self.alpha_values,
            'alpha_roots_df': self.alpha_roots_df,
            'DT_df': self.DT_df,
            'PVA_Mods_df': self.PVA_Mods_df,
            'pva_array': self.pva_array
        }

    # Run the pipeline for the Enki class (Data Generation Only)
    def run_pipeline(self):
        """
        Runs the complete data generation pipeline (Steps 1-20).
        For transformations, use the AlphaTransformer class.
        """
        # Step 1: Get user input for N
        self.N = self.Enki_User_Interface()
        if self.N is None:
            return
        print(f"\n[Step 1] N: {self.N}")

        # Step 2: Create the base array (phi_)
        self.create_base()
        print(f"\n[Step 2] phi_: {self.phi_}")

        # Step 3: Create a list of root arrays
        self.root_arrays()
        print(f"\n[Step 3] Roots Arrays: {self.roots_list_}")

        # Step 4: Create kappa root arrays
        self.create_kappa_root_arrays()
        print(f"\n[Step 4] Kappa Roots: {self.kappa_roots_}, Kappa Total: {self.kappa_total}")

        # Step 5: Create data triangle roots
        self.create_data_triangle_roots()
        print(f"\n[Step 5] Data Triangle Roots: {self.data_triangle_roots}")

        # Step 6: Update roots w/ (theta)
        self.update_theta_root()
        print(f"\n[Step 6] Data Triangle Roots w/ Theta: {self.data_triangle_roots}")

        # Step 7: Update roots w/ (lambda)
        self.update_lambda_root()
        print(f"\n[Step 7] Data Triangle Roots w/ Lambda: {self.data_triangle_roots}")

        # Step 8: Update roots w/ (epsilon)
        self.update_epsilon_root()
        print(f"\n[Step 8] Data Triangle Roots w/ Epsilon: {self.data_triangle_roots}")

        # Step 9: Update roots w/ (kappa_roots_)
        self.update_kappa_roots()
        print(f"\n[Step 9] Data Triangle Roots w/ Kappa Roots: {self.data_triangle_roots}")

        # Step 10: Combine all values of Data Triangle
        self.combine_all_values_DT()
        print(f"\n[Step 10] Combined Values of Data Triangle: {self.combined_values_of_data_triangle}")

        # Step 11: Create PVA array
        self.create_pva_array()
        print(f"\n[Step 11] PVA Array: {self.pva_array}")

        # Step 12: Create DataFrame for data triangle
        self.create_DT_dataframe()
        print(f"\n[Step 12] Data Triangle DataFrame:\n{self.DT_df}")

        # Step 13: Create PVA Mods
        self.create_PVA_Mods()
        print(f"\n[Step 13] PVA Mods:\n{self.PVA_Mods}")

        # Step 14: Create PVA Mods DF
        self.create_PVA_Mods_dataframe()
        print(f"\n[Step 14] PVA Mods DataFrame:\n{self.PVA_Mods_df}")

        # Step 15: Create Alpha Roots Rows
        self.create_alpha_roots_rows()
        print(f"\n[Step 15] Alpha Roots Pre-Pivot:\n{self.alpha_roots_pre_pivot}")

        # Step 16: Create Alpha Roots Post Pivot
        self.create_alpha_roots_post_pivot()
        print(f"\n[Step 16] Alpha Roots Post-Pivot:\n{self.alpha_roots_post_pivot}")

        # Step 17: Combine Alpha Roots
        self.combine_alpha_roots()
        print(f"\n[Step 17] Combined Alpha Roots:\n{self.combined_alpha_roots}")

        # Step 18: Create Alpha Roots DataFrame
        self.create_alpha_roots_dataframe()
        print(f"\n[Step 18] Alpha Roots DataFrame:\n{self.alpha_roots_df}")

        # Step 19: Create Alpha Values
        self.create_alpha()
        print(f"\n[Step 19] Alpha Values:\n{self.alpha_values}")

        # Step 20: Create Alpha Phorms DataFrame
        self.create_alpha_phorms_dataframe()
        print(f"\n[Step 20] Alpha DataFrame (Phorms):\n{self.alpha_phorms_dataframe}")

        print("\n" + "="*50)
        print("Data Generation Complete!")
        print("Use AlphaTransformer class for transformations.")
        print("="*50)
        
        return self.get_alpha_data()


if __name__ == "__main__":
    enki = Enki_V3()
    enki.run_pipeline()
