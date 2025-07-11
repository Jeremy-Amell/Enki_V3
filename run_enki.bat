@echo off
REM Enki V3 Pipeline Runner
REM This batch file makes it easy to run the Enki pipeline on Windows

echo ================================================
echo           ENKI V3 Pipeline Runner
echo ================================================
echo.

REM Change to the src directory
cd /d "F:\Enki_V3\src"

REM Check if we're in the right directory
if not exist "example_usage.py" (
    echo ERROR: Cannot find example_usage.py
    echo Make sure you're running this from the correct directory
    pause
    exit /b 1
)

echo Current directory: %CD%
echo.

REM Check for command line argument
if "%1"=="" (
    echo Running FULL INTERACTIVE pipeline...
    echo You will be prompted for input during execution.
    echo.
    python example_usage.py
) else if "%1"=="test" (
    echo Running QUICK TEST mode...
    echo No user input required.
    echo.
    python example_usage.py test
) else if "%1"=="demo" (
    echo Running DEMONSTRATION mode...
    echo.
    python example_usage.py demo
) else if "%1"=="help" (
    echo.
    python example_usage.py help
) else (
    echo Unknown option: %1
    echo.
    echo Available options:
    echo   run_enki.bat          - Full interactive pipeline
    echo   run_enki.bat test     - Quick automated test
    echo   run_enki.bat demo     - Demonstrate flexibility
    echo   run_enki.bat help     - Show detailed help
)

echo.
echo ================================================
echo                  Execution Complete
echo ================================================
pause
