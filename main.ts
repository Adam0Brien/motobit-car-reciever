radio.onReceivedValue(function (name, value) {
    motobit.enable(MotorPower.On)
    if (name == "right") {
        timerCounter = 0
        if (value > 65) {
            motobit.setMotorSpeed(Motor.Right, MotorDirection.Forward, value)
        } else if (value < 35) {
            motobit.setMotorSpeed(Motor.Right, MotorDirection.Reverse, value)
        } else if (value < 65 && value > 35) {
            motobit.enable(MotorPower.Off)
        }
        displayMotorSpeed(3, value)
        displayMotorSpeed(4, value)
    } else if (name == "left") {
        timerCounter = 0
        if (value > 65) {
            motobit.setMotorSpeed(Motor.Left, MotorDirection.Forward, 50)
        } else if (value < 35) {
            motobit.setMotorSpeed(Motor.Left, MotorDirection.Reverse, 50)
        } else if (value < 65 && value > 35) {
            motobit.enable(MotorPower.Off)
        }
        displayMotorSpeed(0, value)
        displayMotorSpeed(1, value)
        timerCounter = 0
    }
})
function displayMotorSpeed (ledColumn2: number, motorSpeed: number) {
    ledRow3 = pins.map(
    motorSpeed,
    0,
    100,
    0,
    4
    )
    for (let index62 = 0; index62 <= 4; index62++) {
        if (index62 < ledRow3) {
            led.unplot(ledColumn2, index62)
        } else {
            led.plot(ledColumn2, index62)
        }
    }
}
let ledRow3 = 0
let timerCounter = 0
radio.setGroup(1)
motobit.enable(MotorPower.On)
timerCounter = 0
// heartbeat
basic.forever(function () {
    timerCounter += 1
    if (timerCounter > 5) {
        motobit.enable(MotorPower.Off)
    }
})
