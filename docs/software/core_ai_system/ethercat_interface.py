"""
EtherCAT Communication Interface

High-level communication bridge to Beckhoff TwinCAT layer.
This layer does not execute deterministic motion control.
"""

from dataclasses import dataclass


@dataclass
class EtherCATCommand:
    command_type: str
    payload: dict


class EtherCATInterface:
    def send_high_level_target(self, command: EtherCATCommand) -> bool:
        print(f"[ETHERCAT-HL] Sending {command.command_type}: {command.payload}")
        return True
