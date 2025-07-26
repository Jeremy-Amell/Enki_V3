# Enki V3 Pipeline Runner - PowerShell Version
# This PowerShell script makes it easy to run the Enki pipeline

param(
    [string]$Mode = ""
)

Write-Host "================================================" -ForegroundColor Cyan
Write-Host "           ENKI V3 Pipeline Runner" -ForegroundColor Cyan
Write-Host "              (PowerShell Version)" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host

# Change to the src directory
Write-Host "Changing to src directory..." -ForegroundColor Yellow
Set-Location "F:\Enki_V3\src"
Write-Host "Current directory: $(Get-Location)" -ForegroundColor Green

# Check if we're in the right directory
if (-not (Test-Path "enki_batch.py")) {
    Write-Host "ERROR: Cannot find enki_batch.py" -ForegroundColor Red
    Write-Host "Make sure you're running this from the correct directory" -ForegroundColor Red
    Write-Host "Looking for Python files in current directory:" -ForegroundColor Yellow
    Get-ChildItem *.py | ForEach-Object { Write-Host "  - $($_.Name)" }
    Write-Host
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "Found enki_batch.py - proceeding..." -ForegroundColor Green
Write-Host

# Check if Python is available
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Python found: $pythonVersion" -ForegroundColor Green
    } else {
        throw "Python not found"
    }
} catch {
    Write-Host "ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python or add it to your PATH" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host

# Execute based on mode
$pythonExitCode = 0

switch ($Mode.ToLower()) {
    "" {
        Write-Host "Running FULL INTERACTIVE pipeline..." -ForegroundColor Cyan
        Write-Host "You will be prompted for input during execution." -ForegroundColor Yellow
        Write-Host
        Write-Host "Executing: python enki_batch.py" -ForegroundColor Magenta
        python enki_batch.py
        $pythonExitCode = $LASTEXITCODE
    }
    "test" {
        Write-Host "Running QUICK TEST mode..." -ForegroundColor Cyan
        Write-Host "No user input required." -ForegroundColor Yellow
        Write-Host
        Write-Host "Executing: python enki_batch.py test" -ForegroundColor Magenta
        python enki_batch.py test
        $pythonExitCode = $LASTEXITCODE
    }
    "demo" {
        Write-Host "Running DEMONSTRATION mode..." -ForegroundColor Cyan
        Write-Host
        Write-Host "Executing: python enki_batch.py demo" -ForegroundColor Magenta
        python enki_batch.py demo
        $pythonExitCode = $LASTEXITCODE
    }
    "help" {
        Write-Host "Executing: python enki_batch.py help" -ForegroundColor Magenta
        python enki_batch.py help
        $pythonExitCode = $LASTEXITCODE
    }
    default {
        Write-Host "Unknown option: $Mode" -ForegroundColor Red
        Write-Host
        Write-Host "Available options:" -ForegroundColor Yellow
        Write-Host "  .\run_enki.ps1          - Full interactive pipeline"
        Write-Host "  .\run_enki.ps1 test     - Quick automated test"
        Write-Host "  .\run_enki.ps1 demo     - Demonstrate flexibility"
        Write-Host "  .\run_enki.ps1 help     - Show detailed help"
        $pythonExitCode = 1
    }
}

Write-Host
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "                  Execution Complete" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan

if ($pythonExitCode -eq 0) {
    Write-Host "Status: SUCCESS" -ForegroundColor Green
} else {
    Write-Host "Status: FAILED with exit code $pythonExitCode" -ForegroundColor Red
    Write-Host
    Write-Host "If you're seeing errors, check that all required files exist:" -ForegroundColor Yellow
    Write-Host "- enki_class_v2.py"
    Write-Host "- alpha_transformer.py"
    Write-Host "- phorms_mod_table.py"
}

Write-Host
Write-Host "Press Enter to close this window..." -ForegroundColor Yellow
Read-Host
    
 
