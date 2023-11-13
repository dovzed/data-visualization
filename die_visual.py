import plotly.express as px

from die import Die


die = Die()

results = []
for roll_num in range(10000):
    result = die.roll()
    results.append(result)

frequencies = []
poss_results = range(1, die.num_sides+1)
for v in poss_results:
    frequency = results.count(v)
    frequencies.append(frequency)

# Visualize the results
title = "Results of rolling one D6 10,000 times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
