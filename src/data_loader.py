import pandas

df_train = pandas.read_csv("../data/raw/train_ver2.csv", nrows=10**5)
print(df_train.shape)
