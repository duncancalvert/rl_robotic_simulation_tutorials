# 🚀 uv Quick Reference

This guide provides quick reference for common `uv` commands you'll use during the RL Robotics course.

## 📦 Installation

### **Install uv**
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
pip install uv

# Using Homebrew (macOS)
brew install uv
```

### **Verify Installation**
```bash
uv --version
```

## 🏗️ Project Management

### **Create New Project**
```bash
# Initialize a new project with virtual environment
uv init my_project
cd my_project

# Initialize in current directory
uv init .
```

### **Activate Virtual Environment**
```bash
# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### **Deactivate Environment**
```bash
deactivate
```

## 📚 Dependency Management

### **Install Dependencies**
```bash
# Install from requirements.txt
uv pip install -r requirements.txt

# Install specific package
uv pip install package_name

# Install with version constraint
uv pip install "package_name>=2.0.0"

# Install development dependencies
uv pip install --dev package_name
```

### **Install from pyproject.toml**
```bash
# Install all dependencies
uv sync

# Install with development dependencies
uv sync --dev

# Install with specific group
uv sync --group docs
```

### **Update Dependencies**
```bash
# Update specific package
uv pip install --upgrade package_name

# Update all packages
uv pip install --upgrade --upgrade-package all
```

### **Remove Dependencies**
```bash
# Remove package
uv pip uninstall package_name

# Remove multiple packages
uv pip uninstall package1 package2
```

## 🔍 Package Information

### **List Installed Packages**
```bash
# List all packages
uv pip list

# List packages in requirements format
uv pip freeze

# Show package info
uv pip show package_name
```

### **Check for Updates**
```bash
# Check outdated packages
uv pip list --outdated
```

## 🧪 Development Tools

### **Run Scripts**
```bash
# Run Python script in virtual environment
uv run python script.py

# Run with specific Python version
uv run --python 3.9 python script.py

# Run Jupyter notebook
uv run jupyter notebook

# Run tests
uv run pytest
```

### **Add Development Dependencies**
```bash
# Add to pyproject.toml
uv add --dev pytest black flake8

# Add specific version
uv add --dev "pytest>=7.0.0"
```

## 🐍 Python Version Management

### **Use Specific Python Version**
```bash
# Create environment with specific Python version
uv init --python 3.9 my_project

# Run with specific Python version
uv run --python 3.9 python script.py
```

### **List Available Python Versions**
```bash
uv python list
```

## 🔧 Advanced Features

### **Lock File Management**
```bash
# Generate lock file
uv lock

# Install from lock file
uv sync --frozen
```

### **Export Requirements**
```bash
# Export to requirements.txt
uv pip freeze > requirements.txt

# Export with hashes
uv pip freeze --exclude-editable --generate-hashes > requirements.txt
```

### **Clean Environment**
```bash
# Remove virtual environment
rm -rf .venv

# Recreate environment
uv init .
uv sync
```

## 📋 Common Course Commands

### **Setup Course Environment**
```bash
# Clone and setup
git clone https://github.com/duncancalvert/rl_robotic_simulation_tutorials.git
cd rl_robotic_simulation_tutorials
./setup_uv.sh  # macOS/Linux
# or
setup_uv.bat   # Windows
```

### **Install Course Dependencies**
```bash
# From course root
uv pip install -r requirements.txt

# Or use the pyproject.toml
uv sync
```

### **Run Jupyter Notebooks**
```bash
# Activate environment first
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows

# Start Jupyter
jupyter notebook

# Or use uv run
uv run jupyter notebook
```

### **Install Additional Packages**
```bash
# For specific tutorials
uv pip install gymnasium[atari]
uv pip install robosuite

# For development
uv add --dev ipywidgets plotly
```

## 🚨 Troubleshooting

### **Common Issues**

#### **Permission Denied**
```bash
# Fix permissions
chmod +x setup_uv.sh
```

#### **uv Command Not Found**
```bash
# Add to PATH (macOS/Linux)
export PATH="$HOME/.cargo/bin:$PATH"

# Or restart terminal after installation
```

#### **Package Installation Fails**
```bash
# Clear cache and retry
uv cache clean
uv pip install package_name

# Check Python version compatibility
uv python list
```

#### **Virtual Environment Issues**
```bash
# Remove and recreate
rm -rf .venv
uv init .
uv sync
```

## 💡 Tips & Best Practices

1. **Always activate your virtual environment** before working
2. **Use `uv sync`** when you have a `pyproject.toml` file
3. **Use `uv run`** to run commands in the virtual environment
4. **Keep your lock file** for reproducible builds
5. **Use development dependencies** for tools like testing and linting

## 🔗 Additional Resources

- [uv Documentation](https://docs.astral.sh/uv/)
- [uv GitHub Repository](https://github.com/astral-sh/uv)
- [uv vs pip Comparison](https://docs.astral.sh/uv/getting-started/installation.html#why-uv)

---

**Happy coding with uv!** 🚀✨
