import os
import json
# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build
class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = 'UCkbFiBwMYMXAqifXF4xo5Uw' #minimalists

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(channel)
