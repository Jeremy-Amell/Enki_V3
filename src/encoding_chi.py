import pandas as pd
from fractions import Fraction
import random as random
import math as math
from tabulate import tabulate

# Chi State 0 creation
chi_state_0 = {
    "Character": ["Whole", "Half", "Quarter", "Eighth", "Sixteenth", "Thirty-second", "Sixty-fourth", "Hundreds-twenty-eighth", "Two-hundred-fifty-sixth", "Five-hundred-twelfth"],
    "Value": [1, Fraction(1, 2), Fraction(1, 4), Fraction(1, 8), Fraction(1, 16), Fraction(1, 32), Fraction(1, 64), Fraction(1, 128), Fraction(1, 256), Fraction(1, 512)]}

# Chi State 1 creation
chi_state_1 = {
    "Character": ["Dotted Whole", "Dotted Half", "Dotted Quarter", "Dotted Eighth", "Dotted Sixteenth", "Dotted Thirty-second", "Dotted Sixty-fourth", "Dotted Hundreds-twenty-eighth", "Dotted Two-hundred-fifty-sixth", "Dotted Five-hundred-twelfth"],
    "Value": [1 + Fraction(1, 2), Fraction(1, 2) + Fraction(1, 4), Fraction(1, 4) + Fraction(1, 8), Fraction(1, 8) + Fraction(1, 16), Fraction(1, 16) + Fraction(1, 32), Fraction(1, 32) + Fraction(1, 64), Fraction(1, 64) + Fraction(1, 128), Fraction(1, 128) + Fraction(1, 256), Fraction(1, 256) + Fraction(1, 512), Fraction(1, 512) + Fraction(1, 1024)]
}

def create_chi_encoding_df(dictionary, state_value):
    """
    Create a DataFrame for chi states and ensure all lists in the dictionary have the same length.

    Parameters:
        dictionary (dict): A dictionary containing 'Character' and 'Value' keys.

    Returns:
        pd.DataFrame: A DataFrame with the chi states.
    """
    # Ensure all lists in the dictionary have the same length
    lengths = [len(v) for v in dictionary.values()]
    assert all(length == lengths[0] for length in lengths), "All arrays must be of the same length"

    # Create a DataFrame for data_note_length
    chi_encoding_df = pd.DataFrame(dictionary)

    # Add a new column for the float representation of the 'Value' column
    chi_encoding_df["Float Value"] = [float(value) for value in chi_encoding_df["Value"]]

    chi_encoding_df["State"] = state_value
    chi_encoding_df["State"] = chi_encoding_df["State"].astype(int)

    return chi_encoding_df

def main():
    # Create chi states
    chi_encoding_state_0_df = create_chi_encoding_df(chi_state_0, 0)
    chi_encoding_state_1_df = create_chi_encoding_df(chi_state_1, 1)

    # Print the DataFrames
    print("\nChi State 0 DataFrame:")
    print(chi_encoding_state_0_df)
    
    print("\nChi State 1 DataFrame:")
    print(chi_encoding_state_1_df)

    # Return the DataFrames for external use
    return chi_encoding_state_0_df, chi_encoding_state_1_df

if __name__ == "__main__":
    chi_df_0, chi_df_1 = main()
    # You can use chi_df_0 and chi_df_1 for further processing or testing
