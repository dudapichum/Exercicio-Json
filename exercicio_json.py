import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, "input")

# Ler o arquivo escola.json
arquivo = open(os.path.join(INPUT_DIR, "escola.json"), 'r')
escola_json = arquivo.read()
escola_dict = json.loads(escola_json)
# Criar classes, que serão instanciadas de acordo com os dados em escola.json

class Escola:
    def __init__(self, escola, endereco):
        self.escola = escola
        self.endereco = endereco
        self.diretoria = []
        self.salas = []

    def __str__(self):
        return self.escola

    def add_diretoria(self, diretoria):
        self.diretoria.append(diretoria)

    def add_salas(self, sala):
        self.salas.append(sala)

    def get_alunos_maior_18(self):
        # List Comprehensions e Dict Comprehensions
        return [ aluno for sala in self.salas for aluno in sala.alunos if aluno.idade >= 18 ]

        # for sala in self.salas:
        #     aluno = sala.alunos
        #     for idade in aluno:
        #         if idade.idade >= 18: 
        #             aluno_found_maior.append(idade)

        # return aluno_found_maior

    def get_alunos_menor_18(self):
        return [ aluno for sala in self.salas for aluno in sala.alunos if aluno.idade < 18 ]

        # for sala in self.salas:
        #     aluno = sala.alunos
        #     for idade in aluno:
        #         if idade.idade < 18: 
        #             aluno_found_menor.append(idade)

        # return aluno_found_menor

    def get_quantidade_total_alunos(self):
        return sum([ sala.get_total_alunos() for sala in self.salas ]) 

        # soma = 0

        # for sala in escola.salas:
        #     soma += len(sala.alunos) 
        
        # return soma

    def remove_aluno(self, nome_sala, nome_aluno):
        for sala in self.salas:
            if nome_sala == sala.nome_sala:
                for aluno in sala.alunos:
                    if nome_aluno == aluno.nome_aluno:
                        sala.alunos.remove(aluno)


class Diretor:
    def __init__(self, nome_diretor, ano_entrada):
        self.nome_diretor = nome_diretor
        self.ano_entrada = ano_entrada

    def __str__(self):
        return self.nome_diretor


class Sala:
    def __init__(self, serie, nome_sala):
        self.serie = serie
        self.nome_sala = nome_sala
        self.professores = []
        self.alunos = []

    def __str__(self):
        return f"{self.serie} - {self.nome_sala}"

    def __repr__(self):
        return f"{self.serie} - {self.nome_sala}"

    def add_professor(self, professor):
        self.professores.append(professor)

    def add_aluno(self, aluno):
        self.alunos.append(aluno)

    def get_total_alunos(self):
        return len(self.alunos)


class Professor:
    def __init__(self, nome_professor, materia):
        self.nome_professor = nome_professor
        self.materia = materia

    def __str__(self):
        return self.nome_professor

    def __repr__(self):
        return self.nome_professor
    

class Aluno:
    def __init__(self, nome_aluno, idade):
        self.nome_aluno = nome_aluno
        self.idade = idade

    def __str__(self):
        return self.nome_aluno

    def __repr__(self):
        return f"Aluno(nome_aluno={self.nome_aluno}, idade={self.idade})"


def load_data(escola_dict):
    escola = Escola(escola_dict['nomeEscola'], escola_dict['endereco'])

    for diretor_dict in escola_dict['diretoria']:
        diretor = Diretor(diretor_dict['nome'], diretor_dict['anoEntrada'])
        escola.add_diretoria(diretor)

    for sala_dict in escola_dict['salas']:
        sala = Sala(sala_dict['serie'], sala_dict['nome'])    
        escola.add_salas(sala)

        for professor_dict in sala_dict["professores"]:
            professor = Professor(professor_dict['nome'], professor_dict['materia'])
            sala.add_professor(professor)

        for aluno_dict in sala_dict['alunos']:
            aluno = Aluno(aluno_dict['nome'], aluno_dict['idade'])
            sala.add_aluno(aluno)

    return escola

escola = load_data(escola_dict)

# print(escola.get_alunos_maior_18())
# print(escola.get_alunos_menor_18())
# print(escola.get_quantidade_total_alunos())
escola.remove_aluno("A", "Renan Quirino")


