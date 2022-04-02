from django.db.models import Q
from .models import Profile, Skill

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateProfiles(request, profiles, results):
    page = request.GET.get('page')
    alums = profiles.filter(profile_type='alum')
    paginator = Paginator(alums, results)

    try:
        alums = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        alums = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        alums = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, alums


def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains = search_query)

    profiles = Profile.objects.distinct().filter(
        (Q(name__icontains = search_query) |
        Q(short_intro__icontains = search_query) |
        Q(skill__in = skills)) 
        & Q(profile_type='alum')
    )

    return profiles, search_query

def paginateAffiliates(request, profiles, results):
    page = request.GET.get('page')
    affiliates = profiles.filter(profile_type='affiliate')
    paginator = Paginator(affiliates, results)
    try:
        affiliates = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        affiliates = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        affiliates = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, affiliates

def searchAffiliates(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    affiliates = Profile.objects.distinct().filter(
        (Q(name__icontains=search_query) | Q(short_intro__icontains=search_query)) 
        & Q(profile_type='affiliate'))

    return affiliates, search_query
