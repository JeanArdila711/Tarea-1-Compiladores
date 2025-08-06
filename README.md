# Tarea 1 - DFA Minimization

## Student Information

- **Full name:** Jean Carlo Ardila Acevedo - Andrés Felipe Giraldo Restrepo
- **Class Number:** 3952

## Technical Information

- **Operating System:** Windows 11
- **Programming Language:** Python 3.13.5
- **Tools Used:**
    - **Visual Studio Code:** Code editor to write and debug the program
    - **GitHub Classroom:** To submit the code
    - **Git:** For version control and upload to the repository.

## How to Run the Code

1. **Clone the repository**
2. **Run the program:** python main.py
3. Enter input following the given format
4. The program will output the equivalent states in lexicographic order.

---


## Code Explication

The code implements the Kozen based DFA minimization algorithm of reading 14, eliminating redundant states and reducing the size of the automaton without changing its behavior.

The program follows three main steps:

1. **leer_dfa()- Read DFA from the input**
    - Reads the DFA from the input and sotres it in variables
    - Uses set() for the final states
    - Stores the transitions table in a list of lists.

2. **minimizar_dfa() - DFA Minimization Algorithm**
    - Creates an array of **False(distinguished[i][j])**, where **True** indicates that two states are different.
    - Mark as distinct states where one is final and the other is not.
    - Propagaets distinction: If (p,q) has transitions to (r,s) and (r,s) are already marked as distinct, then (p,q) is also marked as distinct.
    - The states left with **False** are equivalent can be merged.

3. **main() - Handling multiple test cases**
    - Read **c**, the number of DFAs to process
    - For each DFA, executes leer_dfa() and minimizar_dfa().
    - Sort and display the equivalent states in lexicographic order.