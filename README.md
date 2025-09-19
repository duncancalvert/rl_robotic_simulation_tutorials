# 🤖 Reinforcement Learning & Robotics Simulation Course

Welcome to an interactive journey through reinforcement learning (RL) with a focus on robotics applications! This repository is designed to take you from basic RL concepts to advanced deep reinforcement learning techniques using real-world robotics simulations.

<p align="center">
  <img src="media/lunar_lander_gif.gif?raw=true" alt="Lunar Lander" width="400"/>
</p>

## Course Summary

This course teaches reinforcement learning through hands-on experience with increasingly complex robotics environments. You'll start with simple control problems and progress to sophisticated robotic manipulation tasks, all while building a solid foundation in RL theory and practice.

---

## Prerequisites

- Basic Python programming
- Understanding of probability and statistics
- Familiarity with machine learning concepts (helpful but not required)
- Enthusiasm for robotics and AI!

---

### **Level 1: Foundations**
- **Classic Control Problems**: Master fundamental RL concepts with simple, interpretable environments
- **Tabular Methods**: Learn Q-learning and value iteration on discrete state spaces
- **Policy Methods**: Understand policy gradients and REINFORCE algorithms

### **Level 2: Deep Reinforcement Learning**
- **Neural Networks in RL**: Combine deep learning with reinforcement learning
- **Value-Based Methods**: Implement DQN, Double DQN, and Dueling DQN
- **Policy-Based Methods**: Master PPO, A2C, and actor-critic architectures

### **Level 3: Robotics Applications**
- **MuJoCo Environments**: Work with realistic physics simulations
- **Manipulation Tasks**: Learn robotic arm control and object manipulation
- **Multi-Agent Systems**: Explore coordination and competition in robotic teams

---

## Technical Requirements

- **Python 3.8+**
- **Gymnasium**: Modern RL environment library
- **MuJoCo**: High-performance physics simulator
- **PyTorch/TensorFlow**: Deep learning frameworks
- **Stable-Baselines3**: Production-ready RL implementations

## 🚀 Quick Start

### **Option 1: Automated Setup (Recommended)**

**macOS/Linux:**
```bash
# Clone the repository
git clone https://github.com/duncancalvert/rl_robotic_simulation_tutorials.git
cd rl_robotic_simulation_tutorials

# Run the automated setup script
./setup_uv.sh
```

**Windows:**
```cmd
# Clone the repository
git clone https://github.com/duncancalvert/rl_robotic_simulation_tutorials.git
cd rl_robotic_simulation_tutorials

# Run the automated setup script
setup_uv.bat
```

### **Option 2: Manual Setup**

```bash
# Clone the repository
git clone https://github.com/duncancalvert/rl_robotic_simulation_tutorials.git
cd rl_robotic_simulation_tutorials

# Install uv (modern Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv init rl_robotics
cd rl_robotics
uv pip install -r ../requirements.txt

# Activate the environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Start with the first tutorial
jupyter notebook ../01_foundations/01_cartpole_q_learning.ipynb
```

---

##  External Resources

### **Documentation**
- [Gymnasium](https://gymnasium.farama.org/): RL environment library
- [MuJoCo](https://mujoco.readthedocs.io/): Physics simulation
- [PyTorch](https://pytorch.org/docs/): Deep learning framework
- [Stable-Baselines3](https://stable-baselines3.readthedocs.io/): RL implementations

### **Research Papers** 📄
- **Foundations**: Sutton & Barto RL textbook
- **Deep RL**: DQN, PPO, SAC original papers
- **Robotics**: Sim-to-real transfer literature
- **Advanced**: Hierarchical RL, meta-learning papers

---

## 🤝 Contributing

This repository is designed for educational use. Feel free to:
- Report bugs or issues
- Suggest improvements
- Share your solutions and insights
- Create additional tutorials

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Gymnasium team for the RL environments
- DeepMind for MuJoCo physics simulator

---

