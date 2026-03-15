from concrete_states import TrafficLight


def state_demo():
    print("=== STATE ===")
    light = TrafficLight()
    for _ in range(4):
        print(light.change())
    print()


if __name__ == "__main__":
    state_demo()
