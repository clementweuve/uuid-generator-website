from apscheduler.schedulers.background import BackgroundScheduler
import os

scheduler = BackgroundScheduler()

def UUID_File_Management():
    Files = os.listdir("static/UUID_files/")
    if Files!=None:
        for file in Files:
            os.remove(f'static/UUID_files/{file}')


def create_UUID_file(filepath:str, UUID_L:list):
    file = open(filepath, "w+")
    for uuid in UUID_L:
        file.write(f"{uuid} \n" )
    file.close()

scheduler.add_job(UUID_File_Management, 'interval', seconds=120)
scheduler.start()