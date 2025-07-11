# Enki V3 Tests Directory

This directory contains test files and development utilities for the Enki V3 project.

## Test Files

- **test_batch_export.py** - Tests for batch export functionality and multiple transformation processing
- **test_export_filenames.py** - Tests for file naming conventions and output file generation
- **test_mod_selection.py** - Tests for mod table selection interface and functionality
- **test_multi_selection.py** - Tests for multiple mod table selection and batch processing

## Running Tests

To run individual test files:
```bash
cd f:\Enki_V3\src\tests
python test_batch_export.py
python test_export_filenames.py
python test_mod_selection.py
python test_multi_selection.py
```

## Development Notes

These test files were created during development to validate specific functionality:
- Mod table selection and validation
- File naming with suffixes
- Batch processing workflows
- Export functionality

All main functionality is now integrated into the main `enki_pipeline.py` script.
