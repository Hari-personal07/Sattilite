from machine import UART, Pin
import time

# === UART Setup for SA818 ===
# For Raspberry Pi Pico: UART0 -> TX=GP0, RX=GP1
sa818 = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))

# === PTT Control Pin ===
ptt = Pin(2, Pin.OUT)
ptt.value(1)  # HIGH = Receive mode (default idle state)

def send_sa818_cmd(cmd):
    """Send AT command to SA818 and print response."""
    sa818.write(cmd + b'\r\n')
    time.sleep(0.3)
    response = b""
    timeout = time.ticks_ms() + 1000
    while time.ticks_ms() < timeout:
        if sa818.any():
            response += sa818.read()
        else:
            time.sleep(0.05)
    if response:
        print("SA818 ->", response.decode().strip())
    else:
        print("No response for:", cmd)

def init_sa818():
    """Initialize SA818 radio settings."""
    print("Initializing SA818...")

    # Connect command (must be sent first)
    send_sa818_cmd(b"AT+DMOCONNECT")

    # Set frequency group:
    # Format: AT+DMOSETGROUP=BW,TX_F,RX_F,TxCTCSS,SQ,RxCTCSS
    # BW: 0=12.5kHz, 1=25kHz
    # Example: TX=RX=443.0000 MHz, no CTCSS, squelch=4
    send_sa818_cmd(b"AT+DMOSETGROUP=0,443.0000,443.0000,0000,4,0000")

    # Set volume (1–8)
    send_sa818_cmd(b"AT+DMOSETVOLUME=4")

    # Set mic gain (0–8)
    send_sa818_cmd(b"AT+SETMIC=2")

    print("SA818 initialized and ready.")

def transmit(duration=5):
    """Enable TX for a given duration (seconds)."""
    print(f"Transmitting for {duration} seconds...")
    ptt.value(0)  # LOW = Transmit
    time.sleep(duration)
    ptt.value(1)  # HIGH = Receive
    print("Back to receive mode.\n")

# === MAIN ===
init_sa818()

while True:
    # Example: transmit every 15 seconds
    transmit(5)
    time.sleep(15)
