#Module used to get the date and time
import time
from flask import Flask, render_template, request, send_file
import uuid_service as service
import filemanager
app = Flask(__name__)


@app.route('/')
def index():
    """
    index function executed when the user come to the main page of the website
    Return: uuid_generator page with parameters
    """
    new_uuid = service.uuid_generation(True)
    return render_template('UUID_generator.j2', UUID=new_uuid, version="4", refreshlink="/",
                           explanation="""
                           The generation of a v4 UUID is simple to comprehend. 
                           The bits that comprise a UUID v4 are generated randomly and with no inherent logic. 
                           Because of this, there is no way to identify information about 
                           the source by looking at the UUID.""")

@app.route('/uuid-v1')
def uuidv1():
    """
    uuidv1 function executed when the user come to the page to get a uuuid V1
    Return: uuid_generator V1 page with parameters
    """
    new_uuid = service.uuid_generation(False)
    return render_template('UUID_generator.j2', UUID=new_uuid, version="1", refreshlink="/uuid-v1",
                           explanation="""
                           UUID v1 is generated by using a combination the host computers 
                           MAC address and the current date and time. In addition to this, 
                           it also introduces another random component just to be sure of its uniqueness. 
                           This means you are guaranteed to get a completely unique ID, unless you generate 
                           it from the same computer, and at the exact same time. In that case, the chance 
                           of collision changes from impossible to very very small because of the random bits. 
                           This guaranteed uniqueness comes at the cost of anonymity. 
                           Because UUID v1 takes the time and your MAC address into consideration, 
                           this also means that someone could potentially 
                           identify the time and place(i.e. computer) of creation. 
                           Try regenerating the UUIDs above, and you will see that 
                           some part of the UUID v1 is constant.""")

@app.route('/file-generator')
def uuid_file_gen():
    """
    uuid_file_gen executed when ther user want to access to the multi-uuids generator
    Return: form page to get multiple uuids
    """
    return render_template('UUID_multiplegenerator.j2')

@app.route('/post-generate', methods=['get', 'post'])
def generate():
    """Function used when the user request a file of uuids
    Return: A file with uuids"""
    uuid_version=request.form['version_select']
    number_uuid=int(request.form['number'])
    date = time.strftime("%Y%m%d-%H%M%S")
    filename=f"{date}_uuid_list.csv"
    uuid_list = service.loop_uuidgeneration(uuid_version, number_uuid)
    filemanager.create_uuid_file(f"static/uuid_files/{filename}", uuid_list)
    return send_file(f"static/uuid_files/{filename}",download_name=f'{filename}',as_attachment=True)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
 