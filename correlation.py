import pandas as pd

phy = list(map(int,input().split()))
his = list(map(int,input().split()))

x=pd.Series(phy)
y=pd.Series(his)

r=x.cov(y)/(x.std()*y.std())

beta1 = (r*y.std())/x.std()

beta0 = y.mean()- beta1*x.mean()
a=int(input())
y = beta0 + beta1*a
print(round(y,1))
