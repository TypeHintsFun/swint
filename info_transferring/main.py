import random
import time
import uuid

import draw
from base.field import Field
from info_transferring.ant import InfoTransferringAnt

field = Field()

for _ in range(100):
    ant = InfoTransferringAnt(
        random.randint(0, 100) + 50,
        random.randint(0, 100) + 50,
        field
    )
    field.ants.append(
        ant
    )
    draw.ant(ant, color=draw.Color.RED)

input_ant: InfoTransferringAnt = field.ants[0]

input_ant.send('Hello world', uuid.uuid1(), is_first_sending_in_system=True)

print(f'\nSuccessful receives: {InfoTransferringAnt.successfully_received_messages_counter}')

input('Press Enter to exit ')
