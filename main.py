import os
import pywebio
import threading

import pywebio.input as inp

from pywebio.output import *

from handlers.menu import TaskHandler
from handlers.parser import check_coins_balance


@pywebio.config(theme='dark')
async def main():
    clear()

    threading.Thread(target=check_coins_balance).start()

    task = TaskHandler()
    logo_path = os.path.join("data", 'logo.jpg')
    put_image(open(logo_path, 'rb').read())

    method = await inp.select(
        'Выберите нужный вариант', [
            'Добавить задание',
            'Список заданий'
        ]
    )

    if method == 'Добавить задание':
        await task.add_task_in_list()
    elif method == 'Список заданий':
        task.get_task_list()


if __name__ == '__main__':
    pywebio.start_server(main, host='127.0.0.1', port=8000)

