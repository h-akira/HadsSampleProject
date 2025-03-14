from hads.shourtcuts import render
from hads.shourtcuts import login_required

@login_required
def index(master):
  return render(master, 'example/index.html', context)
