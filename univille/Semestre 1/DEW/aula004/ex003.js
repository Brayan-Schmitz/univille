const autores = "Machado de Assis,Clarice Lispector,Monteiro Lobato";
const listaAutores = autores.split(",");

listaAutores.forEach((autor) => console.log(autor));

function possuiAutor(autor) {
  return listaAutores.includes(autor)
    ? "Autor encontrado."
    : "Autor não encontrado.";
}

console.log(possuiAutor("Machado de Assis"));

function criarLivro(titulo, autor) {
  return `Livro: ${titulo} | Autor: ${autor}`;
}

console.log(criarLivro("Dom Casmurro", "Machado de Assis"));

console.log(listaAutores.join(", "));
