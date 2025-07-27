const readline = require('readline-sync');

// Exibe os operadores disponíveis
console.log("Operadores: ");
console.log("+ - * /");

// Entrada do operador
let sinal = readline.question("Digite o caracter de operacao: ");

while (sinal !== '+' && sinal !== '-' && sinal !== '*' && sinal !== '/') {
    console.log('\nOperador invalido! Digite novamente');
    console.log("+ - * /");
    sinal = readline.question("Digite o caracter de operacao: ");
}

// Entrada dos operandos
let oper1 = parseFloat(readline.question("Digite o operando 1: "));
let oper2 = parseFloat(readline.question("Digite o operando 2: "));

// Verifica divisão por zero
while (sinal === '/' && oper2 === 0) {
    console.log("Tentativa de divisão por zero!");
    oper2 = parseFloat(readline.question("Digite o operando 2: "));
}

// Processamento com switch
let resultado = 0;
switch (sinal) {
    case '+':
        resultado = oper1 + oper2;
        break;
    case '-':
        resultado = oper1 - oper2;
        break;
    case '*':
        resultado = oper1 * oper2;
        break;
    case '/':
        resultado = oper1 / oper2;
        break;
}

// Exibe o resultado
console.log(`\n${oper1} ${sinal} ${oper2} = ${resultado}`);
