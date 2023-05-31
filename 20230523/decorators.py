# import time
# from functools import *
#
#
# def timp_executie(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         print('Start funcion')
#         result = func(args, kwargs)
#         t2 = time.time() - t1
#         print(f'functia {func.__name__} s-a executat incepand cu {t1} in {t2}s')
#         return result
#
#     return wrapper
#
#
# @timp_executie
# def afisati_informatii(nume, varsta):
#     time.sleep(1)
#     print(f'afisati_informatii a rualt cu parametrii: {nume}, {varsta}')
#     return 1
#
#
# # echivalent cu afisati_informatii = timp_executie(afisati_informatii) daca lipseste @...
#
#
# print(afisati_informatii('Mihai', 25))

import psutil as psutil


def logger(msg):
    def log_warnings():
        print(f'Logging memory data!{msg}')
        def isdebugmodeon():
            print(f'Debugging is active')
        isdebugmodeon()
    log_warnings()
    def log_errors():
        print(f'Error occured')
    log_errors()
logger(15)

def get_virtual_memory():
    return psutil.virtual_memory().percent

logger(get_virtual_memory())