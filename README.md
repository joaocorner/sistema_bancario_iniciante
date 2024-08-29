# Sistema Bancário em Python

## Descrição

Este projeto implementa um sistema bancário básico utilizando Python. As funcionalidades incluem:

- Depósito de valores na conta.
- Saque de valores com controle de limite diário.
- Visualização do extrato das transações realizadas.
- Exibição de saldo com coloração para facilitar a leitura.

A coloração do texto é personalizada através da função `cor_texto`, que permite configurar a cor, negrito e sublinhado dos textos.

## Funcionalidades

1. **Depositar**: Permite ao usuário adicionar um valor ao saldo da conta. O saldo é exibido em verde após um depósito bem-sucedido.
2. **Sacar**: Permite ao usuário retirar um valor do saldo, respeitando as seguintes regras de negócio:
   - Limite de saque diário: o usuário pode realizar no máximo 3 saques por dia.
   - Valor máximo por saque: cada saque está limitado a um valor máximo de R$500,00.
   - Saldo insuficiente: se o saldo for insuficiente para realizar o saque, o sistema impede a operação.
   - Valor de saque inválido: o usuário não pode sacar valores negativos ou zero.
3. **Extrato**: Exibe todas as transações realizadas e o saldo atual. Se o saldo for zero ou negativo, é exibido em vermelho; caso contrário, é exibido em verde.
4. **Sair**: Finaliza o programa.

## Interação

Ao iniciar o programa, o usuário verá o seguinte menu:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Dependendo da escolha, o usuário poderá realizar depósitos, saques ou visualizar o extrato.

## Instalação

Para executar este sistema bancário, siga os passos abaixo:

1. Clone o repositório:
   ```
   git clone https://github.com/seu-usuario/sistema-bancario-python.git
2. Navegue até o diretório do projeto
    ```
    cd sistema-bancario-python
3. Execute o script principal:
    ```
    python sistema_bancario.py
## Funcionalidade de Coloração
A função cor_texto é usada para aplicar estilos aos textos exibidos no terminal. Ela permite personalizar a cor do texto, adicionar negrito ou sublinhado, proporcionando uma experiência de usuário mais rica.

### Exemplo de uso:
```
print(cor_texto("Texto em verde", cor="verde", negrito=True))

