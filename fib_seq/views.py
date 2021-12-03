from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .forms import Fib_seqForm

# Create your views here.


@require_http_methods(["POST", "GET"])
def fib_seqView(request):
    fib_seq_result = None
    if request.method == "POST":
        form = Fib_seqForm(request.POST)
        if form.is_valid():
            fib_seq_result = Fibonacci(int(form.cleaned_data["number"]))
    else:
        form = Fib_seqForm()

    return render(
        request, "fib_seq.html", {"form": form, "fib_seq_result": fib_seq_result}
    )


def Fibonacci(n):

    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        return "Incorrect input"

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
