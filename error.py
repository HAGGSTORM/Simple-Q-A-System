for i in range(5):
    exec('var{}={}'.format(i,i))
print(var1)