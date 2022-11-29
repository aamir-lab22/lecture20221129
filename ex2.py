#!/usr/bin/env python3

import random as random
import math as m
import matplotlib.pyplot as plt

samples = []
p_hat = []
for i in range(200):
	sample = []
	for j in range(50):
		if(random.randint(1, 100) <= 70):
			sample.append(1)
		else:
			sample.append(0)
	p_hat.append(sum(sample)/len(sample))
	samples.append(sample)

normality = 50*0.7*0.3
mu = 0.7
sigma = m.sqrt((0.7*(1-0.7))/50)
lo = 0.7 - 1.96*sigma
hi = 0.7 + 1.96*sigma

plt.plot([0.7, 0.7],[0, 100], '-k')
for i in range(100):
	ll = p_hat[i] - 1.96*sigma
	ul = p_hat[i] + 1.96*sigma
	if (p_hat[i] > lo and p_hat[i] < hi):
		print(95)
		plt.plot([ll, ul], [i + 1, i + 1], '-b')
	elif (p_hat[i] < lo or p_hat[i] > hi):
		print(5)
		plt.plot([ll, ul], [i + 1, i + 1], '-r')
plt.show()

plt.plot([0.7, 0.7],[100, 200], '-k')
for i in range(101, 200):
	ll = p_hat[i] - 1.96*sigma
	ul = p_hat[i] + 1.96*sigma
	if (p_hat[i] > lo and p_hat[i] < hi):
		print(95)
		plt.plot([ll, ul], [i + 1, i + 1], '-b')
	elif (p_hat[i] < lo or p_hat[i] > hi):
		print(5)
		plt.plot([ll, ul], [i + 1, i + 1], '-r')
plt.show()
