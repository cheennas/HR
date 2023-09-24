from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from sport_results.urls import urlpatterns as sportresults_urlpatterns
from personal_data.urls import urlpatterns as personaldata_urlpatterns
from owning_languages.urls import urlpatterns as owninglanguages_urlpatterns
from family_composition.urls import urlpatterns as familycomposition_urlpatterns
from class_category.urls import urlpatterns as classcategory_urlpatterns
from education.urls import urlpatterns as education_urlpatterns
from academic_degree.urls import urlpatterns as academicdegree_urlpatterns
from courses.urls import urlpatterns as courses_urlpatterns
from attestation.urls import urlpatterns as attestation_urlpatterns
from autobiography.urls import urlpatterns as autobiography_urlpatterns
from awards.urls import urlpatterns as awards_urlpatterns
from investigation_retrieval.urls import urlpatterns as investigation_urlpatterns
from sick_leaves.urls import urlpatterns as sickleaves_urlpatterns
from spec_check.urls import urlpatterns as speccheck_urlpatterns
from military_rank.urls import urlpatterns as militaryrank_urlpatterns
from photo.urls import urlpatterns as photo_urlpatterns

from general_info.urls import urlpatterns as generalinfo_urlpatterns
from working_history.urls import urlpatterns as workinghistory_urlpatterns
from orders_list.urls import urlpatterns as orderslist_urlpatterns
from staff_info.urls import urlpatterns as staffinfo_urlpatterns
from personal_info.urls import urlpatterns as personalinfo_urlpatterns

from user.urls import urlpatterns as user_urlpatterns

from word_generator.urls import urlpatterns as wordgenerator_urlpatterns
from staff_main.urls import urlpatterns as staffmain_urlpatterns
from group.urls import urlpatterns as group_urlpatterns
from report_filter.urls import urlpatterns as reportlist_urlpatterns

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]

urlpatterns += sportresults_urlpatterns
urlpatterns += personaldata_urlpatterns
urlpatterns += owninglanguages_urlpatterns
urlpatterns += familycomposition_urlpatterns
urlpatterns += education_urlpatterns
urlpatterns += academicdegree_urlpatterns
urlpatterns += courses_urlpatterns
urlpatterns += attestation_urlpatterns
urlpatterns += autobiography_urlpatterns
urlpatterns += awards_urlpatterns
urlpatterns += classcategory_urlpatterns
urlpatterns += investigation_urlpatterns
urlpatterns += sickleaves_urlpatterns
urlpatterns += speccheck_urlpatterns
urlpatterns += militaryrank_urlpatterns
urlpatterns += photo_urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += generalinfo_urlpatterns
urlpatterns += workinghistory_urlpatterns
urlpatterns += orderslist_urlpatterns
urlpatterns += staffinfo_urlpatterns
urlpatterns += personalinfo_urlpatterns

urlpatterns += user_urlpatterns

urlpatterns += wordgenerator_urlpatterns
urlpatterns += staffmain_urlpatterns
urlpatterns += group_urlpatterns
urlpatterns += reportlist_urlpatterns
