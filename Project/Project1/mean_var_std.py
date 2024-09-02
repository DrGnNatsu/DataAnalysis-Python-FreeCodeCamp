import numpy as np


def calculate(number: list) -> dict:
    if len(number) != 9:
        raise ValueError("List must contain nine numbers.")

    my_dict = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }

    array = np.array(number).reshape(3, 3)

    for key, value in my_dict.items():
        if key == 'mean':
            value.append(array.mean(axis=0).tolist())
            value.append(array.mean(axis=1).tolist())
            value.append(float(array.mean()))
        if key == 'variance':
            value.append(array.var(axis=0).tolist())
            value.append(array.var(axis=1).tolist())
            value.append(float(array.var()))
        if key == 'standard deviation':
            value.append(array.std(axis=0).tolist())
            value.append(array.std(axis=1).tolist())
            value.append(float(array.std()))
        if key == 'max':
            value.append(array.max(axis=0).tolist())
            value.append(array.max(axis=1).tolist())
            value.append(float(array.max()))
        if key == 'min':
            value.append(array.min(axis=0).tolist())
            value.append(array.min(axis=1).tolist())
            value.append(float(array.min()))
        if key == 'sum':
            value.append(array.sum(axis=0).tolist())
            value.append(array.sum(axis=1).tolist())
            value.append(float(array.sum()))

    return my_dict


if __name__ == '__main__':
    print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
