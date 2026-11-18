# 04. AI Agents - Simple Agent with Goal, Tool, and Memory

class SimpleAgent:
    def __init__(self, goal):
        self.goal = goal
        self.memory = []

    def add_numbers(self, a, b):
        res = a + b
        self.memory.append(f"{a} + {b} = {res}")
        return res

if __name__ == "__main__":
    agent = SimpleAgent("Solve math tasks")
    print("Result:", agent.add_numbers(10, 15), "| Memory:", agent.memory)
