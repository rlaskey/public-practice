from random import randrange
import pytest


class Tree:
    def __init__(self, size: int):
        if size < 1:
            raise ValueError("size must be at least 1")

        self.root: None | "Node" = None

        values = range(size)
        stack: list[tuple[int, int]] = [(0, len(values) - 1)]
        while stack:
            left, right = stack.pop()
            if left > right:
                continue
            mid_point = (right + left) // 2
            value = values[mid_point]
            if self.root is None:
                self.root = Node(value)
            else:
                self.root.add(value)

            stack.append((left, mid_point - 1))
            stack.append((mid_point + 1, right))


class Node:
    def __str__(self, level=0, designation="") -> str:
        indent = " " * level * 2
        result = [
            f"{indent}{designation}{self.val} -- {self.size} nodes. level {level}"
        ]
        if self.left:
            result.append(self.left.__str__(level + 1, "L "))
        if self.right:
            result.append(self.right.__str__(level + 1, "R "))
        return "\n".join(result)

    def __init__(self, val: int):
        self.val: int = val
        self.left: None | "Node" = None
        self.right: None | "Node" = None
        self.size: int = 1

    def add(self, val):
        self.size += 1
        if val <= self.val:
            if self.left:
                self.left.add(val)
            else:
                self.left = Node(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = Node(val)

    def element_at_index(self, index) -> "Node":
        if index < 0:
            raise ValueError(f"index must be >= 0")
        if index > self.size - 1:
            raise ValueError(f"index must at most be {self.size - 1}")

        left_size = 0
        if self.left:
            left_size = self.left.size
            if left_size > index:
                return self.left.element_at_index(index)
        if left_size == index:
            return self
        if self.right:
            return self.right.element_at_index(index - left_size - 1)

        raise RuntimeError("not sure how we got here :(")

    def random_element(self) -> "Node":
        return self.element_at_index(randrange(self.size))


def test_trees():
    with pytest.raises(ValueError):
        Tree(-1)
    with pytest.raises(ValueError):
        Tree(-0)

    SIZE = 42
    x = Tree(SIZE)
    assert x.root is not None
    assert x.root.size is SIZE


def test_it():
    SIZE = 88
    tree = Tree(SIZE)
    root = tree.root
    assert root is not None
    assert root.element_at_index(SIZE - 1).val == 87

    for i in range(SIZE):
        assert root.element_at_index(i).val == i

    with pytest.raises(ValueError):
        root.element_at_index(SIZE)
    with pytest.raises(ValueError):
        root.element_at_index(-1)

    assert 0 <= root.random_element().val < SIZE
