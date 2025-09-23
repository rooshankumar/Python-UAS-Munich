from typing import List, Dict, Tuple

# Variable annotations
n: int = 5
name: str = "Alice"

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Dictionary with string keys and integer values
student_scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# Tuple of (string, int)
person: Tuple[str, int] = ("Charlie", 25)

# Function with type hints
def add(a: int, b: int) -> int:
    return a + b

# Usage
print(n)                 # 5
print(name)              # Alice
print(numbers)           # [1, 2, 3, 4, 5]
print(student_scores)    # {'Alice': 90, 'Bob': 85}
print(person)            # ('Charlie', 25)
print(add(10, 20))       # 30
