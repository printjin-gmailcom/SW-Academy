import matplotlib.pylab as p

dir(p)



import matplotlib as ma

len(dir(ma))



import matplotlib.pyplot as plt

len(dir(ma))







import matplotlib.pyplot as plt

# state machine
# 1. 변수를 지정하지 않음. 가장 가까이 있는 것 찾음
# 2. 계층적 디폴트 값이 자동 생성

plt.figure()

plt.figure();

plt.figure(figsize=(10,10))

plt.figure(figsize=(10,5))
plt.axes()

plt.figure(figsize=(10,5))
plt.axes([0, .5, 1, 1])

plt.figure(figsize=(10,5))
plt.axes([.5, .5, .5, 1])

plt.figure(figsize=(10,5))
plt.axes([0, 0, .5, .5])
plt.axes([.5, .5, .5, 1])

plt.figure(figsize=(10,5))
plt.axes([0, 0, .5, .5])
plt.plot([1,2,3,4])
plt.axes([.5, .5, .5, 1])
plt.plot([2,4,5,4])

plt.figure(figsize=(10,5))
plt.axes([0, 0, .5, .5])
plt.plot([1,2,3,4])
plt.grid(True)
plt.axes([.5, .5, .5, 1])
plt.plot([2,4,5,4])

plt.style.available

plt.style.use('ggplot')

plt.plot([1,2,3])

plt.style.use('seaborn-v0_8-pastel')

plt.plot([1,2,3])

plt.style.use('seaborn-v0_8-dark-palette')

plt.plot([1,2,3])

plt.style.use('seaborn-v0_8-whitegrid')

plt.plot([1,2,3])

with plt.xkcd():
    plt.plot([1,2,3,4])

plt.plot([1,2,3,4],[5,6,7,8])

plt.axes(polar=True)
plt.plot([1,2,3,4],[5,6,7,8])

plt.bar([1,2,3,4],[5,6,7,8])

plt.barh([1,2,3,4],[5,6,7,8])

plt.barh([1,2,3,4],[5,6,7,8])
plt.title('뇽')

plt.barh([1,2,3,4],[5,6,7,8])
plt.title('mang')

plt.barh([1,2,3,4],[5,6,7,8])
plt.xlabel('X')
plt.ylabel('Y')

plt.barh([1,2,3,4],[5,6,7,8])
plt.xlabel('X')
plt.xticks([2,3])
plt.ylabel('Y')
plt.yticks([4,7])



import seaborn as sns

tips = sns.load_dataset('tips')

tips.groupby('sex')['tip'].mean().plot.bar()

import matplotlib.pyplot as plt

tips.groupby('sex')['tip'].mean().plot.bar()
plt.title('xxxxxx')

plt.style.available

plt.style.use('Solarize_Light2')

tips.groupby('sex')['tip'].mean().plot.bar()
plt.title('xxxxxx')
plt.grid(False)

tips.groupby('sex')['tip'].mean().plot.bar()
plt.title('xxxxxx')
plt.grid(False)
plt.ylabel('qwer')

fig, axe = plt.subplots(2,2)

fig, axe = plt.subplots(2,3)
axe[0].set_title('tt')

fig, axe = plt.subplots(2,3)
axe[1,2].set_title('tt')

tips.groupby('sex')[['tip']].mean().plot.bar()

x = tips.groupby('sex')[['tip']].mean()

x.plot.bar(color='skyblue')

fig, axe = plt.subplots(2,3)
axe[1,2].set_title('tt')

plt.subplot(2,3,1)

plt.subplot(2,3,2)
plt.plot([1,2,5])





import seaborn as sns

# https://seaborn.pydata.org/tutorial.html

tips = sns.load_dataset('tips')

tips.boxplot()

a = sns.boxplot(data=tips, x='sex', y='tip')

import matplotlib.pyplot as plt

sns.boxplot(data=tips, x='day', y='tip')

plt.show()

sns.violinplot(data=tips, x='day', y='tip')

plt.show()

sns.boxenplot(data=tips, x='day', y='tip')

plt.show()

sns.scatterplot(data=tips, x='day', y='tip')

plt.show()

sns.scatterplot(data=tips, x='total_bill', y='tip')

plt.show()

sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex')

plt.show()

sns.boxplot(data=tips, x='sex', y='tip', hue='day')

plt.show()

plt.figure(figsize=(10,10))
sns.boxplot(data=tips, x='sex', y='tip', hue='day', )

plt.show()

!pip install seaborn --upgrade

sns.lmplot(data=tips, x='total_bill', y='tip')

plt.show()

sns.lineplot(data=tips, x='total_bill', y='tip')

plt.show()



tips.sex

tips.groupby('sex')[['tip']].mean()

tips.groupby('sex')[['tip']].mean().transform(lambda x:x+100000)

tips.groupby('sex')[['tip']].mean().apply(lambda x:x+1)

tips.select_dtype('float64').applymap(lambda x:x+1)



