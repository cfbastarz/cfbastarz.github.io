# Test

```python
# mkdocs: render
def foo():
    ...
```

## Pair Plot

```python
# mkdocs: render

import seaborn as sns

# create pair plot
df = sns.load_dataset("penguins")
sns.pairplot(df, hue="species")
```

