from django.shortcuts import render, redirect
from django .contrib .auth import login
from django .contrib . auth . forms import UserCreationForm


# Create your views here.
def register(request):
    # registration page
    if request.method != 'POST':
        # No submitted data, blank form
        form = UserCreationForm()
    else:
        # Form submitted, process data
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # log in user and redirect to home page
            login(request, new_user)
            return redirect('learning_logs:index')

    # invalid form/blank
    context = {'form': form}
    return render(request, 'registration/register.xhtml', context)
