import numpy as np
import matplotlib.pyplot as plt
#our data
X=np.array([[1,2],
            [1.5,1.9],
            [5,8],
            [8,8],
            [1,0.6],
            [9,11]])
#plotting our original data
plt.scatter(X[:,0],X[:,1],marker="o",s=150,c="b")
plt.show()
colors=10*["g","r","c","b","k"]

class k_means:
    def __init__ (self,k=2,tol=0.001,max_iter=300):
        self.k = k
        self.max_iter =max_iter
        self.tol= tol

    def fit(self,data):
        #geeting centroids
        self.centroids={}
        #here we pick first 2 data points as our initial centroids or we can also use random
        for i in range(self.k):
            self.centroids[i]=data[i]
        #now run our loop
        for i in range(self.max_iter):
            #it contain centroids
            self.classifications={}
            for i in range(self.k):
                #making emplty list where we add k with data
               self.classifications[i]=[]
               #iterating over ddta
            for feature in data:
                #calculating distance from every point
                distances=[np.linalg.norm(feature-self.centroids[centroid]) for centroid in self.centroids]
                classification=distances.index(min(distances))
                self.classifications[classification].append(feature)
            
            prev=dict(self.centroids)
            for classification in self.classifications:
                self.centroids[classification]=np.average(self.classifications[classification],axis=0)
            
            optimized=True
            #where we have to stop
            for c in self.centroids:
                org=prev[c]
                cur=self.centroids[c]
                if np.sum((cur-org)/org*100.0)>self.tol:
                    optimized=False
            if optimized:
                break
    def predict(self,data):
        distances=[np.linalg.norm(data-self.centroids[centroid]) for centroid in self.centroid]
        classification=distaces.index(min(distances))
        return classification


clf=k_means()

clf.fit(X)
for centroid in clf.centroids:
    plt.scatter(clf.centroids[centroid][0],clf.centroids[centroid][1],marker="X",color="k",s=150,linewidth=5)        

for classification in clf.classifications:
    color=colors[classification]
    for featureset in clf.classifications[classification]:
        plt.scatter(featureset[0],featureset[1],marker="o",color=color,s=150,linewidth=5)
plt.show()
        
        
            
            
        
