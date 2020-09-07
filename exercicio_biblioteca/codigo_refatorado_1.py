class Cliente:
    def __init__(self, nome, matricula, endereco, telefone):
        self.nome = nome
        self.matricula = matricula
        self.endereco = endereco
        self.telefone = telefone
        self.ativo = True

    
class Livro:
    def __init__(self, codigo, nome, autor, edicao, isbn):
        self.codigo = codigo
        self.nome = nome
        self.autor = autor
        self.edicao = edicao
        self.isbn = isbn

class Biblioteca:
    def __init__(self):
        self.lista_de_clientes = []
        self.lista_de_livros = []
        self.emprestimos = []
    def listar_livros_emprestados(self):
        for emprestimo in emprestimos:
            return emprestimo.livro.nome

    def cliente_ativo(self, cliente):
        quantidade = 0
        for emprestimo in emprestimos:
            if self.cliente == emprestimo.cliente:
                quantidade += 1
        if quantidade >= 2:
            self.cliente.ativo = False
    
    def cliente_esta_cadastrado(cliente):
        if cliente not in lista_de_clientes:
            return false
        else:
            return true
    def livro_esta_cadastrado(self, livro):
        if livro not in lista_de_livros:
            return false
        else:
            return true

    def fazer_emprestimo(self, cliente, livro, data_emprestimo, data_entrega):
        if cliente_esta_cadastrado(cliente) and livro_esta_cadastrado(livro) and cliente.ativo:
            self.emprestimos.append(Emprestimo(cliente, livro, data_emprestimo, data_entrega))
            self.lista_de_livros.remove(livro)
            
    def cadastrar_clientes(cliente):
        if cliente_esta_cadastrado(cliente):
            lista_de_clientes.append(cliente)
        else:
            print('cliente cadastrado')

    def cadastrar_livro(livro):
        if livro_esta_cadastrado(livro):
            lista_de_livros.append(livro)
        else:
            print('livro cadastrado')
                
class Emprestimo:
    def __init__(self, Livro, Cliente, data_emprestimo, data_entrega):
        self.data_entrega = data_entrega
        self.data_emprestimo = data_emprestimo
        self.cliente = Cliente()
        self.livro = Livro()


