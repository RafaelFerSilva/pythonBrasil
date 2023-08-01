class Cpf:
    # Criar o construtor da classe que já transforma o valor em string e faz a validação
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_e_Valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!!")

    # Sobrescrever o método str para implementar o retorno da classe
    def __str__(self):
        return self.format_cpf()

    # Método para validar o documento
    @staticmethod
    def cpf_e_Valido(documento):
        if len(documento) == 11:
            return True
        else:
            return False

    # Método para formatar o documento
    def format_cpf(self):
        fatia_um = self.cpf[:3]
        fatia_dois = self.cpf[3:6]
        fatia_tres = self.cpf[6:9]
        fatia_quatro = self.cpf[9:]
        return "{}.{}.{}.{}".format(fatia_um, fatia_dois, fatia_tres, fatia_quatro)
