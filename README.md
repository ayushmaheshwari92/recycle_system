# Recycle Rewards System

## Overview
This is a simple command-line based automated collection and reward system for recyclable items. The system accepts items of types A, B, and C, and calculates rewards based on the item type.

## Reward Values
- Type A: INR 0.10
- Type B: INR 0.05
- Type C: INR 0.15

## Features
- Add items to the system.
- View the total reward accumulated.
- Reset the system for a new user session.

## Setup and Running the Project
1. Clone the repository:
    git clone <repository_link>
    cd recycle_rewards

2. Run the program:
    python main.py

## Code Structure
- `recycle_system.py`: Contains the `RecycleSystem` class which handles the core functionality of the system.
- `main.py`: Contains the command-line interface for user interaction.
- `README.md`: Provides an overview and setup instructions for the project.

## Assumptions and Design Decisions
- The item types are restricted to A, B, and C for simplicity.
- The reward values are predefined and fixed.
- The system uses a simple command-line interface for user interaction.
