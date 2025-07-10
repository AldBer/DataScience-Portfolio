import requests
import traceback
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class TelegramBot:
    def __init__(self):
        self.token = os.getenv('TELEGRAM_TOKEN')
        self.chat_id = os.getenv('TELEGRAM_CHAT_ID')
        self.base_url = f"https://api.telegram.org/bot{self.token}"
        
        # Testa a conexão ao iniciar
        self._send_test_message()

    def _send_test_message(self):
        """Envia mensagem de inicialização"""
        self.send_alert("🤖 *Bot Iniciado*\\nModo: " + 
                       ("`TESTE`" if os.getenv('TEST_MODE') == 'True' else "`PRODUÇÃO`"))

    def send_alert(self, message: str, silent: bool = False) -> bool:
        """Envia mensagem formatada com markdown"""
        try:
            payload = {
                'chat_id': self.chat_id,
                'text': message,
                'parse_mode': 'MarkdownV2',
                'disable_notification': silent
            }
            response = requests.post(
                f"{self.base_url}/sendMessage",
                json=payload,
                timeout=5
            )
            return response.status_code == 200
        except Exception as e:
            print(f"⚠️ Falha no envio para Telegram: {str(e)}")
            return False

    def send_error(self, error: Exception, context: str = ""):
        """Envia erros formatados com traceback"""
        tb_str = traceback.format_exc()
        message = (
            f"🚨 *ERRO NO BOT*\\n\\n"
            f"*Contexto*: {context}\\n"
            f"*Hora*: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\\n\\n"
            f"```\n{str(error)}\n```\\n\\n"
            f"*Traceback*:\\n```\n{tb_str}\n```"
        )
        return self.send_alert(message)

# Uso no trading_bot.py
bot = TelegramBot()