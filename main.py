from config import utelegram_config
from config import wifi_config

import utelegram
import network
import utime

from machine import Pin

relay = Pin(26, Pin.OUT)

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.scan()
sta_if.connect(wifi_config['ssid'], wifi_config['password'])

utime.sleep(20)

def start_bot(message):
    bot.send(message['message']['chat']['id'], "Halo, Selamat Datang")

def get_message(message):
    if message['message']['text'].lower() == 'lampu on':
        if relay.value() == 0:
            bot.send(message['message']['chat']['id'],'Lampu Sudah Menyala')
        else:
            relay.value(0)
            bot.send(message['message']['chat']['id'],'Menyalakan Lampu')
    elif message['message']['text'].lower() == 'lampu off':
        if relay.value() == 1:
            bot.send(message['message']['chat']['id'],'Lampu Sudah Mati')
        else:
            relay.value(1)
            bot.send(message['message']['chat']['id'],'Mematikan Lampu')
    else:
        bot.send(message['message']['chat']['id'], 'Perintah tidak ditemukan')

if sta_if.isconnected():
    bot = utelegram.ubot(utelegram_config['token'])
    bot.register('/start', start_bot)
    bot.set_default_handler(get_message)
    print("BOT STANDBY")
    bot.listen()
else:
    print("Gagal Koneksi ke Internet")
