from utime import sleep_ms, sleep
from dfplayer import DFPlayer


#Constants. Change these if DFPlayer is connected to other pins.
UART_INSTANCE=0
TX_PIN =0
RX_PIN=1
BUSY_PIN=6

#Create player instance
player=DFPlayer(UART_INSTANCE, TX_PIN, RX_PIN, BUSY_PIN)


#Check if player is busy.
print('Playing?', player.queryBusy())
#Play the first song (001.mp3) from the first folder (01)


print('Playing track 001.mp3 in folder 07')

while True:
    
    player.playTrack(1,7)   #dot 
#     sleep(0.2)
    


#Pause
print('Pausing')
player.pause()

player.nextTrack()

sleep(15)

player.nextTrack()



