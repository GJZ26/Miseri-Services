import modules.LCD_Driver as lcd
from time import sleep

mylcd = lcd.lcd()

mylcd.backlight(0)
sleep(2)
mylcd.backlight(1)
mylcd.lcd_display_string("Hola mundo")
sleep(2)
mylcd.lcd_clear()
mylcd.lcd_display_string("Hola mundo")
sleep(2)

mylcd.lcd_clear()

fontdata1 = [
    # Char 0 - Upper-left
    [0x00, 0x00, 0x03, 0x04, 0x08, 0x19, 0x11, 0x10],
    # Char 1 - Upper-middle
    [0x00, 0x1F, 0x00, 0x00, 0x00, 0x11, 0x11, 0x00],
    # Char 2 - Upper-right
    [0x00, 0x00, 0x18, 0x04, 0x02, 0x13, 0x11, 0x01],
    # Char 3 - Lower-left
    [0x12, 0x13, 0x1b, 0x09, 0x04, 0x03, 0x00, 0x00],
    # Char 4 - Lower-middle
    [0x00, 0x11, 0x1f, 0x1f, 0x0e, 0x00, 0x1F, 0x00],
    # Char 5 - Lower-right
    [0x09, 0x19, 0x1b, 0x12, 0x04, 0x18, 0x00, 0x00],
    # Char 6 - my test
    [0x1f, 0x0, 0x4, 0xe, 0x0, 0x1f, 0x1f, 0x1f],
]

mylcd.lcd_load_custom_chars(fontdata1)