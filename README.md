# Python Data Structures and Algorithms Examples
This repository contains Python data structures and algorithms examples. The examples are categorized into data structures and algorithms. Each category has its own subcategories. The examples are implemented in Python 3.7.4.

## How to measure the O(?) time complexity of an algorithm?
The time complexity of an algorithm is the total amount of time required by an algorithm to complete its execution. It is usually expressed by using the big O notation. The big O notation is used to describe the upper bound of an algorithm's time complexity. It is used to describe the worst-case scenario of an algorithm's time complexity.

### Rule 1
If an algorithm has a single loop that iterates through n elements, then the time complexity of the algorithm is O(n).

### Rule 2
If an algorithm has two nested loops, where the outer loop iterates through n elements and the inner loop iterates through m elements, then the time complexity of the algorithm is O(n * m).

### Rule 3
If an algorithm has two nested loops, where the outer loop iterates through n elements and the inner loop iterates through n elements, then the time complexity of the algorithm is O(n^2).

### Rule 4
 If an algorithm divides the input size by a constant factor at each step, then the time complexity of the algorithm is O(log n).

### Rule 5
If an algorithm has a recursive function that calls itself n times, then the time complexity of the algorithm is O(2^n).

### Rule 6
If an algorith has multiple statements that are executed sequentially, then the time complexity of the algorithm is the sum of the time complexities of each statement.
