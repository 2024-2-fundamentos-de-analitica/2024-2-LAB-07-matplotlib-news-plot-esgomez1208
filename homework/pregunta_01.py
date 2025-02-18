"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import matplotlib.pyplot as plt
import os

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    # Se crea la carpeta donde se guaradará el archivo
    ruta = 'files/plots'
    if not os.path.exists(ruta):
        os.makedirs(ruta)
    
    # Se leen los datos
    df = pd.read_csv('files/input/news.csv', index_col=0)

    # Colores para cada grafico -> resaltar internet(el unico creciente)
    colors = {
        'Television': 'dimgray',
        'Newspaper': 'grey',
        'Internet' : 'tab:blue',
        'Radio' : 'lightgrey',
    }
    
    # Orden de la capa que tendra el grafico
    zorder = {
        'Television': 1,
        'Newspaper': 1,
        'Internet' : 2,
        'Radio' : 1,
    }

    # Ancho de la linea de cada grafico
    linewidths = {
        'Television': 2,
        'Newspaper': 2,
        'Internet' : 3,
        'Radio' : 2,

    }

    # Se itera sobre cada columna para ver un grafico de lineas
    for col in df.columns:
        plt.plot(df[col],
                 label = col,
                 color = colors[col],
                 zorder = zorder[col],
                 linewidth = linewidths[col]
                 )  
    # Se pone titulo
    plt.title('How people get ther news')
    # Se quitan los remarcados de arriba, izq y der
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    # Se quitan los valores del eje y(no aportan a la grafica)
    plt.gca().axes.get_yaxis().set_visible(False)
    #plt.legend(loc='upper right')

    # Se le da un valor al eje y izquierdo y derecho(para más entendimiento)
    for col in df.columns:

        # Primer indice(fila)
        first_year = df.index[0]
        plt.scatter(
            # Se accede al primer valor de cada columna
            x = first_year,
            y = df[col][first_year],
            color = colors[col],
            zorder = zorder[col]
        )

        # Ultimo indice(fila)
        last_year = df.index[-1]
        plt.scatter(
            # Se accede al ultimo valor de cada columna
            x = last_year,
            y = df[col][last_year],
            color = colors[col],
            zorder = zorder[col]
        )

        # Se le pone texto a cada grafica(a la izquierda)
        plt.text(
            first_year - 0.2,
            df[col][first_year],
            col + ' ' + str(df[col][first_year]) + '%',
            ha = 'right',
            va = 'center',
            color = colors[col]
        )

        # Se le pone texto a cada grafica(a la derecha)
        plt.text(
            last_year + 0.2,
            df[col][last_year],
            col + ' ' + str(df[col][last_year]) + '%',
            ha = 'right',
            va = 'center',
            color = colors[col]
        )

    
    # Guardamos la figura en la carpeta creada
    plt.tight_layout()
    plt.savefig('files/plots/news.png')
    plt.show
