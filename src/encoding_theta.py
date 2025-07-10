import pandas as pd
from tabulate import tabulate

# Define custom encoding standard for the chromatic scale
data_note_choice = {
    'Character': ["A Double Flat", "A Flat", "A Natural", "A Sharp", "A Double Sharp", "B Double Flat", "B Flat", "B Natural", "B Sharp", "B Double Sharp", "C Double Flat", "C Flat", "C Natural", "C Sharp", "C Double Sharp", "D Double Flat", "D Flat", "D Natural", "D Sharp", "D Double Sharp", "E Double Flat", "E Flat", "E Natural", "E Sharp", "E Double Sharp", "F Double Flat", "F Flat", "F Natural", "F Sharp", "F Double Sharp", "G Double Flat", "G Flat", "G Natural", "G Sharp", "G Double Sharp"],
    "Step": ["A♭♭", "A♭", "A♮", "A♯", "A♯♯", "B♭♭", "B♭", "B♮", "B♯", "B♯♯", "C♭♭", "C♭", "C♮", "C♯", "C♯♯", "D♭♭", "D♭", "D♮", "D♯", "D♯♯", "E♭♭", "E♭", "E♮", "E♯", "E♯♯", "F♭♭", "F♭", "F♮", "F♯", "F♯♯", "G♭♭", "G♭", "G♮", "G♯", "G♯♯"],
    'XML Step': ["A", "A", "A", "A", "A", "B", "B", "B", "B", "B", "C", "C", "C", "C", "C", "D", "D", "D", "D", "D", "E", "E", "E", "E", "E", "F", "F", "F", "F", "F", "G", "G", "G", "G", "G"]
}

# Add an enharmonic column to the DataFrame
enharmonic_dict = {
    "A♭♭": "G♮", "A♭": "G♯", "A♮": "A♮", "A♯": "B♭", "A♯♯": "B♮",
    "B♭♭": "A♮", "B♭": "A♯", "B♮": "B♮", "B♯": "C♮", "B♯♯": "C♯",
    "C♭♭": "B♭", "C♭": "B♮", "C♮": "C♮", "C♯": "D♭", "C♯♯": "D♮",
    "D♭♭": "C♮", "D♭": "C♯", "D♮": "D♮", "D♯": "E♭", "D♯♯": "E♮",
    "E♭♭": "D♮", "E♭": "D♯", "E♮": "E♮", "E♯": "F♮", "E♯♯": "F♯",
    "F♭♭": "E♭", "F♭": "E♮", "F♮": "F♮", "F♯": "G♭", "F♯♯": "G♮",
    "G♭♭": "F♮", "G♭": "F♯", "G♮": "G♮", "G♯": "A♭", "G♯♯": "A♮"
}

# Define the alter mapping
alter_mapping = {
    "A♮": 0, "B♮": 0, "C♮": 0, "D♮": 0, "E♮": 0, "F♮": 0, "G♮": 0,
    "A♭♭": -2, "B♭♭": -2, "C♭♭": -2, "D♭♭": -2, "E♭♭": -2, "F♭♭": -2, "G♭♭": -2,
    "A♭": -1, "B♭": -1, "C♭": -1, "D♭": -1, "E♭": -1, "F♭": -1, "G♭": -1,
    "A♯": 1, "B♯": 1, "C♯": 1, "D♯": 1, "E♯": 1, "F♯": 1, "G♯": 1,
    "A♯♯": 2, "B♯♯": 2, "C♯♯": 2, "D♯♯": 2, "E♯♯": 2, "F♯♯": 2, "G♯♯": 2
}

def create_theta_encoding_df(data_note_choice, enharmonic_dict, alter_mapping):
    """
    Create a DataFrame for theta encoding and ensure all lists in the dictionary have the same length.

    Parameters:
        data_note_choice (dict): A dictionary containing 'Character' and 'Value' keys.
        enharmonic_dict (dict): A dictionary mapping values to their enharmonic equivalents.
        alter_mapping (dict): A dictionary mapping values to their alterations.

    Returns:
        pd.DataFrame: A DataFrame with the theta encoding.
    """
    # Create a DataFrame from the data_note_choice dictionary
    theta_encoding_df = pd.DataFrame(data_note_choice)

    # Add an enharmonic column to the DataFrame
    theta_encoding_df['Enharmonic'] = theta_encoding_df['Step'].map(enharmonic_dict)


    # Add the state column to the DataFrame
    theta_encoding_df['Alter'] = theta_encoding_df['Step'].map(alter_mapping)

    return theta_encoding_df

def main():
    # Create theta encoding DataFrame
    theta_encoding_df = create_theta_encoding_df(data_note_choice, enharmonic_dict, alter_mapping)

    # Print the DataFrame
    print("\nTheta Encoding DataFrame:\n")
    print(tabulate(theta_encoding_df, headers='keys', tablefmt='grid'))
    
    # Return the DataFrame for external use
    return theta_encoding_df

if __name__ == "__main__":
    theta_df = main()
