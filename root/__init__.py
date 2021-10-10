from web_getter import Web_Getter
from saver import Saver

task = input('Введите номер задания:')

web_getter = Web_Getter()
saver = Saver()

print('Идет скачивание файла, пожалуйста подождите..')
if saver.save_to_docx(str(task) + ' задание', web_getter.get_variant_text(task=task)):
    print('Успех! Сохранено в папку Documents!')
