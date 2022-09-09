import esptool
SerialPort =''
assert SerialPort!='', 'Oh no! SerialPort is not set'

try:
    cmd =  [
            '--port', SerialPort,
            'flash_id'
            ]
    esptool.main(cmd)
except:
    print('On no! Serial port named :', SerialPort,'was not found' )