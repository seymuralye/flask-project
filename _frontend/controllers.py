from flask import render_template, request, redirect, url_for, flash
from app import app, db, create_app

from models import Product, Category


app = create_app()


@app.route('/')
def shop():
    categories = Category.query.all()
    context = {
        'categories': categories
}
    return render_template('shop.html', **context)


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        if not name or not email or not subject or not message:
            flash('Please fill out all fields', 'danger')
            return redirect(url_for('contact'))
        new_contact = Contact(name=name, email=email, subject=subject, message=message)
        db.session.add(new_contact)
        db.session.commit()
        flash('Your message has been sent!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')





