import os
import secrets
from projectlibrary import app


def save_pdf(form_pdf):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_pdf.filename)
    pdf_fn = random_hex + f_ext
    pdf_path = os.path.join(app.root_path, 'static/pdfs', pdf_fn)
    form_pdf.save(pdf_path)
    
    return pdf_fn
    
    
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/project-images', picture_fn)
    form_picture.save(picture_path)
    
    return picture_fn