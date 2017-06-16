import pandas as pd


if __name__ == '__main__':
    f = pd.read_csv("data/prices.csv", index_col=0)
    print(f)