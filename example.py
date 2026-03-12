from cost_calculator import estimate_cost

model = "gpt-4"
tokens = 2000

cost = estimate_cost(model, tokens)

print("Model:", model)
print("Tokens:", tokens)
print("Estimated cost:", cost)
