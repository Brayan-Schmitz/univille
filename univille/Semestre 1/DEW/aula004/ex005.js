class Evento {
  constructor(nome, local, data, participantes = []) {
    this.nome = nome;
    this.local = local;
    this.data = data;
    this.participantes = participantes;
  }

  quantidadeParticipantes() {
    return this.participantes.length;
  }

  possuiParticipantes() {
    return this.quantidadeParticipantes() > 0;
  }

  possuiLocal() {
    return "local" in this && this.local !== "";
  }

  visaoTela() {
    console.log("===== DADOS DO EVENTO =====");
    console.log(`Evento: ${this.nome}`);
    console.log(`Local: ${this.local}`);
    console.log(`Data: ${this.data.toLocaleDateString("pt-BR")}`);

    console.log(
      `Quantidade de participantes: ${this.quantidadeParticipantes()}`,
    );
    console.log(
      `Possui participantes? ${this.possuiParticipantes() ? "Sim" : "Não"}`,
    );
    console.log(`Possui local? ${this.possuiLocal() ? "Sim" : "Não"}`);

    console.log("\nLista de participantes:");

    if (this.possuiParticipantes()) {
      this.participantes.forEach((participante, indice) => {
        console.log(`${indice + 1}. ${participante}`);
      });
    } else {
      console.log("Nenhum participante cadastrado.");
    }

    console.log("\nPropriedades e valores do objeto:");
    for (const [propriedade, valor] of Object.entries(this)) {
      console.log(`${propriedade}:`, valor);
    }

    console.log("\nTipos das informações:");
    console.log(`nome: ${typeof this.nome}`);
    console.log(`local: ${typeof this.local}`);
    console.log(
      `data: ${this.data instanceof Date ? "object (Date)" : typeof this.data}`,
    );
    console.log(
      `participantes: ${Array.isArray(this.participantes) ? "array" : typeof this.participantes}`,
    );
  }
}

const evento = new Evento(
  "Palestra de JavaScript",
  "Anfiteatro 1",
  new Date("2026-06-26"),
  ["Ana", "Carlos", "João"],
);

evento.visaoTela();
