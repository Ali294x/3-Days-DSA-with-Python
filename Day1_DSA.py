"""Day 1: Arrays + core data structures used heavily in DSA."""

from collections import Counter, deque
from heapq import heappop, heappush
from itertools import accumulate


# ------------------------------
# Array problems (existing Day 1)
# ------------------------------
def build_prefix_sums(numbers: list[int]) -> list[int]:
    """Return the running sum at each position."""
    return list(accumulate(numbers))


def range_sum(prefix_sums: list[int], start: int, end: int) -> int:
    """Return the inclusive range sum using a prefix-sum array."""
    before_start = prefix_sums[start - 1] if start > 0 else 0
    return prefix_sums[end] - before_start


def apply_range_updates(
    size: int, updates: list[tuple[int, int, int]]
) -> list[int]:
    """Apply inclusive range additions in O(size + len(updates)) time."""
    difference = [0] * (size + 1)

    for start, end, value in updates:
        difference[start] += value
        difference[end + 1] -= value

    result: list[int] = []
    current = 0
    for value in difference[:size]:
        current += value
        result.append(current)
    return result


def subarray_sum_count(numbers: list[int], target: int) -> int:
    """Count contiguous subarrays whose sum equals target."""
    prefix_frequency = Counter({0: 1})
    prefix_sum = 0
    count = 0

    for number in numbers:
        prefix_sum += number
        count += prefix_frequency[prefix_sum - target]
        prefix_frequency[prefix_sum] += 1

    return count


def search_rotated(numbers: list[int], target: int) -> int:
    """Return target's index in a rotated sorted array, or -1 if absent."""
    left, right = 0, len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] == target:
            return middle

        if numbers[left] <= numbers[middle]:
            if numbers[left] <= target < numbers[middle]:
                right = middle - 1
            else:
                left = middle + 1
        elif numbers[middle] < target <= numbers[right]:
            left = middle + 1
        else:
            right = middle - 1

    return -1


# ------------------------------
# Stack
# ------------------------------
class Stack:
    """LIFO data structure."""

    def __init__(self) -> None:
        self.items: list[int] = []

    def push(self, value: int) -> None:
        self.items.append(value)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)


# ------------------------------
# Queue
# ------------------------------
class Queue:
    """FIFO data structure."""

    def __init__(self) -> None:
        self.items = deque()

    def enqueue(self, value: int) -> None:
        self.items.append(value)

    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)


# ------------------------------
# Priority Queue (min-heap)
# ------------------------------
class PriorityQueue:
    """A min-priority queue using a heap."""

    def __init__(self) -> None:
        self.heap: list[int] = []

    def push(self, value: int) -> None:
        heappush(self.heap, value)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return heappop(self.heap)

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return self.heap[0]

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def size(self) -> int:
        return len(self.heap)


# ------------------------------
# Tree structure
# ------------------------------
class TreeNode:
    """A node in a binary tree."""

    def __init__(self, value: int):
        self.value = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class BinaryTree:
    """Binary search tree with insert, traversal, search and BFS support."""

    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def insert(self, value: int) -> None:
        new_node = TreeNode(value)

        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, target: int) -> bool:
        current = self.root
        while current is not None:
            if target == current.value:
                return True
            if target < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def inorder(self, node: TreeNode | None = None) -> list[int]:
        if node is None:
            node = self.root
        if node is None:
            return []
        return self.inorder(node.left) + [node.value] + self.inorder(node.right)

    def preorder(self, node: TreeNode | None = None) -> list[int]:
        if node is None:
            node = self.root
        if node is None:
            return []
        return [node.value] + self.preorder(node.left) + self.preorder(node.right)

    def postorder(self, node: TreeNode | None = None) -> list[int]:
        if node is None:
            node = self.root
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.value]

    def bfs(self) -> list[int]:
        if self.root is None:
            return []

        values: list[int] = []
        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            values.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return values


# ------------------------------
# Example runner
# ------------------------------
def run_examples() -> None:
    """Run representative Day 1 examples plus core DSA structures."""
    numbers = [1, 2, 3, 4]
    prefix_sums = build_prefix_sums(numbers)
    print("Prefix sums:", prefix_sums)
    print("Range sum [1, 3]:", range_sum(prefix_sums, 1, 3))

    updates = [(1, 3, 2), (2, 4, 3)]
    print("Difference-array updates:", apply_range_updates(5, updates))

    print("Subarrays summing to 3:", subarray_sum_count([1, 2, 1, 2], 3))
    print("Rotated-array index of 0:", search_rotated([4, 5, 6, 7, 0, 1, 2], 0))

    print("\nStack demo:")
    stack = Stack()
    for value in [10, 20, 30]:
        stack.push(value)
    print("Top element:", stack.peek())
    print("Pop:", stack.pop())
    print("Updated stack size:", stack.size())

    print("\nQueue demo:")
    queue = Queue()
    for value in [1, 2, 3, 4]:
        queue.enqueue(value)
    print("Front:", queue.peek())
    print("Dequeue:", queue.dequeue())
    print("Queue size:", queue.size())

    print("\nPriority queue demo:")
    pq = PriorityQueue()
    for value in [9, 4, 7, 1, 3]:
        pq.push(value)
    print("Priority queue top:", pq.peek())
    print("Pop order:", pq.pop(), pq.pop(), pq.pop())

    print("\nBinary tree demo:")
    tree = BinaryTree()
    for value in [8, 3, 10, 1, 6, 14, 4]:
        tree.insert(value)
    print("Inorder:", tree.inorder())
    print("Preorder:", tree.preorder())
    print("Postorder:", tree.postorder())
    print("BFS:", tree.bfs())
    print("Search 6:", tree.search(6))


if __name__ == "__main__":
    run_examples()
