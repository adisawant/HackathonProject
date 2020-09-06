from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import StringField, TextField, SubmitField, IntegerField,TextAreaField,RadioField,SelectField, DecimalField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import ValidationError

class PredictForm(FlaskForm):
   RFDE_CUST_REG_NUM = StringField('RFDE_CUST_REG_NUM')
   RFDE_RPT_DT = StringField('RFDE_RPT_DT')
   RFDE_TXN_ID = StringField('RFDE_TXN_ID')
   FII = StringField('FII')
   SUB_ACC = StringField('SUB_ACC')
   BRKER = StringField('BRKER')
   SCRIP_NAME = StringField('SCRIP_NAME')
   ISIN = StringField('ISIN')
   TR_DATE = IntegerField('Age')
   TR_TYPE = StringField('TR_TYPE')
   RFDE_SE_REG_NUM = IntegerField('RFDE_SE_REG_NUM')
   RFDE_STLD_CODE= StringField('RFDE_STLD_CODE')
   RATE = DecimalField('RATE')
   QUANTITY = DecimalField('QUANTITY')
   VALUE = DecimalField('VALUE')
   RFDE_INSTR_TYPE = StringField('RFDE_INSTR_TYPE')
   RFDE_REASON_DLAY = StringField('RFDE_REASON_DLAY')
   RFDE_RPT_TYPE = StringField('RFDE_RPT_TYPE')
   RFDE_AMDMNT_REASON = StringField('RFDE_AMDMNT_REASON')
   submit = SubmitField('Predict')
   abc = "" # this variable is used to send information back to the front page
