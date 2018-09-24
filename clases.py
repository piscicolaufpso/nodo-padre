import urllib2
import json
import sys
import socket as sk

class pushetta:
    #funcion que recibe el token con el que se accede, el canal por el cual se envia el mensaje
    def sendNotification(self, token, channel, message):
        data = {
            "body" : message,
            "message_type" : "text/plain"
        }

        req = urllib2.Request('http://api.pushetta.com/api/pushes/{0}/'.format(channel))
        req.add_header('Content-Type', 'application/json')
        req.add_header('Authorization', 'Token {0}'.format(token))

        response = urllib2.urlopen(req, json.dumps(data))


class socket:
    host = "ip del servidor"
    port = "puerto utilizado en el servidor"

    def enviarDatos(self, inp):
        sCliente =  sk.socket()
        sCliente.connect((host, port))
        print("Conectado")
        #ejemplo de envio "1,181,2018-07-22,09:12:10,24.4,NO;1,182,2018-07-22,09:12:10,7.2,NO;2,181,2018-07-22,09:12:10,25.1,NO;2,182,2018-07-22,09:12:10,7.1,NO;"
        salida = inp.encode("UTF8")
        lene = sCliente.send(salida)
        ins = sCliente.recv(512)
        insd = ins.decode("UTF8")
        print("Servidor retorna:", insd)
        sCliente.close()

    def extraerDatos(self):
        sCliente =  sk.socket()
        sCliente.connect((host, port))
        print("Conectado")
        inp = "extraer"
        salida = inp.encode("UTF8")
        lene = sCliente.send(salida)
        ins = sCliente.recv(512)
        insd = ins.decode("UTF8")
        sCliente.close()
        return insd