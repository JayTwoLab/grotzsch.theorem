# Grotzsch's Theorem 

> [English](README.md) , [Korean](README.ko.md)

- **Grotzsch's Theorem** is a fundamental result in graph theory, particularly in the study of planar graphs and their colorability. 
- It states the following:

### Theorem:
**"Every triangle-free planar graph is 3-colorable."**

### Key Concepts:
1. **Triangle-free Graphs**:
   - A graph is triangle-free if it does not contain any cycles of length 3 (no subgraphs forming a triangle).

2. **3-colorable**:
   - A graph is 3-colorable if its vertices can be colored using at most three colors such that no two adjacent vertices share the same color.

3. **Planar Graphs**:
   - A planar graph can be drawn on a plane without any edges crossing.

### Explanation:
Grotzsch's Theorem guarantees that if a planar graph does not have any triangles, it can always be colored with three colors, regardless of the graph's size or complexity. This result is a refinement of the Four-Color Theorem, which asserts that every planar graph is 4-colorable, by imposing the additional restriction of being triangle-free.

### Importance:
- **Graph Coloring**:
  - The theorem provides insights into graph coloring problems, where the objective is to minimize the number of colors used to color a graph under certain constraints.

- **Applications**:
  - This result is used in areas such as map coloring, scheduling, and network design, where specific constraints need to be satisfied.

### Comparison to the Four-Color Theorem:
- While the Four-Color Theorem applies to all planar graphs, Grotzsch's Theorem reduces the maximum number of required colors to 3 for planar graphs without triangles. This demonstrates that removing small cycles (like triangles) simplifies the coloring problem.
