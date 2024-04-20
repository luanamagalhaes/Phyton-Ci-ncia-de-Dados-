# Teoria ou paradigma de programação Orientado a Objetos, é a teoria da TERCEIRIZAÇÃO

# Ecossistema Python é rico em 
    # API                   - coleção de recursos para integração de serviços: pode conter frameworks e/ou bibliotecas
    # Framework             - coleção de classes/categorias e serviços
    # Bibliotecas/Pacotes   - coleção de serviços

class Glicemia: #todo nome de classe tende a começar com maiúsculo
    #Quinta,2012,ac,90,6,2037,246,4

    #é necessário de um método/serviço que crie ou instancie um objeto do tipo Glicemia
    def __init__(self, dia_semana, ano, valor_glicemia, valor_insulina, kcal, carb, qualidade_sono, padel, musculacao_R, musculacao_H, pilates, corrida, caminhada, tenis, sauna, bike, natacao, eliptico, volei_de_areia):
        self.dia_semana = dia_semana
        self.ano = ano
        self.valor_glicemia = int(valor_glicemia)
        self.valor_insulina = int(valor_insulina)
        self.kcal = int(kcal)
        self.carb = int(carb)
        self.qualidade_sono = int(qualidade_sono)
        self.padel = int(padel)
        self.musculacao_R = int(musculacao_R)
        self.musculacao_H = int(musculacao_H)
        self. pilates = int(pilates)
        self.corrida = int(corrida)
        self.caminhada = int(caminhada)
        self.tenis = int(tenis)
        self.sauna = int(sauna)
        self.bike = int(bike)
        self.natacao = int (natacao)
        self.eliptico = int(eliptico)
        self.volei_de_areia = int (volei_de_areia)



    #estamos reescrevendo o método que gera uma string do objeto Glicemia
    def __str__(self):
        return f"Glicemia[Dia:{self.dia_semana}, Ano:{self.ano}, Valor Glicemia:{self.valor_glicemia}, Insulina:{self.valor_insulina}, Kcal:{self.kcal}, Carb.:{self.carb}, Sono:{self.qualidade_sono}, {self.padel}, {self.musculacao_R}, {self.musculacao_H}, {self.pilates}, {self.corrida}, {self.caminhada}, {self.tenis}, {self.sauna}, {self.bike}, {self.natacao}, {self.eliptico}, {self.volei_de_areia}]"