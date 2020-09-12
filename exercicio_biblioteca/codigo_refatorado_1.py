from datetime import datetime, timedelta
class Cliente:
    def __init__(self, nome, matricula, endereco, telefone):
        self.nome = nome
        self.matricula = matricula
        self.endereco = endereco
        self.telefone = telefone
        self.livros_emprestados = []
        self.livros_entregados = []

    def is_inadimplente(self, data_biblioteca):
        for emprestimo in self.livros_emprestados:
            if data_biblioteca <= emprestimo.data_prevista_entrega or len(emprestimo) == 0:
                return False
            else:
                return True

    def is_cadastrado(self, lista_de_clientes):
        for cliente in lista_de_clientes:
            if cliente.matricula == self.matricula:
                return True
            else:
                return False
    def fazer_emprestimo(self, biblioteca, livro, data_prevista_entrega):
        if self.is_cadastrado(biblioteca.lista_de_clientes) and livro.is_cadastrado(biblioteca.lista_de_livros) and (self.is_inadimplente(biblioteca.data_biblioteca) != False) and len(self.livros_emprestados) < 2:
            biblioteca.emprestimos.append(Emprestimo(livro, self, biblioteca.data_biblioteca, data_prevista_entrega))
            self.livros_emprestados.append(Emprestimo(livro, self, biblioteca.data_biblioteca, data_prevista_entrega))
            biblioteca.lista_de_livros.remove(livro)
        else:
            print("Emprestimo n efetuado")

    def devolver_livro(self, biblioteca, livro):
        if livro.is_emprestado(self.livros_emprestados):         
            biblioteca.emprestimos.remove(livro.verificar_livro_id(biblioteca.emprestimos))
            self.livros_emprestados.remove(livro.verificar_livro_id(self.livros_emprestados))
            self.livros_entregados.append(livro, biblioteca.data_biblioteca) 
            biblioteca.cadastrar_livro(livro)

    
class Livro:
    def __init__(self, codigo, nome, autor, edicao, isbn):
        self.codigo = codigo
        self.nome = nome
        self.autor = autor
        self.edicao = edicao
        self.isbn = isbn
    
    def verificar_livro_id(self, emprestimos):
        for emprestimo in emprestimos:
            if emprestimo.livro.codigo == self.codigo:
                return emprestimo 
    
    def is_emprestado(self, emprestimos):
        for emprestimo in emprestimos:
            if emprestimo.livro.codigo == self.codigo:
                return True
            else:
                return False

    def is_cadastrado(self, lista_de_livros):
        for livro in lista_de_livros:
            if livro.codigo == self.codigo:
                return True
            else:
                return False
class Biblioteca:
    def __init__(self):
        self.lista_de_clientes = []
        self.lista_de_livros = []
        self.emprestimos = []
        self.data_biblioteca = datetime.strptime('2020-05-05', '%Y-%m-%d')
    
    def set_dia(self, data):
        if data > self.data_biblioteca:
            self.data_biblioteca = data
        else:
            print("Não é possível setar o dia q ja passou, pois sua maquina do tempo n volta para o passado")
    
    def listar_livros_emprestados(self):
        x = []
        for emprestimo in self.emprestimos:
            x.append(emprestimo.livro.nome)
        return x

    # def is_livro_cadastrado(self, livro):
    #     for lista_livro in self.lista_de_livros:
    #         if lista_livro == livro:
    #             return True
    #         else:
    #             return False

    # def fazer_emprestimo(self, cliente, livro, data_entrega):
    #     if cliente.is_cadastrado(self.lista_de_clientes) and livro.is_cadastrado(self.lista_de_livros) and (cliente.is_inadimplente(self.data_biblioteca) != False):
    #         self.emprestimos.append(Emprestimo(livro, cliente, self.data_biblioteca, data_entrega))
    #         cliente.livros_emprestados.append(Emprestimo(livro, cliente, self.data_biblioteca, data_entrega))
    #         #self.lista_de_livros.remove(livro)
    #     else:
    #         print("Emprestimo n efetuado")
            
    def cadastrar_clientes(self, cliente):
        if cliente.is_cadastrado(self.lista_de_clientes):
            print('cliente ja cadastrado')
        else:
            self.lista_de_clientes.append(cliente)

    def cadastrar_livro(self ,livro):
        if livro.is_cadastrado(self.lista_de_livros) and livro.is_emprestado(self.emprestimos):
            print('livro ja cadastrado')
        else:
            self.lista_de_livros.append(livro)

class Emprestimo:
    def __init__(self, livro, cliente, data_emprestimo, data_prevista_entrega):
        self.data_emprestimo = data_emprestimo
        self.data_prevista_entrega = data_prevista_entrega
        self.cliente = cliente
        self.livro = livro


b = Biblioteca()
yukio = Cliente("yukio", 123456, "Pinhalao",22998813788)
maria = Cliente("maria", 55555, "asd", 22333665)
a_visao = Livro(1245, "A visao", "joao", 12, 6598)
a_pedra = Livro(1255, "A pedra", "paulo", 120, 656984)
b.cadastrar_clientes(yukio)
b.cadastrar_livro(a_visao)
b.cadastrar_livro(a_pedra)
yukio.fazer_emprestimo(b, a_visao, datetime.strptime('2020-05-15', '%Y-%m-%d'))
yukio.fazer_emprestimo(b, a_pedra, datetime.strptime('2020-05-15', '%Y-%m-%d'))
print(b.lista_de_clientes)
print(b.lista_de_livros)
print(b.emprestimos)
print(b.listar_livros_emprestados())