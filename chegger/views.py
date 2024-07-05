from django.shortcuts import render
from .forms import QuestionForm
from .services import generate_answer


def generate_answer_view(request):
    answer = None
    question = None
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data["question"]
            answer = generate_answer(question)
    else:
        form = QuestionForm()

    return render(
        request, "index.html", {"form": form, "question": question, "answer": answer}
    )
