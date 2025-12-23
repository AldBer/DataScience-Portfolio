# data/data_processors.py - VERSÃO CORRIGIDA
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class SalesDataProcessor:
    """Processa dados de vendas para o dashboard"""
    
    @staticmethod
    def generate_sales_from_products(products_data, days=90):
        """Gera dados de vendas simulados baseados em produtos reais"""
        sales_records = []
        
        for product in products_data:
            # Gerar vendas dos últimos 'days' dias
            for i in range(days):
                sale_date = datetime.now() - timedelta(days=days - i)
                
                sales_records.append({
                    'date': sale_date.date(),
                    'product_id': product['id'],
                    'product_name': product['title'][:30],  # Limitar tamanho
                    'category': product['category'],
                    'price': product['price'],
                    'units_sold': np.random.randint(1, 20),
                    'region': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste']),
                    'customer_type': np.random.choice(['Novo', 'Recorrente'])
                })
        
        df = pd.DataFrame(sales_records)
        df['total_sales'] = df['price'] * df['units_sold']
        df['date'] = pd.to_datetime(df['date'])
        
        return df
    
    @staticmethod
    def calculate_kpis(sales_df):
        """Calcula KPIs principais"""
        today = datetime.now().date()
        
        # Vendas hoje
        sales_today = sales_df[sales_df['date'].dt.date == today]['total_sales'].sum()
        
        # Vendas mês atual
        current_month = sales_df[sales_df['date'].dt.month == today.month]
        sales_month = current_month['total_sales'].sum()
        
        # Ticket médio
        avg_ticket = sales_df['total_sales'].mean()
        
        # Clientes únicos
        unique_customers = sales_df['customer_type'].value_counts()
        
        return {
            'sales_today': sales_today,
            'sales_month': sales_month,
            'avg_ticket': avg_ticket,
            'customer_breakdown': unique_customers.to_dict()
        }