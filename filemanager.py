"""OS module used to manage files for the uuid file generator"""
import os
import csv
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()


def uuid_file_management():
    """function that remove all uuids files generated
    
    Return: nothing
    """
    files = os.listdir("static/uuid_files/")
    if files is not None:
        for file in files:
            os.remove(f'static/uuid_files/{file}')


def create_uuid_file(filepath:str, uuid_list:list):
    """function that create the file for the user
    
    Keyword arguments:
    filepath:str -- path where the file is created
    uuid_list:str -- list of uuids generated

    Return: nothing
    """
    with open(filepath, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["uuid",])
        for uuid in uuid_list:
            writer.writerow([uuid,])


scheduler.add_job(uuid_file_management, 'interval', seconds=120)
scheduler.start()
