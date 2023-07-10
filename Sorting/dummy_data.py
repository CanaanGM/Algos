import pandas as pd
import numpy as np
import random

np.random.seed(42)
hundred_k = pd.DataFrame({'data': np.random.randint(1, 1000, size=100000)})
hundred = pd.DataFrame({'data': np.random.randint(1, 1000, size=10000)})


ten_k = [random.randint(1, 1000) for _ in range(1000)]
ten_ten = [random.randint(1, 100) for _ in range(100)]