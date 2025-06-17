### Arquivos de Dados (`data/`)

* `amazon_deforestation.csv`: Dados históricos de desmatamento na Amazônia.
* `biodiversity_index.csv`: Dados históricos do índice de biodiversidade (ou percentual de espécies ameaçadas).
* `global_co2.csv`: Dados históricos de concentração global de CO₂.

### Código Fonte (`src/`)

* **`src/data/data_processing.py`**: Contém a lógica para carregar os dados históricos dos arquivos CSV e gerar projeções lineares simples para os anos futuros.
* **`src/interface/dashboard.py`**: Define a estrutura principal do dashboard Streamlit, incluindo a barra lateral, seleção de indicadores, exibição de gráficos, dicas e o questionário.
* **`src/util/dicas.py`**: Armazena e gerencia as dicas e alertas ambientais que são exibidos na barra lateral.
* **`src/visualization/graficos.py`**: Responsável por criar os gráficos interativos usando a biblioteca Plotly Express.

### Ponto de Entrada (`main.py`)

* **`main.py`**: O script principal para iniciar o aplicativo Streamlit.

## Como Executar o Dashboard

1.  **Pré-requisitos:**
    * Python 3.7+ instalado.
    * Pip (gerenciador de pacotes Python).

2.  **Instalação das Dependências:**
    Navegue até a pasta raiz do projeto (`projetoambiental`) no seu terminal e instale as bibliotecas necessárias:
    ```bash
    pip install streamlit pandas numpy plotly
    ```

3.  **Executar o Aplicativo:**
    Com as dependências instaladas, execute o dashboard a partir da pasta raiz do projeto:
    ```bash
    streamlit run main.py
    ```
    Isso abrirá o dashboard em seu navegador padrão.

## Criadores

* 👨‍💻 Rafael Caires Mergulhão
* 👩‍💻 Maria Isabel
