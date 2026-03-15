# VISITOR

Separa algortimos de estrutura sobre a qual opera. Adiciona operações sem modificar classes. Inspetor visita elementos e age sobre eles. Muitas operações diferentes sobre a estrutura. Esturura raramente muda, operações mudam. Complier AST, exportadores. Operações não relacionadas a elementos,
e operações matemáticas em cadeia (soma,mulitlicaçaõ, chaves,colchetes).

```
visitor/
├── visitor.py
├── concrete_visitors.py
├── element.py
├── concrete_elements.py
└── main.py
```