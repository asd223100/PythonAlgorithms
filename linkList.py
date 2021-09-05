class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None

    def beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def ending(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last_ptr = self.head
        while last_ptr.next:
            last_ptr = last_ptr.next
        last_ptr.next = new_node

    def between(self, pre_node, new_data):
        if pre_node is None:
            print("缺少插入節點的前一個節點")
            return
        new_node = Node(new_data)
        new_node.next = pre_node.next
        pre_node.next = new_node

    def delete_node(self, delete_key):
        ptr = self.head
        if ptr:
            if ptr.data == delete_key:
                self.head = ptr.next
                return
            while ptr:
                if ptr.data == delete_key:
                    break
                prev = ptr
                ptr = ptr.next
            if ptr is None:
                return
            prev.next = ptr.next

    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next
