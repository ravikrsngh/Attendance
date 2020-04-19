from django.shortcuts import render,get_object_or_404
from .forms import *
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.urls import reverse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import cv2
from .video import *
from .facerecogvideo import *
from .fdmtcnnfxn import *
import xlwt
from xlwt import Workbook
from django.contrib.sites.shortcuts import get_current_site
from django.forms import formset_factory
from os import listdir
from django.template.loader import render_to_string
import xlrd


def messagesent(email,name,a):
	mail_subject='DETAILS'
	if a == 0:
		body="Hi , "\
			+name\
			+"\n\n"\
			+"We received your details \n Checking under process \n\n Thank you, \n\n The 4R's"
	if a == 1:
		body="Hi , "\
			+name\
			+"\n\n"\
			+"Your details have been submitted successfully \n\n Thank you, \n\n The 4R's"

	message = str(MIMEText(body,'plain'))
	from_email='semaphore794@gmail.com'
	to_list=[email]
	print(to_list)
	s= smtplib.SMTP('smtp.gmail.com',587)
	s.starttls()
	s.login('semaphore794@gmail.com','gzygpdajxwjgeqkb')
	s.sendmail(from_email,to_list,message)
	s.quit()
	print("Email Sent")


def email_otp(email,name):
	mail_subject = 'ATTENDANCE STATUS'

	body="Hi ,"\
		+name\
		+"\n\n"\
		+"You have been marked present \n\n Thank You, \n\n The 4R's"
	message = str(MIMEText(body,'plain'))
	from_email='semaphore794@gmail.com'
	to_list=[email]
	print(to_list)
	s= smtplib.SMTP('smtp.gmail.com',587)
	s.starttls()
	s.login('semaphore794@gmail.com','gzygpdajxwjgeqkb')
	s.sendmail(from_email,to_list,message)
	s.quit()
	print("Email Sent")

def home(request):
	return render(request,'home.html',{})

def r_teacher(request):
	if request.method == 'POST':
		user_form=userform(data=request.POST)
		teacher_form=teacherform(data=request.POST)
		if user_form.is_valid() and teacher_form.is_valid():
			print("                  Form is valid\n \n \n \n")
			user=user_form.save(commit=False)
			user.set_password(user.password)
			profile=teacher_form.save(commit=False)
			user.save()
			profile.user=user
			profile.save()
			return HttpResponseRedirect(reverse('app:home'))
		else:
			print(user_form.errors,profile_form.errors)
	else:
		user_form=userform()
		teacher_form=teacherform()
		return render(request,'r_teacher.html',{'user_form':user_form ,'teacher_form':teacher_form})

def r_student(request):
	if request.method == 'POST':
			user_form=userform(request.POST, request.FILES)
			student_form=studentform(request.POST, request.FILES)
			if user_form.is_valid() and student_form.is_valid():
				print("                  Form is valid\n \n \n \n")
				user=user_form.save(commit=False)
				profile=student_form.save(commit=False)
				user.save()
				profile.user=user
				profile.save()
				os.mkdir('./app/facenettest/train/'+ user.first_name)
				path=os.getcwd().replace('\\','/')
				path+='/media/'+ str(profile.pic1)
				print(path)
				image=cv2.imread(path)
				print(image)
				imagename='im1.jpg'
				pathimg='./app/facenettest/train/'+user.first_name +'/'
				cv2.imwrite(os.path.join(pathimg,imagename),image)
				os.remove(path)

				path=os.getcwd().replace('\\','/')
				path+='/media/'+ str(profile.pic2)
				print(path)
				image=cv2.imread(path)
				print(image)
				imagename='im2.jpg'
				pathimg='./app/facenettest/train/'+user.first_name +'/'
				cv2.imwrite(os.path.join(pathimg,imagename),image)
				os.remove(path)

				path=os.getcwd().replace('\\','/')
				path+='/media/'+ str(profile.pic3)
				print(path)
				image=cv2.imread(path)
				print(image)
				imagename='im3.jpg'
				pathimg='./app/facenettest/train/'+user.first_name +'/'
				cv2.imwrite(os.path.join(pathimg,imagename),image)
				os.remove(path)

				path=os.getcwd().replace('\\','/')
				path+='/media/'+ str(profile.pic4)
				print(path)
				image=cv2.imread(path)
				print(image)
				imagename='im4.jpg'
				pathimg='./app/facenettest/train/'+user.first_name +'/'
				cv2.imwrite(os.path.join(pathimg,imagename),image)
				os.remove(path)

				path=os.getcwd().replace('\\','/')
				path+='/media/'+ str(profile.pic5)
				print(path)
				image=cv2.imread(path)
				print(image)
				imagename='im5.jpg'
				pathimg='./app/facenettest/train/'+user.first_name +'/'
				cv2.imwrite(os.path.join(pathimg,imagename),image)
				os.remove(path)

				path=os.getcwd().replace('\\','/')
				path+='/media/'+ str(profile.pic6)
				print(path)
				image=cv2.imread(path)
				print(image)
				imagename='im6.jpg'
				pathimg='./app/facenettest/train/'+user.first_name +'/'
				cv2.imwrite(os.path.join(pathimg,imagename),image)
				os.remove(path)

				path=os.getcwd().replace('\\','/')
				path+='/media/'+ str(profile.pic7)
				print(path)
				image=cv2.imread(path)
				print(image)
				imagename='im7.jpg'
				pathimg='./app/facenettest/train/'+user.first_name +'/'
				cv2.imwrite(os.path.join(pathimg,imagename),image)
				os.remove(path)

				path=os.getcwd().replace('\\','/')
				path+='/media/'+ str(profile.pic8)
				print(path)
				image=cv2.imread(path)
				print(image)
				imagename='im8.jpg'
				pathimg='./app/facenettest/train/'+user.first_name +'/'
				cv2.imwrite(os.path.join(pathimg,imagename),image)
				os.remove(path)

				path=os.getcwd().replace('\\','/')
				path+='/media/'+ str(profile.pic9)
				print(path)
				image=cv2.imread(path)
				print(image)
				imagename='im9.jpg'
				pathimg='./app/facenettest/train/'+user.first_name +'/'
				cv2.imwrite(os.path.join(pathimg,imagename),image)
				os.remove(path)

				path=os.getcwd().replace('\\','/')
				path+='/media/'+ str(profile.pic10)
				print(path)
				image=cv2.imread(path)
				print(image)
				imagename='im10.jpg'
				pathimg='./app/facenettest/train/'+user.first_name +'/'
				cv2.imwrite(os.path.join(pathimg,imagename),image)
				os.remove(path)

				path=os.getcwd().replace('\\','/')
				path+='/media/'+ str(profile.pic11)
				print(path)
				image=cv2.imread(path)
				print(image)
				imagename='im11.jpg'
				pathimg='./app/facenettest/train/'+user.first_name +'/'
				cv2.imwrite(os.path.join(pathimg,imagename),image)
				os.remove(path)

				path=os.getcwd().replace('\\','/')
				path+='/media/'+ str(profile.pic12)
				print(path)
				image=cv2.imread(path)
				print(image)
				imagename='im12.jpg'
				pathimg='./app/facenettest/train/'+user.first_name +'/'
				cv2.imwrite(os.path.join(pathimg,imagename),image)
				os.remove(path)

				path=os.getcwd().replace('\\','/')
				path+='/media/'+ str(profile.pic13)
				print(path)
				image=cv2.imread(path)
				print(image)
				imagename='im13.jpg'
				pathimg='./app/facenettest/train/'+user.first_name +'/'
				cv2.imwrite(os.path.join(pathimg,imagename),image)
				os.remove(path)

				path=os.getcwd().replace('\\','/')
				path+='/media/'+ str(profile.pic14)
				print(path)
				image=cv2.imread(path)
				print(image)
				imagename='im14.jpg'
				pathimg='./app/facenettest/train/'+user.first_name +'/'
				cv2.imwrite(os.path.join(pathimg,imagename),image)
				os.remove(path)

				path=os.getcwd().replace('\\','/')
				path+='/media/'+ str(profile.pic15)
				print(path)
				image=cv2.imread(path)
				print(image)
				imagename='im15.jpg'
				pathimg='./app/facenettest/train/'+user.first_name +'/'
				cv2.imwrite(os.path.join(pathimg,imagename),image)
				os.remove(path)

				messagesent(user.email,user.first_name,0)

				pathimg='./app/facenettest/train/'+user.first_name
				wrong_img=faceaccept(pathimg)
				if wrong_img != 0:
					print("PICTURES HAD ERROR")
					current_site=get_current_site(request)
					mail_subject="REINSERT THE REJECTED IMAGES"
					message = render_to_string('reinsert.html', {
		                'user': user,
		                'domain': current_site.domain,
		                'u':user.pk,
						'n':wrong_img,
		            })
					from_email='ravikrsngh.rks@gmail.com'
					to_list=[user.email]
					s= smtplib.SMTP('smtp.gmail.com',587)
					s.starttls()
					s.login('semaphore794@gmail.com','gzygpdajxwjgeqkb')
					s.sendmail(from_email,to_list,message)
					s.quit()
					print("Email Sent")
				else:
					profile.accepted=True
					profile.save()
					messagesent(user.email,user.first_name,1)


				return HttpResponseRedirect(reverse('app:home'))
			else:
				print(user_form.errors,student_form.errors)
				return HttpResponseRedirect(reverse('app:r_student'))
	else:
		user_form=userform()
		student_form=studentform()
		return render(request,'r_student.html',{'user_form':user_form ,'student_form':student_form})


def reinsert(request,u,n):
	user=User.objects.get(pk=u)
	profile=student.objects.get(user=user)
	if request.method == 'POST' and profile.accepted==False:
		imgformset=formset_factory(form=imgform , extra=n)
		imgforms=imgformset(request.POST , request.FILES)
		if imgforms.is_valid():
			print("\n\n\n\n\n forms are valid \n\n\n")
			for form in imgforms:
				img=form.cleaned_data.get('img')
				print(img)
				item='im'+'.jpg'
				t=list()
				pathimg='./app/facenettest/train/'+user.first_name
				for filename in listdir(pathimg):
					t.append(str(filename))
				for i in range(1,16):
					item="im" + str(i)+".jpg"
					if item in t:
						continue
					print("\n\n\nFILENAMES ARE NOT EQUAL\n\n\n")
					break
				print("\n\n\n\n\n Filename going to be created is "+str(item))
				profile.pic=img
				profile.save()
				path=os.getcwd().replace('\\','/')
				path+='/media/'+ str(profile.pic)
				print(path)
				image=cv2.imread(path)
				#print(image)
				imagename=item
				pathimg='./app/facenettest/train/'+user.first_name +'/'
				cv2.imwrite(os.path.join(pathimg,imagename),image)
				os.remove(path)
			messagesent(user.email,user.first_name,0)
			pathimg='./app/facenettest/train/'+user.first_name
			wrong_img=faceaccept(pathimg)
			print(wrong_img)
			if wrong_img != 0:
				current_site=get_current_site(request)
				mail_subject="REINSERT THE REJECTED IMAGES"
				message = render_to_string('reinsert.html', {
					'user': user,
					'domain': current_site.domain,
					'u':user.pk,
					'n':len(wrong_img),
				})
				from_email='ravikrsngh.rks@gmail.com'
				to_list=[user.email]
				s= smtplib.SMTP('smtp.gmail.com',587)
				s.starttls()
				s.login('semaphore794@gmail.com','gzygpdajxwjgeqkb')
				s.sendmail(from_email,to_list,message)
				s.quit()
				print("Email Sent")
			else:
				profile.accepted=True
				profile.save()
				messagesent(user.email,user.first_name,1)
			return HttpResponseRedirect(reverse('app:home'))
		else:
			return HttpResponse("ERROR IN THE FORM")
	else:
		if profile.accepted:
			return HttpResponse("YOU HAVE SUCCESSFULLY SUBMITTED ALL THE DETAILS")
		imgformset=formset_factory(form=imgform , extra=n)
		imgforms=imgformset()
		return render(request,'reinsertimg.html',{'imgforms':imgforms,'imgformset':imgformset})

# def start(request):
# 	start_record()
# 	present=facerecog('xyz.avi')
# 	u=student.objects.all()
#     for i in u:
#         email_otp(i.user.email,i.user.first_name)
#     return HttpResponse("DONE")

#LOGIN SYSTEM
def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('app:home'))
            else:

                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Some one tried to login but failed")
            return HttpResponse("Invalid details")
    else:
        return render(request,'home.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app:home'))

def start(request):
	#Creating a workbook
	wb = Workbook()
	path=os.getcwd().replace('\\','/') #getting the path till current working directory
	path+='/xyz.mp4'   #adding the name of the video file in the path generated above
	start_record()     #Starting the recording of the camera and it saves also
	print(path)
	present,slot=facerecog(path)  #sending the video(path) to the facerecognition function which returns list of students present and the slot being checked.
	print(present)
	sheet1 = wb.add_sheet(slot)  #preparing a sheet for it
	#HEADING OF THE EXCEL SHEET (rows,column,item)
	sheet1.write(0, 0, 'NAME')
	sheet1.write(0, 1, 'USN')
	sheet1.write(0,2,'STATUS')
	r=2
	u=student.objects.all() #Getting all the user who is not a superuser
	#PREPARING THE REQUIRED EXCEL SHEET
	print(u)
	for i in u:
		print("Writing to the sheet")
		sheet1.write(r, 0,i.user.first_name)
		sheet1.write(r, 1,i.usn)
		if i.user.first_name in present:
			print("He is present")
			email_otp(i.user.email,i.user.first_name)
			sheet1.write(r, 2, 'PRESENT')
		else:
			sheet1.write(r, 2, 'ABSENT')
		r=r+1
	#GETTING DATE AND TIME
	all=datetime.datetime.now()
	date=str(all.day)+'_'+str(all.month)+'_'+str(all.year)
	fn=os.getcwd().replace('\\','/')+'/app/records/'+date
	if slot == "slot7":
		os.makedirs(fn)
	s=slot
	slot+='.xls'
	fn+='/'
	wb.save(fn+slot)
	print("EXCEL SHEET IS CREATED")
	#Removing the video after the use
	os.remove(path)
	return render(request,'att.html',{'u':u , 'present':present , 'slot':s,'date':date})




def edit_manual(request,slot,date):
	userprofile=set()
	fn=os.getcwd().replace('\\','/')+'/app/records/'+date+'/'+slot+'.xls'
	wb=xlrd.open_workbook(fn)
	print("Workbook opened")
	sheet = wb.sheet_by_index(0)
	f=list()
	c=student.objects.all().count()
	for i in range(2,c+2):
		s_list=list()
		s_list.append(sheet.cell_value(i,0))
		s_list.append(sheet.cell_value(i,1))
		s_list.append(sheet.cell_value(i,2))
		f.append(s_list)
	s_list=list()
	if request.method == 'POST':
		f=list()
		usn=request.POST.get('usn')
		print("\n\n\n USN is "+usn)
		userprofile.add(student.objects.get(usn=usn))
		c=student.objects.all().count()
		print("Number of students "+str(c))
		fn=os.getcwd().replace('\\','/')+'/app/records/'+date+'/'+slot+'.xls'
		wb=xlrd.open_workbook(fn)
		print("Workbook opened")
		sheet = wb.sheet_by_index(0)
		print(sheet.cell_value(2,1))
		wb1=Workbook()
		sheet1=wb1.add_sheet('slot')
		sheet1.write(0, 0, 'NAME')
		sheet1.write(0, 1, 'USN')
		sheet1.write(0,2,'STATUS')
		for i in range(2,c+2):
			s_list=list()
			print(i)
			sheet1.write(i, 0,sheet.cell_value(i,0))
			s_list.append(sheet.cell_value(i,0))
			sheet1.write(i, 1,sheet.cell_value(i,1))
			s_list.append(sheet.cell_value(i,1))
			print(sheet.cell_value(i,1))
			if sheet.cell_value(i,1) == usn:
				sheet1.write(i,2,"PRESENT")
				s_list.append("PRESENT")
				print("matcehed")
			else:
				print("not matched")
				sheet1.write(i, 2,sheet.cell_value(i,2))
				s_list.append(sheet.cell_value(i,2))
			f.append(s_list)
		os.remove(fn)
		print("Deleted")
		wb1.save(fn)
		print("NEW FILE CREATED")
		print(f)
	return render(request,'edit.html',{'userprofile':userprofile,'s_list':s_list,'f':f})
