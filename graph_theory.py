from collections import deque

# Sample graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# DFS using recursion
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

print("DFS Traversal starting from A:")
dfs(graph, 'A')
print("\n")

# BFS using a queue
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")
            queue.extend([n for n in graph[vertex] if n not in visited])
    print()

print("BFS Traversal starting from A:")
bfs(graph, 'A')


"""
### 🧠 **Explain Like I’m 5 (ELI5)**

Imagine a bunch of **houses** (A, B, C, D, E, F), and **roads** connecting them.
This code is like a game where we want to **visit all the houses**, starting from house **A**.

There are **two ways to explore** the houses:

---

### 🐍 1. **DFS (Depth-First Search)** – "Go deep first"

It’s like this:

* Walk into the first neighbor.
* Then walk into their neighbor.
* And keep going **as far as you can**, even if you're going deep into one direction.
* If you can't go further, go back and try another road.

🧭 It’s like exploring a maze by going **down one path until you can't go further**, then turning back.

---

### 🚌 2. **BFS (Breadth-First Search)** – "Explore all nearby first"

It’s like this:

* Start at house A.
* Visit **all the houses next to A**.
* Then visit all the houses **next to those**, and so on.

🧭 It's like calling all your nearby friends first, then their friends next.

---

### 🖨 **What does the code print?**

```text
DFS Traversal starting from A:
A B D E F C 

BFS Traversal starting from A:
A B C D E F 
```

---

### 📋 **Summary of Output:**

| Type | Order of Visit        |
| ---- | --------------------- |
| DFS  | A → B → D → E → F → C |
| BFS  | A → B → C → D → E → F |

---

Explanation: DFS uses recursive calls to explore as deep as possible before backtracking; BFS uses a queue to explore neighbors level by level. Both techniques are fundamental in solving various graph-related problems.

"""