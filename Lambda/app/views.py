from hads.shourtcuts import render
from hads.shourtcuts import login_required

@login_required
def example(master):
  return render(master, 'example/example.html', context)
