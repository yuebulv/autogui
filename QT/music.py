import winsound


def qt_beep(n=3):
    duration = 1000  # millisecond
    freq = 440  # Hz
    for i in range(n):
        winsound.Beep(freq, duration)