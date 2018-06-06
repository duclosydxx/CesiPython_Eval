import matplotlib
import numpy as np
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from donnees import GetDonnees


class Graphique:
            

    def Dessiner(self):
        n_groups = 12

        donneesRecues = GetDonnees()

        donnees_Paris = donneesRecues["Paris"]
        donnees_Londres = donneesRecues["Londres"]
        print "PARIS: "+str(donnees_Paris)
        print "LONDRES: "+str(donnees_Londres)


        fig, ax = plt.subplots()

        index = np.arange(n_groups)
        bar_width = 0.35

        opacity = 0.4
        error_config = {'ecolor': '0.3'}

        rects1 = ax.bar(index, donnees_Paris, bar_width,
                        alpha=opacity, color='b',
                        label='Paris')

        rects2 = ax.bar(index + bar_width, donnees_Londres, bar_width,
                        alpha=opacity, color='r',
                        label='Londres')


        ax.set_xlabel('Mois')
        ax.set_ylabel('Temperature')
        ax.set_title('Temperatures comparees')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(('Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin','Juillet','Aout','Septembre','Octobre','Novembre','Decembre'))
        ax.legend()

        fig.tight_layout()
        plt.show()
