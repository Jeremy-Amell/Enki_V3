import numpy as np
import pandas as pd
from tabulate import tabulate

note_relationships = {
    'Character': ["Tie", "Slur", "Phrases", "Glissando", "Portamento", "Tuplet", "Chord", "Appregiated Chord"],
    'Definition': [
        "A curved line connecting two notes of the same pitch, indicating they should be played as a single note.",
        "A curved line connecting two or more notes of different pitches, indicating they should be played smoothly.",
        "A musical sentence or idea, often marked by a slur or phrase mark.",
        "A glide from one pitch to another, often notated with a straight or wavy line.",
        "A smooth, continuous slide between two pitches, similar to a glissando but more vocal in nature.",
        "A grouping of notes played within the duration of a single beat, often irregular in rhythm.",
        "A group of notes played simultaneously to create harmony.",
        "A chord where the notes are played in sequence rather than simultaneously."
    ]
}

# Dynamics are indicators of the relative intensity or volume of a musical line.
dynamics = {
    'Character': [
        "Pianississimo", "Pianissimo", "Piano", "Mezzo Piano", "Mezzo Forte", 
        "Forte", "Fortissimo", "Fortississimo", "Sforzando", "Fortepiano", 
        "Crescendo", "Decrescendo", "Niente"
    ],
    'Definition': [
        "Extremely soft.",
        "Very soft.",
        "Soft.",
        "Moderately soft.",
        "Moderately loud.",
        "Loud.",
        "Very loud.",
        "Extremely loud.",
        "A sudden, strong accent.",
        "A strong, loud attack followed by immediate softness.",
        "A gradual increase in volume.",
        "A gradual decrease in volume.",
        "To fade away to nothing."
    ]
}


# Articulations are symbols that indicate how a note should be played or sung.
# They can indicate the attack, duration, and release of a note, as well as the overall character of the sound.
articulations = {
    'Character': ["Staccato", "Staccatissimo", "Legato", "Marcato", "Tenuto", "Fermata", "Accent"],
    'Definition': [
        "A note played shorter than its full value, separated from the next note.",
        "An exaggerated staccato, even shorter and more detached.",
        "Notes played smoothly and connected, without separation.",
        "A note played with emphasis, often louder or more forcefully.",
        "A note held for its full value, sometimes slightly longer.",
        "A pause or hold on a note or rest, beyond its normal duration.",
        "A note played with a strong emphasis or stress."
    ]
}

# Ornaments are embellishments or decorative notes that are added to a melody to enhance its expressiveness and complexity.
# They can include trills, turns, mordents, and other figures that add interest to the music.
ornaments = {
    'Character': ["Tremelo", "Trill", "Upper Mordent", "Lower Mordent", "Turn", "Appoggiatura", "Acciaccatura"],
    'Definition': [
        "A rapid repetition of a single note or alternation between two notes.",
        "A rapid alternation between a note and the one above it.",
        "A single rapid alternation between a note and the one above it.",
        "A single rapid alternation between a note and the one below it.",
        "A sequence of notes that embellishes the main note, typically starting above or below it.",
        "A grace note performed before the main note, taking some of its duration.",
        "A very short grace note played before the main note, almost simultaneously."
    ]
}

#### Need instrument specific encoding.###

def create_encoding_df(data_dict):
    """
    Create a DataFrame for encoding and ensure all lists in the dictionary have the same length.

    Parameters:
        data_dict (dict): A dictionary containing 'Character' and 'Value' keys.

    Returns:
        pd.DataFrame: A DataFrame with the encoding.
    """
    # Create a DataFrame from the data_dict dictionary
    encoding_df = pd.DataFrame(data_dict)

    # Ensure all lists in the dictionary have the same length
    max_length = max(len(v) for v in data_dict.values())
    for key, value in data_dict.items():
        if len(value) < max_length:
            data_dict[key] += [None] * (max_length - len(value))


    return encoding_df

def main():
    # Create encoding DataFrames

    note_relationships_df = create_encoding_df(note_relationships)
    dynamics_df = create_encoding_df(dynamics)
    articulations_df = create_encoding_df(articulations)
    ornaments_df = create_encoding_df(ornaments)

    # Print the DataFrames

    print("\nNote Relationships Encoding DataFrame:\n")
    print(tabulate(note_relationships_df, headers='keys', tablefmt='grid'))

    print("\nDynamics Encoding DataFrame:\n")
    print(tabulate(dynamics_df, headers='keys', tablefmt='grid'))

    print("\nArticulations Encoding DataFrame:\n")
    print(tabulate(articulations_df, headers='keys', tablefmt='grid'))

    print("\nOrnaments Encoding DataFrame:\n")
    print(tabulate(ornaments_df, headers='keys', tablefmt='grid'))

    # Return the DataFrames for external use
    return note_relationships_df, dynamics_df, articulations_df, ornaments_df

if __name__ == "__main__":
    note_relationships_df, dynamics_df, articulations_df, ornaments_df = main()

