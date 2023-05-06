
# Interval Tree with Graphical Display

This is a Python implementation of an interval tree data structure, along with a graphical display of the tree.

## Dependencies

The following Python libraries are required to run the code:

- matplotlib
- numpy

You can install them using pip:

```sh
pip install matplotlib numpy
```

## Usage

The code consists of two main files:

- `interval_tree.py`: Contains the implementation of the interval tree data structure and the function to display it graphically.
- `example.py`: Shows an example usage of the interval tree and the graphical display.

To use the interval tree, import the `IntervalTree` class from `interval_tree.py` and create an instance with a list of intervals:

```python
from interval_tree import IntervalTree, Interval

intervals = [
    Interval(0, 3, 'A'),
    Interval(1, 4, 'B'),
    Interval(2, 5, 'C'),
    Interval(6, 8, 'D'),
    Interval(7, 9, 'E'),
    Interval(10, 11, 'F')
]

tree = IntervalTree(intervals)
```

You can then use the `find` method to retrieve all intervals that intersect a given point:

```python
result = tree.find(3)
print(result)
```

To display the interval tree graphically, import the `display` function from `interval_tree.py` and pass the tree object:

```python
from interval_tree import display

display(tree)
```

This will open a window with the graphical representation of the interval tree:

![Interval Tree Graphical Display](https://i.imgur.com/RQUtX9g.png)

The red lines represent the intervals in the tree, and the black lines represent the boundaries of the nodes.

The `example.py` file shows a complete example of using the interval tree and the graphical display.

## License

This code is released under the MIT License.
