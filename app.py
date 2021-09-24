from flask import Flask, render_template, request
from analysis import *
import json
from flask import g

app = Flask(__name__)
global page
page = 1

@app.route('/')
def records():
    global page 
    start = (page-1) * 100
    end = (page * 100)
    return render_template('records.html',df=df, start=start, end=end, page=page)

@app.route('/changepage' , methods = ['POST'])
def changepage():
    global page 
    page = int(request.form['page'])
    start = 0
    end = 100
    if page > 489:
        page = 1
    else:
        if page == 489:
            start= 48800
            end = 48841
        else:
            start = (page-1) * 100
            end = (page * 100)
    return render_template('records.html',df=df, start=start, end=end, page=page)

@app.route('/analysis')
def analysis():
    global page
    page = 1
    return render_template('analysis.html', total_people=total_people, sexes=[sex_freq.to_html(classes='data', header=False)], work=[work_freq.to_html(classes='data', header=False)], ed=[ed_freq.to_html(classes='data', header=False)], marital=[marital_freq.to_html(classes='data', header=False)], occ=[occ_freq.to_html(classes='data', header=False)], relation=[relation_freq.to_html(classes='data', header=False)], race=[race_freq.to_html(classes='data', header=False)], countr=[country_freq.to_html(classes='data', header=False)], sex_50k=[sex_50k.to_html(classes='data', header=True)], sex_ed=[sex_ed.to_html(classes='data', header=True)], over50k=[fifty_freq.to_html(classes='data', header=True)])

@app.route('/graphs')
def graphs():
    global page
    page = 1
    return render_template('graphs.html')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port ='5150')
