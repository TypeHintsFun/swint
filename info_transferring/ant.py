import time
from dataclasses import dataclass
import random
import uuid
from typing import Optional

from base.ant import Ant
import draw
from consts import AURA_RADIUS
from draw import Color


@dataclass
class InfoTransferringAnt(Ant):
    successfully_received_messages_counter = 0

    def __post_init__(self):
        self.messages: dict[uuid.UUID, int] = {}
        self.act_color: Optional[Color] = Color.RED

    def send(self, message: str, uuid_: uuid.UUID, is_first_sending_in_system: bool = False):
        if random.choice([True, False]) is False and not is_first_sending_in_system:
            print(f'- ant {id(self)} get error while receiving message {uuid_}')

            return  # "Error while sending message" simulation for extreme conditions (fifty-fifty chances!)

        if self.act_color not in (Color.GREEN, Color.BROWN):
            draw.ant(self, color=Color.GREEN)

            self.act_color = Color.GREEN

            # time.sleep(0.05)

        message_received = self.messages.get(uuid_, 0)

        if message_received >= 3:
            # draw.aura(for_ant=self, color=Color.WHITE)
            # for ant in self.iter_near_ants(AURA_RADIUS * 1.3):  # type: InfoTransferringAnt
            #     draw.ant(ant, color=ant.act_color)

            draw.ant(self, color=Color.BROWN)
            self.act_color = Color.BROWN
            return

        self.messages[uuid_] = message_received + 1

        if message_received == 0:  # This ant received this message for the first time
            # Execute some instructions from message or write in memory some info
            type(self).successfully_received_messages_counter += 1
            print(f'+ ant {id(self)} successfully received message {uuid_}')
            draw.title(str(type(self).successfully_received_messages_counter), color=Color.GREEN)

        draw.aura(for_ant=self, color=Color.GREEN)

        draw.ant(self, color=Color.BLUE)
        draw.aura(for_ant=self, color=Color.BLUE)
        near_ants = [*self.iter_near_ants()]
        draw.ant(self, color=Color.GREEN)
        draw.aura(for_ant=self, color=Color.LIGHT_GREEN)

        # Resend message to all near ants
        for ant in near_ants:
            ant.send(message, uuid_)

        # draw.aura(for_ant=self, color=Color.WHITE)
        # for ant in self.iter_near_ants(AURA_RADIUS * 1.3):  # type: InfoTransferringAnt
        #     draw.ant(ant, color=ant.act_color)
