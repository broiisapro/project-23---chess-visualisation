import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random

# Function to draw a sphere
def draw_sphere(ax, center, radius, color):
    u = np.linspace(0, 2 * np.pi, 50)  # Higher resolution for smoothness
    v = np.linspace(0, np.pi, 50)
    x = center[0] + radius * np.outer(np.cos(u), np.sin(v))
    y = center[1] + radius * np.outer(np.sin(u), np.sin(v))
    z = center[2] + radius * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color=color, shade=True, linewidth=0, antialiased=True)

# Function to draw a cylinder
def draw_cylinder(ax, base_center, radius, height, color):
    z = np.linspace(base_center[2], base_center[2] + height, 50)  # Smooth height
    theta = np.linspace(0, 2 * np.pi, 50)  # Smooth circumference
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = base_center[0] + radius * np.cos(theta_grid)
    y_grid = base_center[1] + radius * np.sin(theta_grid)
    ax.plot_surface(x_grid, y_grid, z_grid, color=color, shade=True, linewidth=0, antialiased=True)

# Function to draw a cone
def draw_cone(ax, base_center, radius, height, color):
    z = np.linspace(base_center[2], base_center[2] + height, 50)
    theta = np.linspace(0, 2 * np.pi, 50)
    x_grid = base_center[0] + (radius * (1 - z / height)) * np.outer(np.cos(theta), np.ones_like(z))
    y_grid = base_center[1] + (radius * (1 - z / height)) * np.outer(np.sin(theta), np.ones_like(z))
    z_grid = np.outer(np.ones_like(theta), z)
    ax.plot_surface(x_grid, y_grid, z_grid, color=color, shade=True, linewidth=0, antialiased=True)

# Functions to create chess pieces
def draw_king(ax, position, color):
    x, y = position
    draw_cylinder(ax, (x, y, 0.05), 0.15, 0.1, color)  # Base
    draw_cylinder(ax, (x, y, 0.15), 0.12, 0.3, color)  # Body
    draw_sphere(ax, (x, y, 0.45), 0.1, color)          # Top

def draw_queen(ax, position, color):
    x, y = position
    draw_cylinder(ax, (x, y, 0.05), 0.15, 0.1, color)  # Base
    draw_cylinder(ax, (x, y, 0.15), 0.12, 0.3, color)  # Body
    draw_sphere(ax, (x, y, 0.45), 0.08, color)         # Top
    draw_cone(ax, (x, y, 0.53), 0.08, 0.1, color)      # Crown

def draw_rook(ax, position, color):
    x, y = position
    draw_cylinder(ax, (x, y, 0.05), 0.15, 0.1, color)  # Base
    draw_cylinder(ax, (x, y, 0.15), 0.12, 0.3, color)  # Body
    draw_cylinder(ax, (x, y, 0.45), 0.13, 0.05, color) # Battlements

def draw_bishop(ax, position, color):
    x, y = position
    draw_cylinder(ax, (x, y, 0.05), 0.15, 0.1, color)  # Base
    draw_cylinder(ax, (x, y, 0.15), 0.12, 0.3, color)  # Body
    draw_cone(ax, (x, y, 0.45), 0.1, 0.15, color)      # Top

def draw_knight(ax, position, color):
    x, y = position
    draw_cylinder(ax, (x, y, 0.05), 0.15, 0.1, color)  # Base
    draw_cylinder(ax, (x, y, 0.15), 0.12, 0.3, color)  # Body
    draw_sphere(ax, (x, y, 0.45), 0.1, color)          # Head

def draw_pawn(ax, position, color):
    x, y = position
    draw_cylinder(ax, (x, y, 0.05), 0.12, 0.2, color)  # Base
    draw_sphere(ax, (x, y, 0.25), 0.08, color)         # Top

# Function to create the chessboard and place the pieces
def create_3d_chessboard_with_pieces():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    size = 8
    for i in range(size):
        for j in range(size):
            color = '#DDB88C' if (i + j) % 2 == 0 else '#3B7A57'  # Beige and green
            ax.bar3d(i, j, 0, 1, 1, 0.05, color=color, shade=True)

    piece_types = [draw_king, draw_queen, draw_rook, draw_bishop, draw_knight, draw_pawn]
    piece_positions = [(i, j) for i in range(size) for j in range(size)]
    random.shuffle(piece_positions)

    for idx, position in enumerate(piece_positions[:16]):
        piece_type = random.choice(piece_types)
        piece_color = 'black' if idx % 2 == 0 else 'white'
        piece_type(ax, (position[0] + 0.5, position[1] + 0.5), piece_color)

    ax.view_init(elev=60, azim=30)  # Adjusted elevation and angle
    ax.set_xlim([0, size])
    ax.set_ylim([0, size])
    ax.set_zlim([0, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

# Run the function
create_3d_chessboard_with_pieces()

