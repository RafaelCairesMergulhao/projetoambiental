import random
from datetime import datetime

class TipGenerator:
    """
    Gera dicas e alertas ambientais aleatórios para o dashboard.
    """
    BANCO_DICAS = {
        "desmatamento": [
            {
                "tipo": "dica",
                "conteudo": "Reduza o consumo de carne bovina - a pecuária responde por 80% do desmatamento na Amazônia.",
                "fonte": "INPE"
            },
            {
                "tipo": "alerta",
                "conteudo": "O desmatamento ilegal é uma grave ameaça. Denuncie!",
                "fonte": "IBAMA"
            }
        ],
        "co2": [
            {
                "tipo": "alerta",
                "conteudo": "Nível atual de CO2: 420 ppm - bem acima do limite seguro para um clima estável.",
                "fonte": "NOAA"
            },
            {
                "tipo": "dica",
                "conteudo": "Opte por transporte público ou bicicleta para reduzir sua pegada de carbono.",
                "fonte": "EPA"
            }
        ],
        "biodiversidade": [
            {
                "tipo": "dica",
                "conteudo": "Apoie projetos de conservação de espécies ameaçadas. Cada ação conta!",
                "fonte": "WWF"
            },
            {
                "tipo": "alerta",
                "conteudo": "A perda de habitat é a principal causa de extinção de espécies no Brasil.",
                "fonte": "ICMBio"
            }
        ]
    }

    def get_tip(self, theme: str) -> str:
        """
        Retorna uma dica ou alerta aleatório para um tema específico.
        Args:
            theme (str): O tema da dica (e.g., "desmatamento", "co2", "biodiversidade").
        Returns:
            str: Uma string formatada contendo a dica/alerta, tipo e fonte.
        """
        if theme not in self.BANCO_DICAS:
            return f"**INFO** ⚡\n\nNenhuma informação disponível para o tema: {theme}."
        
        info = random.choice(self.BANCO_DICAS[theme])
        return f"**{info['tipo'].upper()}** ⚡\n\n{info['conteudo']}\n\n_Fonte: {info['fonte']}_"