class MyCtxManager:
    def __init__(self, filename, method='r'):
        self.__file_obj = open(filename, method)

    def __enter__(self):
        return self.__file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__file_obj.close()


with MyCtxManager('../texte/my_data.txt', 'x') as f:
    f.write('saluuut')
