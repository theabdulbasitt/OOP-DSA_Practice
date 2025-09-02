# ...existing code...

class HashMap:
    def __init__(self, size=16, load_factor=0.75):
        self.size = size
        self.load_factor = load_factor
        self.buckets = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def _should_resize(self):
        return (self.count / self.size) >= self.load_factor

    def _resize(self):
        old_buckets = self.buckets
        self.size *= 2
        self.buckets = [[] for _ in range(self.size)]
        self.count = 0
        
        # Re-insert all elements
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def put(self, key, value):
        if self._should_resize():
            self._resize()

        hash_value = self._hash(key)
        bucket = self.buckets[hash_value]
        
        # Check for existing key
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Add new key-value pair
        bucket.append((key, value))
        self.count += 1

    def get(self, key):
        hash_value = self._hash(key)
        bucket = self.buckets[hash_value]
        
        for k, v in bucket:
            if k == key:
                return v
        return None

class HashSet:
    def __init__(self, size=16):
        self.map = HashMap(size)
        
    def add(self, item):
        self.map.put(item, True)
        
    def contains(self, item):
        return self.map.get(item) is not None

# Example usage
if __name__ == "__main__":
    # HashMap example
    map = HashMap()
    map.put("apple", 5)
    map.put("banana", 8)
    print(f"Price of apple: {map.get('apple')}")

    # HashSet example
    set = HashSet()
    set.add("python")
    set.add("java")
    print(f"Contains python? {set.contains('python')}")
    print(f"Contains ruby? {set.contains('ruby')}")