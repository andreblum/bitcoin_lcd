import json
import time
import urllib2
from lcd import lcd_i2c

def btc():
    s = urllib2.urlopen("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC&tsyms=EUR").read()
    prices = json.loads(s)

    return { 
        'btc': prices['BTC']['EUR'],
        'eth': prices['ETH']['EUR'],
        'ltc': prices['LTC']['EUR'],
    }



if __name__ == '__main__':
    lcd_i2c.lcd_init()
    while True:
        try:
            r = btc()
            lcd_i2c.lcd_string("BTC = %6.2f" % r['btc'],lcd_i2c.LCD_LINE_1)
            lcd_i2c.lcd_string("ETH = %6.2f" % r['eth'],lcd_i2c.LCD_LINE_2)
        except:
            lcd_i2c.lcd_string("BTC = ------.--",lcd_i2c.LCD_LINE_1)
            lcd_i2c.lcd_string("ETH = ------.--",lcd_i2c.LCD_LINE_2)
        time.sleep(20)
