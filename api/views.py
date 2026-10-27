import os

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def index(request):
    """Lists the available endpoints."""
    return Response(
        {
            "project": "CSC325 Module 8 - First CI/CD Pipeline",
            "endpoints": ["/api/hello/", "/api/health/"],
        }
    )


@api_view(["GET"])
def hello(request):
    """Simple greeting endpoint."""
    return Response({"message": "Hello from CSC325!"})


@api_view(["GET"])
def health(request):
    """Health check. Also reports which commit is deployed (Render sets RENDER_GIT_COMMIT)."""
    return Response(
        {
            "status": "ok",
            "commit": os.environ.get("RENDER_GIT_COMMIT", "local"),
        }
    )
