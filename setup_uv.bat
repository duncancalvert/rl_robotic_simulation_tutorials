@echo off
REM RL Robotics Course - uv Setup Script for Windows
REM This script automates the installation of uv and project dependencies

echo 🤖 RL Robotics Course - Environment Setup
echo ==========================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH. Please install Python 3.8+ first.
    echo    Visit: https://www.python.org/downloads/
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ Python %PYTHON_VERSION% detected

REM Check if uv is already installed
uv --version >nul 2>&1
if errorlevel 1 (
    echo 📦 Installing uv...
    
    REM Install uv using pip
    pip install uv
    if errorlevel 1 (
        echo ❌ Failed to install uv. Please install manually:
        echo    pip install uv
        pause
        exit /b 1
    )
    echo ✅ uv installed successfully
) else (
    echo ✅ uv is already installed
    for /f "tokens=2" %%i in ('uv --version 2^>^&1') do set UV_VERSION=%%i
    echo    Version: %UV_VERSION%
)

REM Create project directory if it doesn't exist
set PROJECT_DIR=rl_robotics
if not exist "%PROJECT_DIR%" (
    echo 📁 Creating project directory: %PROJECT_DIR%
    uv init %PROJECT_DIR%
) else (
    echo ✅ Project directory already exists: %PROJECT_DIR%
)

cd %PROJECT_DIR%

REM Install dependencies
echo 📦 Installing project dependencies...
uv pip install -r ..\requirements.txt

echo.
echo 🎉 Environment setup complete!
echo.
echo Next steps:
echo 1. Activate the virtual environment:
echo    .venv\Scripts\activate
echo.
echo 2. Start with the first tutorial:
echo    jupyter notebook ..\01_foundations\01_cartpole_q_learning.ipynb
echo.
echo 3. Happy learning! 🚀
echo.
pause
