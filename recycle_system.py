class RecycleSystem:
    REWARD_VALUES = {
        'A': 0.10,
        'B': 0.05,
        'C': 0.15
    }

    def __init__(self):
        self.items = {'A': 0, 'B': 0, 'C': 0}
        self.total_reward = 0.0

    def add_item(self, item_type):
        if item_type in self.REWARD_VALUES:
            self.items[item_type] += 1
            self.total_reward += self.REWARD_VALUES[item_type]
            return f"Item {item_type} added successfully."
        else:
            return f"Invalid item type: {item_type}. Please use A, B, or C."

    def get_total_reward(self):
        return self.total_reward

    def reset_system(self):
        self.items = {'A': 0, 'B': 0, 'C': 0}
        self.total_reward = 0.0
        return "System reset successfully."
