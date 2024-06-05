from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    # Első feladat - A költő
    path('kolto/', lambda request: views.task(request=request, task_name="A költő"), name='kolto'),

    # Második feladat - Formalitás
    path('formalitas/', lambda request: views.task(request=request, task_name="Formalitás"), name='formalitas'),

    # Harmadik feladat - Reliving
    path('reliving/', lambda request: views.task(request=request, task_name="Reliving"), name='reliving'),


    # Első ág - Keresés
    path('kereses/', lambda request: views.branch(request=request, branch_name="Keresés"), name='kereses'),

    # Első feladat - Solar
    path('kereses/solar/', lambda request: views.branch_task(request=request, task_name="Solar", branch_name="Keresés"), name='solar'),

    # Második feladat - A kód
    path('kereses/kod/', lambda request: views.branch_task(request=request, task_name="A kód", branch_name="Keresés"), name='kod'),

    # Harmadik feladat - Ősmagyarok dicsősége
    path('kereses/osmagyarok-dicsosege/', lambda request: views.branch_task(request=request, task_name="Ősmagyarok dicsősége", branch_name="Keresés"), name='osmagyarok-dicsosege'),

    # Negyedik feladat - Iker
    path('kereses/iker/', lambda request: views.task(request=request, task_name="Iker"), name='iker'),


    # Második ág - Logika
    path('logika/', lambda request: views.branch(request=request, branch_name="Logika"), name='logika'),

    # Első feladat - A jászma
    path('logika/jatszma/', lambda request: views.branch_task(request=request, task_name="A játszma", branch_name="Logika"), name='jatszma'),

    # Második feladat - Iker 2
    path('logika/iker-2/', lambda request: views.branch_task(request=request, task_name="Iker 2", branch_name="Logika"), name='iker-2'),

    # Harmadik feladat - Nézőpont
    path('logika/nezopont/', lambda request: views.branch_task(request=request, task_name="Nézőpont", branch_name="Logika"), name='nezopont'),

    # Negyedik feladat - Szótenger
    path('logika/szotenger/', lambda request: views.task(request=request, task_name="Szótenger"), name='szotenger'),


    # Harmadik ág - Művészet
    path('muveszet/', lambda request: views.branch(request=request, branch_name="Művészet"), name='muveszet'),

    # Első feladat - A piac
    path('muveszet/piac/', lambda request: views.branch_task(request=request, task_name="A piac", branch_name="Művészet"), name='piac'),

    # Második feladat - A festmény
    path('muveszet/festmeny/', lambda request: views.branch_task(request=request, task_name="A festmény", branch_name="Művészet"), name='festmeny'),

    # Harmadik feladat - A darab
    path('muveszet/darab/', lambda request: views.branch_task(request=request, task_name="A darab", branch_name="Művészet"), name='darab'),

    # Negyedik feladat - A ritmus
    path('muveszet/ritmus/', lambda request: views.task(request=request, task_name="A ritmus"), name='ritmus'),


    # Negyedik ág - Irodalom
    path('irodalom/', lambda request: views.branch(request=request, branch_name="Irodalom"), name='irodalom'),

    # Első feladat - A mű
    path('irodalom/mu/', lambda request: views.branch_task(request=request, task_name="A mű",
                                                           branch_name="Irodalom"), name='mu'),

    # Második feladat - A zseni
    path('irodalom/zseni/', lambda request: views.branch_task(request=request, task_name="A zseni",
                                                              branch_name="Irodalom"), name='zseni'),

    # Harmadik feladat - Egy kutya
    path('irodalom/egy-kutya/', lambda request: views.branch_task(request=request, task_name="Egy kutya",
                                                                  branch_name="Irodalom"), name='egy-kutya'),

    # Negyedik feladat - A tragédiák diktátora
    path('irodalom/tragediak-diktatora/',
         lambda request: views.task(request=request, task_name="A tragédiák diktátora"), name='tragediak-diktatora'),


    # Utolsó előtti feladat - Az utolsó játszma
    path('utolso-jatszma/', lambda request: views.task(request=request, task_name="Az utolsó játszma"), name='utolso-jatszma'),

    # Utolsó feladat - A tekercs
    path('tekercs/', lambda request: views.last_task(request=request, task_name="A tekercs"), name='tekercs')
]
