# src/interface/dashboard.py

import streamlit as st
import time
from src.data.data_processing import DataProcessor
from src.visualization.graficos import Visualization
from src.util.dicas import TipGenerator

class DashboardApp:
    """
    Classe principal para o aplicativo Streamlit do Dashboard Ambiental.
    """
    def __init__(self):
        self.data_processor = DataProcessor()
        # Inicializa all_data com um dicionário vazio para evitar KeyErrors iniciais
        self.all_data = {} 
        try:
            self.all_data = self.data_processor.get_all_data()
        except Exception as e:
            st.error(f"Erro ao carregar dados iniciais: {e}. Verifique seus arquivos CSV.")
            # Se houver um erro, self.all_data permanecerá vazio ou parcial,
            # e as checagens abaixo lidarão com isso.
        
        self.visualization = Visualization()
        self.tip_generator = TipGenerator()


    def create_dashboard(self):
        """Cria e exibe o dashboard Streamlit."""
        st.title("🌿 Dashboard Ambiental FAESA 2035")

        with st.sidebar:
            st.header("Configurações")
            indicator = st.radio(
                "Selecione o indicador:",
                ("Desmatamento", "Emissões CO₂", "Biodiversidade")
            )

            # Painel de informações (Dicas/Alertas)
            self._display_info_panel(indicator)

            # --- SEÇÃO DO QUESTIONÁRIO ---
            st.markdown("---")
            st.subheader("Questionário") # Título estático "Questionário"

            # Removidas as linhas de inicialização de session_state para as perguntas
            # Removido o argumento 'value' dos st.text_area

            pergunta1 = st.text_area(
                f"Qual seria sua proposta para um futuro melhor em relação a {indicator.lower()}?",
                key=f"pergunta1_{indicator}"
            )

            pergunta2 = st.text_area(
                f"O que você faz para contribuir para um futuro melhor em relação a {indicator.lower()}?",
                key=f"pergunta2_{indicator}"
            )

            # Removido o argumento 'on_click' do st.button
            if st.button("Enviar Respostas", key=f"enviar_{indicator}"):
                if pergunta1 and pergunta2:
                    st.success("Obrigado pelas suas respostas! Suas ideias são valiosas!")
                    # Opcional: Adicione código aqui para salvar as respostas, se desejar manter o registro
                    # Exemplo:
                    # with open("respostas_questionario.txt", "a") as f:
                    #     f.write(f"Indicador: {indicator}\n")
                    #     f.write(f"Proposta: {pergunta1}\n")
                    #     f.write(f"Ações: {pergunta2}\n\n")
                    
                    # Removida a linha st.rerun() que causava o comportamento indesejado
                else:
                    st.warning("Por favor, responda ambas as perguntas antes de enviar.")

            # --- FIM DA SEÇÃO DO QUESTIONÁRIO ---

            # Seção de criadores
            st.markdown("---")
            st.subheader("Criadores")
            st.write("👨‍💻 Rafael Caires Mergulhão 👩‍💻 Maria Isabel")

        # Gráfico principal
        self._display_main_chart(indicator)

    def _display_info_panel(self, indicator: str):
        """Exibe o painel de informações com dicas ou alertas."""
        info_placeholder = st.empty()
        
        # Mapeamento dos nomes de exibição para nomes internos para as dicas
        indicator_map = {
            "Desmatamento": "desmatamento",
            "Emissões CO₂": "co2",
            "Biodiversidade": "biodiversidade"
        }
        
        internal_indicator_name = indicator_map.get(indicator, "desmatamento") # Padrão para desmatamento

        if 'last_info_update' not in st.session_state:
            st.session_state.last_info_update = time.time()
            st.session_state.info_text = self.tip_generator.get_tip(internal_indicator_name)
        
        # Atualiza a dica a cada 10 segundos
        if (time.time() - st.session_state.last_info_update) > 10:
            st.session_state.last_info_update = time.time()
            st.session_state.info_text = self.tip_generator.get_tip(internal_indicator_name)
            st.rerun() 
        
        info_placeholder.info(st.session_state.info_text)

    def _display_main_chart(self, indicator: str):
        """Exibe o gráfico principal com base no indicador selecionado."""
        # Adicione verificações para garantir que os dados existam antes de tentar criar o gráfico
        if indicator == "Desmatamento":
            if 'historico_desmatamento' in self.all_data and 'projetado_desmatamento' in self.all_data:
                fig = self.visualization.create_deforestation_chart(
                    self.all_data['historico_desmatamento'], 
                    self.all_data['projetado_desmatamento']
                )
            else:
                st.warning("Dados de Desmatamento não disponíveis para exibição do gráfico.")
                return
        elif indicator == "Emissões CO₂":
            if 'historico_co2' in self.all_data and 'projetado_co2' in self.all_data:
                fig = self.visualization.create_co2_chart(
                    self.all_data['historico_co2'], 
                    self.all_data['projetado_co2']
                )
            else:
                st.warning("Dados de Emissões CO₂ não disponíveis para exibição do gráfico.")
                return
        elif indicator == "Biodiversidade":
            if 'historico_bio' in self.all_data and 'projetado_bio' in self.all_data:
                fig = self.visualization.create_biodiversity_chart(
                    self.all_data['historico_bio'], 
                    self.all_data['projetado_bio']
                )
            else:
                st.warning("Dados de Biodiversidade não disponíveis para exibição do gráfico.")
                return
        else:
            st.error("Indicador selecionado inválido.")
            return

        st.plotly_chart(fig, use_container_width=True)