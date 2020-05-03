import numpy as np
import tensorflow as tf

from pandas import read_csv
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.optimizers import SGD
from keras import regularizers
