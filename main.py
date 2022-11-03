OLED.init(128, 64)
ESP8266_IoT.init_wifi(SerialPin.P8, SerialPin.P12, BaudRate.BAUD_RATE115200)
ESP8266_IoT.connect_wifi("wifiyann", "147896325123698745")

def on_forever():
    if ESP8266_IoT.wifi_state(False):
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
    else:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
        ESP8266_IoT.connect_kidsiot("70abFYpMBi9xsIzx", "2")
        basic.pause(1000)
    basic.clear_screen()
    basic.pause(1000)
basic.forever(on_forever)

def on_forever2():
    OLED.clear()
    OLED.write_string("température: ")
    OLED.write_num(Environment.octopus_BME280(Environment.BME280_state.BME280_TEMPERATURE_C))
    ESP8266_IoT.upload_kidsiot(Environment.octopus_BME280(Environment.BME280_state.BME280_TEMPERATURE_C))
    basic.pause(5000)
basic.forever(on_forever2)
