from distribution import*
import matplotlib.pyplot as plt

s = []
N = 10
n = np.linspace(0,N,N+1)
for i in range(0,N+1,1):
	a = Binomial(n[i],10,0.5)
	pdf = a.Binomial_PDF()
	s = np.append(s,pdf)

plt.figure(figsize=(10,6))
plt.scatter(n,s)
plt.bar(n,s,color='w',edgecolor='k',linewidth=3,alpha=0.4,label=r'$N=20$, $p=0.5$')
plt.xlim(0,N)
plt.ylim(0,max(s)+0.01)
plt.xticks(fontsize=14, rotation=0)
plt.yticks(fontsize=14, rotation=0)
plt.xlabel(r'$n$',fontsize=20)
plt.ylabel(r'$f(n;N,p)$',fontsize=20)
plt.title('Binomial Distribution',fontsize=15)
plt.tick_params(axis='both', which='major', labelsize=15.6)
plt.legend()

plt.savefig('Binomial.png')
print(s)
plt.show()



