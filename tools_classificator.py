import pandas as pd
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score

class Classificator(object):

    def __init__(self):
        print('inicio')

    def metrics(self, y_train, y_pred):
        
        x = {'acc': accuracy_score(y_train, y_pred), \
              'f1': f1_score(y_train, y_pred),\
              'prec':  precision_score(y_train, y_pred),\
              'rec': recall_score(y_train, y_pred)}   
              
        return x




