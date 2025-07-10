import pandas as pd

def phorms_mod_table(version="default"):
    """
    Creates a Phorms Mod Table based on the specified version.

    Parameters:
        version (str): The version of the mod table to create. Options: "default", "increment", "custom".

    Returns:
        pd.DataFrame: A DataFrame representing the mod table.
    """
    if version == "default":
        mod_table = {
            0: lambda x: x - 1,  # No change
            1: lambda x: x + 1,  # Increment by 1
            2: lambda x: x + 2,  # Increment by 2
            3: lambda x: x + 3   # Increment by 3
        }
    elif version == "increment":
        mod_table = {
            0: lambda x: x + 0,  # No change
            1: lambda x: x + 2,  # Increment by 2
            2: lambda x: x + 4,  # Increment by 4
            3: lambda x: x + 6   # Increment by 6
        }
    elif version == "custom":
        mod_table = {
            0: lambda x: x * 2,  # Multiply by 2
            1: lambda x: x ** 2, # Square the value
            2: lambda x: x - 3,  # Subtract 3
            3: lambda x: x + 5   # Add 5
        }
    else:
        raise ValueError(f"Unknown version '{version}'. Available options: 'default', 'increment', 'custom'.")

    # Convert to a DataFrame
    phorms_mod_table_df = pd.DataFrame.from_dict(mod_table, orient='index', columns=['Transformation'])
    return phorms_mod_table_df