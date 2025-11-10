from machine import UART, Pin
import time

# --- DFPlayer Mini setup (UART0) ---
df_uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
busy = Pin(6, Pin.IN)

# --- SA818 setup (UART1) ---
sa_uart = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))
ptt = Pin(2, Pin.OUT)
pd = Pin(3, Pin.OUT)

# --- DFPlayer functions ---
def send_cmd(cmd, param=0):
    highByte = param >> 8
    lowByte = param & 0xFF
    checksum = 0xFFFF - (0xFF + 0x06 + cmd + 0x00 + highByte + lowByte) + 1
    checksumH = (checksum >> 8) & 0xFF
    checksumL = checksum & 0xFF
    buf = bytes([0x7E, 0xFF, 0x06, cmd, 0x00, highByte, lowByte, checksumH, checksumL, 0xEF])
    df_uart.write(buf)
    time.sleep(0.1)

def init_player():
    send_cmd(0x3F)  # Reset
    time.sleep(1)
    send_cmd(0x06, 20)  # Volume
    time.sleep(0.1)
    print("🎵 DFPlayer ready")

def play_custom(folder, file):
    param = (folder << 8) | file
    send_cmd(0x0F, param)
    print(f"▶️ Playing Folder {folder}, File {file}")

def stop():
    send_cmd(0x16)
    print("⏹️ Stopped")


# --- SA818 functions ---
def sa818_init():
    pd.value(1)  # Power up
    time.sleep(0.5)

    cmd = b"AT+DMOSETGROUP=0,443.0000,443.0000,0000,3,0000\r\n"
    sa_uart.write(cmd)
    time.sleep(0.3)
    print("📡 SA818 configured to 443.000 MHz")

    sa_uart.write(b"AT+DMOSETVOLUME=4\r\n")
    time.sleep(0.2)

# --- Main control ---
def main():
    sa818_init()
    init_player()
    time.sleep(0.5)

    print("🚀 Starting transmission...")
    ptt.value(0)  # Enable transmit
    play_custom(1, 8)

    # Wait until DFPlayer finishes playing
    while busy.value() == 0:
        time.sleep(0.1)

    ptt.value(1)  # Stop transmitting
    print("✅ Transmission complete")


# --- Run ---
if __name__ == "__main__":
    pd.value(1)
    ptt.value(1)
    main()
    