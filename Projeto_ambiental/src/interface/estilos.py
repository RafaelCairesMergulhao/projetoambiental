import streamlit as st

class AppStyles:
    """
    Gerencia os estilos e configurações da página Streamlit.
    """
    CORES = {
        'desmatamento': {
            'historico': "#2e8b57",   # Verde
            'projetado': "#9370db",   # Roxo
            'fundo': "#f7f7f7"
        },
        'co2': {
            'historico': "#3cb371",   # Verde-água
            'projetado': "#ba55d3",   # Lilás
            'limite': "#ff4500"       # Vermelho
        },
        'biodiversidade': {
            'historico': "#20b2aa",   # Verde-água escuro
            'projetado': "#da70d6",   # Orquídea
            'fundo': "#fffaf0"        # Branco floral
        }
    }

    def configure_styles(self):
        """Configura a página Streamlit com título, ícone e layout."""
        st.set_page_config(
            page_title="Dashboard Ambiental FAESA 2035",
            page_icon="🌿",
            layout="wide"
        )
        self._apply_custom_css()

    def _apply_custom_css(self):
        """Aplica estilos CSS personalizados para o dashboard."""
        # Note: Streamlit's internal CSS structure might change.
        # This CSS targets the 'stMetricValue' and 'st-bd' data-testid for styling.
        # The 'st-bd' class was a placeholder in the original and might not directly apply.
        # Focusing on stMetricValue for more reliable styling.
        st.markdown(f"""
            <style>
                /* Estilos para valores das métricas */
                [data-testid="stMetricValue"] {{
                    color: {self.CORES['biodiversidade']['historico']}; /* Exemplo: aplica cor verde-água escuro */
                }}
                /* Se houver necessidade de um fundo específico para um bloco */
                .st-metric {{ /* Targeting the metric container */
                    background-color: {self.CORES['biodiversidade']['fundo']}; 
                    padding: 10px;
                    border-radius: 5px;
                    margin-bottom: 10px;
                }}
            </style>
            """,
            unsafe_allow_html=True
        )