class InstantiateCSVError(Exception):
    """Класс исключения для поврежденных файлов"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if len(args) > 0 else 'Файл item.csv поврежден'

    def str(self):
        return self.message