import network
import socket
import time

class Tello:
    def __init__(self,ssid):
        wifi = network.WLAN(network.STA_IF)
        wifi.active(True)
        wifi.connect(ssid,"")

        while wifi.isconnected() == False:
            print("WiFi({})に接続しようとしています...".format(ssid))
            time.sleep(1)

        wifi_status = wifi.ifconfig()
        print("WiFiに接続されました。")
        print("IPアドレスは {} です。".format(wifi_status[0]))

        self.tello_address = ("192.168.10.1",8889)

        self.tello_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.tello_socket.bind(("",9000))
        self.tello_socket.sendto("command",self.tello_address)

    def sendCommand(self,command):
        print(command)
        self.tello_socket.sendto(command,self.tello_address)
