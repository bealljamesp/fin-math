# Use it when: You want to implement Function Overloading based on the data type of the first argument.

# Instead of writing messy if isinstance(data, list): or elif isinstance(data, np.ndarray): syntax inside a single function, singledispatch modularizes your code into clean, type-specific variations.import functools

import numpy as np


@functools.singledispatch
def process_cost_data(data: any) -> None:
    raise TypeError("Unsupported data type passed to audit pipeline.")


@process_cost_data.register(list)
def _(data: list) -> None:
    print(f"Processing standard Python list of size: {len(data)}")


@process_cost_data.register(np.ndarray)
def _(data: np.ndarray) -> None:
    print(f"Processing optimized NumPy C-array with shape: {data.shape}")


# Execution
process_cost_data([10, 20, 30])  # Automatically maps to the list variant
process_cost_data(np.array([10, 20]))  # Automatically maps to the NumPy variant
