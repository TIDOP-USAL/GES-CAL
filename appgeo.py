import sys
from PyQt5 import uic
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import (QApplication, QMainWindow)
import math
from matplotlib import pyplot as plt
from os import remove
import numpy as np
import ctypes
from PIL import Image

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(screensize)

if user32.GetSystemMetrics(0) >= 1656:
    img = QtGui.QImage('images/mapa_final.png')
else:
    img = QtGui.QImage('images/mapa_final_peq.png')

class pruebageo(QMainWindow):
    def __init__(self):

        super(pruebageo, self).__init__()

        if user32.GetSystemMetrics(0) >= 1656:
            self.ui = uic.loadUi('ui/appgeo.ui', self)
            
            pixmap_image_3 = QtGui.QPixmap(QtGui.QPixmap.fromImage(img))
            pixmap_image_4 = QtGui.QPixmap('images/logoTransp.png')
            pixmap_image_5 = QtGui.QPixmap('images/helicoidal.png')
            pixmap_image_6 = QtGui.QPixmap('images/simple.png')
            pixmap_image_7 = QtGui.QPixmap('images/horizontal.png')
            pixmap_image_8 = QtGui.QPixmap('images/TickVerde.png')
            pixmap_image_9 = QtGui.QPixmap('images/Cruz_roja.png')
            pixmap_image_10 = QtGui.QPixmap('images/espiral.png')
            pixmap_image_11 = QtGui.QPixmap('images/doble.png')
            pixmap_image_12 = QtGui.QPixmap('images/fondoborde.png')

            self.setWindowTitle("GES-Cal")
            self.showMaximized()
        else: 
            self.ui = uic.loadUi('ui/appgeo_peq.ui', self)
            pixmap_image_3 = QtGui.QPixmap(QtGui.QPixmap.fromImage(img))
            pixmap_image_4 = QtGui.QPixmap('images/logoTransp_peq.png')
            pixmap_image_5 = QtGui.QPixmap('images/helicoidal_peq.png')
            pixmap_image_6 = QtGui.QPixmap('images/simple_peq.png')
            pixmap_image_7 = QtGui.QPixmap('images/horizontal_peq.png')
            pixmap_image_8 = QtGui.QPixmap('images/TickVerde.png')
            pixmap_image_9 = QtGui.QPixmap('images/Cruz_roja.png')
            pixmap_image_10 = QtGui.QPixmap('images/espiral_peq.png')
            pixmap_image_11 = QtGui.QPixmap('images/doble_peq.png')
            pixmap_image_12 = QtGui.QPixmap('images/fondoborde_peq.png')

            self.setWindowTitle("GES-Cal")
            self.setMinimumWidth(1000)
            self.setMinimumHeight(680)
            self.setMaximumWidth(1000)
            self.setMaximumHeight(680)
            # self.showMaximized()



        #Configuracion de visibilidad y opciones por defecto por defecto de algunos elementos
        self.ui.gbhorizontal.show()
        self.ui.gbvertical.hide()
        self.ui.gbhelicoidal.hide()
        self.ui.gbmanual.hide()
        self.ui.gbautodemanda.show()
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.gbhelicoidalfinal.hide()
        self.ui.gbinstvertsim.hide()
        self.ui.gbinstvertsim_2.hide()
        self.ui.gbinsthoriz.hide()
        self.ui.lbtick.hide()
        self.ui.lbcruz.hide()
        self.ui.lbtick2.hide()
        self.ui.lbcruz2.hide()

        self.lbconductividadterreno_2.hide()
        self.lemetodoperf.hide()
        self.lbrelleno.hide()
        self.lbconductividadrelleno.hide()
        self.leconductividadrelleno.hide()
        self.lbw_mk_2.hide()
        self.cbrelleno.hide()
        self.teErrorHelicoidal.hide()

        self.ui.cbmanualoauto.setCurrentIndex(1)
        self.ui.cbsondas.setCurrentIndex(0)

        #Label con imagenes
        self.ui.label_2.setPixmap(pixmap_image_3)
        self.ui.label_2.mousePressEvent = self.getPixel

        self.ui.lb_logo.setPixmap(pixmap_image_4)
        self.ui.lbhelicoidal.setPixmap(pixmap_image_5)
        self.ui.lbvsimple.setPixmap(pixmap_image_6)
        self.ui.lbhoriz.setPixmap(pixmap_image_7)
        self.ui.lbtick.setPixmap(pixmap_image_8)
        self.ui.lbcruz.setPixmap(pixmap_image_9)
        self.ui.lbtick2.setPixmap(pixmap_image_8)
        self.ui.lbcruz2.setPixmap(pixmap_image_9)
        self.ui.lbespiral.setPixmap(pixmap_image_10)
        self.ui.lbvertdoble.setPixmap(pixmap_image_11)
        self.ui.label_39.setPixmap(pixmap_image_12)

        #Asignacion de metodos a botones y eventos del raton
        self.ui.pbcalcularpotencia.clicked.connect(self.calcularPotencia)
        self.ui.cbmanualoauto.currentIndexChanged.connect(self.showOrHideGbManual)
        self.ui.cbsondas.currentIndexChanged.connect(self.showOrHideGbHorizontal)
        self.ui.cbrelleno.currentIndexChanged.connect(self.relleno)
        self.ui.pbcalculardemanda_2.clicked.connect(self.calculardemanda)
        self.ui.pbprueba.clicked.connect(self.botonprueba)
        self.ui.pbpotenciafinal.clicked.connect(self.pfinal)
        self.ui.pbNext.clicked.connect(self.goToProyecto)
        self.ui.pbNext_2.clicked.connect(self.goToevaluacion)
        self.ui.pbNext_3.clicked.connect(self.goTomedioambiente)
        self.ui.pbcomenzar.clicked.connect(self.comenzar)
        self.ui.pbcallongitud.clicked.connect(self.longitudperforacion)
        self.ui.pbdisenofinal.clicked.connect(self.disfinal)
        self.ui.pbmapa.clicked.connect(self.showHideInfo)
        self.ui.pbcalinversion.clicked.connect(self.inversioninicial)
        self.ui.cbelectricaogas.currentIndexChanged.connect(self.electricaogas)
        self.ui.cbsondas.currentIndexChanged.connect(self.datosAmostrar)
        self.ui.pbcosteanual.clicked.connect(self.costeanual)
        self.ui.pbcomparar.clicked.connect(self.comparacion)
        self.ui.pbdioxido.clicked.connect(self.emisiones)

        #Datos de pruebas para que se inicie automatico
        self.ui.lesuperficie.setText("100.0")
        self.ui.lealtura.setText("4")
        self.ui.leyear.setText("2019")

        self.gbMaterial.setStyleSheet("QGroupBox {border: 0px solid gray;}")
        self.gbdiametro.setStyleSheet("QGroupBox {border: 0px solid gray;}")
        self.gbconfiguracion.setStyleSheet("QGroupBox {border: 0px solid gray;}")

        self.gbmaterialh.setStyleSheet("QGroupBox {border: 0px solid gray;}")
        self.gbdiametroh.setStyleSheet("QGroupBox {border: 0px solid gray;}")
        self.gbHor1.setStyleSheet("QGroupBox {border: 0px solid gray;}")
        self.gbDiam1.setStyleSheet("QGroupBox {border: 0px solid gray;}")

        self.teInfoMapa.setVisible(False)
        self.inicioAutomatico()

    def datosAmostrar(self):
        self.ui.leconductividadterreno.setText('')
        self.ui.lemetodoperf.setText('')
        if self.cbsondas.currentIndex() == 0:  # Caso Horizontal seleccionado
            self.lbconductividadterreno_2.hide()
            self.lemetodoperf.hide()
            self.lbrelleno.hide()
            self.lbconductividadrelleno.hide()
            self.leconductividadrelleno.hide()
            self.lbw_mk_2.hide()
            self.cbrelleno.hide()
            self.ui.teErrorHelicoidal.hide()

        elif self.cbsondas.currentIndex() == 1: # Caso Vertical seleccionado
            self.lbconductividadterreno_2.show()
            self.lemetodoperf.show()
            self.lbrelleno.show()
            self.lbconductividadrelleno.show()
            self.leconductividadrelleno.show()
            self.lbw_mk_2.show()
            self.cbrelleno.show()
            self.ui.teErrorHelicoidal.hide()
        else: # Caso Helicoidal seleccionado
            self.lbrelleno.hide()
            self.lbconductividadrelleno.hide()
            self.leconductividadrelleno.hide()
            self.lbw_mk_2.hide()
            self.cbrelleno.hide()
            if (self.leconductividadterreno.text() == '1.5') or (self.leconductividadterreno.text() == '2.1') or (self.leconductividadterreno.text() == '2.3'):
                self.ui.teErrorHelicoidal.hide()
            else:
                self.leconductividadterreno.setText('')
                self.ui.teErrorHelicoidal.show()

    def showHideInfo(self):
        if self.pbmapa.text() == 'Mostrar Ayuda':
            self.teInfoMapa.setVisible(True)
            self.pbmapa.setText("Ocultar Ayuda")
        else:
            self.teInfoMapa.setVisible(False)
            self.pbmapa.setText("Mostrar Ayuda")

    def getPixel(self, event):
        global img
        x = event.pos().x()
        y = event.pos().y()
        c = img.pixel(x, y)  # color code (integer): 3532912
        c_rgb = QtGui.QColor(c).getRgb()  # 8bit RGBA: (255, 23, 0, 255)

        col = QtGui.QColor(c_rgb[0], c_rgb[1], c_rgb[2])
        alpha = 1
        values = "{r}, {g}, {b}, {a}".format(r=col.red(), g=col.green(), b=col.blue(), a=alpha )
        self.ui.rgbPicked.setStyleSheet("QLabel { background-color: rgba(" + values + "); }")
        if col.rgb() == 4278337651:
            self.ui.teErrorHelicoidal.hide()
            self.ui.leconductividadterreno.setText('1.5')
            if self.cbsondas.currentIndex() == 1 or self.cbsondas.currentIndex() == 2:
                self.ui.lemetodoperf.setText('Circulacion Inversa')
        elif col.rgb() == 4280725234:
            self.ui.teErrorHelicoidal.hide()
            self.ui.leconductividadterreno.setText('2.1')
            if self.cbsondas.currentIndex() == 1 or self.cbsondas.currentIndex() == 2:
                self.ui.lemetodoperf.setText('Circulacion Inversa')
        elif col.rgb() == 4278362724:
            self.ui.teErrorHelicoidal.hide()
            self.ui.leconductividadterreno.setText('2.3')
            if self.cbsondas.currentIndex() == 1 or self.cbsondas.currentIndex() == 2:
                self.ui.lemetodoperf.setText('Circulacion Inversa')
        elif col.rgb() == 4294630210:
            self.ui.teErrorHelicoidal.hide()
            self.ui.leconductividadterreno.setText('2.5')
            if self.cbsondas.currentIndex() == 1:
                self.ui.lemetodoperf.setText('Rotopercusion')
            elif self.cbsondas.currentIndex() == 2:
                self.ui.teErrorHelicoidal.show()
        elif col.rgb() == 4294480397:
            self.ui.teErrorHelicoidal.hide()
            self.ui.leconductividadterreno.setText('2.7')
            if self.cbsondas.currentIndex() == 1:
                self.ui.lemetodoperf.setText('Rotopercusion')
            elif self.cbsondas.currentIndex() == 2:
                self.ui.teErrorHelicoidal.show()
        elif col.rgb() == 4294531846:
            self.ui.teErrorHelicoidal.hide()
            self.ui.leconductividadterreno.setText('2.9')
            if self.cbsondas.currentIndex() == 1:
                self.ui.lemetodoperf.setText('Rotopercusion')
            elif self.cbsondas.currentIndex() == 2:
                self.ui.teErrorHelicoidal.show()
        elif col.rgb() == 4288224030:
            self.ui.teErrorHelicoidal.hide()
            self.ui.leconductividadterreno.setText('3.2')
            if self.cbsondas.currentIndex() == 1:
                self.ui.lemetodoperf.setText('Rotopercusion')
            elif self.cbsondas.currentIndex() == 2:
                self.ui.teErrorHelicoidal.show()
        else:
            self.ui.teErrorHelicoidal.hide()
            self.ui.leconductividadterreno.setText('No valido')
            if self.cbsondas.currentIndex() == 1:
                self.ui.lemetodoperf.setText('No valido')
            elif self.cbsondas.currentIndex() == 2:
                self.ui.teErrorHelicoidal.show()
            print("Zona seleccionada no valida")
        # myLabel.setStyleSheet("QLabel { background-color: rgba(" + values + "); }")

        # self.ui.label.backgroundColor(c_rgb[0],c_rgb[1],c_rgb[2])
        # return x, y, c_rgb

    def showOrHideGbManual(self):
        # Capturar indice acutal del combobox
        indice = self.ui.cbmanualoauto.currentIndex()
        if indice == 0:
            #si es cero se muestra manual y se oculta el otro
            self.ui.gbmanual.show()
            self.ui.gbautodemanda.hide()
        elif  indice == 1:
            self.ui.gbmanual.hide()
            self.ui.gbautodemanda.show()

    def showOrHideGbHorizontal(self):
        indice2 = self.ui.cbsondas.currentIndex()
        if indice2 == 0:
            self.ui.gbhorizontal.show()
            self.ui.gbvertical.hide()
            self.ui.gbhelicoidal.hide()
        if indice2 == 1:
            self.ui.gbhorizontal.hide()
            self.ui.gbvertical.show()
            self.ui.gbhelicoidal.hide()
        if indice2 == 2:
            self.ui.gbhorizontal.hide()
            self.ui.gbvertical.hide()
            self.ui.gbhelicoidal.show()

    def calcularPotencia(self):
        hacercalculo = True
        #Capturamos los datos de la interfaz grafica
        try:
            cop = float(self.ui.lecop.text())
        except:
            ctypes.windll.user32.MessageBoxW(0, "Establezca un COP válido para el cálculo (Tipo de Bomba).", "Error", 0)
            hacercalculo = False

        #Capturar indice acutal del combobox
        indice = self.ui.cbhoras.currentIndex()

        #Capturar contenido del indice del combobox y convertirlo a float
        horasFuncionamiento = float(self.ui.cbhoras.itemText(indice))
        if indice == 0:
            horas = 1800
        elif indice == 1:
            horas = 2400

        tipodemanda = float(self.ui.cbmanualoauto.currentIndex())
        if tipodemanda == 0:
            try:
                autodeman = float(self.ui.lndemandamanual.text())
            except:
                ctypes.windll.user32.MessageBoxW(0, "Establezca un Valor de demanda.", "Error",  0)
                hacercalculo = False

        else:
            try:
                autodeman = float(self.ui.leautodemanda.text())
            except:
                ctypes.windll.user32.MessageBoxW(0, "Establezca un Valor de auto-demanda válido.", "Error", 0)
                hacercalculo = False

        if hacercalculo == True:
            potencia = autodeman / horas / cop
            self.ui.lepotencia.setText("%.2f" % float(potencia))

    def calculardemanda(self):
        hacercalculo = True
        try:
            superficie = float(self.ui.lesuperficie.text())
        except:
            ctypes.windll.user32.MessageBoxW(0, "Valor superficie incorrecto.", "Error", 0)
            hacercalculo = False
        try:
            altura = float(self.ui.lealtura.text())
        except:
            ctypes.windll.user32.MessageBoxW(0, "Valor altura incorrecta.", "Error", 0)
            hacercalculo = False
        try:
            year = float(self.ui.leyear.text())
        except:
            ctypes.windll.user32.MessageBoxW(0, "Anio incorrecto.", "Error", 0)
            hacercalculo = False

        #cogemos el factor segun el valor del combobox
        indice = self.ui.cborientacion.currentIndex()
        if indice == 0:
            factor = float(1.0)
        elif indice == 1:
            factor = float(0.6)
        elif indice == 2:
            factor = float(0.8)
        elif indice == 3:
            factor = float(0.8)

        if hacercalculo == True:
            autodeuno = (-4.044 * year + 8526.8) * factor
            corraltura = ((altura - 4) * 0.) *autodeuno + autodeuno
            autodemanda = corraltura * superficie
            self.ui.leautodemanda.setText("%.2f" %float(autodemanda))

    #sobredimensionamiento
    def botonprueba(self):
        hacercalculo = True
        try:
            prueba2 = float(self.ui.leyear.text())
            pruebasup = float(self.ui.lesuperficie.text())
        except:
            ctypes.windll.user32.MessageBoxW(0, "Anio y/o superfice no válido.", "Error", 0)
            hacercalculo = False

        if hacercalculo == True:
            prue = ((-0.5 * prueba2) + 1034) / 1000
            pruebafinal = prue * pruebasup
            self.ui.leprueba.setText("%.2f" %float(pruebafinal))

    def pfinal(self):
        hacercalculo = True
        try:
            pot = float(self.ui.lepotencia.text())
            fsob = float(self.ui.leprueba.text())
        except:
            ctypes.windll.user32.MessageBoxW(0, "Potencia y/o sobredimensionamiento no válido.", "Error", 0)
            hacercalculo = False

        if hacercalculo == True:
            res = pot + fsob
            self.ui.lepotenciafinal.setText("%.2f" %float(res))

    def relleno(self):
        rell = self.ui.cbrelleno.currentIndex()
        if rell == 1:
            valor = float(0.7)
        elif rell == 2:
            valor = float(2.45)
        elif rell == 3:
            valor = float(1.98)
        elif rell == 4:
            valor = float(1.20)
        elif rell == 5:
            valor = float(0.5)
        elif rell == 6:
            valor = float(1.8)
        elif rell == 7:
            valor = float(0.4)
        elif rell == 8:
            valor = float(1.7)
        elif rell == 9:
            valor = float(2.4)
        else:
            valor = -99

        if valor == -99:
            self.ui.leconductividadrelleno.setText("--No seleccionado--")
        else:
            self.ui.leconductividadrelleno.setText("%.2f" %float(valor))


    def goToProyecto(self):
        hacercalculo = True

        #Auto rellenamos la informacion de la temperatura de salida
        tdemanda = float(self.ui.cbmanualoauto.currentIndex())
        if tdemanda == 0:
            try:
                deman = float(self.ui.lndemandamanual.text())
            except:
                ctypes.windll.user32.MessageBoxW(0, "Demanda manual invalida.", "Error", 0)
                hacercalculo = False
        else:
            try:
                deman = float(self.ui.leautodemanda.text())
            except:
                ctypes.windll.user32.MessageBoxW(0, "Demanda automatica no valida.", "Error", 0)
                hacercalculo = False


        hfuncionamiento = float(self.ui.cbhoras.currentIndex())
        if hfuncionamiento == 0:
            h = 1800
        elif hfuncionamiento == 1:
            h = 2400

        #comprobamos los demas datos
        try:
            pot = float(self.ui.lepotenciafinal.text())
            cop2 = float(self.ui.lecop.text())
            resterre = float(self.ui.leconductividadterreno.text())
            lean = float(self.ui.leancho.text())
            lela = float(self.ui.lelargo.text())
        except:
            ctypes.windll.user32.MessageBoxW(0, "Revise Potencia Final / COP / Conductivdad térmica / Ancho y Largo del terreno. Datos incorrectos.", "Error", 0)
            hacercalculo = False

        if hacercalculo == True:
            caudal = (758.83 * pot) + 1560.6
            Pc = deman / h

            tsalida1 = (cop2 - 1) / cop2
            tsalida2 = tsalida1 * deman
            tsalida3 = (caudal / 3600) * 4185
            tfinal = 0 - (tsalida2 / tsalida3)
            self.ui.letempsalida.setText("%.2f" % float(tfinal))

            #Auto-rellenamos la informacion de la temperatura minima
            tminima = (tfinal + 0) / 2
            self.ui.letminima.setText("%.2f" % float(tminima))

            hacercalculo2 = True
            #Auto-rellenamos el RP
            if self.ui.cbsondas.currentIndex() == 0:
                if self.ui.rbpe100.isChecked() == False or self.ui.rb32mm.isChecked() == False:
                    ctypes.windll.user32.MessageBoxW(0, "Seleccione Material y Diametro.", "Error", 0)
                    hacercalculo2 = False
                else:
                    k=0.43
                    di = 18
                    d0 = 20
            elif self.ui.cbsondas.currentIndex() == 1:
                if self.ui.cbrelleno.currentIndex() == 0:
                    ctypes.windll.user32.MessageBoxW(0, "Seleccione un Material de relleno.", "Error", 0)
                    hacercalculo2 = False
                if self.ui.rbsimpleU.isChecked() == False and self.ui.rbdobleU.isChecked() == False:
                    ctypes.windll.user32.MessageBoxW(0, "Seleccione una configuración: Simple U / Doble-U.", "Error", 0)
                    hacercalculo2 = False
                if self.ui.rbpe100_2.isChecked():
                    k=0.43
                    if self.ui.rb32mm_2.isChecked():
                        di = 29
                        d0 = 32
                    elif self.ui.rb40mm_2.isChecked():
                        di = 36.3
                        d0 = 40
                    else:
                        ctypes.windll.user32.MessageBoxW(0, "Seleccione Diametro.", "Error", 0)
                        hacercalculo2 = False
                elif self.ui.rbpexa_2.isChecked():
                    k = 0.40
                    if self.ui.rb32mm_2.isChecked():
                        di = 29.1
                        d0 = 32
                    elif self.ui.rb40mm_2.isChecked():
                        di = 36.3
                        d0 = 40
                    else:
                        ctypes.windll.user32.MessageBoxW(0, "Seleccione Diametro.", "Error", 0)
                        hacercalculo2 = False
                else:
                    ctypes.windll.user32.MessageBoxW(0, "Seleccione Material.", "Error", 0)
                    hacercalculo2 = False
            elif self.ui.cbsondas.currentIndex() == 2:
                if self.ui.rbpe100_3.isChecked() == False or self.ui.rb32mm_3.isChecked() == False:
                    ctypes.windll.user32.MessageBoxW(0, "Seleccione Material y Diametro.", "Error", 0)
                    hacercalculo2 = False
                else:
                    k=0.43
                    di = 18
                    d0 = 20
                    if (float(self.ui.leconductividadterreno.text())) != 1.5 and (float(self.ui.leconductividadterreno.text())) != 2.1 and (float(self.ui.leconductividadterreno.text())) != 2.3:
                        ctypes.windll.user32.MessageBoxW(0, "Conductividad térmica error. Solo terrenos azules y verdes.", "Error", 0)
                        hacercalculo2 = False
            if hacercalculo2 == True:
                denominador = 2.0 * math.pi * k
                cociente = d0 / di
                log = math.log(cociente)
                rp = log / denominador
                self.ui.lerp.setText("%.5f" % float(rp))

                #Auto-rellenamos TL
                valorl = self.ui.cbsondas.currentIndex()
                if valorl == 0:
                    tl = 6.34
                if valorl == 1:
                    tl = 17.00
                if valorl == 2:
                    tl = 11.49

                self.ui.letl.setText("%.2f" % float(tl))

                #Auto-rellenamos TFS
                valorfs = self.ui.cbhoras.currentIndex()
                if valorfs == 0:
                    fs = 0.4583
                if valorfs == 1:
                    fs = 0.5833

                self.ui.lefs.setText("%.4f" % float(fs))
                # Auto-rellenamos Rs
                resterre2 = 1 / resterre
                self.ui.lers.setText("%.4f" % float(resterre2))

                self.ui.tabWidget.setCurrentIndex(2)

    def comenzar(self):
        self.ui.tabWidget.setCurrentIndex(1)

    def longitudperforacion(self):
        try:
            tdemanda = float(self.ui.cbmanualoauto.currentIndex())
            if tdemanda == 0:
                demandap = float(self.ui.lndemandamanual.text())
            else:
                demandap = float(self.ui.leautodemanda.text())

            copperforacion = float(self.ui.lecop.text())
            rp = float(self.ui.lerp.text())
            rs = float(self.ui.lers.text())
            fs = float(self.ui.lefs.text())
            tempminima = float(self.ui.letminima.text())
            tl = float(self.ui.letl.text())

            resperf1 = (copperforacion - 1) / copperforacion
            resperf2 = (rp + (rs * fs))
            resperf3 = demandap * resperf1 * resperf2
            resperf4 = tl - tempminima
            resperffinal = resperf3 / resperf4

            if self.ui.cbsondas.currentIndex() == 1:
                factorrelleno = float(self.ui.leconductividadrelleno.text())

            # if self.ui.cbsondas.currentIndex() == 1:
                if self.ui.rbsimpleU.isChecked():
                    print('factor relleno elegido: ')
                    print(factorrelleno)
                    if factorrelleno <= 0.7:
                        print('menor de 0,7')
                        krell = ((factorrelleno - 0.2) * 10) * 0.023
                        print('krell=')
                        print(krell)
                        fsimpledoble = 1

                    else:
                        print('mayor 0,7')
                        krell = ((factorrelleno - 0.2) * 10) * 0.0124
                        fsimpledoble = 1
                        print('krell=')
                        print(krell)

                elif self.ui.rbdobleU.isChecked():
                    if factorrelleno <= 0.7:
                        krell = (((factorrelleno - 0.2) * 10) * 0.024)
                        fsimpledoble = 0.75

                    else:
                        krell = (((factorrelleno - 0.2) * 10) * 0.0075)
                        fsimpledoble = 0.75

            elif self.ui.cbsondas.currentIndex() == 0:
                krell = 0
                fsimpledoble = 1

            elif self.ui.cbsondas.currentIndex() == 2:
                krell = 0
                fsimpledoble = 1

            resperffinalrell = (resperffinal - (resperffinal * krell)) * fsimpledoble

            self.ui.lelongitud.setText("%.2f" % float(resperffinalrell))
        except:
            ctypes.windll.user32.MessageBoxW(0, "Los datos de la pestaña DATOS INICIALES no han sido completados.", "Error",0)

    def disfinal(self):
        hacercalculo2 = True

        try:
            ltotal = float(self.ui.lelongitud.text())
            print(ltotal)
        except:
            ctypes.windll.user32.MessageBoxW(0, "Debe pulsar antes el boton calcular.", "Error", 0)
            hacercalculo2 = False

        if hacercalculo2 == True:
            index = self.ui.cbsondas.currentIndex()
            if index == 2:
                self.ui.gbinstvertsim.hide()
                self.ui.gbinstvertsim_2.hide()
                self.ui.gbinsthoriz.hide()
                self.ui.gbhelicoidalfinal.show()
            elif index == 1:
                print('dentro del if vertical')
                if self.ui.rbsimpleU.isChecked():
                    print('dentro del if rvsimleU check')
                    self.ui.gbhelicoidalfinal.hide()
                    self.ui.gbinstvertsim_2.hide()
                    self.ui.gbinsthoriz.hide()
                    self.ui.gbinstvertsim.show()
                    print('final if rbsimpleU')

                elif self.ui.rbdobleU.isChecked():
                    print('dentro del if rvdobleeU check')
                    self.ui.gbhelicoidalfinal.hide()
                    self.ui.gbinstvertsim_2.show()
                    self.ui.gbinsthoriz.hide()
                    self.ui.gbinstvertsim.hide()
                    print('finsl del if rbdbleU check')

            elif index == 0:
                self.ui.gbinstvertsim.hide()
                self.ui.gbhelicoidalfinal.hide()
                self.ui.gbinstvertsim_2.hide()
                self.ui.gbinsthoriz.show()

            ltotalhel = ltotal / 2
            dhelicoidal = 500
            nsondeoshel = ltotal / 4

            ancho = float(self.ui.leancho.text())
            largo = float(self.ui.lelargo.text())
            ltotaldis = ancho * largo

            self.ui.lesuphord.setText("%.2f" % float(ltotaldis))
            ltotalhorz = ltotal / 2
            self.ui.lesuphorn.setText("%.2f" % float(ltotalhorz))

            if ltotaldis > ltotalhorz:
                self.ui.lbtick.show()
                self.ui.lbcruz.hide()

            elif ltotaldis < ltotalhorz:
                self.ui.lbtick.hide()
                self.ui.lbcruz.show()

                self.ui.checkBoxha.setEnabled(False)
                self.ui.checkBoxha.setStyleSheet("color: black")
                self.ui.checkBoxha.setAttribute(QtCore.Qt.WA_AlwaysShowToolTips)

            self.ui.lesuphord_2.setText("%.2f" % float(ltotaldis))
            lespiral = float(self.ui.lesuphorn.text())
            lespiral2 = lespiral / 4

            self.ui.lesuphorzn_2.setText("%.2f" % float(lespiral2))

            if ltotaldis > lespiral2:
                self.ui.lbtick2.show()
                self.ui.lbcruz2.hide()

            elif ltotaldis < lespiral2:
                self.ui.lbtick2.hide()
                self.ui.lbcruz2.show()

            lsimpleU = float(self.ui.lelongitud.text())
            lsondeosimpleU = lsimpleU / 2
            lnumsondeossimpleU = lsondeosimpleU / 130

            self.ui.lelongtotalvs.setText("%f" % float(lsondeosimpleU))
            self.ui.lenumsondeosvs.setText("%f" % float(lnumsondeossimpleU))
            var1 = float(self.ui.lelongtotalvs.text())
            var2 = float(self.ui.lenumsondeosvs.text())
            longsondeosimpleU = var1 / var2
            self.ui.lelongsondeovs.setText("%f" % float(longsondeosimpleU))

            lsondeosimpleU2 = (lsimpleU / 2) + (0.1 *lsimpleU / 2)
            lnumsondeossimpleU2 = lsondeosimpleU2 / 80

            self.ui.lelongtotalvs_2.setText("%f" % float(lsondeosimpleU2))
            self.ui.lenumsondeosvs_2.setText("%f" % float(lnumsondeossimpleU2))
            var3 = float(self.ui.lelongtotalvs_2.text())
            var4 = float(self.ui.lenumsondeosvs_2.text())
            longsondeosimpleU2 = var3 / var4
            self.ui.lelongsondeovs_2.setText("%f" % float(longsondeosimpleU2))

            lsondeosimpleU3 = (lsimpleU / 2) + (0.15 * lsimpleU / 2)
            lnumsondeossimpleU3 = lsondeosimpleU2 / 60

            self.ui.lelongtotalvs_3.setText("%f" % float(lsondeosimpleU3))
            self.ui.lenumsondeosvs_3.setText("%f" % float(lnumsondeossimpleU3))
            var5 = float(self.ui.lelongtotalvs_3.text())
            var6 = float(self.ui.lenumsondeosvs_3.text())
            longsondeosimpleU3 = var5 / var6
            self.ui.lelongsondeovs_3.setText("%f" % float(longsondeosimpleU3))

            self.ui.lelongtotalvs_7.setText("%.0f" % float(lsondeosimpleU))
            self.ui.lenumsondeosvs_7.setText("%.0f" % float(lnumsondeossimpleU))
            self.ui.lelongsondeovs_7.setText("%.0f" % float(longsondeosimpleU))

            self.ui.lelongtotalvs_8.setText("%.0f" % float(lsondeosimpleU2))
            self.ui.lenumsondeosvs_8.setText("%.0f" % float(lnumsondeossimpleU2))
            self.ui.lelongsondeovs_8.setText("%.0f" % float(longsondeosimpleU2))

            self.ui.lelongtotalvs_9.setText("%.0f" % float(lsondeosimpleU3))
            self.ui.lenumsondeosvs_9.setText("%.0f" % float(lnumsondeossimpleU3))
            self.ui.lelongsondeovs_9.setText("%.0f" % float(longsondeosimpleU3))

            diagonal = math.pow(((ancho * ancho) + (largo * largo)),0.5)
            self.ui.lediamperfovs.setText("%.0f" % float(diagonal))

            if var2 == 1:
               dissondeo = 0
               self.ui.lediamperfovs.setText("%.0f" % float(dissondeo))
            else:
                if var2 > 1:
                    dissondeo = diagonal / (var2 - 1)
                    self.ui.lediamperfovs.setText("%.0f" % float(dissondeo))
                else:
                    self.ui.lediamperfovs.setText('0')

            if var4 > 1:
                dissondeo2 = diagonal / (var4 - 1)
                self.ui.lediamperfovs_2.setText("%.0f" % float(dissondeo2))
            else:
                self.ui.lediamperfovs_2.setText('0')

            if var6 > 1:
                dissondeo3 = diagonal / (var6 - 1)
                self.ui.lediamperfovs_3.setText("%.0f" % float(dissondeo3))
            else:
                self.ui.lediamperfovs_3.setText('0')

            if var2 == 1:
               dissondeo4 = 0
               self.ui.lediamperfovs_7.setText("%.0f" % float(dissondeo4))
            else:
                if var2 > 1:
                    dissondeo4 = diagonal / (var2 - 1)
                    self.ui.lediamperfovs_7.setText("%.0f" % float(dissondeo4))
                else:
                    self.ui.lediamperfovs_7.setText('0')
            if var4 > 1:
                dissondeo5 = diagonal / (var4 - 1)
                self.ui.lediamperfovs_8.setText("%.0f" % float(dissondeo5))
            else:
                self.ui.lediamperfovs_8.setText('0')

            if var6 > 1:
                dissondeo6 = diagonal / (var6 - 1)
                self.ui.lediamperfovs_9.setText("%.0f" % float(dissondeo6))
            else:
                self.ui.lediamperfovs_9.setText('0')


            longitudhelicoidal = ltotal / 16
            self.ui.lelongtotalhel.setText("%.0f" % float(longitudhelicoidal))
            numsondeoshelicoidal = longitudhelicoidal / 25
            self.ui.lenumsondeoshel.setText("%.0f" % float(numsondeoshelicoidal))
            lsondeohelicoidal = longitudhelicoidal / numsondeoshelicoidal
            self.ui.lelongsondeohel.setText("%.0f" % float(lsondeohelicoidal))

            dissondeohel1 = float(self.ui.lenumsondeoshel.text())

            if dissondeohel1 == 1:
               dissondeohel11 = 0
               self.ui.lediamperfhel.setText("%.0f" % float(dissondeohel11))

            else:
                dissondeohel11 = diagonal / (numsondeoshelicoidal - 1)
                self.ui.lediamperfhel.setText("%.0f" % float(dissondeohel11))

            longitudhelicoidal2 = (ltotal / 16) + (0.08 * (ltotal / 16))
            self.ui.lelongtotalhel_2.setText("%.0f" % float(longitudhelicoidal2))

            numsondeoshelicoidal2 = longitudhelicoidal2 / 15
            self.ui.lenumsondeoshel_2.setText("%.0f" % float(numsondeoshelicoidal2))

            lsondeohelicoidal2 = longitudhelicoidal2 / numsondeoshelicoidal2
            self.ui.lelongsondeohel_2.setText("%.0f" % float(lsondeohelicoidal2))

            dissondeohel2 = diagonal / (numsondeoshelicoidal2 - 1)
            self.ui.lediamperfhel_2.setText("%.0f" % float(dissondeohel2))

            longitudhelicoidal3 = (ltotal / 16) + (0.12 * (ltotal / 16))
            self.ui.lelongtotalhel_3.setText("%.0f" % float(longitudhelicoidal3))

            numsondeoshelicoidal3 = longitudhelicoidal3 / 5
            self.ui.lenumsondeoshel_3.setText("%.0f" % float(numsondeoshelicoidal3))

            lsondeohelicoidal3 = longitudhelicoidal3 / numsondeoshelicoidal3
            self.ui.lelongsondeohel_3.setText("%.0f" % float(lsondeohelicoidal3))

            dissondeohel3 = diagonal / (numsondeoshelicoidal3 - 1)
            self.ui.lediamperfhel_3.setText("%.0f" % float(dissondeohel3))

    def inversioninicial(self):
        try:
            metrostotales = float(self.ui.lelongtotalvs_7.text())
            costeperforacion = metrostotales * 45
            self.ui.leperforaciones.setText("%.2f" % float(costeperforacion))
            self.ui.lemrelleno.setText("%.2f" % float(0.0))
            #costeperforacionhorizontal
            if self.ui.cbsondas.currentIndex() == 0:
                self.ui.lemrelleno.setText("%.2f" % float(0.0))
                self.ui.leperforaciones.setText("%.2f" % float(0.0))
                if self.ui.checkBoxha.isChecked():
                    superficienec = float(self.ui.lesuphorn.text())
                    costesuperhor = superficienec * 1 * 16
                    self.ui.lemtierra.setText("%.2f" % float(costesuperhor))
                if self.ui.checkBoxhb.isChecked():
                    superficienec2 = float(self.ui.lesuphorzn_2.text())
                    costesuperhor2 = superficienec2 * 1 * 16
                    self.ui.lemtierra.setText("%.2f" % float(costesuperhor2))

            # costeperforacionverticalsimple
            if self.ui.cbop1.isChecked():
                prlongs1 = float(self.ui.lelongtotalvs.text())
                rotooinver = self.ui.lemetodoperf.text()
                if rotooinver == 'Rotopercusion':
                    prtotals1 = prlongs1 * 44
                    self.ui.leperforaciones.setText("%.2f" % float(prtotals1))
                elif rotooinver == 'Circulacion Inversa':
                    prtotals1 = prlongs1 * 100
                    self.ui.leperforaciones.setText("%.2f" % float(prtotals1))

            if self.ui.cbop2.isChecked():
                prlongs2 = float(self.ui.lelongtotalvs_2.text())
                rotooinver2 = self.ui.lemetodoperf.text()
                if rotooinver2 == 'Rotopercusion':
                    prtotals2 = prlongs2 * 44
                    self.ui.leperforaciones.setText("%.2f" % float(prtotals2))
                elif rotooinver2 == 'Circulacion Inversa':
                    prtotals2 = prlongs2 * 100
                    self.ui.leperforaciones.setText("%.2f" % float(prtotals2))

            if self.ui.cbop3.isChecked():
                prlongs3 = float(self.ui.lelongtotalvs_3.text())
                rotooinver3 = self.ui.lemetodoperf.text()
                if rotooinver3 == 'Rotopercusion':
                    prtotals3 = prlongs3 * 44
                    self.ui.leperforaciones.setText("%.2f" % float(prtotals3))
                elif rotooinver3 == 'Circulacion Inversa':
                    prtotals3 = prlongs3 * 100
                    self.ui.leperforaciones.setText("%.2f" % float(prtotals3))

            if self.ui.cbsondas.currentIndex() == 1:
                ancho = float(self.ui.leancho.text())
                largo = float(self.ui.lelargo.text())
                if ancho > largo:
                    mtierra = ancho * 16
                elif largo > ancho:
                    mtierra = largo * 16
                else:
                    mtierra = largo * 16
                self.ui.lemtierra.setText("%.2f" % float(mtierra))

            # costeperforacionhelicoidal
            if self.ui.cbop1_2.isChecked():
                prlongs1_2 = float(self.ui.lelongtotalhel.text())
                prtotals1_2 = prlongs1_2 * 60
                self.ui.leperforaciones.setText("%.2f" % float(prtotals1_2))
            if self.ui.cbop2_2.isChecked():
                prlongs2_2 = float(self.ui.lelongtotalhel_2.text())
                prtotals2_2 = prlongs2_2 * 60
                self.ui.leperforaciones.setText("%.2f" % float(prtotals2_2))
            if self.ui.cbop3_2.isChecked():
                prlongs3_2 = float(self.ui.lelongtotalhel_3.text())
                prtotals3_2 = prlongs3_2 * 60
                self.ui.leperforaciones.setText("%.2f" % float(prtotals3_2))

            if self.ui.cbsondas.currentIndex() == 2:
                ancho2 = float(self.ui.leancho.text())
                largo2 = float(self.ui.lelargo.text())
                if ancho2 > largo2:
                    mtierra2 = ancho2 * 16
                elif largo2 > ancho2:
                    mtierra2 = largo2 * 16
                else:
                    mtierra2 = largo2 * 16
                self.ui.lemtierra.setText("%.2f" % float(mtierra2))


            # costeperforacionverticaldoble
            if self.ui.cbop1_3.isChecked():
                prlongs1_3 = float(self.ui.lelongtotalvs_7.text())
                prtotals1_3 = prlongs1_3 * 44
                self.ui.leperforaciones.setText("%.2f" % float(prtotals1_3))
            if self.ui.cbop2_3.isChecked():
                prlongs2_3 = float(self.ui.lelongtotalvs_8.text())
                prtotals2_3 = prlongs2_3 * 44
                self.ui.leperforaciones.setText("%.2f" % float(prtotals2_3))

            if self.ui.cbop3_3.isChecked():
                prlongs3_3 = float(self.ui.lelongtotalvs_9.text())
                prtotals3_3 = prlongs3_3 * 44
                self.ui.leperforaciones.setText("%.2f" % float(prtotals3_3))

            pbombacalor = float(self.ui.lepotenciafinal.text())
            costebc = (math.log(pbombacalor) * 2639.8) + 6091.4
            self.ui.lebombadecalor.setText("%.2f" % float(costebc))

            if pbombacalor < 10:
                caccesorios = 2887
                self.ui.lebombadecalor_2.setText("%.2f" % float(caccesorios))
            if pbombacalor > 10:
                caccesorios2 = 3464
                self.ui.lebombadecalor_2.setText("%.2f" % float(caccesorios2))

            cfluido = float(self.ui.lelongitud.text())
            costefluidoperf = 0.00125 * cfluido * 1250
            self.ui.lefluido.setText("%.2f" % float(costefluidoperf))

            # costeperforacionverticalsimple
            if self.ui.cbop1.isChecked():
                longop1 = float(self.ui.lelongtotalvs.text())
                relleval = self.ui.cbrelleno.currentIndex()
                if relleval == 1:
                    precio = float(2.85 * 1.04)
                if relleval == 2:
                    precio = float(1.10 * 0.22)
                if relleval == 3:
                    precio = float(0.72 * 0.14)
                if relleval == 4:
                    precio = float(2.85 * 1.04)
                if relleval == 5:
                    precio = float(0.11 * 0.0067)
                if relleval == 6:
                    precio = float(0.11 * 0.0067)
                if relleval == 7:
                    precio = float(0.19 * 0.012)
                if relleval == 8:
                    precio = float(0.19 * 0.012)
                if relleval == 9:
                    precio = float(3.32 * 0.7)
                totalrelleno = longop1 * precio

                self.ui.lemrelleno.setText("%.2f" % float(totalrelleno))

            if self.ui.cbop2.isChecked():
                longop2 = float(self.ui.lelongtotalvs_2.text())
                relleval2 = self.ui.cbrelleno.currentIndex()
                if relleval2 == 1:
                    precio2 = float(2.85 * 1.04)
                if relleval2 == 2:
                    precio2 = float(1.10 * 0.22)
                if relleval2 == 3:
                    precio2 = float(0.72 * 0.14)
                if relleval2 == 4:
                    precio2 = float(2.85 * 1.04)
                if relleval2 == 5:
                    precio2 = float(0.11 * 0.0067)
                if relleval2 == 6:
                    precio2 = float(0.11 * 0.0067)
                if relleval2 == 7:
                    precio2 = float(0.19 * 0.012)
                if relleval2 == 8:
                    precio2 = float(0.19 * 0.012)
                if relleval2 == 9:
                    precio2 = float(3.32 * 0.7)

                totalrelleno2 = longop2 * precio2

                self.ui.lemrelleno.setText("%.2f" % float(totalrelleno2))

            if self.ui.cbop3.isChecked():
                longop3 = float(self.ui.lelongtotalvs_3.text())
                relleval3 = self.ui.cbrelleno.currentIndex()
                if relleval3 == 1:
                    precio3 = float(2.85 * 1.04)
                if relleval3 == 2:
                    precio3 = float(1.10 * 0.22)
                if relleval3 == 3:
                    precio3 = float(0.72 * 0.14)
                if relleval3 == 4:
                    precio3 = float(2.85 * 1.04)
                if relleval3 == 5:
                    precio3 = float(0.11 * 0.0067)
                if relleval3 == 6:
                    precio3 = float(0.11 * 0.0067)
                if relleval3 == 7:
                    precio3 = float(0.19 * 0.012)
                if relleval3 == 8:
                    precio3 = float(0.19 * 0.012)
                if relleval3 == 9:
                    precio3 = float(3.32 * 0.7)
                totalrelleno3 = longop3 * precio3

                self.ui.lemrelleno.setText("%.2f" % float(totalrelleno3))

            # doble

            if self.ui.cbop1_3.isChecked():
                longop1_3 = float(self.ui.lelongtotalvs_7.text())
                relleval_3 = self.ui.cbrelleno.currentIndex()
                if relleval_3 == 1:
                    precio_3 = float(2.27 * 1.04)
                if relleval_3 == 2:
                    precio_3 = float(0.82 * 0.22)
                if relleval_3 == 3:
                    precio_3 = float(0.58 * 0.14)
                if relleval_3 == 4:
                    precio_3 = float(2.27 * 1.04)
                if relleval_3 == 5:
                    precio_3 = float(0.093 * 0.0067)
                if relleval_3 == 6:
                    precio_3 = float(0.093 * 0.0067)
                if relleval_3 == 7:
                    precio_3 = float(0.15 * 0.012)
                if relleval_3 == 8:
                    precio_3 = float(0.15 * 0.012)
                if relleval_3 == 9:
                    precio_3 = float(2.65 * 0.7)
                totalrelleno_3 = longop1_3 * precio_3

                self.ui.lemrelleno.setText("%.2f" % float(totalrelleno_3))

            if self.ui.cbop2_3.isChecked():
                longop2_3 = float(self.ui.lelongtotalvs_8.text())
                relleval2_3 = self.ui.cbrelleno.currentIndex()
                if relleval2_3 == 1:
                    precio2_3 = float(2.27 * 1.04)
                if relleval2_3 == 2:
                    precio2_3 = float(0.82 * 0.22)
                if relleval2_3 == 3:
                    precio2_3 = float(0.58 * 0.14)
                if relleval2_3 == 4:
                    precio2_3 = float(2.27 * 1.04)
                if relleval2_3 == 5:
                    precio2_3 = float(0.093 * 0.0067)
                if relleval2_3 == 6:
                    precio2_3 = float(0.093 * 0.0067)
                if relleval2_3 == 7:
                    precio2_3 = float(0.15 * 0.012)
                if relleval2_3 == 8:
                    precio2_3 = float(0.15 * 0.012)
                if relleval2_3 == 9:
                    precio2_3 = float(2.65 * 0.7)
                totalrelleno2_3 = longop2_3 * precio2_3

                self.ui.lemrelleno.setText("%.2f" % float(totalrelleno2_3))

            if self.ui.cbop3_3.isChecked():
                longop3_3 = float(self.ui.lelongtotalvs_9.text())
                relleval3_3 = self.ui.cbrelleno.currentIndex()
                if relleval3_3 == 1:
                    precio3_3 = float(2.27 * 1.04)
                if relleval3_3 == 2:
                    precio3_3 = float(0.82 * 0.22)
                if relleval3_3 == 3:
                    precio3_3 = float(0.58 * 0.14)
                if relleval3_3 == 4:
                    precio3_3 = float(2.27 * 1.04)
                if relleval3_3 == 5:
                    precio3_3 = float(0.093 * 0.0067)
                if relleval3_3 == 6:
                    precio3_3 = float(0.093 * 0.0067)
                if relleval3_3 == 7:
                    precio3_3 = float(0.15 * 0.012)
                if relleval3_3 == 8:
                    precio3_3 = float(0.15 * 0.012)
                if relleval3_3 == 9:
                    precio3_3 = float(2.65 * 0.7)

                totalrelleno3_3 = longop3_3 * precio3_3

                self.ui.lemrelleno.setText("%.2f" % float(totalrelleno3_3))

            if self.ui.cbsondas.currentIndex() == 1:
                if self.ui.rbpe100_2.isChecked():
                    if self.ui.rb32mm_2.isChecked():
                        if self.ui.rbsimpleU.isChecked():
                            preson = 3.5
                            longinte = float(self.ui.lelongitud.text())
                            totalinter = preson * longinte

                            self.ui.leintercam.setText("%.2f" % float(totalinter))

            if self.ui.cbsondas.currentIndex() == 1:
                if self.ui.rbpe100_2.isChecked():
                    if self.ui.rb32mm_2.isChecked():
                        if self.ui.rbdobleU.isChecked():
                            preson2 = 6.5
                            longinte2 = float(self.ui.lelongitud.text())
                            totalinter2 = preson2 * longinte2

                            self.ui.leintercam.setText("%.2f" % float(totalinter2))

            if self.ui.cbsondas.currentIndex() == 1:
                if self.ui.rbpe100_2.isChecked():
                    if self.ui.rb40mm_2.isChecked():
                        if self.ui.rbsimpleU.isChecked():
                            preson3 = 5.2
                            longinte3 = float(self.ui.lelongitud.text())
                            totalinter3 = preson3 * longinte3

                            self.ui.leintercam.setText("%.2f" % float(totalinter3))

            if self.ui.cbsondas.currentIndex() == 1:
                if self.ui.rbpe100_2.isChecked():
                    if self.ui.rb40mm_2.isChecked():
                        if self.ui.rbdobleU.isChecked():
                            preson4 = 9.8
                            longinte4 = float(self.ui.lelongitud.text())
                            totalinter4 = preson4 * longinte4

                            self.ui.leintercam.setText("%.2f" % float(totalinter4))

            if self.ui.cbsondas.currentIndex() == 1:
                if self.ui.rbpexa_2.isChecked():
                    if self.ui.rb32mm_2.isChecked():
                        if self.ui.rbsimpleU.isChecked():
                            preson5 = 5.5
                            longinte5 = float(self.ui.lelongitud.text())
                            totalinter5 = preson5 * longinte5

                            self.ui.leintercam.setText("%.2f" % float(totalinter5))

            if self.ui.cbsondas.currentIndex() == 1:
                if self.ui.rbpexa_2.isChecked():
                    if self.ui.rb32mm_2.isChecked():
                        if self.ui.rbdobleU.isChecked():
                            preson6 = 10.5
                            longinte6 = float(self.ui.lelongitud.text())
                            totalinter6 = preson6 * longinte6

                            self.ui.leintercam.setText("%.2f" % float(totalinter6))

            if self.ui.cbsondas.currentIndex() == 1:
                if self.ui.rbpexa_2.isChecked():
                    if self.ui.rb40mm_2.isChecked():
                        if self.ui.rbsimpleU.isChecked():
                            preson7 = 7.5
                            longinte7 = float(self.ui.lelongitud.text())
                            totalinter7 = preson7 * longinte7

                            self.ui.leintercam.setText("%.2f" % float(totalinter7))

            if self.ui.cbsondas.currentIndex() == 1:
                if self.ui.rbpexa_2.isChecked():
                    if self.ui.rb40mm_2.isChecked():
                        if self.ui.rbdobleU.isChecked():
                            preson8 = 12
                            longinte8 = float(self.ui.lelongitud.text())
                            totalinter8 = preson8 * longinte8

                            self.ui.leintercam.setText("%.2f" % float(totalinter8))

            if self.ui.cbsondas.currentIndex() == 0:
                if self.ui.rbpe100.isChecked():
                    if self.ui.rb32mm.isChecked():
                        presonhor1 = 3.5
                        longihorz1 = float(self.ui.lelongitud.text())
                        totalinterhorz1 = presonhor1 * longihorz1

                        self.ui.leintercam.setText("%.2f" % float(totalinterhorz1))

            if self.ui.cbsondas.currentIndex() == 2:
                if self.ui.rbpe100_3.isChecked():
                    if self.ui.rb32mm_3.isChecked():
                        presonhelic = 10.5
                        longiheli = float(self.ui.lelongitud.text())
                        totalinterhel = presonhelic * longiheli

                        self.ui.leintercam.setText("%.2f" % float(totalinterhel))


            #accesorios
            longitudacce = float(self.ui.lelongitud.text())
            totalacc = (longitudacce * 0.77) + 53 + 24.3 + 220 + 100 + 200
            self.ui.leintercam_2.setText("%.2f" % float(totalacc))

            # #inversion total
            perf = float(self.ui.leperforaciones.text())
            bc = float(self.ui.lebombadecalor.text())
            abc = float(self.ui.lebombadecalor_2.text())
            ft = float(self.ui.lefluido.text())
            if self.ui.cbsondas.currentIndex() == 2:
                mr = 0.0
            else:
                mr = float(self.ui.lemrelleno.text())
            ic = float(self.ui.leintercam.text())
            aic = float(self.ui.leintercam_2.text())
            #

            itotal = perf + bc + abc + ft + mr + aic + ic
            self.ui.letotal.setText("%.2f" % float(itotal))
        except:
            ctypes.windll.user32.MessageBoxW(0, "Los datos de la pestaña DATOS INICIALES y/o PROYECTO no han sido completados.", "Error",0)

    def costeanual(self):
        try:
            if self.ui.cbmanualoauto.currentIndex() == 0:
                demand = float(self.ui.lndemandamanual.text())
                copcoste = float(self.ui.lecop.text())
                fundbomba = (demand / copcoste) * 0.12
                self.ui.lefunbomba.setText("%.2f" % float(fundbomba))
            if self.ui.cbmanualoauto.currentIndex() == 1:
                demand1 = float(self.ui.leautodemanda.text())
                copcoste1 = float(self.ui.lecop.text())
                fundbomba1 = (demand1 / copcoste1) * 0.12
                self.ui.lefunbomba.setText("%.2f" % float(fundbomba1))

            pfinal = float(self.ui.lepotenciafinal.text())
            if pfinal <= 10:
                costemant = 65
            elif pfinal > 10 and pfinal < 20:
                costemant = 85
            else:
                costemant = 120
            self.ui.lemantenimiento.setText("%.2f" % float(costemant))

            fbomb = float(self.ui.lefunbomba.text())
            mantsis = float(self.ui.lemantenimiento.text())
            totalanual = fbomb + mantsis
            self.ui.lecosteanual.setText("%.2f" % float(totalanual))
        except:
            ctypes.windll.user32.MessageBoxW(0, "Los datos de la pestaña DATOS INICIALES y/o PROYECTO no han sido completados.", "Error",0)

    def comparacion(self):
        invGeo = []
        invGas = []
        invElec = []
        invGasoleo = []
        invGLP = []
        indices = []
        hacercalculo2 = True

        try:
            lt = float(self.ui.letotal.text())
            ct = float(self.ui.lecosteanual.text())
        except:
            ctypes.windll.user32.MessageBoxW(0, "Calcular la Inversion Inicial y el Coste Anual primero.", "Error", 0)
            hacercalculo2 = False

        if hacercalculo2 == True:
            for i in range(0,24):
                indices.append(i)

            invGeo.append(float(self.ui.letotal.text()))
            for i in range(1, 25):
                nuevo = invGeo[i - 1] + float(self.ui.lecosteanual.text())
                invGeo.append(nuevo)

            if self.ui.rbgasnatural.isChecked():
                self.ui.leinversiongas.setText("")
                self.ui.lecostegas.setText("")
                self.ui.leinversionelec.setText("")
                self.ui.lecosteelec.setText("")
                self.ui.legasoleo.setText("")
                self.ui.lecostegasoleo.setText("")
                self.ui.leglpinver.setText("")
                self.ui.leglpcoste.setText("")

                inversiongasnat = 2115
                self.ui.leinversiongas.setText("%.2f" % float(inversiongasnat))

                demandagas = float(self.ui.cbmanualoauto.currentIndex())
                if demandagas == 0:
                    gas = float(self.ui.lndemandamanual.text())
                else:
                    gas = float(self.ui.leautodemanda.text())

                costegasnat = 51.24 + (0.061 * gas)
                self.ui.lecostegas.setText("%.2f" % float(costegasnat))


                invGas.append(float(self.ui.leinversiongas.text()))
                for i in range(1, 25):
                    nuevo = invGas[i - 1] + float(self.ui.lecostegas.text())
                    invGas.append(nuevo)

                #     dibujamos la grafica

                plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
                         [invGeo[0], invGeo[1], invGeo[2], invGeo[3], invGeo[4], invGeo[5], invGeo[6], invGeo[7],
                          invGeo[8], invGeo[9], invGeo[10], invGeo[11], invGeo[12], invGeo[13], invGeo[14], invGeo[15],
                          invGeo[16], invGeo[17], invGeo[18], invGeo[19], invGeo[20], invGeo[21], invGeo[22],
                          invGeo[23], invGeo[24]],
                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
                         [invGas[0], invGas[1], invGas[2], invGas[3], invGas[4], invGas[5], invGas[6], invGas[7],
                          invGas[8], invGas[9], invGas[10], invGas[11], invGas[12], invGas[13], invGas[14], invGas[15],
                          invGas[16], invGas[17], invGas[18], invGas[19], invGas[20], invGas[21], invGas[22],invGas[23],
                          invGas[24]])
                plt.legend(('Geotermia', 'Gas Natural'),
                           loc='upper left')
                plt.title('BALANCE ECONOMICO')
                plt.xlabel('Tiempo (Anios)')
                plt.ylabel('Coste acumulado (Euros)')

                plt.savefig('grafica.png')
                plt.close()

                # SI el tamanio de pantalla es mas pequeño hay que redimensionar
                if user32.GetSystemMetrics(0) >= 1656:
                    imgGrafica = QtGui.QImage('grafica.png')
                    remove('grafica.png')
                    pixmap_grafica = QtGui.QPixmap(QtGui.QPixmap.fromImage(imgGrafica))
                else:
                    im1 = Image.open('grafica.png')
                    w = 501
                    h = 370
                    im2 = im1.resize((w, h), Image.BICUBIC)
                    im2.save('resized.png')
                    remove('grafica.png')
                    imgGrafica = QtGui.QImage('resized.png')
                    pixmap_grafica = QtGui.QPixmap(QtGui.QPixmap.fromImage(imgGrafica))
                    remove('resized.png')

                self.ui.lbGrafico.setPixmap(pixmap_grafica)

            elif self.ui.rbelec.isChecked():
                self.ui.leinversiongas.setText("")
                self.ui.lecostegas.setText("")
                self.ui.leinversionelec.setText("")
                self.ui.lecosteelec.setText("")
                self.ui.legasoleo.setText("")
                self.ui.lecostegasoleo.setText("")
                self.ui.leglpinver.setText("")
                self.ui.leglpcoste.setText("")

                demandaelec = float(self.ui.cbmanualoauto.currentIndex())
                if demandaelec == 0:
                    elec = float(self.ui.lndemandamanual.text())
                    inversionmanualelec = ((elec / 2400) * 400) / 1.8
                    self.ui.leinversionelec.setText("%.2f" % float(inversionmanualelec))
                    costeelect = 0.13 * elec
                else:
                    superficievivienda = float(self.ui.lesuperficie.text())
                    inversionelec = (superficievivienda * 20) + 400
                    self.ui.leinversionelec.setText("%.2f" % float(inversionelec))
                    elec2 = float(self.ui.leautodemanda.text())
                    costeelect = 0.13 * elec2

                self.ui.lecosteelec.setText("%.2f" % float(costeelect))
                invElec.append(float(self.ui.leinversionelec.text()))
                for i in range(1, 25):
                    nuevo = invElec[i - 1] + float(self.ui.lecosteelec.text())
                    invElec.append(nuevo)

                #     dibujamos la grafica
                plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
                         [invGeo[0], invGeo[1], invGeo[2], invGeo[3], invGeo[4], invGeo[5], invGeo[6], invGeo[7],
                          invGeo[8], invGeo[9], invGeo[10], invGeo[11], invGeo[12], invGeo[13], invGeo[14],
                          invGeo[15],
                          invGeo[16], invGeo[17], invGeo[18], invGeo[19], invGeo[20], invGeo[21], invGeo[22],
                          invGeo[23], invGeo[24]],
                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
                         [invElec[0],  invElec[1],  invElec[2],  invElec[3],  invElec[4],  invElec[5],  invElec[6],  invElec[7],
                          invElec[8],  invElec[9],  invElec[10], invElec[11], invElec[12], invElec[13], invElec[14], invElec[15],
                          invElec[16], invElec[17], invElec[18], invElec[19], invElec[20], invElec[21], invElec[22], invElec[23],
                          invElec[24]])
                plt.legend(('Geotermia', 'Electricidad'),
                           loc='upper left')
                plt.title('BALANCE ECONOMICO')
                plt.xlabel('Tiempo (Anios)')
                plt.ylabel('Coste acumulado (Euros)')
                plt.savefig('grafica.png')
                plt.close()

                # SI el tamanio de pantalla es mas pequeño hay que redimensionar
                if user32.GetSystemMetrics(0) >= 1656:
                    imgGrafica = QtGui.QImage('grafica.png')
                    remove('grafica.png')
                    pixmap_grafica = QtGui.QPixmap(QtGui.QPixmap.fromImage(imgGrafica))
                else:
                    im1 = Image.open('grafica.png')
                    w = 501
                    h = 370
                    im2 = im1.resize((w, h), Image.BICUBIC)
                    im2.save('resized.png')
                    remove('grafica.png')
                    imgGrafica = QtGui.QImage('resized.png')
                    pixmap_grafica = QtGui.QPixmap(QtGui.QPixmap.fromImage(imgGrafica))
                    remove('resized.png')

                self.ui.lbGrafico.setPixmap(pixmap_grafica)

            elif self.ui.rbdiesel.isChecked():
                self.ui.leinversiongas.setText("")
                self.ui.lecostegas.setText("")
                self.ui.leinversionelec.setText("")
                self.ui.lecosteelec.setText("")
                self.ui.legasoleo.setText("")
                self.ui.lecostegasoleo.setText("")
                self.ui.leglpinver.setText("")
                self.ui.leglpcoste.setText("")

                inversiongasoleo = 3490
                self.ui.legasoleo.setText("%.2f" % float(inversiongasoleo))

                demandagas = float(self.ui.cbmanualoauto.currentIndex())
                if demandagas == 0:
                    gasoleo = float(self.ui.lndemandamanual.text())
                else:
                    gasoleo = float(self.ui.leautodemanda.text())

                costegasoleo = (gasoleo * 0.10) + 72.15
                self.ui.lecostegasoleo.setText("%.2f" % float(costegasoleo))


                invGasoleo.append(float(self.ui.legasoleo.text()))
                for i in range(1, 25):
                    nuevo = invGasoleo[i - 1] + float(self.ui.lecostegasoleo.text())
                    invGasoleo.append(nuevo)

                #     dibujamos la grafica
                plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
                         [invGeo[0], invGeo[1], invGeo[2], invGeo[3], invGeo[4], invGeo[5], invGeo[6], invGeo[7],
                          invGeo[8], invGeo[9], invGeo[10], invGeo[11], invGeo[12], invGeo[13], invGeo[14],
                          invGeo[15],
                          invGeo[16], invGeo[17], invGeo[18], invGeo[19], invGeo[20], invGeo[21], invGeo[22],
                          invGeo[23], invGeo[24]],
                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
                         [invGasoleo[0], invGasoleo[1], invGasoleo[2], invGasoleo[3], invGasoleo[4], invGasoleo[5], invGasoleo[6],
                          invGasoleo[7],
                          invGasoleo[8], invGasoleo[9], invGasoleo[10], invGasoleo[11], invGasoleo[12], invGasoleo[13], invGasoleo[14],
                          invGasoleo[15],
                          invGasoleo[16], invGasoleo[17], invGasoleo[18], invGasoleo[19], invGasoleo[20], invGasoleo[21], invGasoleo[22],
                          invGasoleo[23],
                          invGasoleo[24]])
                plt.legend(('Geotermia', 'Gasoleo'),
                           loc='upper left')
                plt.title('BALANCE ECONOMICO')
                plt.xlabel('Tiempo (Anios)')
                plt.ylabel('Coste acumulado (Euros)')
                plt.savefig('grafica.png')
                plt.close()

                # SI el tamanio de pantalla es mas pequeño hay que redimensionar
                if user32.GetSystemMetrics(0) >= 1656:
                    imgGrafica = QtGui.QImage('grafica.png')
                    remove('grafica.png')
                    pixmap_grafica = QtGui.QPixmap(QtGui.QPixmap.fromImage(imgGrafica))
                else:
                    im1 = Image.open('grafica.png')
                    w = 501
                    h = 370
                    im2 = im1.resize((w, h), Image.BICUBIC)
                    im2.save('resized.png')
                    remove('grafica.png')
                    imgGrafica = QtGui.QImage('resized.png')
                    pixmap_grafica = QtGui.QPixmap(QtGui.QPixmap.fromImage(imgGrafica))
                    remove('resized.png')

                self.ui.lbGrafico.setPixmap(pixmap_grafica)

            elif self.ui.rbglp.isChecked():
                self.ui.leinversiongas.setText("")
                self.ui.lecostegas.setText("")
                self.ui.leinversionelec.setText("")
                self.ui.lecosteelec.setText("")
                self.ui.legasoleo.setText("")
                self.ui.lecostegasoleo.setText("")
                self.ui.leglpinver.setText("")
                self.ui.leglpcoste.setText("")

                inversionglp = 2115 + 2000
                self.ui.leglpinver.setText("%.2f" % float(inversionglp))

                demandagas = float(self.ui.cbmanualoauto.currentIndex())
                if demandagas == 0:
                    glp = float(self.ui.lndemandamanual.text())
                else:
                    glp = float(self.ui.leautodemanda.text())

                costeglp = 115 + (0.10 * glp)
                self.ui.leglpcoste.setText("%.2f" % float(costeglp))

                invGLP.append(float(self.ui.leglpinver.text()))
                for i in range(1, 25):
                    nuevo = invGLP[i - 1] + float(self.ui.leglpcoste.text())
                    invGLP.append(nuevo)

                #     dibujamos la grafica
                plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
                         [invGeo[0], invGeo[1], invGeo[2], invGeo[3], invGeo[4], invGeo[5], invGeo[6], invGeo[7],
                          invGeo[8], invGeo[9], invGeo[10], invGeo[11], invGeo[12], invGeo[13], invGeo[14],
                          invGeo[15],
                          invGeo[16], invGeo[17], invGeo[18], invGeo[19], invGeo[20], invGeo[21], invGeo[22],
                          invGeo[23], invGeo[24]],
                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
                         [invGLP[0], invGLP[1], invGLP[2], invGLP[3], invGLP[4], invGLP[5],
                          invGLP[6],
                          invGLP[7],
                          invGLP[8], invGLP[9], invGLP[10], invGLP[11], invGLP[12], invGLP[13],
                          invGLP[14],
                          invGLP[15],
                          invGLP[16], invGLP[17], invGLP[18], invGLP[19], invGLP[20],
                          invGLP[21], invGLP[22],
                          invGLP[23],
                          invGLP[24]])
                plt.legend(('Geotermia', 'GLP'),
                           loc='upper left')
                plt.title('BALANCE ECONOMICO')
                plt.xlabel('Tiempo (Anios)')
                plt.ylabel('Coste acumulado (Euros)')

                plt.savefig('grafica.png')
                plt.close()

                #SI el tamanio de pantalla es mas pequeño hay que redimensionar
                if user32.GetSystemMetrics(0) >= 1656:
                    imgGrafica = QtGui.QImage('grafica.png')
                    remove('grafica.png')
                    pixmap_grafica = QtGui.QPixmap(QtGui.QPixmap.fromImage(imgGrafica))
                else:
                    im1 = Image.open('grafica.png')
                    w = 501
                    h = 370
                    im2 = im1.resize((w, h), Image.BICUBIC)
                    im2.save('resized.png')
                    remove('grafica.png')
                    imgGrafica = QtGui.QImage('resized.png')
                    pixmap_grafica = QtGui.QPixmap(QtGui.QPixmap.fromImage(imgGrafica))
                    remove('resized.png')

                self.ui.lbGrafico.setPixmap(pixmap_grafica)
            else:
                ctypes.windll.user32.MessageBoxW(0, "Seleccione una de las opciones posibles antes de comparar.","Error", 0)


    def emisiones(self):
        try:
            demandatotal = float(self.ui.cbmanualoauto.currentIndex())
            if demandatotal == 0:
                detotal = float(self.ui.lndemandamanual.text())
            else:
                detotal = float(self.ui.leautodemanda.text())

            coptotal = float(self.ui.lecop.text())
            emisiones = detotal / coptotal
            emgeo = emisiones * 0.357

            self.ui.leco2geo.setText("%.2f" % float(emgeo))

            #Gas natural
            demandagas = float(self.ui.cbmanualoauto.currentIndex())
            if demandagas == 0:
                emgas = float(self.ui.lndemandamanual.text())
            else:
                emgas = float(self.ui.leautodemanda.text())

            emisionesgas = emgas * 0.252
            self.ui.leco2gas.setText("%.2f" % float(emisionesgas))

            #Electricidad
            demandaelec = float(self.ui.cbmanualoauto.currentIndex())
            if demandaelec == 0:
                emelec = float(self.ui.lndemandamanual.text())
            else:
                emelec = float(self.ui.leautodemanda.text())

            emisioneselec = emelec * 0.357
            self.ui.leco2elec.setText("%.2f" % float(emisioneselec))

            #Diesel
            demandagasoleo = float(self.ui.cbmanualoauto.currentIndex())
            if demandagasoleo == 0:
                emgasoleo = float(self.ui.lndemandamanual.text())
            else:
                emgasoleo = float(self.ui.leautodemanda.text())

            emisionesgasoleo = float(emgasoleo * 0.311)
            self.ui.leco2gasoleo.setText("%.2f" % float(emisionesgasoleo))

            #GLP
            demandaglp = float(self.ui.cbmanualoauto.currentIndex())
            if demandaglp == 0:
                emglp = float(self.ui.lndemandamanual.text())
            else:
                emglp = float(self.ui.leautodemanda.text())

            emisionesglp = emglp * 0.254
            self.ui.leco2glp.setText("%.2f" % float(emisionesglp))

            #Grafico de barras
            N = 5
            valores = (emgeo*25, emisionesgas*25, emisioneselec*25, emisionesgasoleo*25, emisionesglp*25)

            ind = np.arange(N)  # the x locations for the groups
            width = 0.5  # the width of the bars: can also be len(x) sequence

            p1 = plt.bar(ind, valores, width, color=['orange', 'blue', 'green', 'yellow', 'cyan'])

            #plt.ylabel('Emisiones CO2 acumuladas (kg)')
            plt.title('Emisiones de Dioxido de Carbono Anio 25 [kg]')
            plt.xticks(ind, ('Geotermia', 'Gas Natural', 'Electricidad', 'Gasoleo', 'GLP'))
            plt.yticks(np.arange(0, 500000, 50000))

            plt.savefig('emisiones.png')
            plt.close()
            imgGrafica = QtGui.QImage('emisiones.png')
            remove('emisiones.png')
            pixmap_grafica = QtGui.QPixmap(QtGui.QPixmap.fromImage(imgGrafica))

            self.ui.lbEmisiones.setPixmap(pixmap_grafica)
        except:
            ctypes.windll.user32.MessageBoxW(0, "Los datos de pestañas anteriores no han sido completados correctamente.", "Error",0)


    def inicioAutomatico(self):
        self.calculardemanda()
        self.ui.cbelectricaogas.setCurrentIndex(1)
        self.calcularPotencia()
        self.botonprueba()
        self.pfinal()
        self.leancho.setText('20')
        self.lelargo.setText('20')



    def electricaogas(self):
        elecogas = self.ui.cbelectricaogas.currentIndex()
        if elecogas == 1:
            rescop = 4
            self.ui.lecop.setText("%.2f" % float(rescop))
        elif elecogas == 2:
            rescop = 1.5
            self.ui.lecop.setText("%.2f" % float(rescop))
        else:
            self.ui.lecop.setText("--No seleccionado--")


    def goToevaluacion(self):
        hacercalculo2 = True
        indice = self.ui.cbsondas.currentIndex()
        if indice == 0:
            if(self.ui.checkBoxha.isChecked() == False and self.ui.checkBoxhb.isChecked() == False):
                 ctypes.windll.user32.MessageBoxW(0, "Seleccione una de las opciones posibles antes de continuar.", "Error", 0)
                 hacercalculo2 = False
        elif indice ==1:
            if (self.ui.cbop1_3.isChecked() == False and self.ui.cbop2_3.isChecked() == False and self.ui.cbop3_3.isChecked() == False and
                self.ui.cbop1.isChecked() == False and self.ui.cbop2.isChecked() == False and self.ui.cbop3.isChecked() == False):
                ctypes.windll.user32.MessageBoxW(0, "Seleccione una de las opciones posibles antes de continuar.",
                                                 "Error", 0)
                hacercalculo2 = False
        else:
            if (self.ui.cbop1_2.isChecked() == False and self.ui.cbop2_2.isChecked() == False and self.ui.cbop3_2.isChecked() == False):
                ctypes.windll.user32.MessageBoxW(0, "Seleccione una de las opciones posibles antes de continuar.",
                                                 "Error", 0)
                hacercalculo2 = False

        if hacercalculo2 == True:
            self.ui.tabWidget.setCurrentIndex(3)

    def goTomedioambiente(self):
        self.ui.tabWidget.setCurrentIndex(4)

app = QApplication(sys.argv)
w = pruebageo()
w.show()
sys.exit(app.exec_())