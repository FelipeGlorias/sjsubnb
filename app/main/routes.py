from flask import Blueprint, render_template, redirect, url_for
from app.forms import ListingForm
from app.models import db, Listing

main_bp = Blueprint('main', __name__, template_folder='templates/main')

@main_bp.route('/')
def index():
    listings = Listing.query.all()
    return render_template('index.html', listings=listings)

@main_bp.route('/create', methods=['GET', 'POST'])
def create_listing():
    form = ListingForm()
    if form.validate_on_submit():
        listing = Listing(title=form.title.data, description=form.description.data, price=form.price.data)
        db.session.add(listing)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('create_listing.html', form=form)
