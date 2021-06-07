import pandas as pd
import statistics
import  csv
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go
# reading the file
df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
# finding mean
population_mean = statistics.mean(data)
std_dev = statistics.stdev(data)

def randomSetOfMean(counter):
    dataset = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data))
        dataset.append(randomIndex)

    dataset_mean = statistics.mean(dataset)

    return dataset_mean

mean_list = []
for i in range(0,1000):
    set_of_means= randomSetOfMean(100)
    mean_list.append(set_of_means)


## calculating mean and standard_deviation of the sampling distribution.
std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
# print("mean of sampling distribution:- ",mean)
# print("Standard deviation of sampling distribution:- ", std_deviation)



## findig the standard deviation starting and ending values
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

# Intervention 1
data = df["responses"].tolist()
mean_of_sample1 = statistics(data)


fig = ff.create_distplot([mean_list],["responses"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD MATH LABS"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

# Intervention 2

data = df["reading_time"].tolist()
mean_of_sample2 = statistics(data)


fig = ff.create_distplot([mean_list],["reading_time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD MATH LABS"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

z_score_1 = (mean_of_sample1-mean)/std_deviation
print(f"the z-scre of the 1st intervention is {z_score_1}")

# For the first Intervention
z_score_2 = (mean_of_sample2-mean)/std_deviation
print(f"the z-scre of the 1st intervention is {z_score_2}")
