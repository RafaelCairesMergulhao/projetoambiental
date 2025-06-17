import streamlit as st
from src.interface.dashboard import DashboardApp
from src.interface.estilos import AppStyles

def main():
    """Função principal que inicializa e executa a aplicação Streamlit."""
    try:
        # Configuração inicial do Streamlit (título da página, ícone, layout)
        app_styles = AppStyles()
        app_styles.configure_styles()
        
        # Mensagem de inicialização
        st.toast("🌍 Iniciando Dashboard Ambiental FAESA 2035...", icon="🌿")
        
        # Cria e exibe o dashboard
        dashboard_app = DashboardApp()
        dashboard_app.create_dashboard()

    except FileNotFoundError as e:
        st.error(f"Erro: {e}. Por favor, verifique se todos os arquivos de dados necessários estão presentes.")
        st.stop() 
    except Exception as e:
        st.error(f"Ocorreu um erro inesperado: {e}")
        st.stop() 

if __name__ == "__main__":
    main()