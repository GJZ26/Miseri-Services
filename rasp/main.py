import receiver

espReader = receiver.Receiver(None,"COM3")
espReader.connect()

try:
    while True:
        linea = espReader.readSerial()
        if linea is None or linea == 1:
            pass
        else:
            print(linea)
        pass
except KeyboardInterrupt:
    pass