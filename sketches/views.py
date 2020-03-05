from django.shortcuts import render


def main_page(request):
    return render(request, 'mainpage_template.html')

def sketch_display(request,sketches):
    sketches = str(sketches) + ".png"
    return render(request, 'show_sketch.html',{'sketch_image':sketches})