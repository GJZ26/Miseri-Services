import modules.LCD_Driver as lcd


class LCD:

    screen: lcd.lcd = None
    alien = [[0x00, 0x1f, 0x15, 0x1f, 0x1f, 0x0e, 0x0a, 0x1b]]

    def __init__(self):
        self.screen = lcd.lcd()
        self.screen.lcd_load_custom_chars(self.alien)

    def welcomeScreen(self):
        self.screen.lcd_clear()
        self.screen.lcd_display_string("Miseri Sense", 1, 2)
        self.screen.lcd_write(0xC0)
        self.screen.lcd_display_string("", 2, 5)
        self.screen.lcd_write_char(0)
        self.screen.lcd_display_string("", 2, 7)
        self.screen.lcd_write_char(0)
        self.screen.lcd_display_string("", 2, 9)
        self.screen.lcd_write_char(0)

    def clear(self):
        self.screen.lcd_clear()

    def say(self, message: str = None):
        if message is None:
            self.welcomeScreen()
            return
        self.screen.lcd_display_string(message)
