class Semestre {
  constructor(disciplinas = []) {
    this.disciplinas = disciplinas;
  }

  exibirDisciplinas() {
    this.disciplinas.forEach((disciplina) => console.log(disciplina));
    console.log();
  }

  quantidadeDisciplinas() {
    return this.disciplinas.length;
  }

  possuiJavaScript() {
    return this.disciplinas.includes("JavaScript")
      ? "Cursa JavaScript"
      : "Não cursa JavaScript";
  }

  adicionarDisciplina(disciplina) {
    this.disciplinas.push(disciplina);
  }

  percorrerDisciplinas() {
    for (let i = 0; i < this.disciplinas.length; i++) {
      if (this.disciplinas[i] === "") continue;

      console.log(this.disciplinas[i]);

      if (this.disciplinas[i] === "TCC") {
        console.log("\nLaço interrompido.");
        break;
      }
    }

    console.log();
  }

  saida() {
    console.log("Disciplinas:");
    this.exibirDisciplinas();

    console.log(`Quantidade: ${this.quantidadeDisciplinas()}`);
    console.log(this.possuiJavaScript());

    this.adicionarDisciplina("Engenharia de Software");

    console.log("\nApós adicionar uma disciplina:");
    this.exibirDisciplinas();

    console.log("Percorrendo disciplinas:");
    this.percorrerDisciplinas();
  }
}

const semestre = new Semestre([
  "HTML",
  "CSS",
  "JavaScript",
  "",
  "TCC",
  "Redes",
]);

semestre.saida();
