# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате.

import pickle
print("Вывод из первого блока:")
from PZ_16_1 import Calculator
print("-"*50)


def safe_def(object, file_name):
    with open(file_name, "wb") as f1:
        pickle.dump(object, f1)

def load_def(file_name):
    with open(file_name, "rb") as f1:
        return pickle.load(f1)


calc1 = Calculator(10,8)
calc2 = Calculator(10,10)
calc3 = Calculator(4,8)

safe_def(calc1, "calc1.bin")
safe_def(calc2, "calc2.bin")
safe_def(calc3, "calc3.bin")

calc1_loaded = load_def("calc1.bin")
calc2_loaded = load_def("calc2.bin")
calc3_loaded = load_def("calc3.bin")

print(calc1_loaded.add())
print(calc2_loaded.add())
print(calc3_loaded.add())
