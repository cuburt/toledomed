from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView
from .models import *


class edit_patient_hist(UpdateView):
    model = Patient_History
    fields = ['Physician_Exam',
              'Chief_Complaint',
              'History_of_present_illness',
              'Attending_Physician']



class edit_operation_rec(UpdateView):
    model = Ops_Rec
    fields = ['Operation_Room_Rec',
              'OR_Date_of_Operation',
              'Ops_Rec_RoomNo']


class edit_nurse_rec(UpdateView):
    model = Nurse_Record
    fields = ['Nursing_Record',
              'NR_Date']

class edit_lab_results(UpdateView):
    model = Lab_Report
    fields = ['Lab_TypeID',
              'LabReport',
              'Date']


class edit_anesthesia_rec(UpdateView):
    model = Treatment
    fields = ['Anesthesia_Record',
              'AR_Date',
              'Other_Intake',
              'OI_Date']

