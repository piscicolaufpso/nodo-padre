import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev
from clases import pushetta
from clases import socket

GPIO.setmode(GPIO.BCM)

pipes = [[0xE8, 0xE8, 0xF0, 0xF0, 0xE1], [0xF0, 0xF0, 0xF0, 0xF0, 0xE1], [0xF0, 0xF0, 0xF0, 0xF0, 0xE2]]

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0,17)

radio.setPayloadSize(32)
radio.setChannel(0x76)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)

radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

radio.openReadingPipe(1, pipes[1])
radio.openReadingPipe(2, pipes[2])
radio.printDetails()
radio.startListening()

p = pushetta()
s = socket()
localtime = time.localtime(time.time())
hora_datos_insertar = 1 if localtime.tm_min > 55 else localtime.tm_min + 5
hora_datos_extraer = 1 if localtime.tm_hour > 23 else localtime.tm_hour + 1
salida = s.extraerDatos()
datos = formatearDatos()

while True:
    tiempo_variable = time.localtime(time.time())
    
    while not radio.available(0):
        time.sleep(1/100)

    receivedMessage = []
    radio.read(receivedMessage, radio.getDynamicPayloadSize())
    string = ""
    for n in receivedMessage:
        if(n >= 32 and n <= 126):
            string += chr(n)
    #print("Recivio: {}".format(string))
    if(tiempo_variable.tm_min > hora_datos_insertar):
        analizarEnviar(string, datos)
        #funcion insertar pasando string
    if(tiempo_variable.tm_hour > hora_datos_extraer):
        salida = s.extraerDatos()
        datos = formatearDatos()


def formatearDatos(self, datosEntrada):
    datos = cadena.split(";")
    salida = []
    for x in range(0,len(datos)):
        salida.append(datos[x].split(","))
    #pes_nombre|pesc_id|pece_nombre|sens_nombre|sens_id|rang_maximo|rang_minimo
    return salida

def analizarEnviar(self, datos, valores):
    string = "" 
    tiempo = time.localtime(time.time())
    #ejemplo de envio "1,181,2018-07-22,09:12:10,24.4,NO;1,182,2018-07-22,09:12:10,7.2,NO;2,181,2018-07-22,09:12:10,25.1,NO;2,182,2018-07-22,09:12:10,7.1,NO;"
    pecera = datos.cadena(";")
    for x in range(0,len(pecera)):
        data = pecera[x].split("/")
        string += data[0].","
        string += tiempo.tm_year."-".tiempo.tm_mon."-".tiempo.tm_mday.",".tiempo.tm_hour.":".tiempo.tm_min.":".tiempo.tm_sec.","
        incidencia = "NO"
        for i range(1, leng(data))
            valor = data.split(":")
            string += valor[0].",".valor[1].","
            for i in range(len(valores)):
                if (valores[i][4]==valor[0]):
                    if(valores[i][5]<valor[1]):
                        p.sendNotification("token_pushetta","canal_pushetta","Valor de ".valor[0]." : ".valor[1]." demasiado alto para el pez en pecera ".data[0])
                        incidencia = "SI"
                    elif(valore[i][6]>valor[1]):
                        p.sendNotification("token_pushetta","canal_pushetta","Valor de ".valor[0]." : ".valor[1]." demasiado bajo para el pez en pecera ".data[0])
                        incidencia = "SI"
                string += incidencia.";"
    s.enviarDatos(string)        

            

        