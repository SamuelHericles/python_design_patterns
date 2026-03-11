from singleton import DatabaseConnection


# ---- singleton/main.py
def singleton_demo():
    print("=== SINGLETON ===")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    db1.connect("postgresql://localhost:5432/mydb")
    db2.connect("mysql://localhost:3306/otherdb")  # será ignorado
    print(f"  db1 is db2: {db1 is db2}")
    print(db1.query("SELECT * FROM users"))
    print()


if __name__ == "__main__":
    singleton_demo()
