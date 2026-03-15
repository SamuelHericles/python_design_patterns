from concrete_mediator import ChatRoom
from colleage import ChatUser


def mediator_demo():
    print("=== MEDIATOR ===")
    room = ChatRoom()
    alice = ChatUser("Alice", room)
    bob = ChatUser("Bob", room)
    carol = ChatUser("Carol", room)
    alice.send("Olá a todos!")
    print()


if __name__ == "__main__":
    mediator_demo()
