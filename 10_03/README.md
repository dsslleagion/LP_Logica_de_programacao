

# 📚 Avançando a Matéria de Dia 03/03

## 📚 Introdução às Estruturas de Decisão Simples

### 🎯 Objetivos da Aula
- Compreender os conceitos fundamentais da lógica de programação e a importância da estrutura de decisão.
- Desenvolver sistemas computacionais utilizando ambiente de desenvolvimento.
- Identificar e analisar problemas, desenvolver alternativas e implementar soluções eficazes.
- Explorar operadores lógicos (AND, OR, NOT) e comparadores para avaliação de condições.

### 📚 Conteúdo da Aula

#### 1. Elementos Básicos do Algoritmo
- **Sequência**: Instruções executadas linearmente na ordem correta, garantindo previsibilidade na execução do código.
- **Seleção**: Estruturas condicionais que permitem que diferentes blocos de código sejam executados dependendo de condições específicas.
- **Repetição**: Permite a execução de um bloco de código múltiplas vezes até que uma condição seja satisfeita, essencial para automação de processos repetitivos.

#### 2. Estruturas de Decisão
- **If-Else**: Avalia uma condição e executa um bloco de código caso seja verdadeira; caso contrário, executa outro bloco alternativo.
- **Switch-Case**: Estrutura que avalia múltiplas condições possíveis, tornando a lógica do código mais organizada quando há diversas opções.

#### 3. Operadores Lógicos
- **AND (`&&`)**: Retorna verdadeiro apenas se ambas as condições forem verdadeiras. Exemplo:
```python
if idade >= 18 and possui_habilitacao:
    print("Pode dirigir")
```
- **OR (`||`)**: Retorna verdadeiro se pelo menos uma condição for verdadeira. Exemplo:
```python
if dia == "sábado" or dia == "domingo":
    print("É fim de semana!")
```
- **NOT (`!`)**: Inverte o valor de uma condição. Exemplo:
```python
if not usuario_logado:
    print("Acesso negado")
```

#### 4. Exemplos Práticos
##### Login e Senha (AND)
```python
login_correto = "usuario123"
senha_correta = "senha123"

def verificar_acesso(login, senha):
    if login == login_correto and senha == senha_correta:
        return "Acesso permitido"
    else:
        return "Acesso negado"
```

##### Escolha de Carros (OR)
```python
marca = "Ford"
if marca == "Ford" or marca == "Fiat":
    print("Carro aceito para revisão")
else:
    print("Marca não aceita")
```

##### Uso do NOT
```python
ativo = True
if not ativo:
    print("Usuário inativo")
else:
    print("Usuário ativo")
```

### 📈 Atividade Prática
1. Criar um fluxograma representando a tomada de decisão para liberação de crédito bancário.
2. Desenvolver um pequeno programa que utilize `if-else` e operadores lógicos para decidir se um usuário pode acessar um serviço.
3. Produzir um texto síntese (250-500 caracteres) sobre a importância das estruturas de decisão e operadores lógicos.
4. Aplicar operadores lógicos em um algoritmo que simule um sistema de verificação de idade para acesso a um site adulto.

---

## 📚 Referências
- [Estruturas de Decisão - UNIVESP](https://apps.univesp.br/novotec/estruturas-de-decisao/?curso=viarapida)
- [TreinaWeb - Operadores Lógicos](https://www.treinaweb.com.br/blog/operadores-l%C3%B3gicos)
- [Bóson Treinamentos - Estruturas de Decisão](https://youtu.be/IIt3bc4MBKQ?si=kJAq3S1Hc_7ziWQ1)

🎉 **Boa aula e bons estudos!** 📚💡



# 📚 Avançando a Matéria de Dia 10/03

## 📚 Introdução às Estruturas de Decisão Simples (Continuação)

### 🎯 Objetivos da Aula
- Compreender o processo de tomada de decisão dentro dos algoritmos a partir das estruturas `if` e `else`.
- Conhecer exemplos práticos de aplicação.
- Desenvolver sistemas computacionais utilizando ambiente de desenvolvimento.
- Identificar e analisar problemas, desenvolver alternativas e implementar soluções eficazes durante a execução de um projeto.

### 📚 Conteúdo da Aula

#### 1️⃣ Tomada de Decisão na Programação
Na programação, a capacidade de tomar decisões é essencial. O uso das estruturas `if` e `else` permite avaliar condições e executar diferentes blocos de código conforme o resultado.

Exemplo em Portugol:
```portugol
algoritmo ExemploIdade
var
    idade: inteiro
inicio
    escreva("Digite a sua idade: ")
    leia(idade)

    se (idade >= 18) entao
        escreva("Você é maior de idade. Pode entrar.")
    senao
        escreva("Você é menor de idade. Não pode entrar.")
    fimse
fimalgoritmo
```

#### 2️⃣ Sintaxe Básica do `if-else` em Portugol
```portugol
se (condição) entao
    // Bloco de código executado se a condição for verdadeira
senao
    // Bloco de código executado se a condição for falsa
fimse
```

#### 3️⃣ Comparadores e Lógica de Decisão
Os comparadores são utilizados para avaliar expressões e tomar decisões baseadas em resultados.

Comparadores mais comuns:
- Igualdade (`==`)
- Desigualdade (`!=`)
- Maior que (`>`)
- Menor que (`<`)
- Maior ou igual a (`>=`)
- Menor ou igual a (`<=`)

Exemplo de comparação em Portugol:
```portugol
var previsao: caractere

inicio
    escreva("Qual é a previsão do tempo? (C = Chuva / S = Sem chuva)")
    leia(previsao)

    se (previsao == "C") entao
        escreva("Leve o guarda-chuva.")
    senao
        escreva("Não é necessário levar o guarda-chuva.")
    fimse
fimalgoritmo
```

### 🏆 Atividade Prática
1. Criar um algoritmo em Portugol que verifica se um aluno foi aprovado ou reprovado com base em sua média.
2. Desenvolver um código que simule um sistema de acesso baseado em senha e nível de permissão.
3. Implementar um sistema de verificação para concessão de desconto em uma loja baseado na idade do cliente.

---

## 📚 Avançando a Matéria de Dia 17/03

### 🎯 Objetivos da Aula
- Conhecer a aplicação prática do uso de comparadores de decisão e compreender diferentes cenários que permitem sua aplicação.
- Desenvolver sistemas computacionais utilizando ambiente de desenvolvimento.
- Aplicar operadores lógicos para tomada de decisões em algoritmos.

### 📚 Conteúdo da Aula

#### 1️⃣ Estudo de Caso: Controle de Acesso na Empresa "Grape"
A empresa "Grape" deseja implementar um sistema de controle de acesso mais seguro. O sistema deve permitir a entrada apenas para funcionários autorizados, ou seja, aqueles que são gerentes ou possuem uma permissão especial.

Exemplo de código em Portugol:
```portugol
se (cargo == "Gerente" ou permissoesEspeciais == verdadeiro) entao
    escreva("Acesso permitido!")
senao
    escreva("Acesso negado.")
fimse
```

#### 2️⃣ Comparadores e Tomada de Decisão
Os comparadores permitem analisar valores e determinar o fluxo do programa.

**Exemplo:** Escolha de roupa baseada na temperatura.
```portugol
se (temperatura >= 25) entao
    escreva("Use uma camiseta de manga curta.")
senao
    escreva("Use uma blusa de manga longa.")
fimse
```

#### 3️⃣ Aplicação de Operadores Lógicos
Os operadores lógicos ajudam a construir condições mais complexas para tomada de decisão.

- `&&` (E lógico): Ambas as condições precisam ser verdadeiras.
- `||` (OU lógico): Apenas uma das condições precisa ser verdadeira.
- `!` (NÃO lógico): Inverte o valor de uma condição.

Exemplo de operador `&&`:
```portugol
se (idade >= 18 && possuiHabilitacao == verdadeiro) entao
    escreva("Pode dirigir.")
senao
    escreva("Não pode dirigir.")
fimse
```

### 🏆 Atividade Prática
1. Criar um algoritmo que determina se uma pessoa pode votar.
2. Desenvolver um programa que verifica se um número digitado pelo usuário é positivo, negativo ou zero.
3. Implementar um sistema de segurança que permite ou nega o acesso de um usuário com base em login e senha.

---

## 📚 Referências
- [ALURA - Lógica de Programação](https://cursos.alura.com.br/course/logica-programacao-mergulhe-programacao-javascript)
- [Kenzie - Estruturas Condicionais](https://kenzie.com.br/blog/estruturas-condicionais/)
- [LABENU - Operadores Aritméticos e Comparadores](https://youtu.be/OgxcX1MjbKU?si=c6ZhHVK3Qo9Dukyn)

🎉 **Boa aula e bons estudos!** 📚💡