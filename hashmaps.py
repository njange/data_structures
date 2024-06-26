class HashMap:
    def __init__(self):
        self.size = 10  # initial size of the hashmap
        self.map = [None] * self.size  # initialize an empty array

    def _get_hash(self, key):
        # calculate the hash value for the given key
        return hash(key) % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False

        for i in range(len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def display(self):
        for item in self.map:
            if item is not None:
                print(str(item))

# Example usage:
hashmap = HashMap()
hashmap.add("apple", 5)
hashmap.add("banana", 10)
hashmap.add("orange", 7)

print(hashmap.get("apple"))  # Output: 5
print(hashmap.get("banana"))  # Output: 10
print(hashmap.get("orange"))  # Output: 7

hashmap.delete("banana")
hashmap.display()

# Output:   ['apple', 5]
#           ['orange', 7]
