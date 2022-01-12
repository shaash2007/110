import statistics
import random
import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
data=df["temp"].tolist()
population_mean=statistics.mean(data)
stf_deviation=statistics.stdev(data)
print(population_mean,stf_deviation)
# fig=ff.create_distplot([data],["temp"],show_hist=False)
# fig.add_trace(go.Statter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
# fig.show()
# dataset=[]
# for i in range(0,100):
 #   random_index=random.randint(0,len(data))
  #  value=data[random_index]
   # dataset.append(value)
# mean=statistics.mean(dataset)
# std_deviation=statistics.stdev(dataset)

# print(mean,std_deviation)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)    
    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range (0,1000):
        set_of_mean=random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
setup()