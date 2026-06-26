const gastos = ["500", "1200", "abc", "350", "1000", ""];

function calcularTotal(lista) {
  let total = 0;

  for (let i = 0; i < lista.length; i++) {
    const valor = Number(lista[i]);

    if (isNaN(valor) || lista[i] === "") continue;

    total += valor;
  }

  return total;
}

const totalGastos = calcularTotal(gastos);

console.log(`Total: R$ ${totalGastos}`);

console.log(
  totalGastos > 2000 ? "Limite ultrapassado" : "Gastos dentro do limite",
);
