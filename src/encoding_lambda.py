import pandas as pd
from tabulate import tabulate

data_octave = {
    "Character": ["First Octave", "Second Octave", "Third Octave", "Fourth Octave", "Fifth Octave", "Sixth Octave", "Seventh Octave", "Eighth Octave"],
    "Value": [1, 2, 3, 4, 5, 6, 7, 8]
}

def create_lambda_encoding_df(dictionary):
    """
    Create a DataFrame for lambda states and ensure all lists in the dictionary have the same length.

    Parameters:
        dictionary (dict): A dictionary containing 'Character' and 'Value' keys.

    Returns:
        pd.DataFrame: A DataFrame with the lambda states.
    """
    # Ensure all lists in the dictionary have the same length
    lengths = [len(v) for v in dictionary.values()]
    assert all(length == lengths[0] for length in lengths), "All arrays must be of the same length"

    # Create a DataFrame for data_note_length
    lambda_encoding_df = pd.DataFrame(dictionary)

    return lambda_encoding_df


def main():
    # Create lambda states
    lambda_encoding_df = create_lambda_encoding_df(data_octave)

    # Print the DataFrames
    print("\nLambda Encoding DataFrame:")
    print(tabulate(lambda_encoding_df, headers='keys', tablefmt='grid'))

    # Return the DataFrame for external use
    return lambda_encoding_df

if __name__ == "__main__":
    lambda_df = main()