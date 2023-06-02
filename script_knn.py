

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import sklearn
import math
import numpy as np
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

i = 3

bdd_accidents = pd.read_csv("stat_acc_final.csv")
print(bdd_accidents.type())



