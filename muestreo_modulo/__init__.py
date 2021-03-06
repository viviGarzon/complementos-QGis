# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Muestreo
                                 A QGIS plugin
 Complemento de rotacipon de muestra
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-05-10
        copyright            : (C) 2022 by Lady Viviana Garzón
        email                : viviana.garzon@usal.es
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Muestreo class from file Muestreo.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Muestreo_modulo import Muestreo
    return Muestreo(iface)
