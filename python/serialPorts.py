import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

for port, desc, hwid in sorted(ports):
        print("SerialPort : {}\n\tRS232 driver: {}\n\tUSB-Info: [{}]\n".format(port, desc, hwid))
        
