"""
IGalleryExporter — экспорт изображений в gallery.obrazslov.ru
Согласно Манифесту САН V21.4 (Приложение 18.2)
"""
import os
from typing import List, Dict

class IGalleryExporter:
    def exportPropertyImages(self, propertyId: str) -> Dict:
        """Экспорт всех изображений объекта"""
        pass
    
    def createThematicPage(self, topic: str, imageIds: List[str]) -> str:
        """Создание тематической страницы (50 изображений)"""
        pass
    
    def syncMetadata(self) -> None:
        """Синхронизация метаданных с gallery.obrazslov.ru"""
        pass
