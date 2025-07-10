from django.shortcuts import render

# Create your views here.

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, get_object_or_404
from .models import Case

from django.shortcuts import render
from .models import Case


def index(request):
    return render(request, 'emergency/index.html')

def pending_cases_page(request):
    return render(request, 'emergency/pending_cases.html')

def resolved_cases_page(request):
    return render(request, 'emergency/resolved_cases.html')

def analysis_page(request):
    return render(request, 'emergency/analysis.html')


def home(request):
    pending_cases = Case.objects.filter(status='Reported')
    resolved_cases = Case.objects.filter(status='Resolved')

    # Debugging: Print all case data in the terminal/logs
    print("\n----- Pending Cases -----")
    for case in pending_cases:
        print(f"ID: {case.id}, Title: {case.title}, Description: {case.description}, "
              f"Status: {case.status}, Lat: {case.latitude}, Lng: {case.longitude}, "
              f"Picture: {case.picture.url if case.picture else 'No Image'}")

    print("\n----- Resolved Cases -----")
    for case in resolved_cases:
        print(f"ID: {case.id}, Title: {case.title}, Description: {case.description}, "
              f"Status: {case.status}, Lat: {case.latitude}, Lng: {case.longitude}, "
              f"Picture: {case.picture.url if case.picture else 'No Image'}")

    return render(request, 'emergency/pending_cases.html', {
        'pending_cases': pending_cases,
        'resolved_cases': resolved_cases
    })

    

from django.shortcuts import render
from .models import Case

def case_list(request):
    pending_cases = Case.objects.filter(status='Reported')
    resolved_cases = Case.objects.filter(status='Resolved')

    return render(request, 'cases/case_list.html', {
        'pending_cases': pending_cases,
        'resolved_cases': resolved_cases,
    })


from django.shortcuts import render, get_object_or_404
from .models import Case

def case_detail(request, pk):
    case = get_object_or_404(Case, pk=pk)
    return render(request, 'cases/case_detail.html', {'case': case})

def pending_cases_page(request):
    pending_cases = Case.objects.filter(status='Reported')
    return render(request, 'emergency/pending_cases.html', {'pending_cases': pending_cases})

def resolved_cases_page(request):
    resolved_cases = Case.objects.filter(status='Resolved')
    return render(request, 'emergency/resolved_cases.html', {'resolved_cases': resolved_cases})

from django.shortcuts import render
from .models import Case
from django.db.models import Count, Avg, F
from datetime import datetime

from django.shortcuts import render
from .models import Case
from django.db.models import Count
from django.utils.timezone import now
from datetime import timedelta

def analysis_view(request):
    cases = Case.objects.all()

    # Case Distribution by Type
    case_types = cases.values('title').annotate(count=Count('title'))
    case_labels = [case['title'] for case in case_types]
    case_counts = [case['count'] for case in case_types]

    # Case Trends Over Time (Last 6 Months)
    # months = [(now() - timedelta(days=30 * i)).strftime('%b') for i in range(6)][::-1]
    # case_trend = [
    #     cases.filter(reported_at__month=(now() - timedelta(days=30 * i)).month).count()
    #     for i in range(6)
    # ]
    
    # Get unique case titles
    case_titles = list(cases.values_list('title', flat=True).distinct())

    # Months (last 6)
    months = [(now() - timedelta(days=30 * i)).strftime('%b') for i in range(6)][::-1]
    month_numbers = [(now() - timedelta(days=30 * i)).month for i in range(6)][::-1]

    # Trend per case type per month
    case_trend = []
    for title in case_titles:
        trend = [
            cases.filter(title=title, reported_at__month=month).count()
            for month in month_numbers
        ]
        case_trend.append({
            'label': title,
            'data': trend
        })


    # Case Resolution Rate
   # Resolution Rate per Type
    resolution_rate = []
    for label in case_labels:
        total = cases.filter(title=label).count()
        resolved = cases.filter(title=label, status='Resolved').count()
        rate = (resolved / total * 100) if total else 0
        resolution_rate.append(rate)

    # Average Resolution Time
    # Average Resolution Time per Case Type
    avg_resolution_time = []
    for label in case_labels:
        resolved_cases = cases.filter(title=label, status="Resolved")
        times = [
            (case.resolved_at - case.reported_at).days
            for case in resolved_cases
            if case.resolved_at and case.reported_at
        ]
        avg = sum(times) / len(times) if times else 0
        avg_resolution_time.append(avg)

    
    # print(avg_resolution_time)
    # Geographic Distribution (Latitude & Longitude)
    geo_cases = list(cases.values('latitude', 'longitude', 'title', 'status'))
    # print(geo_cases)

    context = {
        'case_labels': case_titles,
        'months': months,
        'case_trend': case_trend,
        
        'case_labels': case_labels,
        'case_counts': case_counts,
        # 'months': months,
        # 'case_trend': case_trend,
        'resolution_rate': resolution_rate,
        'avg_resolution_time': avg_resolution_time,
        'geo_cases': geo_cases,
    }
    
    print(context)

    return render(request, 'emergency/analysis.html', context)



from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
