from concrete_prototype import Document


# ---- prototype/main.py
def prototype_demo():
    print("=== PROTOTYPE ===")
    original = Document("Relatório Q1", "Conteúdo original", ["financeiro", "2024"])
    clone1 = original.clone()
    clone1.title = "Relatório Q2"
    clone1.tags.append("revisado")

    print(f"Original: {original}")
    print(f"Clone:    {clone1}")
    print()


if __name__ == "__main__":
    prototype_demo()
