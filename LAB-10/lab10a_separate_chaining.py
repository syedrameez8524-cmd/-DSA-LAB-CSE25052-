# Hashing using Separate Chaining
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Hash function
    def hash_function(self, key):
        return key % self.size

    # Insert operation
    def insert(self, key):
        index = self.hash_function(key)
        if key in self.table[index]:
            print(key, "already exists.")
        else:
            self.table[index].append(key)
            print(key, "inserted at index", index)

    # Search operation
    def search(self, key):
        index = self.hash_function(key)
        if key in self.table[index]:
            position = self.table[index].index(key)
            print(key, "found at index", index, "position", position)
        else:
            print(key, "not found.")

    # Delete operation
    def delete(self, key):
        index = self.hash_function(key)
        if key in self.table[index]:
            self.table[index].remove(key)
            print(key, "deleted from index", index)
        else:
            print(key, "not found.")

    # Display hash table
    def display(self):
        print("Hash Table:")
        for i in range(self.size):
            print(i, "->", end=" ")
            for key in self.table[i]:
                print(key, "->", end=" ")
            print("None")


# Main Program
size = int(input("Enter size of hash table: "))
ht = HashTable(size)
while True:
    print("\n===== SEPARATE CHAINING =====")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")
    print("=============================")
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
