from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.shortcuts import render
from .forms import ResumeForm

def render_to_pdf(template_src, context_dict):
    html = render_to_string(template_src, context_dict)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("Error generating PDF", status=500)
    return response


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        education = request.POST.get('education')
        skills = request.POST.get('skills')
        workexperience = request.POST.get('workexperience')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        projects = request.POST.get('projects')
        achievements = request.POST.get('achievements')

        profile_context = {
            'name': name,
            'education': education,
            'skills': skills,
            'workexperience': workexperience,
            'email': email,
            'phone': phone,
            'projects': projects,
            'achievements':achievements,
        }

        if 'generate_pdf' in request.POST:
            return render_to_pdf('resume_pdf.html', profile_context)
        
        return render(request, 'resume.html', profile_context)

    form = ResumeForm()
    context = {"form": form}
    return render(request, "home.html", context=context)
