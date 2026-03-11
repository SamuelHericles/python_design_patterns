from subsystems.cpu import CPU
from subsystems.memory import Memory
from subsystems.hard_drive import HardDrive
from subsystems.bios import BIOS


class Computer:
    def __init__(self):
        self._cpu = CPU()
        self._memory = Memory()
        self._hdd = HardDrive()

    def start(self):
        steps = []
        steps.append(self._cpu.freeze())
        steps.append(
            self._memory.load(
                BIOS.BOOT_ADDRESS, self._hdd.read(BIOS.BOOT_SECTOR, BIOS.SECTOR_SIZE)
            )
        )
        steps.append(self._cpu.jump(BIOS.BOOT_ADDRESS))
        steps.append(self._cpu.execute())
        return "\n".join(steps)
