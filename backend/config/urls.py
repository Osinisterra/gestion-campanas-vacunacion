from django.urls import path
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthView(APIView):
    def get(self, request) -> Response:
        return Response({"status": "ok"})


urlpatterns = [path("api/v1/health/", HealthView.as_view())]
