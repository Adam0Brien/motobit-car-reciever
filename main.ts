radio.onReceivedValue(function (name, value) {
    motobit.enable(MotorPower.On)
    if (name == "right") {
        timerCounter = 0
        if (value > 65) {
            motobit.setMotorSpeed(Motor.Right, MotorDirection.Forward, 50)
        } else if (value < 35) {
            motobit.setMotorSpeed(Motor.Right, MotorDirection.Reverse, 50)
        } else if (value < 65 && value > 35) {
            motobit.enable(MotorPower.Off)
        }
    } else if (name == "left") {
        timerCounter = 0
        if (value > 65) {
            motobit.setMotorSpeed(Motor.Left, MotorDirection.Forward, 50)
        } else if (value < 35) {
            motobit.setMotorSpeed(Motor.Left, MotorDirection.Reverse, 50)
        } else if (value < 65 && value > 35) {
            motobit.enable(MotorPower.Off)
        }
        timerCounter = 0
    }
})
let timerCounter = 0
radio.setGroup(1)
motobit.enable(MotorPower.On)
timerCounter = 0
basic.showLeds(`
    # . . . #
    . . . . .
    . . # . .
    . . . . .
    # . . . #
    `)
basic.showString("hello")
// heartbeat
basic.forever(function () {
    timerCounter += 1
    if (timerCounter > 5) {
        motobit.enable(MotorPower.Off)
    }
})
