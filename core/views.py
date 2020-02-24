from django.shortcuts import render

from .forms import BinNumberForm


def __bin2dec(number):

    if number == 1 or number == 0:
        return number
    
    l = len(str(number))
    firstDigit = number//pow(10,l-1)
    
    return (pow(2,l-1) * firstDigit)+ __bin2dec(number%pow(10,l-1))


def index(request):
    form = BinNumberForm(request.POST or None)
    dec_number = None
    if request.POST:
        if form.is_valid():
            bin_number = form.cleaned_data.get('bin_number')
            dec_number = __bin2dec(bin_number)
    return render(request, 'index.html', {'dec_number': dec_number, 'form': form})
