#### Fonctions secondaires
'''
Ce document permet d'éxecuter et de générer un graphe d'une suite de syracuse
'''

# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    '''
    Fonction de génération de graphe
    '''


    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')

    #return None
    return 0  #Ajustement pour pylint
#######################
def syracuse_l(n):
    """
    retourne la suite de Syracuse de source n

        Args:
            n (int): la source de la suite

        Returns:
            list: la suite de Syracuse de source n
    """
    # votre code ici
    l = [ ]

    am = 0

    while True:
        l.append(int(n))

        if n <= 1:
            break

        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1

        am = max(am, n) #Version opti de pylint
        #if n > am:
        #    am = n

    return l

def temps_de_vol(l):
    """
    Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """

    # votre code ici
    n = 0
    n = len(l)
    return n

def temps_de_vol_en_altitude(l):
    """
    Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    # votre code ici
    n = 0
    init_val = l[0]  #Value initial

    for i in l[1:]: #start au deuxième élement.
        n += 1
        if i <= init_val:
            break

    return n


def altitude_maximale(l):
    """
    retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """

    # votre code ici
    n = 0

    for i in l:
        n = max(n, i)   #version opti de pylint
        #if n < i:
        #    n = i

    return n


#### Fonction principale


def main():
    '''
    Fonction principal
    '''

    # vos appels à la fonction secondaire i'ci
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
