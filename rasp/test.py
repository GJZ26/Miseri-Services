import modules.LCD_Driver as lcd
from time import sleep

mylcd = lcd.lcd()

mylcd.backlight(0)
sleep(1)
mylcd.backlight(1)
mylcd.lcd_display_string("Hola mundo")
sleep(1)
mylcd.lcd_clear()
mylcd.lcd_display_string("Hola mundo")
