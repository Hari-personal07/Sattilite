from machine import UART, Pin
import time

# UART0 on GP0 (TX) and GP1 (RX)
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
busy = Pin(6, Pin.IN)

def send_cmd(cmd, param=0):
    """Send a DFPlayer command frame"""
    highByte = param >> 8
    lowByte = param & 0xFF
    checksum = 0xFFFF - (0xFF + 0x06 + cmd + 0x00 + highByte + lowByte) + 1
    checksumH = (checksum >> 8) & 0xFF
    checksumL = checksum & 0xFF
    buf = bytes([0x7E, 0xFF, 0x06, cmd, 0x00, highByte, lowByte, checksumH, checksumL, 0xEF])
    uart.write(buf)
    time.sleep(0.2)

def init_player():
    """Initialize DFPlayer"""
    send_cmd(0x3F)  # Reset/initialize
    time.sleep(1)
    send_cmd(0x06, 10)  # Set volume (0–30) ithu volume set pannikalam 
    time.sleep(0.1)
    print("DFPlayer initialized")

def play_custom(folder, file):
    """Play specific folder and file — (folder, file)"""
    param = (folder << 8) | file
    send_cmd(0x0F, param)
    print(f"Playing Folder {folder}, File {file}")

def stop():
    send_cmd(0x16)
    print("Playback stopped")


init_player() 
time.sleep(0.7)


play_custom(1, 7) # ithu entha file venumo  atha run pannikalam 

