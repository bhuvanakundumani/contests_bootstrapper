from typing import Any, Optional


class Node:
    def __init__(self, value: Any):
        self._value = value
        self._left = None
        self._right = None

    def __str__(self) -> str:
        return f'<{self.left} - {self.value} - {self.right}>'

    @property
    def value(self) -> Any:
        return self._value

    @property
    def left(self) -> 'Node':
        return self._left

    @property
    def right(self) -> 'Node':
        return self._right

    @value.setter
    def value(self, value) -> None:
        self._value = value

    @left.setter
    def left(self, value) -> None:
        self._left = value

    @right.setter
    def right(self, value) -> None:
        self._right = value


class BinaryTree:
    def __init__(self):
        self._root = None

    def _add(self, value: Any, node: Node) -> None:
        if value < node.value:
            if not node.left:
                node.left = Node(value)
            else:
                self._add(value, node.left)
        else:
            if not node.right:
                node.right = Node(value)
            else:
                self._add(value, node.right)

    def _clear(self, node: Node) -> None:
        node.value = None
        if node.left:
            self._clear(node.left)
        if node.right:
            self._clear(node.right)

    def _find(self, value: Any, node: Node) -> Optional[Node]:
        if node.value == value:
            return node
        elif value < node.value:
            if not node.left:
                return None
            return self._find(value, node.left)
        else:
            if not node.right:
                return None
            return self._find(value, node.right)

    def _print(self, node: Node, prefix: str) -> None:
        prefix += f'{node.value}/'
        print(prefix)
        if node.left:
            self._print(node.left, prefix)
        if node.right:
            self._print(node.right, prefix)

    def add(self, value: Any) -> None:
        if not self._root:
            self._root = Node(value)
        else:
            self._add(value, self._root)

    def clear(self) -> None:
        self._clear(self._root)
        self._root = None

    def find(self, value: Any) -> Optional[Node]:
        if not self._root:
            return None
        return self._find(value, self._root)

    def print(self) -> None:
        if self._root:
            self._print(self._root, prefix='')
        else:
            print('<empty>')

    @property
    def root(self) -> Node:
        return self._root


if __name__ == '__main__':
    t = BinaryTree()
    t.add(5)
    t.add(7)
    t.add(3)
    t.add(21)
    t.add(4)
    t.add(1)
    t.add(2)
    t.add(11)
    print('\nTree:')
    t.print()

    print('\nFinding 4; 11; -1 (non-existent):')
    print(t.find(4))
    print(t.find(11))
    print(t.find(-1))

    print('\nCleared tree:')
    t.clear()
    t.print()
