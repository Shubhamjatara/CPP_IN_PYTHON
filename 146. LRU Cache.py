from typing import Dict


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def showHead(self):
        if self.head:
            print(self.head.key)

    def insertToEnd(self, key, val) -> Node:
        node = Node(key, val)

        if self.head is None:  # better check
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.pre = self.tail
            self.tail = node

        return node

    def deleteNode(self, node: Node | None) -> int | None:
        if node == None:
            return None
        left = node.pre
        right = node.next
        k = node.key
        if not left:

            self.head = right
            if self.head:
                self.head.pre = None
            if self.head is None:
                self.tail = None
            return k

        if not right:

            left.next = None
            self.tail = left
            return k

        left.next = right
        right.pre = left
        return k

    def invalidate(self) -> str:

        return self.deleteNode(self.head)

    def print(self):
        nxt = self.head
        while nxt:
            print(nxt.val)
            nxt = nxt.next

    def showTail(self):
        if self.tail:
            print(self.tail.val)


class LRUCache:

    def __init__(self, capacity: int):
        self.maxCapacity = capacity
        self.capacity = 0
        self.dblist = DoublyLinkedList()
        self.map: Dict[int, Node] = {}

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        value = node.val
        self.dblist.deleteNode(node)
        self.map[key] = self.dblist.insertToEnd(key, value)
        return value

    def put(self, key: int, value: int) -> None:

        if key in self.map:
            self.dblist.deleteNode(self.map[key])
            self.map[key] = self.dblist.insertToEnd(key, value)
            return

        if self.capacity == self.maxCapacity:
            k = self.dblist.invalidate()
            if k is not None:
                self.map.pop(k, None)
                self.capacity -= 1

        self.map[key] = self.dblist.insertToEnd(key, value)
        self.capacity += 1


l = LRUCache(2)
l.put(1, 1)
l.put(2, 2)
print(l.get(1))
l.put(3, 3)
print(l.get(2))
l.put(4, 4)
print(l.get(1))
print(l.get(3))
print(l.get(4))


""" l = DoublyLinkedList()
l.insertToEnd(1, 1)

l.insertToEnd(2, 2)

l.insertToEnd(3, 3)
print(l.invalidate())
l.insertToEnd(4, 4)
print(l.invalidate())
l.insertToEnd(5, 5)
print(l.invalidate()) """
