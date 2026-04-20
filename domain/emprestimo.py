from dataclasses import dataclasses

@dataclasses
class Emprestimo:
    id: int
    crianca_id: int
    brinquedo_id: int
    datas: int
    status: str
    multa: float

    def calcular_multa(self, dias_atraso: int):
        if dias_atraso > 0:
            self.multa = dias_atraso * 2.0
        else:
            self.multa = 0.0

    def validar_idade_crianca(self, idade_crianca: int):
        if idade_crianca < 3:
            raise ValueError("Crianças menores de 3 anos não podem emprestar brinquedos.")

    def brinquedo_indisponivel(self, brinquedo_disponivel: bool):
        if not brinquedo_disponivel:
            raise ValueError("Brinquedo indisponível para empréstimo.")
    
    def maximo_emprestimos(self, emprestimos_ativos: int):
        if emprestimos_ativos >= 2:
            raise ValueError("Máximo de 2 empréstimos ativos por criança")
    
    def atualizar_status(self, novo_status: str):
        if novo_status not in ["disponivel", "devolvido", "atrasado"]:
            raise ValueError("Status inválido. Use 'disponivel', 'devolvido' ou 'atrasado'.")
        self.status = novo_status
    
    def bloquear_crianca(self, dias_atraso: int):
        if dias_atraso > 3:
            raise ValueError("Criança bloqueada por atraso superior a 3 dias.")

    
    


