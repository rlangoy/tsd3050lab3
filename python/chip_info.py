import esptool
SerialPort ='com68'
cmd =  [
        '--port', SerialPort,
        'flash_id'
        ]
esptool.main(cmd)