class Produto {
  constructor(nome, categoria, preco, estoque) {
    this.nome = nome;
    this.categoria = categoria;
    this.preco = Number(preco);
    this.estoque = estoque;
  }

  nivelEstoque() {
    return this.estoque < 5 ? "baixo" : "adequado";
  }

  saida() {
    console.log(`Produto: ${this.nome}`);
    console.log(`Categoria: ${this.categoria}`);
    console.log(`Preço: R$ ${this.preco}`);
    console.log(`Estoque: ${this.nivelEstoque()}`);
    console.log();
  }

  visaoTela() {
    console.log(`Produto: ${this.nome} (${typeof this.nome})`);
    console.log(`Categoria: ${this.categoria} (${typeof this.categoria})`);
    console.log(`Preço: ${this.preco} (${typeof this.preco})`);
    console.log(
      `Estoque: ${this.nivelEstoque()} (${typeof this.nivelEstoque()})`,
    );
    console.log();
  }
}

const monitor = new Produto("Monitor", "Informática", "899.90", 5);

monitor.saida();
monitor.visaoTela();

const cadeira = new Produto("Cadeira", "Escritório", "450.00", 30);

cadeira.saida();
cadeira.visaoTela();
