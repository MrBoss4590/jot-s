basic.forever(function () {
    music.play(music.stringPlayable("G A B F - C5 E C ", 286), music.PlaybackMode.UntilDone)
    basic.showLeds(`
        . . . . .
        # # # . .
        # . # . .
        # . # . .
        # # # . .
        `)
    basic.showLeds(`
        # . . # .
        # . # . .
        # # . . .
        # # . . .
        # . # . .
        `)
})
