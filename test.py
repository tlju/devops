#!/usr/bin/env python
import os
from datetime import timedelta
import random


if __name__ == '__main__':

    # 使用django配置文件进行设置
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devops.settings')
    # 让django初始化
    import django
    django.setup()

    from redismultibeat import RedisBeatManager
    from devops import celery_app as app

    app.loader.import_default_modules()
    tasks = list(sorted(name for name in app.tasks if not name.startswith('celery.')))
    print(tasks)

    manager = RedisBeatManager(app=app)
    for task in manager.iter_tasks():
        print(task)

    # print('remove----------------------', end='')
    # print(manager.remove('task_check_scheduler'))
    # for task in manager.iter_tasks():
    #     print(task)
    #
    # print(manager.remove('task_check_scheduler'))
    #
    # print('add----------------------', end='')
    # print(manager.add(**{
    #     'name': 'task_check_scheduler_cron_2',
    #     'task': 'tasks.tasks.task_check_scheduler',
    #     'schedule': timedelta(seconds=7200),
    #     "args": (None, 1, 3),
    # }))
    # for task in manager.iter_tasks():
    #     print(task)
    #
    # print('modify----------------------', end='')
    # print(manager.modify(**{
    #     'name': 'task_check_scheduler_cron_2',
    #     'task': 'tasks.tasks.task_check_scheduler',
    #     'schedule': timedelta(seconds=random.randint(3600,7200)),
    #     "args": (None, 1, 3),
    # }))
    # for task in manager.iter_tasks():
    #     print(task)
    #
    # print(manager.task('task_check_scheduler'))
    #
    # print(manager.remove_all())
    #
    # for task in manager.iter_tasks():
    #     print(task)
    #
    print(manager.remove_all())
    manager.close()
