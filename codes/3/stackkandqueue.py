from dataclasses import dataclass, field
from typing import Generic, TypeVar
from collections import deque

T = TypeVar("T")


# ---------------- STACK ----------------
@dataclass
class Stack(Generic[T]):
    items: list[T] = field(default_factory=list)

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)


# ---------------- QUEUE ----------------
@dataclass
class Queue(Generic[T]):
    items: deque[T] = field(default_factory=deque)

    def enqueue(self, item: T) -> None:
        self.items.append(item)

    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()

    def front(self) -> T:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)


# ---------------- MAIN PROGRAM ----------------

# Stack
print("STACK")
stack: Stack[int] = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Stack:", stack.items)
print("Top element:", stack.peek())
print("Popped element:", stack.pop())
print("Stack after pop:", stack.items)
print("Stack size:", stack.size())


# Queue
print("\nQUEUE")
queue: Queue[str] = Queue()

queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

print("Queue:", list(queue.items))
print("Front element:", queue.front())
print("Dequeued element:", queue.dequeue())
print("Queue after dequeue:", list(queue.items))
print("Queue size:", queue.size())