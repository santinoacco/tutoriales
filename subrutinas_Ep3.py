#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

def Graficar(xdata,ydata,xErr=None,yErr=None,fitdata=[],**kwargs):
    """
    Grafica los puntos (x,y) con sus errores asociados,
    si fitdata!=[] entonces tambien grafica (x,f(x)),
    para algun f(.) definido 

    # Parameters:
        
        xdata: datos del eje x

        ydata: datos del eje y

        xErr: error de x

        yErr: error de y

        fitdata: array-type de puntos ajustados f(x)

        example kwargs = {
               'xlabel':'$L$ $[m]$',
               'ylabel':'$T$ $[s]$',
               'data_label':'Datos',
               'data_fmt':'k.:',
               'fit_label':'Ajuste por cuadrados minimos',
               'fit_fmt':'r'
              }
    # Returns:

        ax: matplotlib.pyplot.Axes

    # Nota: requiere "matplotlib.pyplot as plt"

    """
    # --init objects
    fig, ax = plt.subplots()

    # --plot y vs x with error bars
    ax.errorbar(
        xdata,
        ydata,
        yerr=yErr,
        xerr=xErr,
        fmt=kwargs['data_fmt'],
        label=kwargs['data_label']
    )
    
    if len(fitdata)>0:
        ax.plot(xdata,
                fitdata,
                color=kwargs['fit_fmt'],
                label=kwargs['fit_label']
               )


    ax.set_xlabel(kwargs['xlabel'],fontsize=18)
    ax.set_ylabel(kwargs['ylabel'],fontsize=18)
    
    plt.legend()
    
    return ax

def prop_log10_err(x,xErr):
    """
    suponiendo X = log_10(x), calculamos XErr

    Nota: requiere Numpy
    """
    XErr = abs(xErr/(x*numpy.log(10)))
    return XErr

def ComputeRsquare(y,f):
    """
    Calcula y devuelve el valor del coeficiente de determinacion R^2,
    dado por:
    $R^2 = 1 - \frac{SS_res}{SS_tot}$

    # Parameters:

        y: (list-type) coordenadas en el eje Y de los puntos experimentales

        f: (list-typw) valores predichos por una función f(.)

    # Returns:
        res: R^2
    """
    y = np.asarray(y)
    f = np.asarray(f)
    ymean = np.mean(y)
    ss_res=0
    ss_tot = 0
    for i in range(len(y)):
        ss_res += (y[i]-f[i])**2
        ss_tot += (y[i]-ymean)**2
    res = 1 - ss_res/ss_tot
    
    return res