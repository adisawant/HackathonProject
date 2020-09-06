from flask import Flask, url_for, render_template, redirect
from forms import PredictForm
from flask import request, sessions
import requests
from flask import json
from flask import jsonify
from flask import Request
from flask import Response
import urllib3
import json
# from flask_wtf import FlaskForm

app = Flask(__name__, instance_relative_config=False)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'development key' #you will need a secret key

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')

@app.route('/', methods=('GET', 'POST'))

def startApp():
    form = PredictForm()
    return render_template('index.html', form=form)

@app.route('/predict', methods=('GET', 'POST'))
def predict():
    form = PredictForm()
    if form.submit():

        # NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation
        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer '
                 + " eyJraWQiOiIyMDIwMDgyMzE4MzIiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC01NTAwMDhRUFkzIiwiaWQiOiJJQk1pZC01NTAwMDhRUFkzIiwicmVhbG1pZCI6IklCTWlkIiwiaWRlbnRpZmllciI6IjU1MDAwOFFQWTMiLCJnaXZlbl9uYW1lIjoiQWRpdHlhIiwiZmFtaWx5X25hbWUiOiJTYXdhbnQiLCJuYW1lIjoiQWRpdHlhIFNhd2FudCIsImVtYWlsIjoiYWRpdHlhLnNhd2FudEBsbnRpbmZvdGVjaC5jb20iLCJzdWIiOiJhZGl0eWEuc2F3YW50QGxudGluZm90ZWNoLmNvbSIsImFjY291bnQiOnsidmFsaWQiOnRydWUsImJzcyI6ImZhYjVjN2Y1OGE0YzQzNmViNzQ3NGU2ZjliMThiMDdlIiwiZnJvemVuIjp0cnVlfSwiaWF0IjoxNTk5Mzg4MTEzLCJleHAiOjE1OTkzOTE3MTMsImlzcyI6Imh0dHBzOi8vaWFtLmJsdWVtaXgubmV0L2lkZW50aXR5IiwiZ3JhbnRfdHlwZSI6InVybjppYm06cGFyYW1zOm9hdXRoOmdyYW50LXR5cGU6YXBpa2V5Iiwic2NvcGUiOiJpYm0gb3BlbmlkIiwiY2xpZW50X2lkIjoiZGVmYXVsdCIsImFjciI6MSwiYW1yIjpbInB3ZCJdfQ.q6KyhT3q8NKUZ6aU-N6Ps2kRnMALqgRRP09zm-6n173EZ_AFmaSTAlZcu1Wgg2xtcd3cMSrVzIJyGAYwv0MdE7b2kQuXw-daLodC0YmWxtQIkpeX2dKifMnaLOV3-rVUkZ66XZjzRCUY9eZxGco1NeUeDuYz-UktL_aij0zNq-uTT_9KPa-TSDilMBhdHa1gcbDYFxYLwI1uNmVTBpsOc5_umX6ADk3pITFr30SHqzyn4gpLF6AMIzD9YByYLbGsq7HIsoW9xwYTGWjn0eP46l6SLPaUcnLcSW5s8A57X8znblin8B934R0kbPXJ1XXj-UjcvmBT8lkpuWElzhD3yA","refresh_token":"OKBe2yC5w9-srfioDY0QrpJZ_XcapZeGyh0dp8jjU8OE3_zioF0MsAHIjotxCK8wCXJitGj8Dz1IW1QmWcL7ctFP5RnJzBBXxteV9wpjuZ8oRbN-0bnqx9nj1WlexZcw__pmtzhyd7rT1Tv78AYu3LbvRV78sN5DDyQ4fMYAjmE8VTqk9i7zzIXaRFFbpNKM053xel_i78mXqHEOYpnyLdgHcZNoEzCP7v4i42C9daBsbfXftaVGiB4jrancUrNn6okDGG-uyKMVOWn8O6foRU0TJZrP-XYNd4kk05MsPQgAjWg55kDW4joNmdWVKE87QZCUJZrawPqg1mjVQz5bWR9DVM0DgQbeCYpZzGeIACtx8CCk-lRLTSgElb8hGr3D9EzCPMpdCgKFdaGD83JNnJpwNocfJWse-voHPwtqO57FOR1Mj9Bn_fJN54qUz9bzPoM51Zvd9jrPkRr0mbav73OHgxzsINvR9x1ZXYKlRbXm4Hbemtv5HZcsyCT3o0Fqja8e_2X7m0HkYi0pIT0vCERb64hkPvnYUhXyoRxkhTKuTNp-QM9BeonDhfPIODxPzUbJriUf_46TbPaghkudZV-5GN_j7SECv56nMgkNp2eua-REPP4WCB4f5hG9m1YaZECSUM2Xj88D-QR_Jt_nQOs1hfJGr59tavBq92Q-nS6zpbNGHdEdlioYnghgk6FGa69EqmOS7xyXwq0C62MyV-dNq1r_uQTPlp21CckbN3KLQImOoQt8KTbqvgU7j8RB67ONMucgX_6ijpK9AO_FHpGfhAvTH_TjjBv8pabNhml1WUP4TooyPJ4JkEFVeulKNJ5j2rtKUMyh29fJSZ1BYyDkLadAnY5zv22M672TGcblKiA8-RTUoQtCbB7dYWM2TrFCy58F4nenKH_KapsDs-KJkZIT56ncnWPK1Dk2XM2zoOPN3dZNohoQJin07glP5DEOb-7KHTfSl29F8P6ZrPHfkDOE0lTm5-EghhxHMj20tTDSyre72chTvX8Jh4Vu1s07NVdyaLpzOLwly8CI2gS30PrvyECjFkEhemhA2_dbaCMI8A6RuVY1mkLgxa-PEguVtibbUszjVFis_NHnZxaW",
                  'ML-Instance-ID':"7416447f-2eec-4a9d-9bfc-9f1258921d52::"}

        if(form.VALUE.data == None): 
          python_object = []
        else:
          python_object = [form.RFDE_CUST_REG_NUM.data, 	   form.RFDE_RPT_DT.data,form.RFDE_TXN_ID.data,form.FII.data,form.SUB_ACC.data,form.BRKER.data,form.SCRIP_NAME.data,form.ISIN.data,form.TR_DATE.data,form.TR_TYPE.data,form.RFDE_SE_REG_NUM.data,form.RFDE_STLD_CODE.data, float(form.RATE.data),float(form.QUANTITY.data),float(form.VALUE.data),form.RFDE_INSTR_TYPE.data, form.RFDE_REASON_DLAY.data,form.RFDE_RPT_TYPE.data,form.RFDE_AMDMNT_REASON.data]
        #Transform python objects to  Json

        userInput = []
        userInput.append(python_object)

        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {"input_data": [{"fields": ["RFDE_CUST_REG_NUM", "RFDE_RPT_DT", "RFDE_TXN_ID",
          "FII", "SUB_ACC", "BRKER","SCRIP_NAME","ISIN","TR_DATE","TR_TYPE","RFDE_SE_REG_NUM","RFDE_STLD_CODE","RATE","QUANTITY","VALUE","RFDE_INSTR_TYPE","RFDE_REASON_DLAY","RFDE_RPT_TYPE","RFDE_AMDMNT_REASON"], "values": userInput }]}

        response_scoring = requests.post("https://us-south.ml.cloud.ibm.com/v4/deployments/4639944c-7afe-41f3-9f62-ae5925cdb11b/predictions", json=payload_scoring, headers=header)

        output = json.loads(response_scoring.text)
        print(output)
        for key in output:
          ab = output[key]
        

        for key in ab[0]:
          bc = ab[0]    #[key]
        
        #roundedCharge = round(bc[0][0],2)

  
        form.abc = bc #this returns the response back to the front page
	
	#if (form.VALUE.data=='0'):
	 #form.abc = "Fail"
	#else :
	 #form.abc = "Success"
	#print(form.abc)
        return render_template('index.html', form=form)