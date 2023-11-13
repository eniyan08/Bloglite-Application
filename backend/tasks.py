from celery import Celery
from celery.schedules import crontab
from httplib2 import Http
from json import dumps
# import workers
celery = Celery("simple job", broker = "redis://localhost", backend = "redis://localhost")
# def make_celery(app):
#     celery = Celery(
#         app.import_name,
#         backend=app.config['CELERY_RESULT_BACKEND'],
#         broker=app.config['CELERY_BROKER_URL']
#     )
#     celery.conf.update(app.config)

#     class ContextTask(celery.Task):
#         def __call__(self, *args, **kwargs):
#             with app.app_context():
#                 return self.run(*args, **kwargs)

    # celery.Task = ContextTask
    # return celery





# from app import app
# from tasks import make_celery, main
import random, time
# celery = workers.celery
# @celery.task()
def main(username):
   
    url = 'https://chat.googleapis.com/v1/spaces/AAAALRDI6jc/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=2dZxClgXYTdAb9EvpAJfopFKAmcJ639EKCMjkMEZLZA%3D'
    bot_message = {
        'text': username +' has posted'}
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
    print(response)

def daily_main(args):
    url = 'https://chat.googleapis.com/v1/spaces/AAAALRDI6jc/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=2dZxClgXYTdAb9EvpAJfopFKAmcJ639EKCMjkMEZLZA%3D'
    bot_message = {
        'text': args + 'common....Be a active user'}
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
    print(response)




@celery.task()
def task11(username):
    
    main(username)
    return random.randint(1,100)

@celery.task()
def task22():
    return "post exported"

@celery.task()
def daily_task(args):
    daily_main(args)
    return "hi"

@celery.task()
def monthly_task(args):
    monthly_main(args)
    return "hi"

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    sender.add_periodic_task(crontab(hour=17, minute=0),daily_task.s('heyyy'))

    sender.add_periodic_task(crontab(0,0, day_of_month='1'),monthly_task.s('heyyy'))


if __name__ == '__main__':
    main()