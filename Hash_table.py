class DoubleHashMap:
    def __init__(self, capacity=13): # Choice of prime index size baseline
        self.capacity = capacity
        self.keys = [None] * capacity
        self.values = [0] * capacity

    def _primary_hash(self, key):
        return sum(ord(c) for c in key) % self.capacity

    def _secondary_hash(self, key):
        # Must return non-zero offsets relative to a secondary prime
        return 7 - (sum(ord(c) for c in key) % 7)

    def record_word(self, key):
        home_idx = self._primary_hash(key)
        step_val = self._secondary_hash(key)
        i = 0
        
        while i < self.capacity:
            probe_idx = (home_idx + i * step_val) % self.capacity
            
            if self.keys[probe_idx] is None:
                self.keys[probe_idx] = key
                self.values[probe_idx] = 1
                return
            if self.keys[probe_idx] == key:
                self.values[probe_idx] += 1
                return
            i += 1

    def fetch_word_count(self, key):
        home_idx = self._primary_hash(key)
        step_val = self._secondary_hash(key)
        i = 0
        while i < self.capacity:
            probe_idx = (home_idx + i * step_val) % self.capacity
            if self.keys[probe_idx] is None:
                return 0
            if self.keys[probe_idx] == key:
                return self.values[probe_idx]
            i += 1
        return 0
