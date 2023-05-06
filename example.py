from intervaltree import Interval, IntervalTree
from graphviz import Digraph

# Create the interval tree
tree = IntervalTree()
tree.add(Interval(1, 5, "Interval 1"))
tree.add(Interval(3, 8, "Interval 2"))
tree.add(Interval(6, 10, "Interval 3"))
tree.add(Interval(9, 12, "Interval 4"))
tree.add(Interval(11, 15, "Interval 5"))

# Display the interval tree graphically
dot = Digraph()
for interval in tree:
    dot.node(str(id(interval)), label=f"[{interval.begin}, {interval.end}): {interval.data}")
    if interval.parent is not None:
        dot.edge(str(id(interval.parent)), str(id(interval)))
dot.render("interval_tree.gv", view=True)
