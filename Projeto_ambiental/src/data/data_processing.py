# src/data/data_processing.py

import pandas as pd
import numpy as np
import os

class DataProcessor:
    """
    Processa e carrega os dados ambientais históricos e gera projeções.
    """
    def __init__(self, data_path='data'):
        self.data_path = data_path
        self.datasets = {}
        self._load_historical_data()

    def _load_historical_data(self):
        """Carrega os dados históricos dos arquivos CSV."""
        try:
            # Note: The actual file names are amazon_deforestation.csv, biodiversity_index.csv, global_co2.csv
            # But we want to map them to more dashboard-friendly keys for internal use.
            self.datasets['amazon_deforestation'] = pd.read_csv(os.path.join(self.data_path, 'amazon_deforestation.csv'))
            self.datasets['biodiversity_index'] = pd.read_csv(os.path.join(self.data_path, 'biodiversity_index.csv'))
            self.datasets['global_co2'] = pd.read_csv(os.path.join(self.data_path, 'global_co2.csv'))
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Erro ao carregar arquivo de dados: {e}. Certifique-se de que os arquivos CSV estão na pasta 'data'.")
        except Exception as e:
            raise Exception(f"Erro inesperado ao carregar dados históricos: {e}")

    def get_historical_data(self, indicator_key: str) -> pd.DataFrame:
        """
        Retorna os dados históricos para um indicador específico usando a chave interna.
        Args:
            indicator_key (str): Chave interna do indicador (e.g., 'amazon_deforestation', 'biodiversity_index', 'global_co2').
        Returns:
            pd.DataFrame: DataFrame contendo os dados históricos.
        Raises:
            ValueError: Se o indicador não for encontrado.
        """
        if indicator_key not in self.datasets:
            raise ValueError(f"Indicador '{indicator_key}' não encontrado nos dados históricos.")
        return self.datasets[indicator_key].copy() # Retorna uma cópia para evitar modificações externas

    def generate_projected_data(self, indicator_key: str, start_year: int, end_year: int) -> pd.DataFrame:
        """
        Gera dados projetados de forma linear ou com base em tendências para um indicador.
        Args:
            indicator_key (str): Chave interna do indicador (e.g., 'amazon_deforestation', 'biodiversity_index', 'global_co2').
            start_year (int): Ano de início da projeção.
            end_year (int): Ano de fim da projeção.
        Returns:
            pd.DataFrame: DataFrame contendo os dados projetados.
        Raises:
            ValueError: Se o indicador for desconhecido para projeção.
        """
        historical_df = self.get_historical_data(indicator_key)
        if historical_df.empty:
            return pd.DataFrame()

        last_historical_year = historical_df['Ano'].max()
        if start_year <= last_historical_year:
            start_year = last_historical_year + 1

        projection_years = range(start_year, end_year + 1)
        num_years = len(projection_years)

        # Ensure correct column names for historical data
        if indicator_key == 'amazon_deforestation':
            value_col = 'Area_km2'
            if value_col not in historical_df.columns:
                raise ValueError(f"Coluna '{value_col}' não encontrada no DataFrame histórico para desmatamento.")
            last_value = historical_df[value_col].iloc[-1]
            # Simple linear increase for projection
            projected_values = np.linspace(last_value, last_value * 1.5, num_years)
            return pd.DataFrame({'Ano': projection_years, value_col: projected_values})
        elif indicator_key == 'global_co2':
            value_col = 'CO2_ppm'
            if value_col not in historical_df.columns:
                raise ValueError(f"Coluna '{value_col}' não encontrada no DataFrame histórico para CO2.")
            last_value = historical_df[value_col].iloc[-1]
            # Simple linear increase for projection
            projected_values = np.linspace(last_value, last_value * 1.05, num_years)
            return pd.DataFrame({'Ano': projection_years, value_col: projected_values})
        elif indicator_key == 'biodiversity_index':
            value_col = 'Species_threatened_pct'
            if value_col not in historical_df.columns:
                raise ValueError(f"Coluna '{value_col}' não encontrada no DataFrame histórico para biodiversidade.")
            last_value = historical_df[value_col].iloc[-1]
            # Simple linear increase for projection
            projected_values = np.linspace(last_value, last_value * 1.2, num_years)
            return pd.DataFrame({'Ano': projection_years, value_col: projected_values})
        else:
            raise ValueError(f"Projeção não configurada para o indicador: {indicator_key}")

    def get_all_data(self, projection_end_year: int = 2035):
        """
        Retorna todos os datasets, históricos e projetados, usando chaves padronizadas.
        """
        data = {}
        # Mapping from internal file names to desired dictionary keys
        indicator_key_map = {
            'amazon_deforestation': 'desmatamento',
            'global_co2': 'co2',
            'biodiversity_index': 'bio'
        }

        for internal_name, data_key_prefix in indicator_key_map.items():
            historical_df = self.get_historical_data(internal_name)
            projected_df = self.generate_projected_data(internal_name, historical_df['Ano'].max() + 1, projection_end_year)

            data[f'historico_{data_key_prefix}'] = historical_df
            data[f'projetado_{data_key_prefix}'] = projected_df
        return data