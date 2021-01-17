import statistics as st
import plotly.figure_factory as ff
import csv
import random
import pandas as pd

dataset = []

df = pd.read_csv("medium_data.csv")

data = df["publication"].tolist()

publication_mean = st.mean(data)

def random_set_of_mean(counter):

    for i in range(0,counter) :
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    
    mean = st.mean(dataset)
    return mean

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_mean = random_set_of_mean(30)
        mean_list.append(set_of_mean)
    show_fig(mean_list)


fig = ff.create_distplot([dataset],["publication"],show_hist=False)
fig.show()

dataset_mean = st.mean(dataset)

print(f"{dataset_mean} is mean !!!")

