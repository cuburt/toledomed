from django.contrib.auth.models import User
from django import forms
from .models import *
import datetime

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ['username','email','password']




class ScheduleForm(forms.ModelForm):

    Setup_Date = forms.DateField(widget=forms.TextInput, initial=datetime.datetime.now().date)
    Setup_Time = forms.CharField(widget=forms.TextInput, initial=datetime.datetime.now().strftime('%I:%M %p'))
    Requested_Date = forms.CharField(widget=forms.TextInput)
    Requested_Time = forms.CharField(widget=forms.TextInput )

    class Meta:
        model = Schedule_Information
        fields = ['Concern',
                  'Setup_Date',
                  'Setup_Time',
                  'Requested_Date',
                  'Requested_Time'
                  ]

class IdentityForm(forms.ModelForm):
    DateOfBirth = forms.DateField(widget=forms.DateInput)
    Mid_Name = forms.CharField(required=False)
    class Meta:
        model = Identity_Information
        fields = ['First_Name',
                  'Mid_Name',
                  'Last_Name',
                  'DateOfBirth',
                  'SexID',
                  'Civil_StatusID',
                  'ReligionID',
                  'NationalityID',
                  'Home_Address',
                  'Personal_Phone',
                  'Occupation',
                  'Office_Address',
                  'Employer',
                  'Office_Phone',
                  'profile_picture'
                  ]


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient_Information
        fields = ['Height',
                  'Weight',
                  'NCE',
                  'Relationship_to_NCE']


class PatientHistoryForm(forms.ModelForm):
    class Meta:
        model = Patient_History
        fields = ['Physician_Exam',
                  'Chief_Complaint',
                  'History_of_present_illness',
                  'Attending_Physician']

class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ['UO_Date_of_operation',
                  'Operation_RoomNo',
                  'Duration_of_operation']

class Lab_ReportForm(forms.ModelForm):
    class Meta:
        model = Lab_Report
        fields = ['Lab_TypeID',
                  'LabReport',
                  'Date']

class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ['Anesthesia_Record',
                  'AR_Date',
                  'Other_Intake',
                  'OI_Date']

class Nurse_RecordForm(forms.ModelForm):
    class Meta:
        model = Nurse_Record
        fields = ['Nursing_Record',
                  'NR_Date']

class Ops_RecForm(forms.ModelForm):
    class Meta:
        model = Ops_Rec
        fields = ['Operation_Room_Rec',
                  'OR_Date_of_Operation',
                  'Ops_Rec_RoomNo']


class ScheduleListForm(forms.ModelForm):

    class Meta:
        model = Schedule_List
        fields = ['Schedules']
        

