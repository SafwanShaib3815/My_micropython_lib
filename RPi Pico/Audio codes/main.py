#GPIO  2 & 3  pin 4 and 5 are the output


import os as uos
import wavePlayer
from time import sleep
player = wavePlayer.wavePlayer()

try:
    player.play('sounds/smb_mariodie3.wav')
#     while True:
#         # repeat this over and over until the keyboard shuts down the circuit
#         player.play('sounds/typical-trap-loop-140bpm3.wav')

    

except KeyboardInterrupt:
    player.stop()
    print("wave player terminated")
    
