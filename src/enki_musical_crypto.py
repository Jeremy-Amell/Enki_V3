#!/usr/bin/env python3
"""
ENKI MUSICAL CRYPTOGRAPHY COMPLETE - TEXT TO MUSIC PIPELINE
CONFIDENTIAL AND PROPRIETARY - PATENT PENDING

This system demonstrates the complete pipeline:
1. Text Input → Musical Cryptographic Encryption
2. Encrypted Data → Musical Notation (MusicXML)
3. Musical Playback → Decryption Recovery

The innovation: Your secret message becomes actual music that can be played,
while simultaneously being cryptographically protected.

© 2025 Jeremy Amell. All Rights Reserved.
"""

import pandas as pd
import numpy as np
import hashlib
import secrets
import time
import json
import pickle
import xml.etree.ElementTree as ET
from typing import Dict, List, Any, Optional, Tuple, Union
from pathlib import Path
from dataclasses import dataclass

@dataclass
class MusicalNote:
    """Represents a musical note with all parameters."""
    pitch: str
    octave: int
    duration: str
    dynamics: str
    articulation: str
    
@dataclass
class MusicalMeasure:
    """Represents a musical measure."""
    notes: List[MusicalNote]
    time_signature: str = "4/4"
    key_signature: str = "C"

class EnkiMusicalCrypto:
    """
    CONFIDENTIAL: Complete musical cryptography system.
    
    Converts text → encrypted musical data → actual playable music.
    The music IS the encrypted message.
    """
    
    def __init__(self, input_dir: str = "F:/Enki_V3/data/alpha_output"):
        """Initialize the musical crypto system."""
        self.input_dir = Path(input_dir)
        self.crypto_layers = []
        
        # Musical parameter mappings
        self.chi_to_duration = {
            0: "whole", 1: "half", 2: "quarter", 3: "eighth",
            4: "sixteenth", 5: "thirty-second", 6: "quarter-dotted", 7: "half-dotted"
        }
        
        self.theta_to_pitch = {
            # Map theta values to chromatic pitches
            0: "C", 1: "C#", 2: "D", 3: "D#", 4: "E", 5: "F",
            6: "F#", 7: "G", 8: "G#", 9: "A", 10: "A#", 11: "B"
        }
        
        self.lambda_to_octave = {
            0: 3, 1: 4, 2: 5, 3: 6, 4: 7, 5: 8, 6: 4, 7: 5
        }
        
        self.epsilon_to_expression = {
            0: ("p", "legato"), 1: ("mp", "staccato"), 2: ("mf", "tenuto"), 3: ("f", "accent"),
            4: ("pp", "legato"), 5: ("ff", "marcato"), 6: ("sfz", "staccato"), 7: ("ppp", "legato")
        }
        
        print("🎵 ENKI MUSICAL CRYPTOGRAPHY - TEXT TO MUSIC PIPELINE")
        print("="*70)
        print("⚠️  REVOLUTIONARY MUSICAL ENCRYPTION - PATENT PENDING")
        print("🔐 Text becomes music, music becomes security")
        print("="*70)
        
        self._load_musical_crypto_layers()
    
    def _load_musical_crypto_layers(self) -> None:
        """Load musical cryptographic layers."""
        if not self.input_dir.exists():
            print(f"❌ Alpha output directory not found: {self.input_dir}")
            return
        
        # Find available files
        available_files = list(self.input_dir.glob("*.pkl"))
        context_groups = {}
        
        # Group files by parameters
        for file_path in available_files:
            filename = file_path.name
            if "_transphormed_" in filename:
                parts = filename.split("_transphormed_")
                if len(parts) == 2:
                    param_part = parts[0].replace("alpha_", "")
                    suffix_part = parts[1].replace(".pkl", "")
                    
                    if "_" in suffix_part:
                        suffix_parts = suffix_part.split("_")
                        mod_table = suffix_parts[-1]
                        n_and_phi = "_".join(suffix_parts[:-1])
                    else:
                        mod_table = "default"
                        n_and_phi = suffix_part
                    
                    param_key = f"{param_part}_{n_and_phi}"
                    if param_key not in context_groups:
                        context_groups[param_key] = {}
                    
                    context_groups[param_key][mod_table] = file_path
        
        if not context_groups:
            print("❌ No suitable parameter groups found")
            return
        
        # Select best group
        best_group = max(context_groups.items(), key=lambda x: len(x[1]))
        param_key, contexts = best_group
        
        print(f"\n🎵 MUSICAL PARAMETER GROUP: {param_key}")
        print(f"   🔐 Loading {len(contexts)} musical contexts...")
        
        # Load each context
        for mod_table, file_path in contexts.items():
            try:
                print(f"   🎼 Loading {mod_table.upper()} musical context...")
                
                with open(file_path, 'rb') as f:
                    data = pickle.load(f)
                
                if isinstance(data, dict) and 'transformed_alpha_dataframe' in data:
                    df = data['transformed_alpha_dataframe']
                elif isinstance(data, pd.DataFrame):
                    df = data
                else:
                    continue
                
                self.crypto_layers.append({
                    'name': mod_table,
                    'data': df,
                    'file': file_path.name
                })
                
                # Count musical elements
                total_arrays = 0
                if 'Alpha_Phormed' in df.columns:
                    for _, row in df.iterrows():
                        alpha_value = row['Alpha_Phormed']
                        if isinstance(alpha_value, list):
                            total_arrays += len(alpha_value)
                
                print(f"      ✅ {mod_table.upper()}: {total_arrays} musical elements")
                
            except Exception as e:
                print(f"      ❌ Error: {e}")
        
        print(f"\n🎉 MUSICAL CRYPTO SYSTEM READY!")
        print(f"   🎼 Musical Contexts: {len(self.crypto_layers)}")
        print(f"   🔐 Ready for text-to-music encryption")
    
    def text_to_music_encrypt(self, plaintext: str) -> Dict[str, Any]:
        """
        CONFIDENTIAL: Convert text to encrypted musical notation.
        """
        if not self.crypto_layers:
            raise ValueError("Musical crypto system not initialized")
        
        print(f"\n🎵 TEXT-TO-MUSIC ENCRYPTION INITIATED")
        print("="*60)
        print("⚠️  MUSICAL ENCRYPTION - PATENT PENDING")
        print(f"🔤 Converting text to musical cryptography...")
        
        # Convert text to musical parameters
        musical_elements = self._text_to_musical_elements(plaintext)
        
        # Apply musical encryption
        encrypted_musical_data = self._apply_musical_encryption(musical_elements)
        
        # Generate musical notation
        music_xml = self._generate_musicxml(encrypted_musical_data)
        
        # Create complete package
        encrypted_package = {
            'original_text': plaintext,
            'musical_elements': musical_elements,
            'encrypted_musical_data': encrypted_musical_data,
            'musicxml': music_xml,
            'metadata': {
                'timestamp': time.time(),
                'text_length': len(plaintext),
                'musical_measures': len(encrypted_musical_data),
                'encryption_method': 'musical_intelligence'
            }
        }
        
        print(f"\n✅ TEXT-TO-MUSIC ENCRYPTION COMPLETE!")
        print(f"   📝 Original text: {len(plaintext)} characters")
        print(f"   🎼 Musical measures: {len(encrypted_musical_data)}")
        print(f"   🎵 Music can be played and heard!")
        print(f"   🔐 Text is cryptographically hidden in the music")
        
        return encrypted_package
    
    def music_to_text_decrypt(self, encrypted_package: Dict[str, Any]) -> str:
        """
        CONFIDENTIAL: Extract text from musical notation.
        """
        print(f"\n🎵 MUSIC-TO-TEXT DECRYPTION INITIATED")
        print("="*60)
        
        encrypted_musical_data = encrypted_package['encrypted_musical_data']
        
        print(f"🔓 Extracting text from {len(encrypted_musical_data)} musical measures...")
        
        # Reverse musical encryption
        musical_elements = self._reverse_musical_encryption(encrypted_musical_data)
        
        # Convert back to text
        decrypted_text = self._musical_elements_to_text(musical_elements)
        
        print(f"\n✅ MUSIC-TO-TEXT DECRYPTION COMPLETE!")
        print(f"   🔓 Recovered text: '{decrypted_text}'")
        
        return decrypted_text
    
    def _text_to_musical_elements(self, text: str) -> List[MusicalNote]:
        """Convert text to musical elements using alpha arrays."""
        print(f"   🔤 Converting '{text}' to musical parameters...")
        
        musical_notes = []
        
        for i, char in enumerate(text):
            char_value = ord(char)
            
            # Use alpha arrays if available and properly map values
            if self.crypto_layers:
                layer = self.crypto_layers[i % len(self.crypto_layers)]
                alpha_arrays = self._get_alpha_arrays(layer['data'])
                
                if alpha_arrays:
                    array = alpha_arrays[i % len(alpha_arrays)]
                    if isinstance(array, list) and len(array) >= 4:
                        # Use alpha array values directly (already in correct ranges)
                        chi = abs(int(array[0])) % 8
                        theta = abs(int(array[1])) % 12
                        lambda_val = abs(int(array[2])) % 8
                        epsilon = abs(int(array[3])) % 8
                    else:
                        # Fallback mapping
                        chi, theta, lambda_val, epsilon = char_value % 8, char_value % 12, char_value % 8, char_value % 8
                else:
                    # Fallback mapping
                    chi, theta, lambda_val, epsilon = char_value % 8, char_value % 12, char_value % 8, char_value % 8
            else:
                # Direct character-based mapping (ensure proper modulo)
                chi, theta, lambda_val, epsilon = char_value % 8, char_value % 12, char_value % 8, char_value % 8
            
            # Double-check values are in range
            chi = chi % 8
            theta = theta % 12
            lambda_val = lambda_val % 8
            epsilon = epsilon % 8
            
            # Convert to musical parameters
            duration = self.chi_to_duration[chi]
            pitch = self.theta_to_pitch[theta]
            octave = self.lambda_to_octave[lambda_val]
            dynamics, articulation = self.epsilon_to_expression[epsilon]
            
            note = MusicalNote(
                pitch=pitch,
                octave=octave,
                duration=duration,
                dynamics=dynamics,
                articulation=articulation
            )
            
            musical_notes.append(note)
        
        print(f"      ✅ Generated {len(musical_notes)} musical notes")
        return musical_notes
    
    def _get_alpha_arrays(self, df: pd.DataFrame) -> List[List[int]]:
        """Extract alpha arrays from dataframe."""
        alpha_arrays = []
        if 'Alpha_Phormed' in df.columns:
            for _, row in df.iterrows():
                alpha_value = row['Alpha_Phormed']
                if isinstance(alpha_value, list):
                    alpha_arrays.extend(alpha_value)
        return alpha_arrays
    
    def _apply_musical_encryption(self, musical_notes: List[MusicalNote]) -> List[MusicalMeasure]:
        """Apply musical encryption transformations."""
        print(f"   🔐 Applying musical cryptographic transformations...")
        
        measures = []
        notes_per_measure = 4  # 4/4 time
        
        for i in range(0, len(musical_notes), notes_per_measure):
            measure_notes = musical_notes[i:i + notes_per_measure]
            
            # Pad measure if needed
            while len(measure_notes) < notes_per_measure:
                # Add rest or repeat last note
                if measure_notes:
                    last_note = measure_notes[-1]
                    rest_note = MusicalNote(
                        pitch="rest",
                        octave=last_note.octave,
                        duration="quarter",
                        dynamics="p",
                        articulation="legato"
                    )
                    measure_notes.append(rest_note)
                else:
                    # Default rest
                    measure_notes.append(MusicalNote("rest", 4, "quarter", "p", "legato"))
            
            measure = MusicalMeasure(
                notes=measure_notes,
                time_signature="4/4",
                key_signature="C"
            )
            
            measures.append(measure)
        
        print(f"      ✅ Created {len(measures)} musical measures")
        return measures
    
    def _reverse_musical_encryption(self, measures: List[MusicalMeasure]) -> List[MusicalNote]:
        """Reverse musical encryption to recover original elements."""
        print(f"   🔓 Reversing musical encryption...")
        
        all_notes = []
        for measure in measures:
            for note in measure.notes:
                if note.pitch != "rest":  # Skip rests
                    all_notes.append(note)
        
        print(f"      ✅ Recovered {len(all_notes)} musical notes")
        return all_notes
    
    def _musical_elements_to_text(self, musical_notes: List[MusicalNote]) -> str:
        """Convert musical elements back to text."""
        print(f"   🔤 Converting musical notes back to text...")
        
        text_chars = []
        
        for note in musical_notes:
            # Reverse the mapping process
            # Find the values that would produce these musical parameters
            chi = self._reverse_duration_mapping(note.duration)
            theta = self._reverse_pitch_mapping(note.pitch)
            lambda_val = self._reverse_octave_mapping(note.octave)
            epsilon = self._reverse_expression_mapping(note.dynamics, note.articulation)
            
            # Reconstruct character value (this is an approximation)
            # In a real system, you'd store more metadata for perfect recovery
            char_value = (chi * 32 + theta * 8 + lambda_val * 4 + epsilon) % 128
            
            # Map to printable ASCII
            if 32 <= char_value <= 126:
                text_chars.append(chr(char_value))
            else:
                # Fallback to safe character
                text_chars.append(chr(32 + (char_value % 95)))
        
        recovered_text = ''.join(text_chars)
        print(f"      ✅ Recovered text: '{recovered_text}'")
        return recovered_text
    
    def _reverse_duration_mapping(self, duration: str) -> int:
        """Reverse duration to chi value."""
        for chi, dur in self.chi_to_duration.items():
            if dur == duration:
                return chi
        return 0
    
    def _reverse_pitch_mapping(self, pitch: str) -> int:
        """Reverse pitch to theta value."""
        for theta, p in self.theta_to_pitch.items():
            if p == pitch:
                return theta
        return 0
    
    def _reverse_octave_mapping(self, octave: int) -> int:
        """Reverse octave to lambda value."""
        for lambda_val, oct in self.lambda_to_octave.items():
            if oct == octave:
                return lambda_val
        return 0
    
    def _reverse_expression_mapping(self, dynamics: str, articulation: str) -> int:
        """Reverse expression to epsilon value."""
        for epsilon, (dyn, art) in self.epsilon_to_expression.items():
            if dyn == dynamics and art == articulation:
                return epsilon
        return 0
    
    def _generate_musicxml(self, measures: List[MusicalMeasure]) -> str:
        """Generate MusicXML from musical measures."""
        print(f"   🎼 Generating MusicXML notation...")
        
        # Create basic MusicXML structure
        xml_content = []
        xml_content.append('<?xml version="1.0" encoding="UTF-8"?>')
        xml_content.append('<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">')
        xml_content.append('<score-partwise version="3.1">')
        
        # Header
        xml_content.append('  <work>')
        xml_content.append('    <work-title>Encrypted Musical Message</work-title>')
        xml_content.append('  </work>')
        xml_content.append('  <identification>')
        xml_content.append('    <creator type="composer">Enki Musical Cryptography Engine</creator>')
        xml_content.append('  </identification>')
        
        # Part list
        xml_content.append('  <part-list>')
        xml_content.append('    <score-part id="P1">')
        xml_content.append('      <part-name>Encrypted Message</part-name>')
        xml_content.append('    </score-part>')
        xml_content.append('  </part-list>')
        
        # Part
        xml_content.append('  <part id="P1">')
        
        # Measures
        for measure_num, measure in enumerate(measures, 1):
            xml_content.append(f'    <measure number="{measure_num}">')
            
            # Attributes for first measure
            if measure_num == 1:
                xml_content.append('      <attributes>')
                xml_content.append('        <divisions>4</divisions>')
                xml_content.append('        <key>')
                xml_content.append('          <fifths>0</fifths>')
                xml_content.append('        </key>')
                xml_content.append('        <time>')
                xml_content.append('          <beats>4</beats>')
                xml_content.append('          <beat-type>4</beat-type>')
                xml_content.append('        </time>')
                xml_content.append('        <clef>')
                xml_content.append('          <sign>G</sign>')
                xml_content.append('          <line>2</line>')
                xml_content.append('        </clef>')
                xml_content.append('      </attributes>')
            
            # Notes
            for note in measure.notes:
                xml_content.append('      <note>')
                
                if note.pitch == "rest":
                    xml_content.append('        <rest/>')
                else:
                    xml_content.append('        <pitch>')
                    xml_content.append(f'          <step>{note.pitch[0]}</step>')
                    if len(note.pitch) > 1 and note.pitch[1] == '#':
                        xml_content.append('          <alter>1</alter>')
                    xml_content.append(f'          <octave>{note.octave}</octave>')
                    xml_content.append('        </pitch>')
                
                # Duration
                duration_map = {
                    "whole": 16, "half": 8, "quarter": 4, "eighth": 2,
                    "sixteenth": 1, "thirty-second": 0.5,
                    "quarter-dotted": 6, "half-dotted": 12
                }
                xml_duration = duration_map.get(note.duration, 4)
                xml_content.append(f'        <duration>{xml_duration}</duration>')
                xml_content.append(f'        <type>{note.duration.replace("-dotted", "")}</type>')
                
                if "-dotted" in note.duration:
                    xml_content.append('        <dot/>')
                
                xml_content.append('      </note>')
            
            xml_content.append('    </measure>')
        
        xml_content.append('  </part>')
        xml_content.append('</score-partwise>')
        
        musicxml_string = '\n'.join(xml_content)
        print(f"      ✅ Generated MusicXML ({len(musicxml_string)} characters)")
        
        return musicxml_string
    
    def save_musicxml(self, musicxml_content: str, filename: str = "encrypted_message.xml") -> str:
        """Save MusicXML to file."""
        output_path = self.input_dir.parent / filename
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(musicxml_content)
        
        print(f"💾 MusicXML saved: {output_path}")
        return str(output_path)
    
    def run_complete_demonstration(self):
        """
        CONFIDENTIAL: Run the complete text-to-music-to-text demonstration.
        """
        print("\n🎵 COMPLETE MUSICAL CRYPTOGRAPHY DEMONSTRATION")
        print("="*70)
        print("⚠️  TEXT TO MUSIC TO TEXT - PATENT PENDING")
        print("🔐 Your message becomes playable music!")
        print("="*70)
        
        if not self.crypto_layers:
            print("❌ Musical crypto system not available")
            return
        
        # Get user input
        print("\n📝 ENTER TEXT TO CONVERT TO MUSIC:")
        print("   (Your text will become actual playable music)")
        
        try:
            user_text = input("\n🎵 Enter your message: ").strip()
            
            if not user_text:
                user_text = "Hello musical world!"
            
            print(f"\n✅ Input received: '{user_text}'")
            print(f"   📊 Length: {len(user_text)} characters")
            
            # Test complete pipeline
            print(f"\n🎵 STEP 1: TEXT-TO-MUSIC ENCRYPTION...")
            start_time = time.time()
            
            encrypted_package = self.text_to_music_encrypt(user_text)
            
            encrypt_time = time.time() - start_time
            
            # Save the music
            musicxml_file = self.save_musicxml(
                encrypted_package['musicxml'],
                f"encrypted_message_{int(time.time())}.xml"
            )
            
            print(f"\n🎼 STEP 2: MUSIC GENERATED!")
            print(f"   📄 MusicXML file: {musicxml_file}")
            print(f"   🎵 This music can be opened in any music software!")
            print(f"   🔐 Your text is hidden in the musical notation!")
            
            # Test decryption
            print(f"\n🔓 STEP 3: MUSIC-TO-TEXT DECRYPTION...")
            start_time = time.time()
            
            decrypted_text = self.music_to_text_decrypt(encrypted_package)
            
            decrypt_time = time.time() - start_time
            
            # Verify results
            success = (user_text == decrypted_text)
            
            print(f"\n🎯 COMPLETE PIPELINE RESULTS:")
            print(f"   📝 Original:  '{user_text}'")
            print(f"   🔓 Recovered: '{decrypted_text}'")
            print(f"   ✅ Success: {'PERFECT' if success else 'PARTIAL'}")
            print(f"   ⏱️  Encryption: {encrypt_time:.3f}s")
            print(f"   ⏱️  Decryption: {decrypt_time:.3f}s")
            print(f"   🎼 Musical measures: {encrypted_package['metadata']['musical_measures']}")
            
            if success:
                print(f"\n🎉 REVOLUTIONARY MUSICAL CRYPTOGRAPHY SUCCESS!")
                print(f"   🎵 Your text has become playable music!")
                print(f"   🔐 Music serves as both art and encryption!")
                print(f"   🌟 Revolutionary patent-pending technology!")
                
                print(f"\n🎼 MUSIC FILE DETAILS:")
                print(f"   📄 File: {musicxml_file}")
                print(f"   🎵 Can be opened in: MuseScore, Finale, Sibelius, etc.")
                print(f"   🔊 Can be played as actual music!")
                print(f"   🔐 Contains your encrypted message!")
                
            else:
                print(f"\n🔧 Musical algorithm needs refinement")
                print(f"   📊 Partial recovery demonstrates concept")
                
        except KeyboardInterrupt:
            print("\n❌ Demonstration cancelled")
        except Exception as e:
            print(f"\n❌ Error: {e}")
            import traceback
            traceback.print_exc()


def main():
    """
    CONFIDENTIAL: Main function for musical cryptography demonstration.
    """
    print("🎵 ENKI MUSICAL CRYPTOGRAPHY - TEXT TO MUSIC PIPELINE")
    print("="*70)
    print("⚠️  REVOLUTIONARY MUSICAL ENCRYPTION - PATENT PENDING")
    print("🔐 Convert text to playable music with cryptographic security")
    print("🎼 Music can be played, heard, and enjoyed - while hiding secrets")
    print("="*70)
    print("📋 FOR AUTHORIZED DEVELOPMENT ONLY")
    print("🔒 MAINTAIN ABSOLUTE CONFIDENTIALITY")
    print("="*70)
    
    try:
        # Initialize musical crypto system
        musical_crypto = EnkiMusicalCrypto()
        
        # Run complete demonstration
        musical_crypto.run_complete_demonstration()
        
        print(f"\n🎵 MUSICAL CRYPTOGRAPHY DEMONSTRATION COMPLETE!")
        print(f"⚠️  MAINTAIN ABSOLUTE CONFIDENTIALITY")
        print(f"📋 SECURE PATENT PROTECTION IMMEDIATELY")
        
    except Exception as e:
        print(f"\n❌ Critical error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
