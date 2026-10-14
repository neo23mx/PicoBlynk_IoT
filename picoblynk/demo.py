from machine import Pin

class Device:
    def __init__(self, mqtt):
        self.mqtt = mqtt
        self.led = Pin("LED", Pin.OUT)
        self.led.value(0)

    def connected(self):
        print("Esperando comandos del boton V0...")
        self.mqtt.publish("get/ds", "V0")

    def process_message(self, topic, payload):
        print("Mensaje:", topic, payload)

        if topic =="downlink/ds/Switch Control":
            estado = int(payload)
            self.led.value(estado)
            print("LED encendido" if estado else "LED apagado")

    def update(self):
        pass