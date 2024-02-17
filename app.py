from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import numpy as np
from keras.models import model_from_json
from tensorflow.keras import optimizers
import os
import keras
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.applications.vgg16 import decode_predictions
from tensorflow.keras.applications.vgg16 import VGG16
import numpy as np

def loadModel():
    json_file = open("model.json", 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")

    loaded_model.compile(optimizer=optimizers.RMSprop(lr=2e-4),
                loss='categorical_crossentropy',
                metrics=['acc'])

    return loaded_model

#แก้ที่นี่
def decode(class_num):
    
    
    if class_num == 0:
        return "Flute"
    
    if class_num == 1:
        return "Guiro"
    
    if class_num == 2:
        return "Bagpipes"
    
    if class_num == 3:
        return "Drums"
    
    if class_num == 4:
        return "Didgeridoo"
    
    if class_num == 5:
        return "Dulcimer"
    
    if class_num == 6:
        return "Trombone"
    
    if class_num == 7:
        return "Castanets"
    
    if class_num == 8:
        return "Tambourine"
    
    if class_num == 9:
        return "Acordian"
    
    if class_num == 10:
        return "Banjo"
    
    if class_num == 11:
        return "Marakas"
    
    if class_num == 12:
        return "Saxaphone"
    
    if class_num == 13:
        return "Ocarina"
    
    if class_num == 14:
        return "Clavichord"
    
    if class_num == 15:
        return "Harp"
    
    if class_num == 16:
        return "Trumpet"
    
    if class_num == 17:
        return "Steel Drum"
    
    if class_num == 18:
        return "Alphorn"
    
    if class_num == 19:
        return "Guitar"
    
    if class_num == 20:
        return "Tuba"
    
    if class_num == 21:
        return "Concertina"
    
    if class_num == 22:
        return "Harmonica"
    
    if class_num == 23:
        return "Violin"
    
    if class_num == 24:
        return "Bongo Drum"
    
    if class_num == 25:
        return "Clarinet"
    
    if class_num == 26:
        return "Piano"
    
    if class_num == 27:
        return "Casaba"
    
    if class_num == 28:
        return "Xylophone"
    
    if class_num == 29:
        return "Sitar"
    
    if class_num == 30:
        return "Bagpipes"
    
    return "No Prediction"

app = Flask(__name__)
model = loadModel()
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 


@app.route('/')
def home():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['photograph']
      filename = secure_filename(f.filename)
      upload_location = os.path.join(app.config['UPLOAD_FOLDER'],filename)
      f.save(upload_location)

      img = load_img(upload_location  , target_size=(224, 224))
      x = img_to_array(img)
      x = np.expand_dims(x, axis=0)
      x = preprocess_input(x)
      predict_x=model.predict([x]) 
      y_pred=np.argmax(predict_x,axis=1)[0]
      print(y_pred, type(y_pred))
      class_name = decode(y_pred)

      return class_name

@app.route('/page1', methods = ['GET', 'POST'])
def page1():
    return render_template('page1.html')		

@app.route('/page2', methods = ['GET', 'POST'])
def page2():
    return render_template('page2.html')	

@app.route('/page3', methods = ['GET', 'POST'])
def page3():
    return render_template('page3.html')	

@app.route('/page4', methods = ['GET', 'POST'])
def page4():
    return render_template('page4.html')	

if __name__ == '__main__':
   app.run(debug = True)

