basic.forever(function () {
    pins.digitalWritePin(DigitalPin.P0, 1)
    if (pins.analogReadPin(AnalogPin.P1) > 500) {
        basic.showIcon(IconNames.Happy)
        basic.showNumber(pins.analogReadPin(AnalogPin.P1))
    } else {
        basic.showIcon(IconNames.Sad)
        basic.showNumber(pins.analogReadPin(AnalogPin.P1))
    }
    pins.digitalWritePin(DigitalPin.P0, 0)
    basic.pause(1000)
})
