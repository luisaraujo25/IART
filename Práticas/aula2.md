## Breadth-First Search 
Strategy: Nodes at lowest depth are expanded first.

## Depth-First Search
Strategy: Always expand one of the deepest nodes in the tree.

## Uniform Cost Search
Strategy: Always expand the border node with the lowest cost (measured by the solution cost function).
Cost is not h.
Soma do caminho todo.

## Greedy Search
Strategy: Expand the node that appears to be closest to the solution.

## A* Algorithm Search
The A * algorithm combines the greedy with the uniform search
minimizing the sum of the path already carried out with the minimum
expected until the solution.
Soma o path todo.

<br>


# Exercícios

## 2.1

a) C <br>
b) E <br>
c) D <br>
d) C <br>
e) G <br>

## 2.2

a)

State representation -> B[3][3] = B[N][N]
(Xs,Ys)

Initial state -> 0 position

Cost -> Number of moves to get to the correct position.

Heuristic -> Number of pieces out of place

Objective state:

1 2 3

4 5 6

7 8 0

Conditions for a play:
- A piece can be moved to an adjacent spot
- The spot where the piece is moved must be empty

| Operators | Precondition | Effect                  | Cost |
| --------- | ------------ | ----------------------- | ---- |
| up        | Ys>1         | B[Xs][Ys] = B[Xs][Ys-1] | 1    |
| down      | Ys<3         | B[Xs][Ys] = B[Xs][Ys+1] | 1    |
| left      | Xs>1         | B[Xs][Ys] = B[Xs-1][Ys] | 1    |
| right     | Xs<3         | B[Xs][Ys] = B[Xs+1][Ys] | 1    |


https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/
https://www.101computing.net/breadth-first-traversal-of-a-binary-tree/
