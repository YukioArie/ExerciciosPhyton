## Gerenciamento Biblioteca

- Implemente um software para gerenciar o empréstimo de livros de uma biblioteca;
- Utilize o POO;
- Utilize as boas práticas de programação;
- Desenvolva diagramas de caso de uso e de classes para auxiliar seu entendimento do problema;
- Regras de negocio:
 - Cada empréstimo tem uma data limite de 7 dias;
 - Cada pessoa tem um limite máximo de 02 livros emprestados;
 - Pessoa não pode solicitar novo empréstimo se estiver em débito, ou seja, não tenha devolvido livro no tempo correto;
 - Alunos ou funcionários são cadastrados por bibliotecário, com nome, matrícula, endereço e telefone;
 - Quando a pessoa for cadastrada, esta já poderá utilizar o serviço de empréstimo de livros;
 - Os livros são cadastrados pelo bibliotecário, com código, nome, autor, edição e ISBN;
 - Ao ser realizado o empréstimo, deve-se registrar:
   - Lista de livros emprestados;
   - Data e hora do início do empréstimo;
   - Data e hora limite do empréstimo;
   - Identificação da pessoa que está realizando o empréstimo;
 - Ao ser realizada a devolução os livros devem retornar a lista de disponíveis e o empréstimo deve registrar a data e hora da devolução;
 - O sistema não pode permitir o empréstimo de livro que encontra-se emprestado;
