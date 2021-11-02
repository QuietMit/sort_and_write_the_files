import os
path = os.path.join(os.getcwd())

def open_and_write(path):
    ''' Читает файлы, сортирует по количеству строк и записывает текст в один файл по возрастанию числа строк.
    
    Каждый блок текста начинается с имени файла-исходника, и числа строк в файле-исходнике.
    Блок кода для функции подготовлен на компьютере с установленной ОС Windows 7 с ограниченным доступом к администрированию,
    поэтому функция не работает в кодировке utf-8. '''
    new_dict = {}
    file_names = ['1.txt', '2.txt', '3.txt']
    for file in file_names:
        with open(path + '\\' + file, 'rt', encoding='cp1251') as text:
            name = file
            page = text.readlines()  # возвращается список, с элементами - 'строками'
            count = len(page)  # количество строк в тексте соответствует длине списка, состоящего из объектов-'строк'
            new_dict[name] = (count, page)
    # return new_dict # проверка
    n_l = []
    for key in sorted(new_dict, key = lambda x: new_dict[x][0]):
        n_l += [key + '\n']
        n_l += [str(new_dict[key][0]) + '\n']
        n_l += new_dict[key][1]
        n_l += ['\n']   
    # print(n_l) # проверка
    
    with open('united_data', 'wt', encoding='cp1251') as whole_text:
        for line in n_l:
            whole_text.write(line)
    with open('united_data', 'rt', encoding='cp1251') as file:
        return file.read()    
    
print(open_and_write(path))