#!/bin/bash

# RL Robotics Course - uv Setup Script
# This script automates the installation of uv and project dependencies

set -e  # Exit on any error

echo "🤖 RL Robotics Course - Environment Setup"
echo "=========================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    echo "   Visit: https://www.python.org/downloads/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✅ Python $PYTHON_VERSION detected"

# Check if uv is already installed
if command -v uv &> /dev/null; then
    echo "✅ uv is already installed"
    UV_VERSION=$(uv --version)
    echo "   Version: $UV_VERSION"
else
    echo "📦 Installing uv..."
    
    # Install uv using the official installer
    if command -v curl &> /dev/null; then
        curl -LsSf https://astral.sh/uv/install.sh | sh
        echo "✅ uv installed successfully"
    else
        echo "❌ curl is not available. Please install curl or install uv manually:"
        echo "   pip install uv"
        exit 1
    fi
    
    # Add uv to PATH for current session
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# Create project directory if it doesn't exist
PROJECT_DIR="rl_robotics"
if [ ! -d "$PROJECT_DIR" ]; then
    echo "📁 Creating project directory: $PROJECT_DIR"
    uv init "$PROJECT_DIR"
else
    echo "✅ Project directory already exists: $PROJECT_DIR"
fi

cd "$PROJECT_DIR"

# Install dependencies
echo "📦 Installing project dependencies..."
uv pip install -r ../requirements.txt

echo ""
echo "🎉 Environment setup complete!"
echo ""
echo "Next steps:"
echo "1. Activate the virtual environment:"
echo "   source .venv/bin/activate"
echo ""
echo "2. Start with the first tutorial:"
echo "   jupyter notebook ../01_foundations/01_cartpole_q_learning.ipynb"
echo ""
echo "3. Happy learning! 🚀"
echo ""
echo "Note: If you're using Windows, activate the environment with:"
echo "   .venv\\Scripts\\activate"
