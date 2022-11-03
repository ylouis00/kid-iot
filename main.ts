OLED.init(128, 64)
ESP8266_IoT.initWIFI(SerialPin.P8, SerialPin.P12, BaudRate.BaudRate115200)
ESP8266_IoT.connectWifi("wifiyann", "147896325123698745")
basic.forever(function on_forever() {
    if (ESP8266_IoT.wifiState(false)) {
        basic.showLeds(`
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        `)
    } else {
        basic.showLeds(`
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        `)
        ESP8266_IoT.connectKidsiot("70abFYpMBi9xsIzx", "2")
        basic.pause(1000)
    }
    
    basic.clearScreen()
    basic.pause(1000)
})
basic.forever(function on_forever2() {
    OLED.clear()
    OLED.writeString("température: ")
    OLED.writeNum(Environment.octopus_BME280(Environment.BME280_state.BME280_temperature_C))
    ESP8266_IoT.uploadKidsiot(Environment.octopus_BME280(Environment.BME280_state.BME280_temperature_C))
    basic.pause(5000)
})
