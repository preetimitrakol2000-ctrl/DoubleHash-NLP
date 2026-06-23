# DoubleHash-NLP

A clean-room implementation of an open-addressed text tracking array optimized for smart speaker micro-engines. Instead of relying on built-in python dictionaries or linked collision buckets, this subsystem uses **Double Hashing** ($H(k, i) = (H_1(k) + i \cdot H_2(k)) \pmod m$) to maintain single flat structures.

## ⚡ Data Structure Properties
* **Collision Resolution:** Dual-function open addressing step bounds.
* **Secondary Hash Formula:** $H_2(k) = R - (k \pmod R)$, preventing stepping cycles.
* **Lookup Efficiency:** Uniformly distributed average-case $O(1)$ search lookups.
