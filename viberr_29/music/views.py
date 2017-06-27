from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# CreateView - whenever we want to make a form to create a new object
# UpdateView - a form for updating the object
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# authenticate - will take the user and pass and check if it exist in the database
# login - just attaches a sessions id so that no mater the page you are on you won't need to log.in every time
from django.views.generic import View
from .forms import UserForm, LoginForm




# https://www.youtube.com/watch?v=c3yB0_4Yd48&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK&index=29

#generic view - instead of using functions we use classes


class IndexView(generic.ListView):      # generic.ListView is a type of generic view that list all objects
    template_name = 'music/index.html'  # this points what template we are going to use
    context_object_name = 'all_albums'  # this is used to create a custom variable for object_list

    def get_queryset(self):             # this will query the db for the info we want
        return Album.objects.all()      # every time we query this it would return a list of all our object and
                                        # store it on a variable named object_list


class DetailView(generic.DetailView):   # Detail view is the detail of one object
    model = Album                       # what model in which we are getting the detail of
    template_name = 'music/detail.html'

# this class creates the form view to create a new album/object

class AlbumCreate(CreateView):
    model = Album                       # what object we want to create
    fields = ['artist', 'album_title', 'genre', 'album_logo']   # what are the fields we want the user to input. this refers to our DB feilds for album
    # we don't need to specify the template name when using model form. just need to follow the name format

class AlbumUpdate(UpdateView):
    model = Album                       # what table are we going to need
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')   # after we delete it where do we want it to go


# https://www.youtube.com/watch?v=aCotgGyS2gc&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK&index=35
class UserFormView(View):
    form_class = UserForm               # what is the blueprint/table we are going to use (forms.py class UserForm)
    template_name = 'music/registration_form.html'

    # whenever we use a class base views we can separate the get an post into built in functions

    # display a blank form
    def get(self, request):             # This is called when the user want this form and it is a get request
        form = self.form_class(None)    # We want to user the UserForm and we don't need anything to pass
                                            # since this is just a blank data that the user will fill in
        return render(request, self.template_name, {'form': form})

    # process the form data
    def post(self, request):            # When they submit a form and it is a post request
        form = self.form_class(request.POST)    # request.POST since we need to pass in what the user put in the form
                                                # when the user hits the submit button the inputs will be stored in (request.POST)
        if form.is_valid():             # this would check if the form they submitted is valid

            user = form.save(commit=False)  # this is just storing the data locally and not yet saving it on the DB

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)     # this is used whenever we want to change a password
            user.save()                     # this save the user and pass on the database

            user = authenticate(username=username, password=password)        # This will check if the username and password exist in our database

            if user is not None:            # if the user exist

                if user.is_active:          # if the user status is active
                    login(request, user)    # this is how you log them in and attach a session
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})      # This gives them a blank form again, if they did not log in properly



class LoginFormView(View):
    form_class = LoginForm
    template_name = 'music/log-in.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


    def post(self, request):

        form = self.form_class(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('music:index')
        else:
            return render(request, self.template_name, {'form': form})

class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('music:log-in')





























