from hads.urls import Path
from .views import index

urlpatterns = [
  Path("index", index, name="home")
]
