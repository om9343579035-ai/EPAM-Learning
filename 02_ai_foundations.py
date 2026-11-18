# 02. AI Foundations - Basic Linear Model Simulation

def predict(x, weight=2.0, bias=1.0):
    return (weight * x) + bias

if __name__ == "__main__":
    sample_input = 5
    print("Predicted Output:", predict(sample_input))
