import pdfkit

def generate_pdf_from_html(html):
    
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    
    
    pdf = pdfkit.from_string(html, False, configuration=config)
    return pdf
