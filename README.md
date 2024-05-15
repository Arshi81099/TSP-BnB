
README - Traveling Salesman Problem (TSP) using Branch and Bound Algorithm

Overview
This repository contains an implementation of the Traveling Salesman Problem (TSP) using the Branch and Bound algorithm. The Traveling Salesman Problem is a classic problem in combinatorial optimization, where the task is to find the shortest possible route that visits each city exactly once and returns to the original city.

Implementation Details
The implementation is in Python, leveraging its simplicity and readability. The Branch and Bound algorithm is a systematic method for solving combinatorial optimization problems. It works by dividing the problem into smaller subproblems, evaluating each subproblem using a lower bound, and then recursively solving promising subproblems. This process continues until the optimal solution is found or all promising subproblems are eliminated.

Usage
Install Python: Make sure you have Python installed on your system. You can download it from python.org.

Clone the Repository: Clone this repository to your local machine using Git:

bash
Copy code
git clone https://github.com/Arshi81099/tsp-bnb.git
Navigate to the Directory: Enter the cloned repository directory:

bash
Copy code
cd tsp-bnb
Install Dependencies: Install the required dependencies using pip:

bash
Copy code
pip install -r requirements.txt
Run the Algorithm: Execute the Python script to run the Branch and Bound algorithm on the provided TSP instances:

bash
Copy code
python tsp_bnb.py
Input Data
The input data consists of a distance matrix representing the distances between cities. Each row and column in the matrix corresponds to a city, and the value at position (i, j) represents the distance from city i to city j. The matrix is symmetric, and the diagonal elements are typically set to infinity or zero.

Output
The output of the algorithm is the optimal tour that visits each city exactly once and returns to the original city, along with the total distance traveled.

Contributing
Contributions are welcome! If you find any bugs or want to improve the algorithm, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Special thanks to the contributors of the original Branch and Bound algorithm implementation, as well as the developers of the Python programming language and its scientific computing libraries.
