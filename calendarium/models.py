from django.contrib.auth.models import Permission, User
from django.db import models
import datetime

# DEFAULT 1 CONTAINS DUMMY OR NULL DATA or NONE


# Personal Information-----------------------------------
class Civil_Status(models.Model):
    Civil_Status = models.CharField(max_length=50)

    def __str__(self):
        return self.Civil_Status


class Sex(models.Model):
    Sex = models.CharField(max_length=50)

    def __str__(self):
        return self.Sex


class Religion(models.Model):
    Religion = models.CharField(max_length=50)

    def __str__(self):
        return self.Religion


class Nationality(models.Model):
    Nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.Nationality


class Identity_Information(models.Model):
    user = models.ForeignKey(User, default=1)
    First_Name = models.CharField(max_length=100)
    Mid_Name = models.CharField(max_length=100, default='')
    Last_Name = models.CharField(max_length=100)
    DateOfBirth = models.DateField()
    Age = models.IntegerField()
    SexID = models.ForeignKey(Sex, on_delete=models.CASCADE)
    Civil_StatusID = models.ForeignKey(Civil_Status, on_delete=models.CASCADE)
    ReligionID = models.ForeignKey(Religion, on_delete=models.CASCADE)
    NationalityID = models.ForeignKey(Nationality, on_delete=models.CASCADE)
    Home_Address = models.CharField(max_length=300)
    Personal_Phone = models.CharField(max_length=50)
    profile_picture = models.FileField()
    Occupation = models.CharField(max_length=100, default='None')
    Office_Address = models.CharField(max_length=300, default='None')
    Employer = models.CharField(max_length=100, default='None')
    Office_Phone = models.CharField(max_length=50, default='None')


    def __str__(self):
        return self.Last_Name + ' - ' + self.First_Name




class Patient_Information(models.Model):
    Identity_InformationID = models.ForeignKey(Identity_Information, on_delete=models.CASCADE)
    Height = models.DecimalField(decimal_places=1, max_digits=2)
    Weight = models.DecimalField(decimal_places=1, max_digits=4)
    NCE = models.CharField(max_length=50, default='None')
    Relationship_to_NCE = models.CharField(max_length=50, default='None')

    def __str__(self):
        return self.Identity_InformationID


#Assessment Records----------------------------------
class Assessment(models.Model):
    full_name = models.CharField(max_length=50)
    Patient_InfoID = models.ForeignKey(Patient_Information, on_delete=models.CASCADE)
    def __str__(self):
        return self.full_name

class Patient_History(models.Model):
    Physician_Exam = models.TextField(max_length=300)
    AssessmentID = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    Chief_Complaint = models.TextField(max_length=300)
    History_of_present_illness = models.TextField(max_length=300)
    Attending_Physician = models.CharField(max_length=180)
    Date = models.DateField()
    def __str__(self):
        return str(self.Date)


class Patient_Record(models.Model):
    Patient_HistoryID = models.ForeignKey(Patient_History, on_delete=models.CASCADE)
    Date = models.DateField()
    Assessment = models.TextField(max_length=180)
    Treatment = models.TextField(max_length=180)
    def __str__(self):
        return str(self.Date)

class Lab_Type(models.Model):
    LabType = models.CharField(max_length=180)
    def __str__(self):
        return self.LabType

class Lab_Report(models.Model):
    Lab_TypeID = models.ForeignKey(Lab_Type, on_delete=models.CASCADE)
    Patient_HistoryID = models.ForeignKey(Patient_History, on_delete=models.CASCADE)
    LabReport = models.TextField(max_length=180)
    Date = models.DateField()
    def __str__(self):
        return str(self.Lab_TypeID)


class Operation(models.Model):
    AssessmentID = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    UO_Date_of_operation = models.DateField(default='')
    Operation_RoomNo = models.IntegerField(default='')
    Duration_of_operation = models.TimeField(default='')
    def __str__(self):
        return str(self.UO_Date_of_operation)+' - '+str(self.Duration_of_operation)

#Operational Records----------------------------------
class Operational_Record(models.Model):
    OperationID = models.ForeignKey(Operation, on_delete=models.CASCADE)

class Treatment(models.Model):
    Operational_RecordID = models.ForeignKey(Operational_Record, on_delete=models.CASCADE)
    Anesthesia_Record = models.CharField(max_length=180)
    AR_Date = models.DateField()
    Other_Intake = models.CharField(max_length=180)
    OI_Date = models.DateField()
    def __str__(self):
        return str(self.AR_Date) +': Anesthesia'+ str(self.OI_Date) +': Other Intake'


class Nurse_Record(models.Model):
    Operational_RecordID = models.ForeignKey(Operational_Record, on_delete=models.CASCADE)
    Nursing_Record = models.TextField(max_length=180)
    NR_Date = models.DateField()
    def __str__(self):
        return str(self.NR_Date)

class Ops_Rec(models.Model):
    Operational_RecordID = models.ForeignKey(Operational_Record, on_delete=models.CASCADE)
    Operation_Room_Rec = models.TextField(max_length=180)
    OR_Date_of_Operation = models.DateField()
    Ops_Rec_RoomNo = models.IntegerField()
    def __str__(self):
        return str(self.OR_Date_of_Operation)+' - '+str(self.Ops_Rec_RoomNo)









#Schedule Setup--------------------------------------------


class Service_Type(models.Model):
    Type = models.CharField(max_length=50)
    image = models.FileField(default="null")

    def __str__(self):
        return self.Type

class Services(models.Model):
    service_type = models.ForeignKey(Service_Type, on_delete=models.CASCADE)
    service_title = models.CharField(max_length=50)
    duration = models.IntegerField()
    image = models.FileField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.service_title



class Schedule_Information(models.Model):
    user = models.ForeignKey(User, default=1)
    Concern = models.TextField(max_length=180)
    Setup_Time = models.TimeField()
    Setup_Date = models.DateField()
    Requested_Date = models.DateField()
    Requested_Time = models.TimeField()
    def __str__(self):
        return str(self.Requested_Date)



class Schedule_List(models.Model):
    Schedules = models.ForeignKey(Schedule_Information, on_delete=models.CASCADE)




		








