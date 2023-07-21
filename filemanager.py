import os
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()


def uuid_file_management():
    files = os.listdir("static/UUID_files/")
    if files != None:
        for file in files:
            os.remove(f'static/UUID_files/{file}')


def create_uuid_file(filepath: str, uuid_list: list):
    file = os.open(filepath, "w+")
    for uuid in uuid_list:
        file.write(f"{uuid} \n")
    file.close()


scheduler.add_job(uuid_file_management, 'interval', seconds=120)
scheduler.start()
