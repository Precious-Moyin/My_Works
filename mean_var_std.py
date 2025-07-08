import numpy as np

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers")  

    new_array = np.array(input_list).reshape(3, 3)
    print(new_array)  

    calculations = {
        "mean": [
            new_array.mean(axis=0).tolist(), 
            new_array.mean(axis=1).tolist(), 
            new_array.mean().item()],
        "variance": [
            new_array.var(axis=0).tolist(), 
            new_array.var(axis=1).tolist(), 
            new_array.var().item()],
        "standard deviation": [
            new_array.std(axis=0).tolist(), 
            new_array.std(axis=1).tolist(), 
            new_array.std().item()],
        "max": [
            new_array.max(axis=0).tolist(), 
            new_array.max(axis=1).tolist(), 
            new_array.max().item()],
        "min": [
            new_array.min(axis=0).tolist(), 
            new_array.min(axis=1).tolist(), 
            new_array.min().item()],
        "sum": [
            new_array.sum(axis=0).tolist(), 
            new_array.sum(axis=1).tolist(), 
            new_array.sum().item()]
    }

    return calculations

result = calculate(input_list)
print(result)