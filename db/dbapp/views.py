from django.http import JsonResponse
from django.shortcuts import render
from dbapp.models import Medicine
from django.core.paginator import Paginator


def go_to_medicine_page(request):
    return render(request, "index.html")


def show_medicine_page(request):
    search_query = request.GET.get("search", "")
    if search_query:
        medicine_data = Medicine.objects.filter(brand_name__icontains=search_query)
    else:
        medicine_data = Medicine.objects.all()

    paginator = Paginator(medicine_data, 20)
    page_number = request.GET.get("page")
    medicines = paginator.get_page(page_number)

    return render(
        request,
        "data.html",
        {
            "medicines": medicines,
            "search_query": search_query,
        },
    )


