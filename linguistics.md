# Estimating the mean from an "iid" sample

(iid means "independent and identically distributed")

```
data = c(3, 1, 2, 4, 2)

# The sample mean
mn = mean(data)

# The "standard error of the mean"
se = sd(data) / sqrt(length(data))
```

The estimated mean is "on average" `se` units away from the population mean.

Let's see what we get with a simulated data set whose population mean
is known to be zero:

```
data = rnorm(20)
mn = mean(data)
se = sd(data) / sqrt(length(data))
```

To really understand what is going on, we can do a "simulation study"
in which we repeat the random data generation many times and
calculate the statistics for each generated data set.

```
mn_all = NULL
se_all = NULL
for (i in 1:1000) {
    data = rnorm(20)
    mn = mean(data)
    se = sd(data) / sqrt(20)
    mn_all = c(mn_all, mn)
    se_all = c(se_all, se)
}
```

The average of the averages is close to the population mean, which is zero:

```
mean(mn_all)
```

The average of the SE values is close to 1/sqrt(20), which is its
exact value:

```
mean(se_all)
```

The sample mean value are on average SE units away from their true value:

```
sqrt(mean(mn_all^2))
```

# Repeated measures

What if our data collection involves collecting repeated measurements
on each study subject?  How does this affect the behavior of the
sample mean?

Typically if we have repeated measures on subjects, there are "subject
effects" that uniquely influence the values of each individual
subject.

```
subeffects = rnorm(20)
subeffects = rep(subeffects, each=2)
data = subeffects + rnorm(40)
mn = mean(data)
se = sd(data) / sqrt(40)
```

Now we can repeat our simulation study to see how the sample mean behaves:

```
mn_all = NULL
se_all = NULL
for (i in 1:1000) {
    subeffects = rnorm(20)
    subeffects = rep(subeffects, each=2)
    data = subeffects + rnorm(40)
    mn = mean(data)
    se = sd(data) / sqrt(40)
    mn_all = c(mn_all, mn)
    se_all = c(se_all, se)
}
```

# Longitudinal data

```
tm = c(0, 1, 2, 3)
icept = rnorm(300)
slope = rnorm(300)



```

# Variance components

wmat = array(0, c(100, 4))
ii = seq(100)
wmat[,1] = 1*((ii %% 4) == 0)
wmat[,2] = 1*((ii %% 4) == 1)
wmat[,3] = 1*((ii %% 4) == 2)
wmat[,4] = 1*((ii %% 4) == 3)

smat = array(0, c(100, 20))
ii = seq(100)
wmat[,1] = 1*((ii %% 4) == 0)
wmat[,2] = 1*((ii %% 4) == 1)
wmat[,3] = 1*((ii %% 4) == 2)
wmat[,4] = 1*((ii %% 4) == 3)


ii = seq(20) %% 4
model.matrix(~0+as.factor(ii))


# Crossed effects
