
###################################################

#Tested in Ubuntu 18.04 and 19.10

#Install the following packages

# sudo apt install tesseract-ocr
# sudo apt install tesseract-ocr-eng
# sudo apt install python3-pip
# sudo pip3 install opencv-python
# sudo pip3 install setuptools
# sudo pip3 install pytesseract
# sudo apt install openvpn
#sudo apt install wget

# execute the following command on your terminal 
#(inside the directory) 

# python3 vpn.py

# Ctrl + C for cancel

###################################################
#import webbrowser
import numpy as np
from urllib.request import urlopen
import cv2
import os
import pytesseract as ocr
from PIL import Image
import os
import zipfile

current_path = os.getcwd()
try: os.mkdir(current_path)
except:pass


def us1():
    while 1:
        print("Choose VPNs File:")
        print("1 - vpnbook-us1-tcp80.ovpn")
        print("2 - vpnbook-us1-tcp443.ovpn")
        print("3 - vpnbook-us1-udp53.ovpn")
        print("4 - vpnbook-us1-udp25000.ovpn")
        print("5 - Home")
        print("Enter a number: ", end="")
        v = input()
        s = ''
        if v == "1":
            vpn("vpnbook-us1-tcp80.ovpn")
        elif v == "2":
            vpn("vpnbook-us1-tcp443.ovpn")
        elif v == "3":
            vpn("vpnbook-us1-udp53.ovpn")
        elif v == "4":
            vpn("vpnbook-us1-udp25000.ovpn")
        elif v == "5":
            home()
        else:
            os.system("clear")
            print("Number invalid!")

def us2():
    while 1:
        print("Choose VPNs File:")
        print("1 - vpnbook-us2-tcp80.ovpn")
        print("2 - vpnbook-us2-tcp443.ovpn")
        print("3 - vpnbook-us2-udp53.ovpn")
        print("4 - vpnbook-us2-udp25000.ovpn")
        print("5 - Home")
        print("Enter a number: ", end="")
        v = input()
        s = ''
        if v == "1":
            vpn("vpnbook-us2-tcp80.ovpn")
        elif v == "2":
            vpn("vpnbook-us2-tcp443.ovpn")
        elif v == "3":
            vpn("vpnbook-us2-udp53.ovpn")
        elif v == "4":
            vpn("vpnbook-us2-udp25000.ovpn")
        elif v == "5":
            home()
        else:
            os.system("clear")
            print("Number invalid!")

def ca1():
    while 1:
        print("Choose VPNs File:")
        print("1 - vpnbook-ca198-tcp80.ovpn")
        print("2 - vpnbook-ca198-tcp443.ovpn")
        print("3 - vpnbook-ca198-udp53.ovpn")
        print("4 - vpnbook-ca198-udp25000.ovpn")
        print("5 - Home")
        print("Enter a number: ", end="")
        v = input()
        s = ''
        if v == "1":
            vpn("vpnbook-ca198-tcp80.ovpn")
        elif v == "2":
            vpn("vpnbook-ca198-tcp443.ovpn")
        elif v == "3":
            vpn("vpnbook-ca198-udp53.ovpn")
        elif v == "4":
            vpn("vpnbook-ca198-udp25000.ovpn")
        elif v == "5":
            home()
        else:
            os.system("clear")
            print("Number invalid!")

def ca2():
    while 1:
        print("Choose VPNs File:")
        print("1 - vpnbook-ca222-tcp80.ovpn")
        print("2 - vpnbook-ca222-udp53.ovpn")
        print("3 - vpnbook-ca222-udp25000.ovpn")
        print("4 - Home")
        print("Enter a number: ", end="")
        v = input()
        s = ''
        if v == "1":
            vpn("vpnbook-ca222-tcp80.ovpn")
        elif v == "2":
            vpn("vpnbook-ca222-udp53.ovpn")
        elif v == "3":
            vpn("vpnbook-ca222-udp25000.ovpn")
        elif v == "4":
            home()
        else:
            os.system("clear")
            print("Number invalid!")

def fr1():
    while 1:
        print("Choose VPNs File:")
        print("1 - vpnbook-fr1-tcp80.ovpn")
        print("2 - vpnbook-fr1-udp53.ovpn")
        print("3 - vpnbook-fr1-udp25000.ovpn")
        print("4 - Home")
        print("Enter a number: ", end="")
        v = input()
        s = ''
        if v == "1":
            vpn("vpnbook-fr1-tcp80.ovpn")
        elif v == "2":
            vpn("vpnbook-fr1-udp53.ovpn")
        elif v == "3":
            vpn("vpnbook-fr1-udp25000.ovpn")
        elif v == "4":
            home()
        else:
            os.system("clear")
            print("Number invalid!")

def fr8():
    while 1:
        print("Choose VPNs File:")
        print("1 - vpnbook-fr8-tcp80.ovpn")
        print("2 - vpnbook-fr8-tcp443.ovpn")
        print("3 - vpnbook-fr8-udp53.ovpn")
        print("4 - vpnbook-fr8-udp25000.ovpn")
        print("5 - Home")
        print("Enter a number: ", end="")
        v = input()
        s = ''
        if v == "1":
            vpn("vpnbook-fr8-tcp80.ovpn")
        elif v == "2":
            vpn("vpnbook-fr8-tcp443.ovpn")
        elif v == "3":
            vpn("vpnbook-fr8-udp53.ovpn")
        elif v == "4":
            vpn("vpnbook-fr8-udp25000.ovpn")
        elif v == "5":
            home()
        else:
            os.system("clear")
            print("Number invalid!")

def pl2():
    while 1:
        print("Choose VPNs File:")
        print("1 - vpnbook-pl226-tcp80.ovpn")
        print("2 - vpnbook-pl226-tcp443.ovpn")
        print("3 - vpnbook-pl226-udp53.ovpn")
        print("4 - vpnbook-pl226-udp25000.ovpn")
        print("5 - Home")
        print("Enter a number: ", end="")
        v = input()
        s = ''
        if v == "1":
            vpn("vpnbook-pl226-tcp80.ovpn")
        elif v == "2":
            vpn("vpnbook-pl226-tcp443.ovpn")
        elif v == "3":
            vpn("vpnbook-pl226-udp53.ovpn")
        elif v == "4":
            vpn("vpnbook-pl226-udp25000.ovpn")
        elif v == "5":
            home()
        else:
            os.system("clear")
            print("Number invalid!")

def de4():
    while 1:
        print("Choose VPNs File:")
        print("1 - vpnbook-de4-tcp80.ovpn")
        print("2 - vpnbook-de4-tcp443.ovpn")
        print("3 - vpnbook-de4-udp53.ovpn")
        print("4 - vpnbook-de4-udp25000.ovpn")
        print("5 - Home")
        print("Enter a number: ", end="")
        v = input()
        s = ''
        if v == "1":
            vpn("vpnbook-de4-tcp80.ovpn")
        elif v == "2":
            vpn("vpnbook-de4-tcp443.ovpn")
        elif v == "3":
            vpn("vpnbook-de4-udp53.ovpn")
        elif v == "4":
            vpn("vpnbook-de4-udp25000.ovpn")
        elif v == "5":
            home()
        else:
            os.system("clear")
            print("Number invalid!")

def downloadImage(url):
    try:
        print("Downloading %s" % (url))
        image_name = str(url).split('/')[-1]
        resp = urlopen(url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        cv2.imwrite(image_name, image)
    except Exception as error:
        print(error)

def home():

    os.system("clear")
    
    while 1:
        print("Choose VPNs Locales:")
        print("1 - US1")
        print("2 - US2")
        print("3 - CA1")
        print("4 - CA2")
        print("5 - FR1")
        print("6 - FR8")
        print("7 - PL")
        print("8 - DE4")
        print("9 - Exit")
        print("Enter a number: ", end="")
        v = input()

        if v == "1":
            os.system("clear")
            us1()
        elif v == "2":
            us2()
        elif v == "3":
            ca1()
        elif v == "4":
            ca2()
        elif v == "5":
            fr1()
        elif v == "6":
            fr8()
        elif v == "7":
            pl2()
        elif v == "8":
            de4()
        elif v == "9":
            exit(0)
        else:
            os.system("clear")
            print("Number invalid!")

def vpn(vpn):
    phrase = ocr.image_to_string(Image.open('password.php?.png'))
    s = ''
    for i in phrase:
        if i != '' and i != ' ':
            s += i
    os.system("clear")
    print("Usuário: vpnbook")
    print("Senha atual: " + s)
    os.system("sudo openvpn " + vpn)
    #webbrowser.open('https://whatismyip.com.br', new=0, autoraise=True)

if __name__ == '__main__':
    urls = ["https://www.vpnbook.com/password.php?.png"]
    os.system("rm VPN*")

    os.system("wget https://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-US1.zip")
    os.system("wget https://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-US2.zip")
    os.system("wget https://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-PL226.zip")
    os.system("wget https://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-DE4.zip")
    os.system("wget https://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-CA222.zip")
    os.system("wget https://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-CA198.zip")
    os.system("wget https://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-FR1.zip")
    os.system("wget https://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-FR8.zip")

    fantasy_zip1 = zipfile.ZipFile('VPNBook.com-OpenVPN-US1.zip')
    fantasy_zip2 = zipfile.ZipFile('VPNBook.com-OpenVPN-US2.zip')
    fantasy_zip3 = zipfile.ZipFile('VPNBook.com-OpenVPN-PL226.zip')
    fantasy_zip4 = zipfile.ZipFile('VPNBook.com-OpenVPN-DE4.zip')
    fantasy_zip5 = zipfile.ZipFile('VPNBook.com-OpenVPN-CA222.zip')
    fantasy_zip6 = zipfile.ZipFile('VPNBook.com-OpenVPN-CA198.zip')
    fantasy_zip7 = zipfile.ZipFile('VPNBook.com-OpenVPN-FR1.zip')
    fantasy_zip8 = zipfile.ZipFile('VPNBook.com-OpenVPN-FR8.zip')

    fantasy_zip1.extractall('')
    fantasy_zip1.close()
    fantasy_zip2.extractall('')
    fantasy_zip2.close()
    fantasy_zip3.extractall('')
    fantasy_zip3.close()
    fantasy_zip4.extractall('')
    fantasy_zip4.close()
    fantasy_zip5.extractall('')
    fantasy_zip5.close()
    fantasy_zip6.extractall('')
    fantasy_zip6.close()
    fantasy_zip7.extractall('')
    fantasy_zip7.close()
    fantasy_zip8.extractall('')
    fantasy_zip8.close()
    os.system("rm *zip")
    for url in urls:
        downloadImage(url)
    home()



