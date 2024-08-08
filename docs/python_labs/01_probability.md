# Probability and Distributions

outcomes        ：        客观的所有互斥结果
events        ：        0个或多个outcomes集合
sample space        ：        所有可能outcomes的集合，互斥且详尽

---

概率
概率空间：sample space，events space和probability function
概率函数是将事件映射到区间 [0,1] 的实值函数，概率函数遵循概率公理（Kolmogorov Axioms）

---

加法 OR probability

```{math}
P(A \cup B) = P(A) + P(B) - P(A \cap B)
```

当AB互斥：
```{math}
P(A \cup B) = P(A) + P(B)
```

---

乘法 AND probability

不独立 Dependent
```{math}
P(A∩B)=P(A)∗P(B|A)
```

独立 Independent
```{math}
P(A∩B)=P(A)∗P(B)
```

互斥 Mutually exclusive
```{math}
P(A∩B)=0
```

---

有条件的 Conditional
```{math}
P(A|B)=\frac{P(A,B)}{P(B)}
```

独立 Independent
```{math}
P(A,B)=P(A)∗P(B)
```

不相交 Disjoint
```{math}
P(A,B)=0
```

可交换 Exhangeable
```{math}
P(A then B)=P(B then A)
```

---

因式分解联合概率 Factoring joint probabilities

```{math}
P(A,B)=P(A|B) \ast P(B)
```

```{math}
P(A,B,C)=P(A|B,C)∗P(B,C)=P(A|B,C)∗P(B|C)∗P(C)
```

---

概率分布 Probability Distributions

离散: binomial 二项，Poisson 泊松，geometric 几何
连续: normal 正态/高斯，exponential 指数，uniform 均匀

概率质量函数 Probability Mass Function (PMF) 
```{math}
\sum_{x \in X} f_x(x) = 1
```
离散变量的概率和为1

累积分布函数 cdf cumulative distribution function
```{math}
F_X(b) = \sum_{x \in [-\infty,b]} f_X(x)
```

概率密度函数 Probability Density Function (PDF)
```{math}
\int_{-\infty}^\infty f_x(x)dx = 1
```
域的积分为1

cdf
```{math}
P(X \le x) = F_X(x) = \int_{-\infty}^x f(u)du
```

---

正态分布pdf
```{math}
X \sim Norm(\mu,\sigma^2) \text{, where}
```
```{math}
f_x(x,\mu,\sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}, (x,\mu,\sigma^2) \in (\mathbb{R},\mathbb{R},\mathbb{R}_+)
```

```python
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100) #bounds and granularity
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()
```

---

函数的期望 Expectation：函数在概率分布下的平均值，离散分布计算加权平均值，权重由 x 值处的概率决定

离散分布
```{math}
E[f] = \sum_x f(x)^r p(x)
```

连续分布
```{math}
E[f] = \int f(x)^r p(x) dx
```

Bernoulli distribution
```{math}
E[x] = \sum_{x=0,1} x\ast p(x,\theta) = 0\ast(1-\theta) + 1\ast\theta = \theta
```

---

方差 Variance

```{math}
Var(X) = E[(X-E[X])^2] = \int (X-E[X])^2 p(x) dx\text{连续情况}
```

偏度 Skewness 分布的对称性

```{math}
\alpha_3 = \frac{E(X-E[X])^3}{(\sqrt{Var(X)})^3}
```

峰度 Kurtosis 分布的峰值

```{math}
\alpha_4 = \frac{E(X-E[X])^4}{(\sqrt{Var(X)})^4}
```

---

对于正态分布，mean = median = mode。均值，中位数，众数相同

联合分布

```{math}
P_{XY}(x,y) = P(X=x,Y=y)
```

条件分布的期望

```{math}
E[X|Y=y_j] = \sum_{X} x_iP_{X|Y}(x_i|y_j)
```

协方差 Covariance

```{math}
cov[x,y] = E[(x-E[x])(y-E[y])] = E_{x,y}[xy]-E_x[x]E_y[y]
```

相关性/相关系数 Correlation (correlation coefficient)

```{math}
\rho_{XY} = \frac{Cov(X,Y)}{\sigma_x\sigma_y}
```

如果XY独立，cov(X,Y)= corr(X,Y) = 0


