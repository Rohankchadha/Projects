from django.shortcuts import render, HttpResponse
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.platypus import PageBreak

# Create your views here.
def main(request):
    return render(request,'pdfdownload/main.html')


def download_data(request,a,b):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.setFontSize(28)
    p.drawString(70, 750, 'Online Lab Report')
    p.setFontSize(19)
    p.drawString(400, 750, 'Estimate')
    p.drawString(20, 730, '----------------------------------------------------------------------------------------')
    p.drawString(20, 540, '----------------------------------------------------------------------------------------')
    p.setFontSize(16)
    p.drawString(90, 650, 'Issued to')
    p.drawString(440, 650, 'Issued by')
    p.setFontSize(12)
    p.drawString(100, 630, b[0])
    p.drawString(450, 630, b[1])
    p.drawString(50, 480, 'Sr. No')
    p.drawString(130, 480, 'Name')
    p.drawString(190, 480, 'Parameter')
    p.drawString(290, 480, 'Min. Value')
    p.drawString(400, 480, 'Max. Value')
    p.drawString(500, 480, 'Score')
    b=0
    c=450
    for i in range(0,len(a)):
        # if (c-b)>70:
            p.drawString(50, c-b,str(i+1))
            p.drawString(130, c-b,str(a[i][0]))
            p.drawString(190, c-b,str(a[i][1]))
            p.drawString(290, c-b,str(a[i][2]))
            p.drawString(400, c-b,str(a[i][3]))
            p.drawString(500, c-b,str(a[i][4]))
            b+=30
        # else:
        #     c=700
        #     b=0
        #     PageBreak()

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")

def get_data(request):
    a=[['Harry','blood','12gm','19gm',78],['Harry','blood','12gm','19gm',78],['Harry','blood','12gm','19gm',78],['Harry','blood','12gm','19gm',78],['Harry','blood','12gm','19gm',78],['Harry','blood','12gm','19gm',78],['Harry','blood','12gm','19gm',78],['Harry','blood','12gm','19gm',78],['Harry','blood','12gm','19gm',78],['Harry','blood','12gm','19gm',78],['Harry','blood','12gm','19gm',78],['Harry','blood','12gm','19gm',78],['Harry','blood','12gm','19gm',78],['Harry','blood','12gm','19gm',78]]
    b=['Mr. Harry Olsen','Dr. Klassen']
    return download_data(request,a,b)