import calendar
from django.shortcuts import *
from django.contrib.auth import *
from django.contrib.auth.models import *
from .forms import *
from .models import *
import datetime
import dateutil.parser
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from .utils import render_to_pdf
from django.db.models import Q
import smtplib

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']



def result(request):

    profiles = Identity_Information.objects.filter(user=request.user)
    identity_results = Identity_Information.objects.all()
    service_results = Services.objects.all()
    query = request.GET.get("q")
    if query:

        identity_results = identity_results.filter(
            Q(First_Name__icontains=query)|
            Q(Mid_Name__icontains=query)|
            Q(Last_Name__icontains=query)
        ).distinct()
        service_results = service_results.filter(
            Q(service_title__icontains=query)
        ).distinct()
        return render(request, 'calendarium/result.html', {
            'profiles': profiles,
            'identity_results': identity_results,
            'service_results':service_results,
            'user': request.user
        })
    else:
        return render(request, 'calendarium/home.html', {'profiles': profiles})

def index(request):

        if not request.user.is_authenticated():
            return render(request, 'calendarium/index.html')
        else:
            profiles = Identity_Information.objects.filter(user=request.user)
            return render(request, 'calendarium/home.html', {'profiles': profiles})




def profile(request, identity_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        identity = get_object_or_404(Identity_Information, pk=identity_id) #takes Identity_Information with an id of identity_id
        profiles = Identity_Information.objects.filter(user=request.user) #for base.html and url.py
        user = request.user
        try:
            patient_info = Patient_Information.objects.get(Identity_InformationID=identity_id) # for base.html and url.py
            assessment = Assessment.objects.get(Patient_InfoID=patient_info.id)
            try:
                schedule = Schedule_Information.objects.filter(user = request.user)
                try:
                    patient_history = Patient_History.objects.get(AssessmentID=assessment.id)
                    try:
                        patient_record = Patient_Record.objects.filter(Patient_HistoryID=patient_history.id)
                        try:
                            lab_report = Lab_Report.objects.filter(Patient_HistoryID=patient_history.id)
                            try:
                                operation = Operation.objects.get(AssessmentID=assessment.id)
                                operational_record = Operational_Record.objects.get(OperationID=operation.id)
                                try:
                                    treatment = Treatment.objects.filter( Operational_RecordID=operational_record.id)
                                    try:
                                        nurse_rec = Nurse_Record.objects.filter(Operational_RecordID=operational_record.id)
                                        try:
                                            ops_rec = Ops_Rec.objects.filter(Operational_RecordID=operational_record.id)
                                            return render(request, 'calendarium/profile.html', {
                                                                                    'user':user,
                                                                                    'identity':identity,
                                                                                    'profiles': profiles,
                                                                                    'patient_info': patient_info,
                                                                                    'patient_history':patient_history,
                                                                                    'assessment': assessment,
                                                                                                'schedule': schedule,
                                                                                    'lab_report':lab_report,
                                                                                    'operation': operation,
                                                                                    'patient_record': patient_record,
                                                                                    'operational_record': operational_record,
                                                                                    'treatment': treatment,
                                                                                    'nurse_rec':nurse_rec,
                                                                                    'ops_rec':ops_rec
                                                                                   })
                                        except Exception as H:
                                            return render(request, 'calendarium/profile.html', {'user':user,'identity': identity,
                                                                                                'profiles': profiles,
                                                                                                'patient_info': patient_info,
                                                                                                'patient_history': patient_history,
                                                                                                'assessment': assessment,
                                                                                                'schedule': schedule,
                                                                                                'lab_report': lab_report,
                                                                                                'operation': operation,
                                                                                                'patient_record': patient_record,
                                                                                                'operational_record': operational_record,
                                                                                                'treatment': treatment,
                                                                                                'nurse_rec': nurse_rec,
                                                                                                'ops_rec_error': H
                                                                                                })
                                    except Exception as G:
                                        return render(request, 'calendarium/profile.html', {'user':user,'identity': identity,
                                                                                            'profiles': profiles,
                                                                                            'patient_info': patient_info,
                                                                                            'patient_history': patient_history,
                                                                                            'assessment': assessment,
                                                                                            'schedule': schedule,
                                                                                            'lab_report': lab_report,
                                                                                            'operation': operation,
                                                                                            'patient_record': patient_record,
                                                                                            'operational_record':operational_record,
                                                                                            'treatment': treatment,
                                                                                            'nurse_rec_error': G
                                                                                            })
                                except Exception as F:
                                    return render(request, 'calendarium/profile.html', {'user':user,'identity': identity,
                                                                                        'profiles': profiles,
                                                                                        'patient_info': patient_info,
                                                                                        'patient_history':patient_history,
                                                                                        'assessment': assessment,
                                                                                        'schedule': schedule,
                                                                                        'lab_report':lab_report,
                                                                                        'patient_record': patient_record,
                                                                                        'operation':operation,
                                                                                        'operational_record': operational_record,
                                                                                        'treatment_error': F
                                                                                        })
                            except Exception as E:
                                return render(request, 'calendarium/profile.html', {'user':user,'identity': identity,
                                                                                    'profiles': profiles,
                                                                                    'patient_info': patient_info,
                                                                                    'patient_history':patient_history,
                                                                                    'assessment': assessment,
                                                                                    'schedule': schedule,
                                                                                    'lab_report':lab_report,
                                                                                    'patient_record': patient_record,
                                                                                    'operation_error': E
                                                                                    })
                        except Exception as I:
                            return render(request, 'calendarium/profile.html', {'user': user, 'identity': identity,
                                                                                'profiles': profiles,
                                                                                'patient_info': patient_info,
                                                                                'patient_history': patient_history,
                                                                                'assessment': assessment,
                                                                                'schedule': schedule,
                                                                                'patient_record': patient_record,
                                                                                'lab_rep_error': I
                                                                                })

                    except Exception as D:
                        return render(request, 'calendarium/profile.html', {'user':user,'identity': identity,
                                                                            'profiles': profiles,
                                                                            'patient_info': patient_info,
                                                                            'patient_history':patient_history,
                                                                            'assessment':assessment,
                                                                            'schedule': schedule,
                                                                            'patient_rec_error': D
                                                                            })
                except Exception as C:
                    return render(request, 'calendarium/profile.html', {'user':user,'identity': identity,
                                                        'profiles': profiles,
                                                        'patient_info': patient_info,
                                                        'assessment': assessment,
                                                        'schedule':schedule,
                                                        'patient_hist_error': C})


            except Exception as B:
                return render(request, 'calendarium/profile.html', {'user':user,'identity': identity,
                                                                    'profiles': profiles,
                                                                    'patient_info':patient_info,
                                                                    'assessment': assessment,
                                                                    'patient_hist_error': B})
        except Exception as A:
            return render (request, 'calendarium/profile.html', {'user':user,'identity': identity,
                                                                'profiles': profiles,
                                                                 'patient_info_error':A
                                                                 })





def create_patient_info(request, identity_id):

    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        identity = get_object_or_404(Identity_Information, pk=identity_id) #takes Identity_Information with an id of identity_id
        profiles = Identity_Information.objects.filter(user=request.user) #for base.html and url.py
        patient_form = PatientForm(request.POST or None)
        id_info = Identity_Information.objects.get(id=identity_id)
        if patient_form.is_valid():
            try:
                a = patient_form.save(commit=False)
                a.Identity_InformationID = id_info
                a.save()
                pa_info = Patient_Information.objects.get(Identity_InformationID=id_info)
                for data in profiles:
                    b = Assessment(full_name=str(data.Last_Name+'-'+data.First_Name),Patient_InfoID=pa_info)
                    b.save()
                return redirect('/user='+str(identity_id)+'/')

            except Exception as a:
                return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                                'profiles': profiles,
                                                                'form': patient_form,
                                                                'error': a
                                                                })
        return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                        'profiles': profiles,
                                                        'form': patient_form,
                                                        })


def create_patient_hist(request, identity_id, patient_id, assessment_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        identity = get_object_or_404(Identity_Information, pk=identity_id)  # takes Identity_Information with an id of identity_id
        patient_info = get_object_or_404(Patient_Information, Identity_InformationID=identity.id)
        profiles = Identity_Information.objects.filter(user=request.user)  # for base.html and url.py
        # form for patient history
        ass_id = Assessment.objects.get(Patient_InfoID = patient_id )
        patient_hist_form = PatientHistoryForm(request.POST or None)
        if patient_hist_form.is_valid():
            try:
                a = patient_hist_form.save(commit=False)
                a.AssessmentID = ass_id
                a.save()
                return redirect('/user=' + str(identity_id) + '/')

            except Exception as b:
                return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                                    'profiles': profiles,
                                                                    'patient_info': patient_info,
                                                                    'form': patient_hist_form,
                                                                    'error': b
                                                                    })
        return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                        'profiles': profiles,
                                                        'patient_info':patient_info,
                                                        'form': patient_hist_form,
                                                        })


def create_operation_rec(request, identity_id,patient_id,assessment_id,operation_id, ops_rec_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        identity = get_object_or_404(Identity_Information,pk=identity_id)  # takes Identity_Information with an id of identity_id
        profiles = Identity_Information.objects.filter(user=request.user)  # for base.html and url.py
        ops_rec_form = Ops_RecForm(request.POST or None)
        opr_id = Operational_Record.objects.get(OperationID=operation_id)
        if ops_rec_form.is_valid():
            try:
                c = ops_rec_form.save(commit=False)
                c.Operational_RecordID = opr_id
                c.save()

                return redirect('/user=' + str(identity_id) + '/patient=' + str(patient_id) + '/assessment=' + str(
                    assessment_id) + '/operation=' + str(operation_id) + '/ops_rec=' + str(
                    ops_rec_id) + '/view_operation_rec/')
            except Exception as f:
                return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                                    'profiles': profiles,
                                                                    'form': ops_rec_form,
                                                                    'error': f
                                                                    })
        return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                        'profiles': profiles,
                                                        'form': ops_rec_form,
                                                        })


def create_operation(request, identity_id, patient_id , assessment_id,):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        identity = get_object_or_404(Identity_Information,pk=identity_id)
        patient_info = get_object_or_404(Patient_Information, Identity_InformationID=identity.id)
        patient_history = Patient_History.objects.get(AssessmentID = assessment_id)
        lab_report =Lab_Report.objects.filter(Patient_HistoryID=patient_history.id)
        profiles = Identity_Information.objects.filter(user=request.user)
        operation_form = OperationForm(request.POST or None)
        ass_id = Assessment.objects.get(Patient_InfoID=patient_id)

        if operation_form.is_valid():
            try:
                a = operation_form.save(commit=False)
                a.AssessmentID = ass_id
                a.save()
                op_info = Operation.objects.get(AssessmentID=ass_id)
                b = Operational_Record(OperationID=op_info)
                b.save()
                return redirect('/user=' + str(identity_id) + '/')

            except Exception as d:
                return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                                             'profiles': profiles,
                                                                             'patient_history':patient_history,
                                                                             'patient_info': patient_info,
                                                                             'lab_report': lab_report,
                                                                             'error': d
                                                                                 })
        return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                                     'profiles': profiles,
                                                                     'patient_history':patient_history,
                                                                     'patient_info': patient_info,
                                                                     'lab_report': lab_report,
                                                                     'form': operation_form,
                                                                        })


def create_nurse_rec(request, identity_id,patient_id,assessment_id,operation_id, ops_rec_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        identity = get_object_or_404(Identity_Information,
                                     pk=identity_id)  # takes Identity_Information with an id of identity_id
        profiles = Identity_Information.objects.filter(user=request.user)  # for base.html and url.py
        # form for treatment, nurse record and operation record
        nurse_rec_form = Nurse_RecordForm(request.POST or None)
        opr_id = Operational_Record.objects.get(OperationID=operation_id)
        if nurse_rec_form.is_valid():
            try:
                b = nurse_rec_form.save(commit=False)
                b.Operational_RecordID = opr_id
                b.save()
                return redirect('/user=' + str(identity_id) + '/patient=' + str(patient_id) + '/assessment=' + str(
                    assessment_id) + '/operation=' + str(operation_id) + '/ops_rec=' + str(
                    ops_rec_id) + '/view_nurse_rec/')

            except Exception as f:
                return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                                    'profiles': profiles,
                                                                    'form': nurse_rec_form,
                                                                    'error': f
                                                                    })
        return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                        'profiles': profiles,
                                                        'form': nurse_rec_form,
                                                        })


def create_lab_results(request, identity_id,patient_id,assessment_id,patient_hist_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        identity = get_object_or_404(Identity_Information,pk=identity_id)  # takes Identity_Information with an id of identity_id
        patient_info = get_object_or_404(Patient_Information, Identity_InformationID=identity.id)
        patient_history = get_object_or_404(Patient_History, AssessmentID = assessment_id )
        profiles = Identity_Information.objects.filter(user=request.user)  # for base.html and url.py
        # form for lab report
        lab_report_form = Lab_ReportForm(request.POST or None)
        ph_info = Patient_History.objects.get(AssessmentID=assessment_id)
        if lab_report_form.is_valid():
            try:
                a = lab_report_form.save(commit=False)
                a.Patient_HistoryID = ph_info
                a.save()
                return redirect('/user='+str(identity_id)+'/patient='+str(patient_id)+'/assessment='+str(assessment_id)+'/patient_hist='+str(patient_hist_id)+'/view_lab_results/')

            except Exception as c:
                return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                                                'profiles': profiles,
                                                                                'patient_info':patient_info,
                                                                               'patient_history': patient_history,
                                                                                'form': lab_report_form,
                                                                                'error': c
                                                                                })
        return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                                   'profiles': profiles,
                                                                   'patient_info':patient_info,
                                                                   'patient_history':patient_history,
                                                                   'form': lab_report_form,
                                                                    })


def create_anesthesia_rec(request, identity_id,patient_id,assessment_id,operation_id, ops_rec_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        identity = get_object_or_404(Identity_Information,
                                     pk=identity_id)  # takes Identity_Information with an id of identity_id
        profiles = Identity_Information.objects.filter(user=request.user)  # for base.html and url.py
        # form for treatment, nurse record and operation record
        treatment_form = TreatmentForm(request.POST or None)

        opr_id = Operational_Record.objects.get(OperationID=operation_id)
        if treatment_form.is_valid():
            try:
                a = treatment_form.save(commit=False)
                a.Operational_RecordID = opr_id
                a.save()
                return redirect('/user='+str(identity_id)+'/patient='+str(patient_id)+'/assessment='+str(assessment_id)+'/operation='+str(operation_id)+'/ops_rec='+str(ops_rec_id)+'/view_anesthesia_rec/')

            except Exception as e:
                return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                                    'profiles': profiles,
                                                                    'form': treatment_form,
                                                                    'error': e
                                                                    })
        return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                        'profiles': profiles,
                                                        'form': treatment_form,
                                                        })









def view_patient_hist(request, identity_id, patient_id, assessment_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        try:
            identity = get_object_or_404(Identity_Information, pk=identity_id)
            profiles = Identity_Information.objects.filter(user=request.user)
            patient_info = get_object_or_404(Patient_Information, Identity_InformationID=identity_id)
            assessment = get_object_or_404(Assessment, Patient_InfoID=patient_id)
            patient_hist = get_object_or_404(Patient_History, AssessmentID = assessment_id)
            title = 'Patient History'
            return render(request, 'calendarium/view_details.html', {'identity':identity,
                                                             'profiles': profiles,
                                                                 'patient_info': patient_info,
                                                                 'assessment': assessment,
                                                                 'details': patient_hist,
                                                                 'title':title
                                                                 })
        except:
            return redirect('/user='+str(identity_id)+'/')

def view_operation_rec(request, identity_id,patient_id,assessment_id,operation_id, ops_rec_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        try:
            identity = get_object_or_404(Identity_Information, pk=identity_id)
            profiles = Identity_Information.objects.filter(user=request.user)
            patient_info = get_object_or_404(Patient_Information, Identity_InformationID=identity_id)
            assessment = get_object_or_404(Assessment, Patient_InfoID=patient_id)
            operation = get_object_or_404(Operation, AssessmentID=assessment_id)
            operational_record = get_object_or_404(Operational_Record, OperationID=operation_id)
            ops_rec = Ops_Rec.objects.filter(Operational_RecordID = ops_rec_id)
            title = 'Operations Record'
            return render(request, 'calendarium/view_list.html', {'identity': identity,
                                                                 'profiles': profiles,
                                                              'patient_info': patient_info,
                                                              'assessment': assessment,
                                                              'operation': operation,
                                                              'operational_record': operational_record,
                                                              'details': ops_rec,
                                                                 'title': title})
        except:
            return redirect('/user=' + str(identity_id) + '/')


def view_nurse_rec(request, identity_id,patient_id,assessment_id,operation_id, ops_rec_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        try:
            identity = get_object_or_404(Identity_Information, pk=identity_id)
            profiles = Identity_Information.objects.filter(user=request.user)
            patient_info = get_object_or_404(Patient_Information, Identity_InformationID=identity_id)
            assessment= get_object_or_404(Assessment,Patient_InfoID = patient_id )
            operation = get_object_or_404(Operation, AssessmentID = assessment_id)
            operational_record = get_object_or_404(Operational_Record, OperationID=operation_id)
            nurse_rec = Nurse_Record.objects.filter(Operational_RecordID = ops_rec_id)
            title = 'Nurse Record'
            return render(request, 'calendarium/view_list.html', {'identity': identity,
                                                                 'profiles': profiles,
                                                              'patient_info': patient_info,
                                                              'assessment': assessment,
                                                              'operation': operation,
                                                              'operational_record': operational_record,
                                                                 'details': nurse_rec,
                                                                 'title': title
                                                             })
        except:
            return redirect('/user=' + str(identity_id) + '/')


def view_lab_results(request, identity_id,patient_id,assessment_id,patient_hist_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        try:
            identity = get_object_or_404(Identity_Information, pk=identity_id)
            profiles = Identity_Information.objects.filter(user=request.user)
            patient_info = get_object_or_404(Patient_Information, Identity_InformationID=identity_id)
            assessment= get_object_or_404(Assessment,Patient_InfoID = patient_id )
            patient_hist = get_object_or_404(Patient_History, AssessmentID=assessment_id)
            lab_res = Lab_Report.objects.filter(Patient_HistoryID = patient_hist_id)
            title = 'Lab Results'
            return render(request, 'calendarium/view_list.html', {'identity': identity,
                                                                 'profiles': profiles,
                                                              'patient_info': patient_info,
                                                              'assessment':assessment,
                                                              'patient_history':patient_hist,
                                                                 'details': lab_res,
                                                                 'title': title
                                                                 })
        except:
            return redirect('/user=' + str(identity_id) + '/')


def view_patient_rec(request, identity_id,patient_id,assessment_id,patient_hist_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        try:
            identity = get_object_or_404(Identity_Information, pk=identity_id)
            profiles = Identity_Information.objects.filter(user=request.user)
            patient_info = get_object_or_404(Patient_Information, Identity_InformationID=identity_id)
            assessment= get_object_or_404(Assessment,Patient_InfoID = patient_id )
            patient_hist = get_object_or_404(Patient_History, AssessmentID=assessment_id)
            patient_rec = Patient_Record.objects.filter(Patient_HistoryID = patient_hist_id)
            title = 'Patient Record'
            return render(request, 'calendarium/view_list.html', {'identity': identity,
                                                                 'profiles': profiles,
                                                              'patient_info': patient_info,
                                                              'assessment':assessment,
                                                              'patient_history':patient_hist,
                                                                 'details': patient_rec,
                                                                 'title': title
                                                                 })
        except:
            return redirect('/user=' + str(identity_id) + '/')



def view_anesthesia_rec(request, identity_id,patient_id,assessment_id,operation_id, ops_rec_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        try:
            identity = get_object_or_404(Identity_Information, pk=identity_id)
            profiles = Identity_Information.objects.filter(user=request.user)
            patient_info = get_object_or_404(Patient_Information, Identity_InformationID=identity_id)
            assessment = get_object_or_404(Assessment, Patient_InfoID=patient_id)
            operation = get_object_or_404(Operation, AssessmentID=assessment_id)
            operational_record = get_object_or_404(Operational_Record, OperationID=operation_id)
            anesthesia_rec = Treatment.objects.filter(Operational_RecordID=ops_rec_id)
            title = 'Anesthesia Record'
            return render(request, 'calendarium/view_list.html', {'identity': identity,
                                                                 'profiles': profiles,
                                                              'patient_info': patient_info,
                                                              'assessment': assessment,
                                                              'operation': operation,
                                                              'operational_record': operational_record,
                                                              'details': anesthesia_rec,
                                                                 'title': title
                                                                 })
        except:
            return redirect('/user=' + str(identity_id) + '/')



def edit_profile(request, identity_id):

    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:

        user = request.user
        identity = get_object_or_404(Identity_Information, pk=identity_id)
        instance = get_object_or_404(Identity_Information,  user = request.user)
        profiles = Identity_Information.objects.filter(user=request.user)
        identity_form = IdentityForm(request.POST or None, instance= instance)

        if identity_form.is_valid():
            try:
                post = identity_form.save(commit=False)
                post.user = request.user
                try:
                    post.profile_picture = request.FILES['profile_picture']
                except:
                    pass
                try:
                    dob =  dateutil.parser.parse(request.POST['DateOfBirth'])
                    tod = datetime.date.today()
                    my_age = (tod.year - dob.year) - int((tod.month, tod.day) < (dob.month, dob.day))

                    post.Age = my_age
                except:
                    pass

                post.save()

                return redirect('/user=' + str(identity_id) + '/')
            except Exception as e:
                return render(request, 'calendarium/create_form.html', {'user': user,
                                                            'identity': identity,
                                                            'profiles': profiles,
                                                                        'form': identity_form,
                                                                        'error': e})

        return render(request, 'calendarium/create_form.html', {'user': user,
                                                            'identity': identity,
                                                            'profiles': profiles,
                                                                'form':identity_form})


def edit_patient_info(request, identity_id):

    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:

        identity = get_object_or_404(Identity_Information,pk=identity_id)  # takes Identity_Information with an id of identity_id
        profiles = Identity_Information.objects.filter(user=request.user)
        instance = get_object_or_404(Patient_Information, Identity_InformationID = identity_id)
        patient_form = PatientForm(request.POST or None, instance=instance)
        id_info = Identity_Information.objects.get(id=identity_id)
        if patient_form.is_valid():
            try:
                a = patient_form.save(commit=False)
                a.Identity_InformationID = id_info
                a.save()

                return redirect('/user=' + str(identity_id) + '/')

            except Exception as a:
                return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                                        'profiles': profiles,
                                                                        'form': patient_form,
                                                                        'error': a
                                                                        })
        return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                                'profiles': profiles,
                                                                'form': patient_form,
                                                                })


def edit_patient_hist(request, identity_id, patient_id, assessment_id, patient_hist_id ):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:

        instance = get_object_or_404(Patient_History, id = patient_hist_id)
        identity = get_object_or_404(Identity_Information, pk=identity_id)  # takes Identity_Information with an id of identity_id
        patient_info = get_object_or_404(Patient_Information, Identity_InformationID=identity.id)
        profiles = Identity_Information.objects.filter(user=request.user)  # for base.html and url.py
        # form for patient history
        ass_id = Assessment.objects.get(Patient_InfoID = patient_id )
        patient_hist_form = PatientHistoryForm(request.POST or None, instance=instance)
        if patient_hist_form.is_valid():
            try:
                a = patient_hist_form.save(commit=False)
                a.AssessmentID = ass_id
                a.save()
                return redirect('/user='+str(identity_id)+'/patient='+str(patient_id)+'/assessment='+str(assessment_id)+'/view_patient_hist/')

            except Exception as b:
                return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                                    'profiles': profiles,
                                                                    'patient_info': patient_info,
                                                                    'form': patient_hist_form,
                                                                    'error': b
                                                                    })
        return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                        'profiles': profiles,
                                                        'patient_info':patient_info,
                                                        'form': patient_hist_form,
                                                        })


def edit_anesthesia_rec(request, identity_id,patient_id,assessment_id,operation_id, ops_rec_id, anesthesia_rec_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        instance = get_object_or_404(Treatment, id=anesthesia_rec_id)
        identity = get_object_or_404(Identity_Information, pk=identity_id)  # takes Identity_Information with an id of identity_id
        profiles = Identity_Information.objects.filter(user=request.user)  # for base.html and url.py
        # form for treatment, nurse record and operation record
        treatment_form = TreatmentForm(request.POST or None, instance= instance)

        opr_id = Operational_Record.objects.get(OperationID=operation_id)
        if treatment_form.is_valid():
            try:
                a = treatment_form.save(commit=False)
                a.Operational_RecordID = opr_id
                a.save()
                return redirect('/user='+str(identity_id)+'/patient='+str(patient_id)+'/assessment='+str(assessment_id)+'/operation='+str(operation_id)+'/ops_rec='+str(ops_rec_id)+'/view_anesthesia_rec/')

            except Exception as e:
                return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                                    'profiles': profiles,
                                                                    'form': treatment_form,
                                                                    'error': e
                                                                    })
        return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                        'profiles': profiles,
                                                        'form': treatment_form,
                                                        })


def edit_lab_results(request, identity_id,patient_id,assessment_id,patient_hist_id, lab_rep_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        instance = get_object_or_404(Lab_Report, id=lab_rep_id)
        identity = get_object_or_404(Identity_Information,pk=identity_id)  # takes Identity_Information with an id of identity_id
        patient_info = get_object_or_404(Patient_Information, Identity_InformationID=identity.id)
        patient_history = get_object_or_404(Patient_History, AssessmentID = assessment_id )
        profiles = Identity_Information.objects.filter(user=request.user)  # for base.html and url.py
        # form for lab report
        lab_report_form = Lab_ReportForm(request.POST or None, instance= instance)
        ph_info = Patient_History.objects.get(AssessmentID=assessment_id)
        if lab_report_form.is_valid():
            try:
                a = lab_report_form.save(commit=False)
                a.Patient_HistoryID = ph_info
                a.save()
                return redirect('/user='+str(identity_id)+'/patient='+str(patient_id)+'/assessment='+str(assessment_id)+'/patient_hist='+str(patient_hist_id)+'/view_lab_results/')

            except Exception as c:
                return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                                                'profiles': profiles,
                                                                                'patient_info':patient_info,
                                                                               'patient_history': patient_history,
                                                                                'form': lab_report_form,
                                                                                'error': c
                                                                                })
        return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                                   'profiles': profiles,
                                                                   'patient_info':patient_info,
                                                                   'patient_history':patient_history,
                                                                   'form': lab_report_form,
                                                                    })


def edit_nurse_rec(request, identity_id,patient_id,assessment_id,operation_id, ops_rec_id, nurse_rec_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        instance = get_object_or_404(Nurse_Record, id = nurse_rec_id)
        identity = get_object_or_404(Identity_Information,pk=identity_id)  # takes Identity_Information with an id of identity_id
        profiles = Identity_Information.objects.filter(user=request.user)  # for base.html and url.py
        # form for treatment, nurse record and operation record
        nurse_rec_form = Nurse_RecordForm(request.POST or None, instance=instance)
        opr_id = Operational_Record.objects.get(OperationID=operation_id)
        if nurse_rec_form.is_valid():
            try:
                b = nurse_rec_form.save(commit=False)
                b.Operational_RecordID = opr_id
                b.save()
                return redirect('/user=' + str(identity_id) + '/patient=' + str(patient_id) + '/assessment=' + str(
                    assessment_id) + '/operation=' + str(operation_id) + '/ops_rec=' + str(
                    ops_rec_id) + '/view_nurse_rec/')

            except Exception as f:
                return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                                    'profiles': profiles,
                                                                    'form': nurse_rec_form,
                                                                    'error': f
                                                                    })
        return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                        'profiles': profiles,
                                                        'form': nurse_rec_form,
                                                        })
def edit_operation_rec(request, identity_id,patient_id,assessment_id,operation_id, ops_rec_id, op_rec_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        instance = get_object_or_404(Ops_Rec, id = op_rec_id)
        identity = get_object_or_404(Identity_Information,pk=identity_id)  # takes Identity_Information with an id of identity_id
        profiles = Identity_Information.objects.filter(user=request.user)  # for base.html and url.py
        ops_rec_form = Ops_RecForm(request.POST or None, instance=instance)
        opr_id = Operational_Record.objects.get(OperationID=operation_id)
        if ops_rec_form.is_valid():
            try:
                c = ops_rec_form.save(commit=False)
                c.Operational_RecordID = opr_id
                c.save()

                return redirect('/user=' + str(identity_id) + '/patient=' + str(patient_id) + '/assessment=' + str(
                    assessment_id) + '/operation=' + str(operation_id) + '/ops_rec=' + str(
                    ops_rec_id) + '/view_operation_rec/')
            except Exception as f:
                return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                                    'profiles': profiles,
                                                                    'form': ops_rec_form,
                                                                    'error': f
                                                                    })
        return render(request, 'calendarium/create_form.html', {'identity': identity,
                                                        'profiles': profiles,
                                                        'form': ops_rec_form,
                                                        })



def view_anesthesia_rec_details(request, identity_id,patient_id,assessment_id,operation_id, ops_rec_id, anesthesia_rec_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        identity = get_object_or_404(Identity_Information, pk=identity_id)
        profiles = Identity_Information.objects.filter(user=request.user)
        patient_info = get_object_or_404(Patient_Information, Identity_InformationID=identity_id)
        assessment = get_object_or_404(Assessment, Patient_InfoID=patient_id)
        operation = get_object_or_404(Operation, AssessmentID=assessment_id)
        operational_record = get_object_or_404(Operational_Record, OperationID=operation_id)
        anesthesia_rec = Treatment.objects.get(id = anesthesia_rec_id)
        title = 'Anesthesia Record'
        return render(request, 'calendarium/view_details.html', {'identity': identity,
                                                                 'profiles': profiles,
                                                              'patient_info': patient_info,
                                                              'assessment': assessment,
                                                              'operation': operation,
                                                              'operational_record': operational_record,
                                                              'details': anesthesia_rec,
                                                                 'title': title
                                                                 })

def view_oi_rec_details(request, identity_id,patient_id,assessment_id,operation_id, ops_rec_id, anesthesia_rec_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        identity = get_object_or_404(Identity_Information, pk=identity_id)
        profiles = Identity_Information.objects.filter(user=request.user)
        patient_info = get_object_or_404(Patient_Information, Identity_InformationID=identity_id)
        assessment = get_object_or_404(Assessment, Patient_InfoID=patient_id)
        operation = get_object_or_404(Operation, AssessmentID=assessment_id)
        operational_record = get_object_or_404(Operational_Record, OperationID=operation_id)
        anesthesia_rec = Treatment.objects.get(id = anesthesia_rec_id)
        title = 'Other Intake Record'
        return render(request, 'calendarium/view_details.html', {'identity': identity,
                                                                 'profiles': profiles,
                                                              'patient_info': patient_info,
                                                              'assessment': assessment,
                                                              'operation': operation,
                                                              'operational_record': operational_record,
                                                              'details': anesthesia_rec,
                                                                 'title': title
                                                                 })

def view_operation_rec_details(request, identity_id,patient_id,assessment_id,operation_id, ops_rec_id, op_rec_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        identity = get_object_or_404(Identity_Information, pk=identity_id)
        profiles = Identity_Information.objects.filter(user=request.user)
        patient_info = get_object_or_404(Patient_Information, Identity_InformationID=identity_id)
        assessment = get_object_or_404(Assessment, Patient_InfoID=patient_id)
        operation = get_object_or_404(Operation, AssessmentID=assessment_id)
        operational_record = get_object_or_404(Operational_Record, OperationID=operation_id)
        ops_rec = Ops_Rec.objects.get(id = op_rec_id)
        title = 'Operations Record'
        return render(request, 'calendarium/view_details.html', {'identity': identity,
                                                                 'profiles': profiles,
                                                              'patient_info': patient_info,
                                                              'assessment': assessment,
                                                              'operation': operation,
                                                              'operational_record': operational_record,
                                                              'details': ops_rec,
                                                                 'title': title
                                                                 })



def view_nurse_rec_details(request, identity_id,patient_id,assessment_id,operation_id, ops_rec_id, nurse_rec_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        identity = get_object_or_404(Identity_Information, pk=identity_id)
        profiles = Identity_Information.objects.filter(user=request.user)
        patient_info = get_object_or_404(Patient_Information, Identity_InformationID=identity_id)
        assessment= get_object_or_404(Assessment,Patient_InfoID = patient_id )
        operation = get_object_or_404(Operation, AssessmentID = assessment_id)
        operational_record = get_object_or_404(Operational_Record, OperationID=operation_id)
        nurse_rec = Nurse_Record.objects.get(id = nurse_rec_id)
        title = 'Nurse Record'
        return render(request, 'calendarium/view_details.html', {'identity': identity,
                                                                 'profiles': profiles,
                                                              'patient_info': patient_info,
                                                              'assessment': assessment,
                                                              'operation': operation,
                                                              'operational_record': operational_record,
                                                                 'details': nurse_rec,
                                                                 'title': title
                                                                 })


def view_lab_results_details(request, identity_id,patient_id,assessment_id,patient_hist_id, lab_rep_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        identity = get_object_or_404(Identity_Information, pk=identity_id)
        profiles = Identity_Information.objects.filter(user=request.user)
        patient_info = get_object_or_404(Patient_Information, Identity_InformationID=identity_id)
        assessment= get_object_or_404(Assessment,Patient_InfoID = patient_id )
        patient_hist = get_object_or_404(Patient_History, AssessmentID=assessment_id)
        lab_res = Lab_Report.objects.get(id = lab_rep_id)
        title = 'Lab Results'
        return render(request, 'calendarium/view_details.html', {'identity': identity,
                                                                 'profiles': profiles,
                                                              'patient_info': patient_info,
                                                              'assessment':assessment,
                                                              'patient_history':patient_hist,
                                                                 'details': lab_res,
                                                                 'title': title
                                                                 })

def view_patient_rec_details(request, identity_id, patient_id, assessment_id, patient_hist_id, patient_rec_id):
    if not request.user.is_authenticated():
        return render(request, 'calendarium/login.html')
    else:
        identity = get_object_or_404(Identity_Information, pk=identity_id)
        profiles = Identity_Information.objects.filter(user=request.user)
        patient_info = get_object_or_404(Patient_Information, Identity_InformationID=identity_id)
        assessment = get_object_or_404(Assessment, Patient_InfoID=patient_id)
        patient_hist = get_object_or_404(Patient_History, AssessmentID=assessment_id)
        patient_rec = Patient_Record.objects.get(id=patient_rec_id)
        title = 'Patient Record'
        return render(request, 'calendarium/view_details.html', {'identity': identity,
                                                                 'profiles': profiles,
                                                                 'patient_info': patient_info,
                                                                 'assessment': assessment,
                                                                 'patient_history': patient_hist,
                                                                 'details': patient_rec,
                                                                 'title': title
                                                                 })
def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('/admin/')
            elif user.is_superuser:
                login(request, user)
                return redirect('/admin/')
            elif user.is_active:
                login(request, user)
                profiles = Identity_Information.objects.filter(user=request.user)
                return render(request, 'calendarium/home.html',{'profiles':profiles} )
            else:
                return render(request, 'calendarium/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'calendarium/login.html', {'error_message': 'Invalid login'})
    return render(request, 'calendarium/login.html')


def sign_up(request):
    form = UserForm(request.POST or None)
    identity_form = IdentityForm(request.POST or None , request.FILES or None)

    if form.is_valid() and identity_form.is_valid() :
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                post = identity_form.save(commit=False)
                post.user = request.user
                try:
                    dob =  dateutil.parser.parse(request.POST['DateOfBirth'])
                    tod = datetime.date.today()
                    my_age = (tod.year - dob.year) - int((tod.month, tod.day) < (dob.month, dob.day))

                    post.Age = my_age
                except:
                    pass
                post.profile_picture = request.FILES['profile_picture']

                post.save()

        profiles = Identity_Information.objects.filter(user=request.user)
        return render(request, 'calendarium/home.html', {'profiles': profiles})

    return render(request, 'calendarium/msform.html', {"form": form,
                                                       "i_form": identity_form})
def set_appointment(request):
    profiles = Identity_Information.objects.filter(user=request.user)
    form = ScheduleForm(request.POST or None)
    if form.is_valid():
        appointment = form.save(commit=False)
        appointment.user = request.user
        rd = dateutil.parser.parse(request.POST['Requested_Date'])
        schedules = Schedule_Information.objects.filter(Requested_Date=rd.date())
        if schedules:
            message = 'You cannot set an appointment on this date'
            return render(request, 'calendarium/set_appointment.html', {'form': form, 'profiles': profiles, 'error_message':message})
        else:
            appointment.save()
            message = 'You have Successffully Set an appointment'
            return render(request, 'calendarium/set_appointment.html', {'form': form, 'profiles':profiles, 'success_message': message})
    return render(request, 'calendarium/set_appointment.html', {'form': form, 'profiles':profiles})

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    return render(request, 'calendarium/index.html', {"form": form})


def next_month(request, identity_id, year, month):
    new_month = int(month)
    new_year = int(year)
    if new_month == 12:
        new_month = 1
        new_year += 1
    else:
        new_month += 1
    days_in_month = []
    months_in_year = []
    month_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    temp_month_name = []
    month_name = []
    hc = calendar.HTMLCalendar(calendar.SUNDAY)
    for month in month_count:
        for days in hc.itermonthdays(new_year, month):
            if days < 10:
                days_in_month.append('0'+str(days))
            else:
                days_in_month.append(days)
        temp_month_name.append(calendar.month_name[month])
        month_name.append(temp_month_name)
        temp_month_name = []
        months_in_year.append(days_in_month)
        days_in_month = []
    months_in_year = {'currentMonth': months_in_year[new_month - 1],'Month': months_in_year}
    month_name = {'currentMonth': month_name[new_month - 1],'Month': month_name}
    if new_month < 10:
        new_month = '0'+str(new_month)
    else: pass
    new_index = {'month_index':new_month,'year_index': new_year}
    tod = datetime.date.today()
    today = tod.day
    this_month = tod.month
    this_year = tod.year
    # ====== set appointment
    service_type = Service_Type.objects.all()
    services = Services.objects.all()
    schedule_list = Schedule_Information.objects.filter(user=request.user)
    schedules = Schedule_Information.objects.all()
    profiles = Identity_Information.objects.filter(user=request.user)
    form = ScheduleForm(request.POST or None)

    if form.is_valid():
        appointment = form.save(commit=False)
        appointment.user = request.user
        rd = dateutil.parser.parse(request.POST['Requested_Date'])
        rt = dateutil.parser.parse(request.POST['Requested_Time'])
        schedules = Schedule_Information.objects.filter(Requested_Date=rd.date(), Requested_Time=rt.time())

        if schedules:
            message = 'You cannot set an appointment on this date'
            return render(request, 'calendarium/calendar.html', {'form': form,
                                                                 'profiles': profiles,
                                                                 'error_message': message})

        else:
            appointment.save()
            message = 'You have Successffully Set an appointment'
            return redirect('/calendarium/user=' + str(identity_id) + '/')

    return render(request, 'calendarium/calendar.html', {'schedules': schedules,
                                                         'service_type': service_type,
                                                         'schedule_list': schedule_list,
                                                         'user': request.user,
                                                         'months': month_name,
                                                         'dates_per_month': months_in_year,
                                                         'index': new_index,
                                                         'today': today,
                                                         'this_month': this_month,
                                                         'this_year': this_year,
                                                         'services': services,
                                                         'form': form,
                                                         'profiles': profiles})

def prev_month(request,identity_id,year, month):
    new_month = int(month)
    new_year = int(year)
    if new_month == 1:
        new_month = 12
        new_year -= 1
    else:
        new_month -= 1
    days_in_month = []
    months_in_year = []
    month_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    temp_month_name = []
    month_name = []
    hc = calendar.HTMLCalendar(calendar.SUNDAY)
    for month in month_count:
        for days in hc.itermonthdays(new_year, month):
            if days < 10:
                days_in_month.append('0'+str(days))
            else:
                days_in_month.append(days)
        temp_month_name.append(calendar.month_name[month])
        month_name.append(temp_month_name)
        temp_month_name = []
        months_in_year.append(days_in_month)
        days_in_month = []
    months_in_year = {'currentMonth': months_in_year[new_month - 1],'Month': months_in_year}
    month_name = {'currentMonth': month_name[new_month - 1],'Month': month_name}
    if new_month < 10:
        new_month = '0'+str(new_month)
    else: pass
    new_index = {'month_index': new_month,'year_index': new_year}

    tod = datetime.date.today()
    today = tod.day
    this_month = tod.month
    this_year = tod.year
    # ====== set appointment
    service_type = Service_Type.objects.all()
    services = Services.objects.all()
    schedule_list = Schedule_Information.objects.filter(user=request.user)
    schedules = Schedule_Information.objects.all()
    profiles = Identity_Information.objects.filter(user=request.user)
    form = ScheduleForm(request.POST or None)

    if form.is_valid():
        appointment = form.save(commit=False)
        appointment.user = request.user
        rd = dateutil.parser.parse(request.POST['Requested_Date'])
        rt = dateutil.parser.parse(request.POST['Requested_Time'])
        schedules = Schedule_Information.objects.filter(Requested_Date=rd.date(), Requested_Time=rt.time())

        if schedules:
            message = 'You cannot set an appointment on this date'
            return render(request, 'calendarium/calendar.html', {'form': form,
                                                                 'profiles': profiles,
                                                                 'error_message': message})

        else:
            appointment.save()
            message = 'You have Successffully Set an appointment'
            return redirect('/calendarium/user=' + str(identity_id) + '/')

    return render(request, 'calendarium/calendar.html', {'service_type':service_type,
                                                         'schedules': schedules,
                                                         'schedule_list': schedule_list,
                                                         'user': request.user,
                                                         'months': month_name,
                                                         'dates_per_month': months_in_year,
                                                         'index': new_index,
                                                         'today': today,
                                                         'this_month': this_month,
                                                         'this_year': this_year,
                                                         'services': services,
                                                         'form': form,
                                                         'profiles': profiles})



def welcome_calendar(request, identity_id):
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    days_in_month = []
    months_in_year = []
    month_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    temp_month_name = []
    month_name = []
    hc = calendar.HTMLCalendar(calendar.SUNDAY)

    for month in month_count:
        for days in hc.itermonthdays(current_year, month):
            if days < 10:
                days_in_month.append('0'+str(days))
            else:
                days_in_month.append(days)

        temp_month_name.append(calendar.month_name[month])
        month_name.append(temp_month_name)
        temp_month_name = []
        months_in_year.append(days_in_month)
        days_in_month = []

    months_in_year = {'currentMonth': months_in_year[current_month - 1],'Month': months_in_year}
    month_name = {'currentMonth': month_name[current_month - 1],'Month': month_name}
    if current_month < 10:
        current_month = '0'+str(current_month)
    else: pass
    index = {'month_index': current_month,'year_index': current_year}
    tod = datetime.date.today()
    today = tod.day
    this_month = tod.month
    this_year = tod.year

    #====== set appointment
    service_type = Service_Type.objects.all()
    services = Services.objects.all()
    schedule_list = Schedule_Information.objects.filter(user = request.user)
    schedules = Schedule_Information.objects.all()
    profiles = Identity_Information.objects.filter(user=request.user)
    form = ScheduleForm(request.POST or None)

    if form.is_valid():
        appointment = form.save(commit=False)
        appointment.user = request.user
        rd = dateutil.parser.parse(request.POST['Requested_Date'])
        rt = dateutil.parser.parse(request.POST['Requested_Time'])
        schedules = Schedule_Information.objects.filter(Requested_Date=rd.date(),Requested_Time=rt.time())

        if schedules:
            message = 'You cannot set an appointment on this date'
            return render(request, 'calendarium/calendar.html',{'form': form,
                                                                'profiles': profiles,
                                                                'error_message': message})

        else:
            appointment.save()
            message = 'You have Successffully Set an appointment'
            return redirect('/calendarium/user='+str(identity_id)+'/')

    return render(request, 'calendarium/calendar.html', {'service_type':service_type,
                                                         'schedules':schedules,
                                                         'schedule_list':schedule_list,
                                                         'user':request.user,
                                                         'months': month_name,
                                                         'dates_per_month': months_in_year,
                                                         'index': index,
                                                         'today':today,
                                                         'this_month': this_month,
                                                         'this_year': this_year,
                                                         'services':services,
                                                         'form': form,
                                                         'profiles': profiles})


def generate_patient_rec(request ,identity_id, *args, **kwargs):
    patient_info = Patient_Information.objects.get(Identity_InformationID=identity_id)  # for base.html and url.py
    assessment = Assessment.objects.get(Patient_InfoID=patient_info.id)
    patient_history = Patient_History.objects.get(AssessmentID=assessment.id)
    patient_record = Patient_Record.objects.filter(Patient_HistoryID=patient_history.id)
    profiles = Identity_Information.objects.filter(pk = identity_id)
    template = get_template('calendarium/patient_record_pdf.html')
    context = {'profiles':profiles,'patient_record':patient_record,'patient_history':patient_history}
    html = template.render(context)
    pdf = render_to_pdf('calendarium/patient_record_pdf.html',context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Record_%s.pdf" %(identity_id)
        content = "inline; filename='%s'" %(filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")

















