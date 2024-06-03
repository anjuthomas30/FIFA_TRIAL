from flask import Flask,render_template,request
import pickle
import pandas as pd

app=Flask(__name__)

@app.route('/')
def player_position():
    return render_template('index.html')

@app.route('/input_GK',methods=['GET','POST'])
def inputgk():
      if request.method=='GET':
          
       return render_template('input_GK.html')
@app.route('/prediction',methods=['GET','POST'])
def prediction_GK():
    if request.method=='POST':
      with open("model_GK.pkl","rb") as model_file:
            model=pickle.load(model_file)
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
   


@app.route('/input_FW',methods=['GET','POST'])
def inputfw():
   if request.method=='GET':
           
      return render_template('input_FW.html')
@app.route('/prediction_FW',methods=['GET','POST'])
def prediction_FW():
    if request.method=='POST':
      with open("model_FW.pkl","rb") as model_file:
        model=pickle.load(model_file)
      league_rank=request.form['league_rank']
      print(league_rank)
      international_reputation=request.form['international_reputation']
      weak_foot=request.form['weak_foot']
      skill_moves=request.form['skill_moves']
      work_rate=request.form['work_rate']
      body_type=request.form['body_type']
      attacking_short_passing=request.form['attacking_short_passing']
      attacking_volleys=request.form['attacking_volleys']
      skill_ball_control=request.form['skill_ball_control']
      
      movement_reactions=request.form['movement_reactions']
      power_shot_power=request.form['power_shot_power']
      power_long_shots=request.form['power_long_shots']
      mentality_positioning=request.form['mentality_positioning']
      mentality_composure=request.form['mentality_composure']
      shooting=request.form['shooting']
      passing=request.form['passing']
      
      dribbling=request.form['dribbling']

      model=pickle.load(open('model_FW.pkl','rb'))

      rating=model.predict([[1.0,5,4,4,6,3,91,88,96,94,86,94,93,96,92.0,91.0,95.0]])
      print(rating)
      rating=model.predict([[float(league_rank),int(international_reputation),int(weak_foot),int(skill_moves),int(body_type),int(work_rate),int(attacking_short_passing),int(attacking_volleys),
                             int(skill_ball_control),int(movement_reactions),int(power_shot_power),int(power_long_shots),
                             int(mentality_positioning),int(mentality_composure),float(shooting),
                             float(passing),float(dribbling)]])
      
      print(rating)
    return render_template('prediction_FW.html',rating=rating)



@app.route('/input_DEF',methods=['GET','POST'])
def inputdef():
   if request.method=='GET':
       
    return render_template('input_DEF.html')


@app.route('/prediction_DEF',methods=['GET','POST'])
def prediction_DEF():
    if request.method=='POST':
      with open("model_DEF.pkl","rb") as model_file:
            model=pickle.load(model_file)
      league_rank=request.form['league_rank']
      print(league_rank)
      international_reputation=request.form['international_reputation']
      weak_foot=request.form['weak_foot']
      work_rate=request.form['work_rate']
      body_type=request.form['body_type']
      attacking_heading_accuracy=request.form['attacking_heading_accuracy']
      attacking_short_passing	=request.form['attacking_short_passing']
      skill_ball_control=request.form['skill_ball_control']
      
      movement_reactions=request.form['movement_reactions']
      mentality_interceptions=request.form['mentality_interceptions']
      mentality_composure=request.form['mentality_composure']
      defending_sliding_tackle=request.form['defending_sliding_tackle']
      passing=request.form['passing']
      defending=request.form['defending']
      physic=request.form['physic']
      dribbling=request.form['dribbling']

      model=pickle.load(open('model_DEF.pkl','rb'))

      rating=model.predict([[1.0,3,3,8,2,87,79,77,89,90,90,86,71.0,91.0,86.0,71.0]])
      print(rating)
      rating=model.predict([[float(league_rank),int(international_reputation),int(weak_foot),int(work_rate),int(body_type),int(attacking_heading_accuracy),int(attacking_short_passing),
                             int(skill_ball_control),int(movement_reactions),int(mentality_interceptions),
                             int(mentality_composure),int(defending_sliding_tackle),float(passing),float(defending),
                             float(physic),float(dribbling)]])
      print(rating)
    return render_template('prediction_DEF.html',rating=rating)



   
@app.route('/input_MID',methods=['GET','POST'])
def inputmid():
   if request.method=='GET':      
      return render_template('input_MID.html')
@app.route('/prediction',methods=['GET','POST'])
def prediction_MID():
    if request.method=='POST':
      with open("model_MID.pkl","rb") as model_file:
        model=pickle.load(model_file)
      with open("le_MID.pkl","rb") as f:
        le_mid=pickle.load(f)
      league_rank=request.form['league_rank']
      print(league_rank)
      international_reputation=request.form['international_reputation']
      weak_foot=request.form['weak_foot']
      skill_moves=request.form['skill_moves']
      work_rate=request.form['work_rate']
      body_type=request.form['body_type']
      preferred_foot=request.form['preferred_foot']
      attacking_short_passing=request.form['attacking_short_passing']
      skill_dribbling=request.form['skill_dribbling']
      skill_long_passing=request.form['skill_long_passing']
      skill_ball_control=request.form['skill_ball_control']
      
      movement_reactions=request.form['movement_reactions']
      
      power_long_shots=request.form['power_long_shots']
      
      mentality_composure=request.form['mentality_composure']
      shooting=request.form['shooting']
      passing=request.form['passing']
      
      dribbling=request.form['dribbling']
      S=[[float(league_rank),int(international_reputation),int(weak_foot),
                             int(skill_moves),(work_rate),(body_type),int(preferred_foot),
                             int(attacking_short_passing),int(skill_dribbling),int(skill_long_passing),
                             int(skill_ball_control),int(movement_reactions),int(power_long_shots),
                             int(mentality_composure),float(shooting),
                             float(passing),float(dribbling)]]
      le_mid=pickle.load(open('le_MID.pkl','rb'))
      to_encode=S.select_dtypes(['object'])
      for col in to_encode.columns:
         S[col]=le_mid.transform(to_encode[col])
         
      model=pickle.load(open('model_MID.pkl','rb'))

      rating=model.predict([[1.0,3,3,2,0,2,1,84,69,84,79,87,81,84,73.0,76.0,72.0]])
      print(rating)
      rating=model.predict(S)
      
      print(rating)
    return render_template('prediction.html',rating=rating)   



 

if __name__=='__main__':
  app.run()