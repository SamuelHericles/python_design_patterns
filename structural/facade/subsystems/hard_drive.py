class HardDrive:
    def read(self, lba, size):
        return f"  HDD: read {size} bytes from sector {lba}"
