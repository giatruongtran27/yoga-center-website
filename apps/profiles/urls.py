from django.urls import include, path

from apps.profiles.views import bills_view, profile_view, profile_trainee_view, profile_trainer_view, profile_certificate_view
from apps.roll_calls.views import GetRollCallListApiView


app_name = 'profile'

urlpatterns = [
    path('', profile_view.ProfileView.as_view(), name='index'),
    path('bills/', bills_view.BillListView.as_view(), name='accounts-bills'),
    path('trainee/update-health-condition',
         profile_view.update_health_condition, name='update-health-condition'),
    path('cards/', profile_trainee_view.TraineeCardsView.as_view(),
         name='profile-trainee-cards'),
    path('cards/<int:pk>/', profile_trainee_view.TraineeCardDetailView.as_view(),
         name='profile-trainee-cards-detail'),

    # get Roll Call List for CARD, render to FullCalendar
    path('cards/<int:pk>/roll-call-list', GetRollCallListApiView.as_view(),
         name='profile-trainee-cards-roll-call-list'),

    # REFUND REQUEST
    path('accounts/cards/<int:pk>/refunds/new/', profile_trainee_view.RefundNewView.as_view(),
         name='profile-trainee-card-refunds-new'),
    path('accounts/cards/<int:card_id>/refunds/<int:pk>/', profile_trainee_view.RefundDetailView.as_view(),
         name='profile-trainee-card-refunds-detail'),
    path('accounts/cards/<int:card_id>/refunds/<int:pk>/delete', profile_trainee_view.detele_refund_request,
         name='profile-trainee-card-refunds-delete'),
    # ----- TRAINER ----- #
    path('trainers/info/',
         profile_trainer_view.TrainerInfoView.as_view(), name='trainers-info'),
    path('trainers/info/edit/',
         profile_trainer_view.TrainerInfoEditView.as_view(), name='trainers-info-edit'),
    path('trainers/yoga-classes/',
         profile_trainer_view.TrainerYogaClassView.as_view(), name='trainers-yoga-classes'),
    path('trainers/yoga-classes/<slug:slug>/',
         profile_trainer_view.TrainerYogaClassDetailView.as_view(), name='trainers-yoga-classes-detail'),
    # ----- CERTIFICATE -----
    path('certificates/',
         profile_certificate_view.ProfileCerfiticateView.as_view(), name='certificates'),
    path('certificates/new/',
         profile_certificate_view.ProfileCertificateNewView.as_view(), name='certificates-new'),
    path('certificates/<int:pk>/',
         profile_certificate_view.ProfileCertificateDetailView.as_view(), name='certificates-detail'),
    path('certificates/<int:pk>/edit/',
         profile_certificate_view.ProfileCertificateEditView.as_view(), name='certificates-edit'),
    path('certificates/<int:pk>/delete/',
         profile_certificate_view.CertificateDeleteView.as_view(), name='certificates-delete'),
]
