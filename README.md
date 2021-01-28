# Data frames.
*Implementation of some of the objects in Pandas.*
## Use

- Provide data as dictionary
- Provide index (Optional)

## Example: 

```py
d = {'Sun Hours': [4.5,4.0,5.1,5],
     'Max Temp': [19.6,19.1,19.6,20.0],
     'Min Temp': [12.7,12.5,13.3,12.1],
     'Rain (mm)': [82,109,65,76],
     'Rain Days': [13,20,10,9.7]}
df1 = MyDataFrame(d)
df2 = MyDataFrame(d, index = ['Clare', 'Galway','Dublin', 
  'Wexford'])

df2.print()

df2.sort_values('Rain (mm)')
df2.print()

df2.mean()
df2.min()
df2.max()
```
