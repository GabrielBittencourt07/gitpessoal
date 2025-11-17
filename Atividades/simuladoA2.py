from __future__ import annotations
import time
from datetime import datetime
from abc import ABC, abstractmethod
import numpy as np

class Livro:    
    def __init__(self, titulo: str, autor: str, genero: str, estado_de_conservacao: str = None):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        self._edc = estado_de_conservacao 

    @property
    def titulo(self): 
        return self._titulo

class Transacao: 
    def __init__(self, datatime: datetime, usuario1: Usuario, usuario2: Usuario, livro1: Livro, livro2: Livro = None, status: str = "Pendente"):
        self._data = datatime 
        self._status = status
        self._solicitante = usuario1
        self._solicitado = usuario2
        self._livro_pedido = livro1 
        self._livro_oferecido = livro2

    def validartransacao(self): 
        self._status = "concluído"

    def cancelartransacao(self): 
       self._status = "cancelado"

    @property
    def solicitante(self): 
        return self._solicitante

    @property
    def solicitado(self): 
        return self._solicitado
    
    @property
    def status(self): 
        return self._status
    
    @property
    def analisartransacao(self):
        return f"O usuario {self._solicitante._nome_usuario}, solicitou a troca de {self._livro_pedido.titulo} por {self._livro_oferecido.titulo} em {self._data}, status da transação: {self._status}"


class BookMatch(ABC):
    dicionario_de_livros = dict()
    
    def __init__(self):
        pass

    @property
    def lista_livros(self): 
        lista_livros = list()
        for usuario, lista_de_livros_usuario in self.dicionario_de_livros.items():
            for livro in lista_de_livros_usuario: 
                lista_livros.append(livro.titulo)
        return lista_livros
    
    @abstractmethod
    def transacoes(self):...

    @abstractmethod
    def solicitartrocas(self, livro1: Livro, livro2: Livro = None):...

    @abstractmethod
    def verificartrocaspendentes(self):...

    def verificarlivrosdisponiveis(self):
        return self.dicionario_de_livros

    @abstractmethod
    def aceitarsolicitacoesdetroca(self):...

    @abstractmethod
    def cancelarsolicitacaodetroca(self):...
        


class Usuario(BookMatch): 
    
    def __init__(self, nome_usuario: str):
        self._livros_usuario  = []
        self._nome_usuario = nome_usuario
        BookMatch.dicionario_de_livros[self] = self._livros_usuario
        self._transacoes = []
        self._notas = []
        

    def adicionarlivro(self, livro: Livro): 
        self._livros_usuario.append(livro)


    def transacoes(self):
        for transacao in self._transacoes: 
            print(f"[Transação {self._transacoes.index(transacao)}] {transacao.analisartransacao}\n")


    def solicitartrocas(self, livro1: Livro, livro2: Livro = None):
        if not isinstance(livro1, Livro):
            raise ValueError("O livro proposto para troca deve ser da classe \"Livro\"")
        if livro2 is not None and not isinstance(livro2, Livro):
            raise ValueError("O livro proposto para troca deve ser da classe \"Livro\"")

        if livro1.titulo not in self.lista_livros: 
            raise KeyError("O livro solicitado não existe em nosso acervo.") #Seria legal dar opções de livros com mesmo autores que existem no acervo.
        
        for usuario, lista_de_livros_usuario in BookMatch.dicionario_de_livros.items():
            for livro in lista_de_livros_usuario: 
                if livro.titulo == livro1.titulo: 
                    transacao = Transacao(datetime.now(), self, usuario, livro, livro2)
                    self._transacoes.append(transacao)
                    usuario._transacoes.append(transacao)


    def aceitarsolicitacoesdetroca(self, index_transacao: int):
        transacao = self._transacoes[index_transacao]

        if self == transacao.solicitante: 
            raise PermissionError("Você que solicitou essa transação, você não tem permissão para aceita-la.")
        
        else: 
            transacao.validartransacao()
        

    def cancelarsolicitacaodetroca(self, index_transacao: int):
        self._transacoes[index_transacao].cancelartransacao()

    def verificartrocaspendentes(self):
        for transacao in self._transacoes: 
            if transacao.status == "pendente":
                print(transacao.analisartransacao)

    @property
    def usuarios_para_avaliar(self): 
        usuarios_para_avaliar = {}
        for transacao in self._transacoes: 
            if transacao.status  == "concluído":
                usuario1 = transacao.solicitante 
                usuario2 = transacao.solicitado 

                if self is usuario1: 
                    usuarios_para_avaliar[usuario2._nome_usuario] = usuario2
                else: 
                    usuarios_para_avaliar[usuario1._nome_usuario] = usuario1 

        return list(usuarios_para_avaliar.keys())
    
    def avaliar_usuario(self, usuario: str, nota: int | float):

        if self._nome_usuario == usuario: 
            raise PermissionError("Você não pode avaliar você mesmo.")
        
        usuarios_para_avaliar = {}
        for transacao in self._transacoes: 
            usuario1 = transacao.solicitante 
            usuario2 = transacao.solicitado 

            if self is usuario1: 
                usuarios_para_avaliar[usuario2._nome_usuario] = usuario2
            else: 
                usuarios_para_avaliar[usuario1._nome_usuario] = usuario1 

        usuarios_para_avaliar[usuario]._notas.append(nota)

    @property
    def nota(self): 
        return np.mean(self._notas)
    


print("--- INICIANDO SIMULAÇÃO BOOKMATCH ---")

# 1. Instanciar Usuários
usuario_a = Usuario("Alice_Leitora")
usuario_b = Usuario("Bob_TrocaFácil")
print(f"Usuários criados: {usuario_a._nome_usuario} e {usuario_b._nome_usuario}")

# 2. Instanciar Livros
livro_a_pedido = Livro("Duna", "Frank Herbert", "Ficção Científica")
livro_b_oferecido = Livro("1984", "George Orwell", "Distopia")
livro_c_extra = Livro("Cem Anos de Solidão", "G.G. Márquez", "Realismo Mágico")

# 3. Adicionar Livros ao Acervo dos Usuários
usuario_b.adicionarlivro(livro_a_pedido)  # Bob tem o livro que Alice quer
usuario_a.adicionarlivro(livro_b_oferecido) # Alice tem o livro que oferece
usuario_a.adicionarlivro(livro_c_extra)

print("\n--- STATUS DO ACERVO GERAL ---")
print(f"Livros no acervo (global): {BookMatch.lista_livros}")
print("-" * 35)

# 4. Alice solicita a troca (Livro A PEDIDO, Livro B OFERECIDO)
# Alice está solicitando Duna de Bob, e oferece 1984.
try:
    # Alice tenta trocar o livro que ela oferece (1984) pelo livro que ela quer (Duna)
    # A lógica atual do solicitartrocas é complexa, mas vamos simular a busca.
    # Nota: A função solicitartrocas inicia transações com todos que tem o livro.
    # Estamos assumindo que a transação é criada entre Alice e Bob.
    
    # Execução real: Alice solicita o livro "Duna"
    usuario_a.solicitartrocas(livro1=livro_a_pedido, livro2=livro_b_oferecido)
    print(f"SOLICITAÇÃO: Alice solicitou 'Duna' (de Bob), oferecendo '1984'.")

except KeyError as e:
    print(f"Erro: {e}")

# 5. Análise da Transação (Ambos os lados)
# Deve haver uma transação pendente na lista de ambos.

print("\n--- ANÁLISE DAS TRANSAÇÕES PENDENTES (Lado de Bob) ---")
# Bob é o solicitado. Ele vê a solicitação de Alice.
usuario_b.verificartrocaspendentes() 

# 6. Bob aceita a transação (Bob é o solicitado)
# Bob é o usuário 2, ele tem permissão para aceitar.
index_transacao_bob = 0 # Assume que é a primeira e única transação na lista de Bob
usuario_b.aceitarsolicitacoesdetroca(index_transacao_bob)

# 7. Verificação do Status Final
print(f"STATUS FINAL DA TRANSAÇÃO: {usuario_b._transacoes[index_transacao_bob].status}")

# 8. Verificação do Sistema de Avaliação (Usuários aptos)
print("\n--- AVALIAÇÃO ---")
print(f"Alice deve avaliar: {usuario_a.usuarios_para_avaliar}")
print(f"Bob deve avaliar: {usuario_b.usuarios_para_avaliar}")

