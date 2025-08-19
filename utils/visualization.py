"""
Visualization utilities for reinforcement learning experiments.

This module provides common plotting functions and visualization tools used across
different tutorials and assignments.
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from typing import List, Dict, Any, Optional, Tuple
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Set style for matplotlib
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class RLVisualizer:
    """A comprehensive visualizer for reinforcement learning experiments."""
    
    def __init__(self, figsize: Tuple[int, int] = (12, 8)):
        self.figsize = figsize
        self.colors = sns.color_palette("husl", 10)
        
    def plot_training_curves(self, 
                            rewards: List[float], 
                            losses: Optional[List[float]] = None,
                            epsilons: Optional[List[float]] = None,
                            title: str = "Training Progress",
                            save_path: Optional[str] = None) -> None:
        """
        Plot training curves including rewards, losses, and exploration.
        
        Args:
            rewards: List of episode rewards
            losses: List of training losses (optional)
            epsilons: List of exploration values (optional)
            title: Plot title
            save_path: Path to save the plot (optional)
        """
        fig, axes = plt.subplots(2 if losses else 1, 1, figsize=self.figsize)
        if not losses:
            axes = [axes]
            
        # Plot rewards
        axes[0].plot(rewards, color=self.colors[0], alpha=0.7, linewidth=1)
        axes[0].set_title(f"{title} - Episode Rewards")
        axes[0].set_xlabel("Episode")
        axes[0].set_ylabel("Reward")
        axes[0].grid(True, alpha=0.3)
        
        # Plot losses if provided
        if losses:
            axes[1].plot(losses, color=self.colors[1], alpha=0.7, linewidth=1)
            axes[1].set_title("Training Loss")
            axes[1].set_xlabel("Step")
            axes[1].set_ylabel("Loss")
            axes[1].grid(True, alpha=0.3)
            
        # Plot epsilon if provided
        if epsilons:
            ax2 = axes[0].twinx()
            ax2.plot(epsilons, color=self.colors[2], alpha=0.5, linewidth=1, linestyle='--')
            ax2.set_ylabel("Epsilon", color=self.colors[2])
            ax2.tick_params(axis='y', labelcolor=self.colors[2])
            
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
    def plot_learning_comparison(self, 
                                results: Dict[str, List[float]], 
                                title: str = "Algorithm Comparison",
                                window_size: int = 100,
                                save_path: Optional[str] = None) -> None:
        """
        Compare learning curves of different algorithms.
        
        Args:
            results: Dictionary mapping algorithm names to reward lists
            title: Plot title
            window_size: Size of moving average window
            save_path: Path to save the plot (optional)
        """
        plt.figure(figsize=self.figsize)
        
        for i, (name, rewards) in enumerate(results.items()):
            # Calculate moving average
            if len(rewards) >= window_size:
                moving_avg = np.convolve(rewards, np.ones(window_size)/window_size, mode='valid')
                episodes = np.arange(window_size-1, len(rewards))
            else:
                moving_avg = rewards
                episodes = np.arange(len(rewards))
                
            plt.plot(episodes, moving_avg, 
                    color=self.colors[i % len(self.colors)], 
                    label=name, linewidth=2, alpha=0.8)
            
        plt.title(title)
        plt.xlabel("Episode")
        plt.ylabel("Reward (Moving Average)")
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
    def plot_action_distribution(self, 
                                actions: List[int], 
                                action_names: Optional[List[str]] = None,
                                title: str = "Action Distribution",
                                save_path: Optional[str] = None) -> None:
        """
        Plot the distribution of actions taken by an agent.
        
        Args:
            actions: List of action indices
            action_names: Names for each action (optional)
            title: Plot title
            save_path: Path to save the plot (optional)
        """
        plt.figure(figsize=(10, 6))
        
        # Count actions
        unique_actions, counts = np.unique(actions, return_counts=True)
        
        if action_names:
            labels = [action_names[i] for i in unique_actions]
        else:
            labels = [f"Action {i}" for i in unique_actions]
            
        # Create bar plot
        bars = plt.bar(range(len(unique_actions)), counts, 
                      color=self.colors[:len(unique_actions)], alpha=0.7)
        
        # Add value labels on bars
        for bar, count in zip(bars, counts):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                    f'{count}', ha='center', va='bottom')
            
        plt.title(title)
        plt.xlabel("Actions")
        plt.ylabel("Count")
        plt.xticks(range(len(unique_actions)), labels, rotation=45)
        plt.grid(True, alpha=0.3, axis='y')
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
    def plot_state_visits(self, 
                          states: List[Tuple], 
                          state_names: Optional[List[str]] = None,
                          title: str = "State Visit Heatmap",
                          save_path: Optional[str] = None) -> None:
        """
        Create a heatmap of state visits.
        
        Args:
            states: List of state tuples
            state_names: Names for state dimensions (optional)
            title: Plot title
            save_path: Path to save the plot (optional)
        """
        if not states:
            print("No states provided for visualization")
            return
            
        # Convert states to numpy array
        states_array = np.array(states)
        
        if states_array.shape[1] != 2:
            print("State visualization currently supports 2D states only")
            return
            
        # Create 2D histogram
        plt.figure(figsize=(10, 8))
        
        # Determine bin edges
        x_bins = np.linspace(states_array[:, 0].min(), states_array[:, 0].max(), 50)
        y_bins = np.linspace(states_array[:, 1].min(), states_array[:, 1].max(), 50)
        
        # Create histogram
        H, xedges, yedges = np.histogram2d(states_array[:, 0], states_array[:, 1], 
                                          bins=[x_bins, y_bins])
        
        # Plot heatmap
        im = plt.imshow(H.T, origin='lower', extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]],
                       aspect='auto', cmap='viridis')
        
        plt.colorbar(im, label='Visit Count')
        plt.title(title)
        
        if state_names:
            plt.xlabel(state_names[0])
            plt.ylabel(state_names[1])
        else:
            plt.xlabel("State Dimension 1")
            plt.ylabel("State Dimension 2")
            
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
    def create_interactive_plot(self, 
                               rewards: List[float], 
                               title: str = "Interactive Training Progress") -> go.Figure:
        """
        Create an interactive plot using Plotly.
        
        Args:
            rewards: List of episode rewards
            title: Plot title
            
        Returns:
            Plotly figure object
        """
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            y=rewards,
            mode='lines',
            name='Episode Rewards',
            line=dict(color='blue', width=2),
            hovertemplate='Episode: %{x}<br>Reward: %{y:.2f}<extra></extra>'
        ))
        
        fig.update_layout(
            title=title,
            xaxis_title="Episode",
            yaxis_title="Reward",
            hovermode='x unified',
            template='plotly_white'
        )
        
        return fig

def plot_episode_rewards(rewards: List[float], 
                         title: str = "Episode Rewards",
                         save_path: Optional[str] = None) -> None:
    """Quick function to plot episode rewards."""
    visualizer = RLVisualizer()
    visualizer.plot_training_curves(rewards, title=title, save_path=save_path)

def plot_algorithm_comparison(results: Dict[str, List[float]], 
                             title: str = "Algorithm Comparison",
                             save_path: Optional[str] = None) -> None:
    """Quick function to compare algorithms."""
    visualizer = RLVisualizer()
    visualizer.plot_learning_comparison(results, title=title, save_path=save_path)
