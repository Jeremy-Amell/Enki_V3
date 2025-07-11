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
    elif version == "chromatic":
        # Chromatic pitch transformations focusing on 12-tone equal temperament (Theta values)
        mod_table = {
            0: lambda x: x % 12,           # Map to 12-tone chromatic scale (C, C#, D, D#, E, F, F#, G, G#, A, A#, B)
            1: lambda x: (x + 7) % 12,     # Perfect fifth up (circle of fifths progression)
            2: lambda x: (x + 4) % 12,     # Major third up (major chord relationships)
            3: lambda x: (x + 3) % 12      # Minor third up (minor chord relationships)
        }
    elif version == "rhythmic":
        # Rhythmic/temporal transformations focusing on note durations (Chi values)
        mod_table = {
            0: lambda x: x % 8,            # Map to common note values (whole=1, half=2, quarter=4, eighth=8)
            1: lambda x: (x * 2) % 8,      # Double the rhythmic speed (shorter durations)
            2: lambda x: max(1, x // 2),   # Half the rhythmic speed (longer durations)
            3: lambda x: (x + 1) % 8 + 1   # Shift to next rhythmic subdivision
        }
    elif version == "harmonic":
        # Harmonic transformations for chord progressions and voice leading
        mod_table = {
            0: lambda x: x % 12,           # Root note (fundamental)
            1: lambda x: (x + 4) % 12,     # Major third above
            2: lambda x: (x + 7) % 12,     # Perfect fifth above  
            3: lambda x: (x + 10) % 12     # Minor seventh above (dominant 7th)
        }
    elif version == "modal":
        # Modal transformations using different musical modes
        mod_table = {
            0: lambda x: x % 7,            # Diatonic scale (7 notes)
            1: lambda x: [0,2,4,5,7,9,11][x % 7],  # Major (Ionian) mode
            2: lambda x: [0,2,3,5,7,8,10][x % 7],  # Minor (Aeolian) mode
            3: lambda x: [0,1,3,5,7,8,10][x % 7]   # Phrygian mode (exotic/Spanish)
        }
    elif version == "octave":
        # Octave and register transformations (Lambda values)
        mod_table = {
            0: lambda x: x % 8,            # Constrain to 8 octaves (0-7)
            1: lambda x: min(7, x + 1),    # Transpose up one octave
            2: lambda x: max(0, x - 1),    # Transpose down one octave
            3: lambda x: 7 - (x % 8)       # Invert octave (high becomes low)
        }
    else:
        raise ValueError(f"Unknown version '{version}'. Available options: 'default', 'increment', 'custom', 'chromatic', 'rhythmic', 'harmonic', 'modal', 'octave'.")

    # Convert to a DataFrame
    phorms_mod_table_df = pd.DataFrame.from_dict(mod_table, orient='index', columns=['Transformation'])
    return phorms_mod_table_df