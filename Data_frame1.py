import pandas as pd

Marks1 = {"Prabhat": 30, "Nishant": 20, "Yash": 25}
Marks2 = {"Prabhat": 28, "Nishant": 26, "Yash": 30}
data = {"Python": Marks1, "Web Development": Marks2}
Mydataframe = pd.DataFrame(data)
print(Mydataframe)
