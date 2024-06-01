from flask import Flask,render_template,request
import pickle
import pandas as pd

with open("model_GK.pkl","rb") as model_file:
         model=pickle.load(model_file)

app=Flask(__name__)

@app.route('/')
def player_position():
    return render_template('index.html')

@app.route('/input',methods=['GET','POST'])
def characterstics():
   if request.method=='POST':
      player_position=request.form['player_position']
      print(player_position)
   return render_template('input.html')


@app.route('/prediction',methods=['GET','POST'])
def prediction():
   if request.method=='POST':
      league_rank=request.form['league_rank']
      print(league_rank)
      international_reputation=request.form['international_reputation']
      weak_foot=request.form['weak_foot']
      body_type=request.form['body_type']
      movement_reactions=request.form['movement_reactions']
      power_shot_power=request.form['power_shot_power']
      GK_attribute=request.form['GK_attribute']

      model=pickle.load(open('model_GK.pkl','rb'))
      rating=model.predict([[1.0,3,3,3,88,59,237]])
      print(rating)
      rating=model.predict([[float(league_rank),int(international_reputation),int(weak_foot),int(body_type),int(movement_reactions),int(power_shot_power),int(GK_attribute)]])
      print(rating)
   return render_template('prediction.html',rating=rating)
   

if __name__=='__main__':
  app.run()