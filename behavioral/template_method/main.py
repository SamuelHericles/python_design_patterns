from concrete_classes import (
    CSVMiner,
    JSONMiner,
)


def template_method_demo():
    print("=== TEMPLATE METHOD ===")
    print("  CSV Miner:")
    CSVMiner().mine("data.csv")
    print("  JSON Miner:")
    JSONMiner().mine("data.json")
    print()


if __name__ == "__main__":
    template_method_demo()
