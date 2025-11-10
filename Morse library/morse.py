from machine import Pin, PWM
import time

# --- Setup ---
buzzer = PWM(Pin(26))
buzzer.duty_u16(0)
FREQ = 700
DOT = 0.1
DASH = 0.3
GAP = 0.1
LETTER_GAP = 0.3
WORD_GAP = 0.7

def beep(duration):
    buzzer.freq(FREQ)
    buzzer.duty_u16(32768)
    time.sleep(duration)
    buzzer.duty_u16(0)
    time.sleep(GAP)

# --- Individual Letter Functions ---
def A(): beep(DOT); beep(DASH)
def B(): beep(DASH); beep(DOT); beep(DOT); beep(DOT)
def C(): beep(DASH); beep(DOT); beep(DASH); beep(DOT)
def D(): beep(DASH); beep(DOT); beep(DOT)
def E(): beep(DOT)
def F(): beep(DOT); beep(DOT); beep(DASH); beep(DOT)
def G(): beep(DASH); beep(DASH); beep(DOT)
def H(): beep(DOT); beep(DOT); beep(DOT); beep(DOT)
def I(): beep(DOT); beep(DOT)
def J(): beep(DOT); beep(DASH); beep(DASH); beep(DASH)
def K(): beep(DASH); beep(DOT); beep(DASH)
def L(): beep(DOT); beep(DASH); beep(DOT); beep(DOT)
def M(): beep(DASH); beep(DASH)
def N(): beep(DASH); beep(DOT)
def O(): beep(DASH); beep(DASH); beep(DASH)
def P(): beep(DOT); beep(DASH); beep(DASH); beep(DOT)
def Q(): beep(DASH); beep(DASH); beep(DOT); beep(DASH)
def R(): beep(DOT); beep(DASH); beep(DOT)
def S(): beep(DOT); beep(DOT); beep(DOT)
def T(): beep(DASH)
def U(): beep(DOT); beep(DOT); beep(DASH)
def V(): beep(DOT); beep(DOT); beep(DOT); beep(DASH)
def W(): beep(DOT); beep(DASH); beep(DASH)
def X(): beep(DASH); beep(DOT); beep(DOT); beep(DASH)
def Y(): beep(DASH); beep(DOT); beep(DASH); beep(DASH)
def Z(): beep(DASH); beep(DASH); beep(DOT); beep(DOT)

def _0(): beep(DASH); beep(DASH); beep(DASH); beep(DASH); beep(DASH)
def _1(): beep(DOT); beep(DASH); beep(DASH); beep(DASH); beep(DASH)
def _2(): beep(DOT); beep(DOT); beep(DASH); beep(DASH); beep(DASH)
def _3(): beep(DOT); beep(DOT); beep(DOT); beep(DASH); beep(DASH)
def _4(): beep(DOT); beep(DOT); beep(DOT); beep(DOT); beep(DASH)
def _5(): beep(DOT); beep(DOT); beep(DOT); beep(DOT); beep(DOT)
def _6(): beep(DASH); beep(DOT); beep(DOT); beep(DOT); beep(DOT)
def _7(): beep(DASH); beep(DASH); beep(DOT); beep(DOT); beep(DOT)
def _8(): beep(DASH); beep(DASH); beep(DASH); beep(DOT); beep(DOT)
def _9(): beep(DASH); beep(DASH); beep(DASH); beep(DASH); beep(DOT)

# --- Map letters to functions ---
MORSE_FUNCS = {
    'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I,
    'J': J, 'K': K, 'L': L, 'M': M, 'N': N, 'O': O, 'P': P, 'Q': Q, 'R': R,
    'S': S, 'T': T, 'U': U, 'V': V, 'W': W, 'X': X, 'Y': Y, 'Z': Z,
    '0': _0, '1': _1, '2': _2, '3': _3, '4': _4, '5': _5, '6': _6,
    '7': _7, '8': _8, '9': _9
}

# --- Function to play a full message ---
def play(message):
    for char in message.upper():
        if char == ' ':
            time.sleep(WORD_GAP)
        elif char in MORSE_FUNCS:
            print(f"Playing {char}")
            MORSE_FUNCS[char]()
            time.sleep(LETTER_GAP)
    print("✅ Message complete!")
