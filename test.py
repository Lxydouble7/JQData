import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.cm as cm

sample = [  ['For business', 0.7616104043587437],
            ['For home and cottages', 0.6890139579274699],
            ['Consumer electronics', 0.039868871866136635],
            ['Personal things', 0.7487893699793786],
            ['Services', 0.747226678171249],
            ['Services', 0.23463661173977313],
            ['Animals', 0.6504301798258314],
            ['For home and cottages', 0.49567857024037665],
            ['For home and cottages', 0.9852681814098107],
            ['Transportation', 0.8134867587477912],
            ['Animals', 0.49988690699674654],
            ['Consumer electronics', 0.15086800344617235],
            ['For business', 0.9485494576819328],
            ['Hobbies and Leisure', 0.25766871111905243],
            ['For home and cottages', 0.31704508627659533],
            ['Animals', 0.6192114570078333],
            ['Personal things', 0.5755788287287359],
            ['Hobbies and Leisure', 0.10106922056341394],
            ['Animals', 0.16834618003738577],
            ['Consumer electronics', 0.7570803588496894] ]

train = pd.DataFrame(data=sample,  columns=['parent_category_name','deal_probability'])
parent_categories = train['parent_category_name'].unique()
print("种类"+str(len(parent_categories)))
fig, ax = plt.subplots(figsize=(10,8))
colors = iter(cm.rainbow(np.linspace(0, 1, len(parent_categories))))

for parent_category in parent_categories:
    ax.plot(range(len(train[train["parent_category_name"] == parent_category])),
            sorted(train[train["parent_category_name"] == parent_category].deal_probability.values),
            color = next(colors),
            marker = "o",
            label = parent_category)

plt.ylabel('likelihood that an ad actually sold something', fontsize=12)
plt.title('Distribution of likelihood that an ad actually sold something')
plt.legend(loc = "best")
plt.show()

train = pd.DataFrame(data=sample,  columns=['parent_category_name','deal_probability'])
parent_categories = train['parent_category_name'].unique()

fig, ax = plt.subplots(figsize=(18,9))
colors = iter(cm.rainbow(np.linspace(0, 1, len(parent_categories))))

for parent_category in parent_categories:
    ax.scatter(
        train[train["parent_category_name"] == parent_category].parent_category_name.values,
        train[train["parent_category_name"] == parent_category].deal_probability.values,
        color = next(colors),
        label = parent_category
    )

plt.ylabel('likelihood that an ad actually sold something', fontsize=12)
plt.title('Distribution of likelihood that an ad actually sold something')
plt.legend(loc = "best")
plt.show()