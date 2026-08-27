class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def create_list(self):
        self.head = None
        n = int(input("Enter number of nodes to create: "))
        for i in range(n):
            data = int(input(f"Enter value for node {i + 1}: "))
            self.insert_at_end(data)
        print("Linked list created successfully.")

    def insert_at_beginning(self):
        data = int(input("Enter value to insert at beginning: "))
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"{data} inserted at the beginning.")

    def insert_at_end(self, data=None):
        if data is None:
            data = int(input("Enter value to insert at end: "))
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        if data is not None:
            print(f"{data} inserted at the end.")

    def insert_at_index(self):
        index = int(input("Enter index to insert at (0-based): "))
        data = int(input("Enter value to insert: "))
        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            print(f"{data} inserted at index {index}.")
            return
        temp = self.head
        count = 0
        while temp is not None and count < index - 1:
            temp = temp.next
            count += 1
        if temp is None:
            print("Index out of range.")
            return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
        print(f"{data} inserted at index {index}.")

    def delete_by_value(self):
        value = int(input("Enter value to delete: "))
        if self.head is None:
            print("List is empty.")
            return
        if self.head.data == value:
            self.head = self.head.next
            print(f"Value {value} deleted.")
            return
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.data == value:
                prev.next = curr.next
                print(f"Value {value} deleted.")
                return
            prev = curr
            curr = curr.next
        print(f"Value {value} not found in list.")

    def delete_first_node(self):
        if self.head is None:
            print("List is empty.")
            return
        deleted = self.head.data
        self.head = self.head.next
        print(f"Deleted first node with value {deleted}.")

    def delete_last_node(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.next is None:
            deleted = self.head.data
            self.head = None
            print(f"Deleted last node with value {deleted}.")
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        deleted = temp.next.data
        temp.next = None
        print(f"Deleted last node with value {deleted}.")

    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        print(f"Number of nodes: {count}")

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(elements) + " -> None")


# Main menu-driven program
sll = SinglyLinkedList()

while True:
    print("\n----- Singly Linked List Menu -----")
    print("1. Create a linked list")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at specific index")
    print("5. Delete by value")
    print("6. Delete first node")
    print("7. Delete last node")
    print("8. Count number of nodes")
    print("9. Display/Traversal")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        sll.create_list()
    elif choice == 2:
        sll.insert_at_beginning()
    elif choice == 3:
        sll.insert_at_end()
    elif choice == 4:
        sll.insert_at_index()
    elif choice == 5:
        sll.delete_by_value()
    elif choice == 6:
        sll.delete_first_node()
    elif choice == 7:
        sll.delete_last_node()
    elif choice == 8:
        sll.count_nodes()
    elif choice == 9:
        sll.display()
    elif choice == 10:
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
