from logging import debug
from flask import Flask, render_template, request
import statistics as stat
import re

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

import joblib
from scrap import Scrap

from googletrans import  Translator

vec = joblib.load('model/vector_ind.joblib')
pred = joblib.load('model/pnews_ind.joblib')

vec_en = joblib.load('model/vector_en.joblib')
pred_en = joblib.load('model/pnews_en.joblib')

port_stem = PorterStemmer()
ts = Translator()

def stemming(content):
    stem_content = re.sub('[^a-zA-Z]', ' ', content)
    stem_content = stem_content.lower()
    stem_content = stem_content.split()
    stem_content = [port_stem.stem(word) for word in stem_content if not word is stopwords.words(lg)]  
    stem_content = ' '.join(stem_content)
    return stem_content


app = Flask(__name__) 




# ROUTING

@app.route('/') 
def home():
  return render_template('kosong.html')
  
@app.route('/news-predict/')
def news_pred():
  return render_template('index_np.html')
    
@app.route('/result-news-predict/', methods=['GET', 'POST'])
def result_np():
    prediction = []
    err = 'False'
    text1 = ''
    tltext1 = ''
    title1 = []
    content1 = []
    
    if request.method == 'POST': 
      text = request.form.get('text')
      tltext = request.form.get('ttl')
      url = request.form.get('url')
      text1 += text
      tltext1 += text
    else:
      pass
    
    if len(text) > 2:
      tltext = tltext
      tltext = stemming(tltext)
      tltext = vec.transform([tltext])
      prediction_t1 = pred.predict(tltext)
      
      text = text
      text = ts.translate(text, dest='english')
      lg = 'english'
      text = stemming(text)
      text = vec_en.transform([text])
      prediction_t2 = pred_en.predict(text)
      
      for i in prediction_t1:
      	prediction.append(i)
      	
      for j in prediction_t2:
      	prediction.append(j)
    else:
      prediction_t1 = [1,0]
      prediction_t2 = [1,0]
      
      for i in prediction_t1:
      	prediction.append(i)
    
      for j in prediction_t2:
      	prediction.append(j)
    
    if len(url) > 2:
      try:
        
          url = url
          tc = Scrap(url)
          title = tc['title']
          content = tc['content']
          
          title1 += title
          content1 += content
          
          lg = 'indonesian'
          title = [stemming(t) for t in title]
          lg = 'english'
          content = [stemming(c) for c in content]
          
          title = [ts.translate(t, dest='indonesian') for t in title]
          title = vec.transform(title)
          
          content = [ts.translate(c, dest='english') for c in content]
          content = vec_en.transform(content)
         
          prediction_ut = pred.predict(title)
          prediction_uc = pred_en.predict(content)
	      
          for i in prediction_ut:
	          prediction.append(i)
          for j in prediction_uc:
	          prediction.append(j)
	          
      except ValueError:
          err = 'True'
      
    else:
      prediction_ut = [1,0]
      prediction_uc = [1,0]
      
      for i in prediction_ut:
      	prediction.append(i)
      for j in prediction_uc:
      	prediction.append(j)
      
    
    nbenar = []
    nsalah = []
    
    for i in prediction:
    	if i == 1:
    		nbenar.append(i)
    	elif i == 0:
    		nsalah.append(i)
    	else:
    		pass
    
    nbenar = len(nbenar)
    nsalah = len(nsalah)
    
    benar = (100/len(prediction)) * nbenar
    salah = (100/len(prediction)) * nsalah
    
    ac = ''
    at = ''
    for i in content1:
      ac += ' ' + i
    for i in title1:
      at += ' ' + i
    
    return render_template('result_np.html', benar=benar, salah=salah, nbenar=nbenar, nsalah=nsalah, error=err, text=text1, tltext=tltext1, tit=at, con= ac)

@app.route('/result-news-predict/', methods=['POST'])
def rate():
    valrate = request.form.get('valrate')
    nama = request.form.get('nama')
    ulas = request.form.get('ulas')


if __name__ == '__main__': 
    app.run(debug=True) 
