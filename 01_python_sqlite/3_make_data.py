import pandas as pd
import numpy as np

np.random.seed(10)

# データ作成
N = 7
id = range(N)
japanese = np.random.randint(0, 101, N)
english = np.random.randint(0, 101, N)
math = np.random.randint(0, 101, N)
year_list = ["B4", "M1", "M2"]
prob_list = [0.4, 0.3, 0.3]
year = np.random.choice(year_list, N, p=prob_list)

# データ保存
students_df = pd.DataFrame({
    "id": id,
    "japanese": japanese,
    "english": english,
    "math": math,
    "year": year
    })
students_df.to_csv("students.csv", index=False)
print(students_df)
