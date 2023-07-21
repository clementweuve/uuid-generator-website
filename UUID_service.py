import uuid
import time
import random

def uuid_generation(version4:bool):
    if version4==True:
        return(str(uuid.uuid4()))
    else:
        return(str(uuid.uuid1()))
    
def loop_uuidgeneration(version4:bool, n:int):
    UUID_List=[]
    for _ in range(n):
        UUID_List.append(uuid_generation(version4))
        time.sleep(random.uniform(0.01, 0.07))
    return UUID_List