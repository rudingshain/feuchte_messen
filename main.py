def on_forever():
    pins.digital_write_pin(DigitalPin.P0, 1)
    if pins.analog_read_pin(AnalogPin.P1) > 500:
        basic.show_icon(IconNames.HAPPY)
        basic.show_number(pins.analog_read_pin(AnalogPin.P1))
    else:
        basic.show_icon(IconNames.SAD)
        basic.show_number(pins.analog_read_pin(AnalogPin.P1))
    pins.digital_write_pin(DigitalPin.P0, 0)
    basic.pause(1000)
basic.forever(on_forever)