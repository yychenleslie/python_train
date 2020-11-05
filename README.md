# python_train
some useful practices

## for_loop

ways of for_loop

1. in the way of range: 

```python
import numpy as np
a = np.array([[1,2,3],[5,5,5],[3,4,5],[6,6,6]])
print('a:\n{}'.format(a))
N = a.shape[1]
for i in range(N):
    print('The {} column: {}'.format( i, a[:,i]))
```

2. another way:

```python
names = ['黄杰','杨艾','李丰庆','戴晓勇','龚书楠','陈炎英']
counter = 0
for name in names:
    counter = counter + 1
    print('The {} person‘s name: {}'.format(counter,name))
    print('{} 恭喜1B111李丰庆取得Offer！！! ^_^'.format(name))
```

3. zip

```python
names = ['黄杰','杨艾','李丰庆','戴晓勇','龚书楠','陈炎英']
print('names:{}'.format(names))
N = len(names)
for name, i in zip(names, range(N)):
    print('The {} person‘s name: {}'.format(i+1,name))
    print('{} 恭喜1B111李丰庆取得Offer！！! ^_^'.format(name))
```

4. for_loop in for_loop

```python
import numpy as np
a = np.array([[1,2,3],[5,5,5],[3,4,5],[6,6,6]])
counter = 0
M = a.shape[0]
N = a.shape[1]
for x in range(M):
    for y in range(N):
        counter = counter +1
        print('The {} number: {}'.format( counter, a[x,y]))
```