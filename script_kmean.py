#on appelle tous ce qui pourait ètre utile
import numpy
import matplotlib.pyplot as plt
import matplotlib as mpl
import sklearn
import numpy as np
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
import json

#programme principale du script, il utilise la latitude, longitude et centroides pour estimer les différents clusters approprié
def K_mean(latitude, longitude, centroides):
  info = list(range(len(latitude)))
  #on met les informations de manière a ce que ce soit utilisable
  for i in range(len(latitude)):
    test = [latitude[i],longitude[i]]
    info[i]=test
  info = np.array(info)

  #pour le nombre de clusters, nous prendrons le nombre de centroides, car n centroides = n clusters
  kmeans = KMeans(n_clusters = len(centroides))
  kmeans.fit(info)
  cluster = kmeans.labels_

  return cluster


cluster = K_mean(latitude, longitude, centroides)#appelle la fonction principale K_mean avec les valeurs donné au préalable
#on ouvre un fichier pour sauveguarder les données
with open("fichier_cluster.json","w") as fichier:
  json.dump(cluster,fichier) #met la réponse attendue en format JSON et sauveguarde dans fichier_cluster.json

