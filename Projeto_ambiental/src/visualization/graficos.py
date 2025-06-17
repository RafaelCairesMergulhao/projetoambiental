import plotly.graph_objects as go
from src.interface.estilos import AppStyles # Importa a classe de estilos

class Visualization:
    """
    Gerencia a criação de gráficos interativos com Plotly para o dashboard.
    """
    def __init__(self):
        self.colors = AppStyles.CORES # Acessa as cores através da classe de estilos

    def _create_base_chart(self, historico, projetado, y_col: str, title: str, y_axis_title: str, indicator_type: str):
        """
        Cria um gráfico base com dados históricos e projetados.
        Args:
            historico (pd.DataFrame): DataFrame com dados históricos.
            projetado (pd.DataFrame): DataFrame com dados projetados.
            y_col (str): Nome da coluna do eixo Y.
            title (str): Título do gráfico.
            y_axis_title (str): Título do eixo Y.
            indicator_type (str): Tipo do indicador para seleção de cores (e.g., 'desmatamento', 'co2', 'biodiversidade').
        Returns:
            go.Figure: Objeto Figure do Plotly.
        """
        fig = go.Figure()

        # Linha histórica
        if not historico.empty:
            fig.add_trace(go.Scatter(
                x=historico['Ano'],
                y=historico[y_col],
                name='Histórico',
                line=dict(color=self.colors[indicator_type]['historico'], width=3),
                mode='lines+markers'
            ))

        # Linha projetada
        if not projetado.empty:
            fig.add_trace(go.Scatter(
                x=projetado['Ano'],
                y=projetado[y_col],
                name='Projetado',
                line=dict(color=self.colors[indicator_type]['projetado'], width=3, dash='dash'),
                mode='lines+markers'
            ))

        # Layout do gráfico
        fig.update_layout(
            title={'text': title, 'x': 0.5, 'xanchor': 'center'},
            xaxis_title='Ano',
            yaxis_title=y_axis_title,
            hovermode='x unified',
            plot_bgcolor='white',
            legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
        )
        return fig

    def create_deforestation_chart(self, historico, projetado):
        """Cria gráfico de desmatamento com dados históricos e projeções."""
        fig = self._create_base_chart(
            historico, projetado,
            y_col='Area_km2',
            title='Desmatamento da Amazônia (km²/ano)',
            y_axis_title='Área Desmatada (km²)',
            indicator_type='desmatamento'
        )
        return fig

    def create_co2_chart(self, historico, projetado):
        """Cria gráfico de concentração de CO2 atmosférico."""
        fig = self._create_base_chart(
            historico, projetado,
            y_col='CO2_ppm',
            title='Concentração de CO₂ Atmosférico (ppm)',
            y_axis_title='Partes por milhão (ppm)',
            indicator_type='co2'
        )
        # Adiciona linha de limite crítico de CO2
        fig.add_hline(
            y=450,
            line=dict(color=self.colors['co2']['limite'], width=2, dash='dot'),
            annotation_text="Limite Seguro (450ppm)",
            annotation_position="bottom right"
        )
        return fig

    def create_biodiversity_chart(self, historico, projetado):
        """Cria gráfico de espécies ameaçadas de extinção."""
        fig = self._create_base_chart(
            historico, projetado,
            y_col='Species_threatened_pct',
            title='Espécies Ameaçadas de Extinção (%)',
            y_axis_title='Porcentagem de Espécies',
            indicator_type='biodiversidade'
        )
        return fig