from machine import UART, Pin
import time

# === UART SETUP ===
# Using UART0 with TX=GP16, RX=GP17
uart = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))

print("\n=== UART AT Command Test ===")
time.sleep(1)

def send_at(cmd):
    """Send AT command and print raw response."""
    full_cmd = cmd + b'\r\n'
    print("\nSending:", full_cmd)
    uart.write(full_cmd)
    time.sleep(0.5)

    response = b""
    timeout = time.ticks_ms() + 1000
    while time.ticks_ms() < timeout:
        if uart.any():
            response += uart.read()
        else:
            time.sleep(0.05)
    if response:
        print("Response:", response)
    else:
        print("No response from module.")

# === MAIN TEST ===
try:
    send_at(b"AT")                  # Basic attention command
    send_at(b"AT+DMOCONNECT")       # SA818 connect test
except Exception as e:
    print("Error:", e)
