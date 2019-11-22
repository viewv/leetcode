# 获取一个集合的所有子集，也就是幂集

## Python 的第一种方法
这种方法是利用了很多python的高级特性

```python
from itertools import product, compress


def powerset(nums):
    return [list(compress(nums, pattern)) for pattern in product((0, 1), repeat=len(nums))]
```

