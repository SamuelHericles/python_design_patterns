# FACTORY METHOD

Define interface para criar objetos, mas deixa subclasses decidirem qual classe instanciar. Não crie objetos no new,delegepara o método factory.

Estrutura de arquivos (abstracted into sections below):

```
factory_method/
├── creator.py          # Classe abstrata com factory method
├── concrete_creator.py # Implementações concretas do criador
├── product.py          # Interface do produto
├── concrete_product.py # Produtos concretos
└── main.py             # Cliente
```