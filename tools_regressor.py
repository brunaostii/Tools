import matplotlib.pyplot as plt


class Regressor(object):


    def __init__(self):
        print('')


    def plot_regressor_linear(self, X_test, y_test, y_pred):
        ''' Plota a linha de tendência, todos os dados tem que estar do mesmo tamanho'''

        plt.scatter(X_test, y_test,  color='black')
        plt.plot(X_test, y_pred, color='blue', linewidth=3)

        plt.xticks(())
        plt.yticks(())

        plt.show()