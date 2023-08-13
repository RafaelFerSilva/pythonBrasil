from datetime import datetime, timedelta


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        mes = self.momento_cadastro.month - 1
        return meses_do_ano[mes]

    def dia_semana(self):
        dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        dia = self.momento_cadastro.weekday()
        return dias_semana[dia]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada


    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro