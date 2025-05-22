from django.shortcuts import render , redirect

from django.views import View

from . models import Course , CategoryChoices , LevelChoices

from .forms import CourseCreateForm

from instructors.models import Instructors

from django.db.models import Q

from django.contrib.auth.decorators import login_required

# Create your views here.

class CourseListView(View):

    def get(self, request, *args , **kwargs):

        query = request.GET.get('query')
        print(query)

        courses = Course.objects.all()

        if query:

                courses = Course.objects.filter(Q(title__icontains = query)|
                                                Q(description__icontains = query)|
                                                Q(instructor__name__icontains =query)| # since instructor is a forign key we have to specify the name of instructor
                                                Q(category__icontains = query)|
                                                Q(type__icontains = query)|
                                                Q(level__icontains =query)|
                                                Q(fees__icontains = query))

        

        print(courses)

        data = {
             'query' : query,
            'courses': courses,
            'page' : 'courses-page'
        }
        return render(request, 'courses/courses-list.html', context= data)
    
    
    
class HomeListView(View):

    def get(self,request,*args,**kwargs):

        data = {'page' : 'home-page'}

        return render(request,'courses/home.html',context = data)
    
# @login_required(login_url='login')   
    
class InstructorCourseListView(View):

    def get(self, request, *args, **kwargs):

        instructor = Instructors.objects.get(id=1)

        courses = Course.objects.filter(instructor =instructor)
        print(courses)

        data = { 
            'page': 'instructor-courses-page',
            'courses' : courses}        
        
        return render(request, 'courses/instructor-courses-list.html', context=data)
    
# class CourseCreateView(View):

#     def get(self , request , *args , **kwargs):
            
#         data ={
#             'categories': CategoryChoices,
#             'levels': LevelChoices,
#                 }

#         return render (request, 'courses/create-course.html', context=data)
    
#     def post(self, request, *args, **kwargs):

#             form_data = request.POST

#             image = request.FILES.get('image')

#             title = form_data.get('title')
       
#             description = form_data.get('description')

#             category = form_data.get('category')

#             level = form_data.get('level')

#             fees = form_data.get('fees')

#             offer_fee = form_data.get('offer_fee')

#             instructor = 'John Doe'

#             print(title, description,category,level,image,fees,offer_fee)

#             course = Courses.objects.create(title=title,description=description , image=image,
#                                    category=category,level=level, instructor=instructor,
#                                    fees=fees, offer_fee=offer_fee)
#             course.save()

#             return redirect('instructor-courses-list')



# with the help of Django-forms



class CourseCreateView(View):

    def get(self , request , *args , **kwargs):
            
        # data ={
        #     'categories': CategoryChoices,
        #     'levels': LevelChoices,
        #         }

        form = CourseCreateForm()
        
        data = {
            'form': form
        }

        return render (request, 'courses/course-create.html', context=data)
    
    def post(self, request, *args, **kwargs):

        form = CourseCreateForm(request.POST, request.FILES)

        instructor = Instructors.objects.get(id=1)

        if form.is_valid():

            # print(form.cleaned_data)

            # form.cleaned_data['instructor'] = 'John Doe'

            # form.save()

            course = form.save(commit=False)

            course . instructor =instructor


            course.save()
        

            return redirect('instructor-courses-list')
        

        data = {'form': form }

        print(form.errors)

        return render (request, 'courses/course-create.html', context=data)
    
class InstructorCoursesDetailView(View):

    def get(self, request , *args , **kwargs):

        uuid = kwargs.get('uuid')

        course = Course.objects.get(uuid=uuid)

        data = {
            'course' : course
        }

        return render(request,'courses/instructor-course-detail.html', context= data)
    
class InstructorCoursesDeleteView(View) :

    def get(self , request , *args , **kwargs):

        uuid = kwargs.get('uuid')

        course = Course.objects.get(uuid=uuid)

        course.delete()

        return redirect('instructor-courses-list')
    

class InstructorCoursesUpdateView(View):

    def get(self, request , *args, **kwargs):

        uuid = kwargs.get('uuid')

        course = Course.objects.get(uuid=uuid)

        form = CourseCreateForm(instance=course)

        data = {
            'form' : form ,

        }

        return render(request,'courses/instructor-course-update.html', context=data)
    
    def post (self,request,args,*kwargs):

        uuid = kwargs.get('uuid')

        course = Course.objects.get(uuid=uuid)

        form = CourseCreateForm(request.POST,request.FILES,instance=course)

        if form.is_valid():

            form.save()

            return redirect('instructor-courses-list')
        
        data = {'form': form}

        print(form.errors)

        return render(request,'courses/instructor-course-update.html',context = data)
    