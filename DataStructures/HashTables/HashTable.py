""" Represents a hash table Data Structure. """


class HashTable():
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.length = 0

    def _hash(self, key):
        return sum(index * ord(character) for index, character in enumerate(repr(key), start=1)) % self.size

    def set(self, key, value):
        hashed_location = self._hash(key)
        if self.data[hashed_location] is None:
            self.data[hashed_location] = (key, value)
            self.lenghth += 1
        return None

    def get(self, key):
        hashed_location = self._hash(key)
        return self.data[hashed_location][1] if self.data[hashed_location] is not None else None

    def keys(self):
        return [items[0] for items in self.data if items is not None]

    def values(self):
        return [items[1] for items in self.data if items is not None]

    def items(self):
        return [items for items in self.data if items is not None]

    def update(self, key, value):
        hashed_location = self._hash(key)
        self.data[hashed_location] = (key, value)

    def delete(self, key):
        hashed_location = self._hash(key)
        self.data[hashed_location] = None
        self.length -= 1


if __name__ == "__main__":
    new_hash = HashTable(10)
    new_hash.set("name", "John")
    print("Age: ", new_hash.get("Age"))
    print("Name:", new_hash.get("name"))
    print("Setting age:", new_hash.set("Age", "25"))
    print("Getting age:", new_hash.get("Age"))
    print("Keys: ", new_hash.keys())
    print("Values: ", new_hash.values())
    print("Items: ", new_hash.items())
    print("Updating name:", new_hash.update("name", "John Doe"))
    print("Getting updated name name:", new_hash.get("name"))
    print("Deleting name:", new_hash.delete("name"))
    print("Current Keys (after deleting name): ", new_hash.keys())
