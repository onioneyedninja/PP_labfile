import pandas as pd

Data_dict = {"SNo": [1, 2, 3, 4, 5], "Name": ["Prabhat", "laxman", "Kailash", "Kishan", "Ravi"],
             "Fee Status": ["Paid", "Not Paid", "Paid", "Not Paid", "Not paid"]}

mydataframe = pd.DataFrame(Data_dict)
print(mydataframe)
mydataframe.loc[1] = [2, "Laxman", "Paid"]
print("\n", mydataframe)
