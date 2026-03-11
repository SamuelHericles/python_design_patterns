class CPU:
    def freeze(self):
        return "  CPU: freeze"

    def jump(self, address):
        return f"  CPU: jump to {address}"

    def execute(self):
        return "  CPU: execute"
