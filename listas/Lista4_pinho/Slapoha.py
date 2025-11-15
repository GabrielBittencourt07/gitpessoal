from __future__ import annotations
from abc import ABC, abstractmethod


class Dono(): 
    def __new__(cls,*args,**kwargs): #pra lembrar pra gente que essa poha existe, mas se formos usar é pra colocar algum código antes\depois da criação do objeto
        return super().__new__()

    def __init__(self, nome_dono: str, idade: int, email: str) -> None:   
        self._nome_dono = nome_dono
        self._idade = idade
        self._email = email
        self._portfolios = []

    @property
    def email(self) -> str: 
        return self._email
    
    @email.setter
    def email(self, novo_email: str) -> None: 
        self._email = novo_email


    @property
    def idade(self)-> int: 
        return self._idade
    
    @idade.setter
    def idade(self, valor_idade: int) -> None: 
        if valor_idade > 0:
            self._idade = valor_idade
        else: 
            raise ValueError("Idade Inválida.")
    
    def add_portfolios(self, portfolio: Portfolio) -> None: 
        if not isinstance(portfolio, Portfolio):
            raise ValueError("Objeto no formato inválido. Anexe um Portfólio.")

        self._portfolios.append(portfolio) 
    
    @property
    def portfolios(self) -> None:
        return self._portfolios


class SecoesObrigatorias(ABC):
    @abstractmethod
    def SecaoEducacao(nome_curso: str, nome_instituicao: str, data: str, informacoes_adicionais: str  = None ):...

    @abstractmethod
    def SecaoExperiencia(nome_cargo: str, nome_empresa: str, data: str, responsabilidades: str | list[str]):... 

    @abstractmethod 
    def SecaoProjetos(nome_projeto: str, descricao: str, data_inicio: str, data_fim:str, link: str = None ):... 

class AboutMe(ABC): 
    @abstractmethod
    def aboutme(texto_informativo: str):...

class Secaohabilidade(ABC):
    @abstractmethod
    def secaohabilidade(lista_de_skills: str | list[str]): ...

class SecaoIdiomas(ABC): 
    @abstractmethod
    def secaoidiomas( Idioma_nivel: dict[str:str]):...



class Portfolio(SecoesObrigatorias): #Classe pai   
    def __new__(cls,*args,**kwargs): #pra lembrar pra gente que essa poha existe, mas se formos usar é pra colocar algum código antes\depois da criação do objeto
        return super().__new__()
    
    def __init__(self, dono: Dono, nome_portfolio: str) -> None:
        dono.add_portfolios(self)
        self._nome_portfolio = nome_portfolio
        self._secoes = []

    def __str__(self) -> str:
        return self._nome_portfolio
    
    def SecaoEducacao(nome_curso: str, nome_instituicao: str, data: str, informacoes_adicionais: str = None):
        return super().SecaoEducacao(nome_instituicao, data, informacoes_adicionais)
    
    def SecaoProjetos(nome_projeto: str, descricao: str, data_inicio: str, data_fim: str, link: str = None):
        return super().SecaoProjetos(descricao, data_inicio, data_fim, link)

    def SecaoExperiencia(nome_cargo: str, nome_empresa: str, data: str, responsabilidades: str | list[str]):
        return super().SecaoExperiencia(nome_empresa, data, responsabilidades)



class PortfolioManager(Portfolio): #classe do dono que pode modificar o portifólip

    def __init__(self, dono: Dono, nome_portfolio: str) -> None:
        super().__init__(dono, nome_portfolio)



    def add_sessao(self, sessao: str) -> None: 
        self._secoes.append(sessao)
    

class PortfolioView(Portfolio): #Classe do recrutador com apenas permissão de visualização
    pass

        
    