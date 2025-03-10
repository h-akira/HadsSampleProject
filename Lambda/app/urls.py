from hads.urls import Path
from .views import example

urlpatterns = [
  Path("example", example, name="example")
]
