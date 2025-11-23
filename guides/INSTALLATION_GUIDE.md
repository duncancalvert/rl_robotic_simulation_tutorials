# Install Guide

This guide will help you set up your environment for the RL course.

### **Python Version**
- **Python**: 3.9+ (3.12 recommended, don't use Python 3.13+)
- **Package Manager**: uv (recommended) or conda/pip

## Quick Start (Recommended)

### **Option 1: Using uv (Recommended)**

```bash
# Install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or using pip:
pip install uv

# Create a virtual environment
uv venv --python 3.12

# Install dependencies
uv pip install -r requirements.txt
```

### **Option 2: Using Conda (Alternative)**

```bash
# Install Miniconda if you don't have it
# Download from: https://docs.conda.io/en/latest/miniconda.html

# Create a new conda environment
conda create -n rl_robotics python=3.9
conda activate rl_robotics

# Install PyTorch (choose appropriate version for your system)
# For CPU only:
conda install pytorch torchvision torchaudio cpuonly -c pytorch

# For CUDA (if you have NVIDIA GPU):
# conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

# Install other dependencies
pip install -r requirements.txt
```

### **Option 3: Using pip with Virtual Environment**

```bash
# Create a virtual environment
python -m venv rl_robotics
source rl_robotics/bin/activate  # On Windows: rl_robotics\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 📦 Detailed Installation Steps

### **Step 1: Install Python**

#### **macOS**
```bash
# Using Homebrew (recommended)
brew install python@3.9

# Or download from python.org
# https://www.python.org/downloads/macos/
```

#### **Ubuntu**
```bash
sudo apt update
sudo apt install python3.9 python3.9-venv python3.9-pip
```

#### **Windows**
- Download Python from [python.org](https://www.python.org/downloads/)
- Make sure to check "Add Python to PATH" during installation

### **Step 2: Install uv (Recommended Package Manager)**

#### **macOS/Linux**
```bash
# Using curl (recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or using pip
pip install uv

# Or using Homebrew
brew install uv
```

#### **Windows**
```bash
# Using pip
pip install uv

# Or download from GitHub releases
# https://github.com/astral-sh/uv/releases
```

### **Step 3: Install MuJoCo**

#### **macOS**
```bash
# Install MuJoCo
brew install mujoco

# Set environment variables
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib' >> ~/.zshrc
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib' >> ~/.bash_profile
```

#### **Ubuntu**
```bash
# Download MuJoCo
wget https://github.com/deepmind/mujoco/releases/download/2.3.0/mujoco-2.3.0-linux-x86_64.tar.gz

# Extract to /opt
sudo tar -xf mujoco-2.3.0-linux-x86_64.tar.gz -C /opt

# Set environment variables
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/mujoco-2.3.0/bin' >> ~/.bashrc
echo 'export MUJOCO_PATH=/opt/mujoco-2.3.0' >> ~/.bashrc
```

#### **Windows**
- Download MuJoCo from [GitHub releases](https://github.com/deepmind/mujoco/releases)
- Extract to `C:\mujoco`
- Add `C:\mujoco\bin` to your PATH environment variable

### **Step 4: Install Deep Learning Framework**

#### **PyTorch (Recommended)**
```bash
# Using uv (recommended)
uv pip install torch torchvision torchaudio

# Using pip
pip install torch torchvision torchaudio

# CUDA support (if you have NVIDIA GPU)
# uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

#### **TensorFlow (Alternative)**
```bash
# Using uv
uv pip install tensorflow

# Using pip
pip install tensorflow

# GPU support
# uv pip install tensorflow[gpu]
```

### **Step 5: Install Core Dependencies**

```bash
# Using uv (recommended)
uv pip install gymnasium[all]
uv pip install stable-baselines3
uv pip install sb3-contrib

# Install scientific computing packages
uv pip install numpy scipy pandas matplotlib seaborn

# Install Jupyter and interactive tools
uv pip install jupyter notebook ipywidgets

# Or using pip
pip install gymnasium[all]
pip install stable-baselines3
pip install sb3-contrib
pip install numpy scipy pandas matplotlib seaborn
pip install jupyter notebook ipywidgets
```

### **Step 6: Install Additional Tools**

```bash
# Using uv (recommended)
uv pip install plotly
uv pip install wandb tensorboard
uv pip install pybullet robosuite

# Or using pip
pip install plotly
pip install wandb tensorboard
pip install pybullet robosuite
```

## 🔧 Troubleshooting

### **Common Issues**

#### **uv Installation Problems**
```bash
# Check if uv is properly installed
uv --version

# If you get errors, try:
pip uninstall uv
pip install uv --upgrade
```

#### **MuJoCo Installation Problems**
```bash
# Check if MuJoCo is properly installed
python -c "import mujoco; print('MuJoCo installed successfully')"

# If you get errors, try:
uv pip uninstall mujoco
uv pip install mujoco --no-cache-dir
```

#### **Gymnasium Environment Issues**
```bash
# Test basic gymnasium installation
python -c "import gymnasium as gym; env = gym.make('CartPole-v1'); print('Gymnasium working')"

# If you get errors, try:
uv pip install gymnasium[all] --upgrade
```

#### **PyTorch CUDA Issues**
```bash
# Check PyTorch CUDA support
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"

# If CUDA is not available, reinstall PyTorch with CUDA support
uv pip uninstall torch torchvision torchaudio
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### **Environment Variable Issues**

#### **macOS/Linux**
```bash
# Check environment variables
echo $LD_LIBRARY_PATH
echo $MUJOCO_PATH

# If empty, add them manually
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
export MUJOCO_PATH=/usr/local
```

#### **Windows**
```cmd
# Check environment variables
echo %PATH%

# Add MuJoCo to PATH manually in System Properties > Environment Variables
```

## 🧪 Testing Your Installation

Create a test script to verify everything is working:

```python
# test_installation.py
import sys
print(f"Python version: {sys.version}")

try:
    import gymnasium as gym
    print("✓ Gymnasium installed")
    
    env = gym.make('CartPole-v1')
    print("✓ Basic environment working")
    
    import torch
    print(f"✓ PyTorch installed (CUDA: {torch.cuda.is_available()})")
    
    import mujoco
    print("✓ MuJoCo installed")
    
    import stable_baselines3
    print("✓ Stable-Baselines3 installed")
    
    print("\n🎉 All packages installed successfully!")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Please check your installation")
```

Run the test:
```bash
# Using uv
uv run python test_installation.py

# Or activate environment first
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
python test_installation.py
```

## 📚 Additional Resources

### **Documentation**
- [uv Documentation](https://docs.astral.sh/uv/)
- [Gymnasium Documentation](https://gymnasium.farama.org/)
- [MuJoCo Documentation](https://mujoco.readthedocs.io/)
- [PyTorch Documentation](https://pytorch.org/docs/)
- [Stable-Baselines3 Documentation](https://stable-baselines3.readthedocs.io/)

### **Community Support**
- [Course Discussion Forum](link-to-forum)
- [GitHub Issues](link-to-repo-issues)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/reinforcement-learning)

### **Getting Help**
If you encounter issues:

1. **Check the troubleshooting section above**
2. **Search existing issues** in the course repository
3. **Ask in the course discussion forum**
4. **Create a detailed issue** with error messages and system info

## 🚀 Next Steps

After successful installation:

1. **Clone the course repository**
2. **Navigate to the first tutorial**
3. **Start with Level 1: Foundations**
4. **Join the course community**

---

**Happy coding!** 🎉

If you have any installation issues, don't hesitate to ask for help in the course community.
