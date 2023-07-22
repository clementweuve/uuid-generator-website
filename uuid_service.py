"""module used to generate uuid"""
import uuid
import time
import random

def uuid_generation(version4:bool):
    """Generate UUID
    
    Keyword arguments:
    version4:bool -- if True, UUIDV4 generated. If False, UUIDV1 generated.

    Return: UUID str
    """
    if version4 is True:
        return(str(uuid.uuid4()))
    return(str(uuid.uuid1()))


def loop_uuidgeneration(version4:bool, n_uuid:int):
    """Generate a list of uuid
    
    Keyword arguments:
    version4:bool -- if True, UUIDV4 generated. If False, UUIDV1 generated.
    n_uuid:int -- number uuids generated

    Return: UUID list
    """
    uuid_list=[]
    for _ in range(n_uuid):
        uuid_list.append(uuid_generation(version4))
        time.sleep(random.uniform(0.01, 0.07))
    return uuid_list
