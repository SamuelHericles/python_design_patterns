from proxy import ProxyImage


def proxy_demo():
    print("=== PROXY (Virtual/Lazy Loading) ===")
    img = ProxyImage("foto_grande.jpg")
    print("  Proxy criado, imagem ainda não carregada")
    print(img.display())
    print(img.display())  # segundo acesso: sem recarga
    print()


if __name__ == "__main__":
    proxy_demo()
