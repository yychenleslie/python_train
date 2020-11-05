import numpy as np


# Method 1
a = np.array([[1,2,3],[5,5,5],[3,4,5],[6,6,6]])
print('a:\n{}'.format(a))
N = a.shape[1]
for i in range(N):
    print('The {} column: {}'.format( i, a[:,i]))


M = a.shape[0]
for j in range(M):
    print('The {} row: {}'.format( j, a[j,:]))
    
counter = 0
for x in range(M):
    for y in range(N):
        counter = counter +1
        print('The {} number: {}'.format( counter, a[x,y]))

# deal with the number of diagonal line
counter = 0
for x,y in zip(range(M),range(N)):
    counter = counter +1
    print('The {} number: {}'.format( counter, a[x,y]))




# Name
names = ['黄杰','杨艾','李丰庆','戴晓勇','龚书楠','陈炎英']
print('names:{}'.format(names))
N = len(names)
print(N)
for i in range(N):
    print('The {} person‘s name: {}'.format(i+1,names[i]))
    print('{} 恭喜1B111李丰庆取得Offer！！! ^_^'.format(names[i]))

counter = 0
for name in names:
    counter = counter + 1
    print('The {} person‘s name: {}'.format(counter,name))
    print('{} 恭喜1B111李丰庆取得Offer！！! ^_^'.format(name))

for name, i in zip(names, range(N)):
    print('The {} person‘s name: {}'.format(i+1,name))
    print('{} 恭喜1B111李丰庆取得Offer！！! ^_^'.format(name))


