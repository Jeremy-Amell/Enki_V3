# Enki V3 Archive Directory

This directory contains legacy files that are no longer actively used in the current Enki V3 pipeline but are preserved for historical reference and potential future use.

## Archived Files

### enki_class.py
- **Status**: Legacy version replaced by `enki_class_v2.py`
- **Last Active**: Pre-July 2025
- **Reason for Archive**: Superseded by refactored version with improved architecture
- **Description**: Original Enki class implementation
- **Dependencies**: None in current pipeline
- **Notes**: Contains original algorithm implementations that may be useful for reference

## Archive Policy

Files in this directory:
- Are not imported by any active code
- Are kept for historical reference and potential future use
- Should not be deleted without careful consideration
- May contain valuable algorithm implementations or design patterns

## Restoration

If you need to restore any archived file:
1. Copy (don't move) the file back to the main `src` directory
2. Update imports in relevant files if needed
3. Test thoroughly to ensure compatibility with current codebase

## Future Candidates

Other files that might be archived in the future:
- Any encoding modules not actively used (`encoding_*.py`)
- Old transformation implementations
- Deprecated utility functions
