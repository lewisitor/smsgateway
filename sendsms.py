import serial
import time

class TextMessage:
        def __init__(self, recipient="+237676036219", message="TextMessage.content not set."):
            self.recipient = recipient
            self.content = message

        def setRecipient(self, number):
            self.recipient = number

        def setContent(self, message):
            self.content = message

        def connectPhone(self):
            self.ser = serial.Serial('COM12', 460800, timeout=5, xonxoff = False, rtscts = False, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE)
            time.sleep(1)

        def sendMessage(self):
           # self.ser.write('ATZ\r')
            #time.sleep(1)
           
            start_cmd='AT+CMGF=1\r'
            start_byte=start_cmd.encode('utf-8')

            num_cmd='AT+CMGS="'+self.recipient+'"\r\n'
            num_byte=num_cmd.encode('utf-8')

            msg_cmd=self.content+"\x1A"
            msg_byte=msg_cmd.encode('utf-8')

            self.ser.write(start_byte)
            
            #self.ser.write('AT+CMGF=1\r')
            time.sleep(1)
            self.ser.write(num_byte)
            #self.ser.write('''AT+CMGS="''' + self.recipient + '''"\r''')
            time.sleep(1)
            #self.ser.write(self.content + "\r")
            self.ser.write(msg_byte)
            time.sleep(1)
            #self.ser.write(chr(26))
            #time.sleep(1)

        def disconnectPhone(self):
            self.ser.close()

sms = TextMessage("+237676036219","Mummy i sent this message from my computer")
sms.connectPhone()
sms.sendMessage()
sms.disconnectPhone()
print("message sent successfully")
