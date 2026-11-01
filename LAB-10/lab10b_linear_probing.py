# Hashing using Linear Probing
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.count = 0

    # Hash function
    def hash_function(self, key):
        return key % self.size

    # Insert operation
    def insert(self, key):
        if self.count == self.size:
            print("Hash table is full.")
            return
        index = self.hash_function(key)
        i = 0
        while i < self.size:
            new_index = (index + i) % self.size
            if self.table[new_index] == key:
                print(key, "already exists.")
                return
            if self.table[new_index] is None or self.table[new_index] == "DELETED":
                self.table[new_index] = key
                self.count += 1
                print(key, "inserted at index", new_index)
                return
            i += 1

    # Search operation
    def search(self, key):
        index = self.hash_function(key)
        i = 0
        while i < self.size:
            new_index = (index + i) % self.size
            if self.table[new_index] is None:
                break
            if self.table[new_index] == key:
                print(key, "found at index", new_index)
                return
            i += 1
        print(key, "not found.")

    # Delete operation
    def delete(self, key):
        index = self.hash_function(key)
        i = 0
        while i < self.size:
            new_index = (index + i) % self.size
            if self.table[new_index] is None:
                break
            if self.table[new_index] == key:
                self.table[new_index] = "DELETED"
                self.count -= 1
                print(key, "deleted from index", new_index)
                return
            i += 1
        print(key, "not found.")

    # Display hash table
    def display(self):
        print("Hash Table:")
        for i in range(self.size):
            print(i, "->", self.table[i])


# Main Program
size = int(input("Enter size of hash table: "))
ht = HashTable(size)
while True:
    print("\n===== LINEAR PROBING =====")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")
    print("==========================")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        ht.insert(int(input("Enter key: ")))
    elif choice == 2:
        ht.search(int(input("Enter key to search: ")))
    elif choice == 3:
        ht.delete(int(input("Enter key to delete: ")))
    elif choice == 4:
        ht.display()
    elif choice == 5:
        print("Program terminated.")
        break
    else:
        print("Invalid choice.")
