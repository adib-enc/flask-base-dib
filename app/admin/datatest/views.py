from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import current_user, login_required
from flask_rq import get_queue

from app import db
from app.admin.datatest.forms import (
    DatatestForm,
)
from app.decorators import admin_required
from app.email import send_email
from app.models import Datatest
import json
datatest = Blueprint('datatest', __name__)


@datatest.route('/')
@login_required
@admin_required
def index():
    """Admin dashboard page."""
    datatest = Datatest.query.all()
    return render_template('master/datatest/index.html',
        datatest=datatest)


@datatest.route('/create', methods=['GET', 'POST'])
@login_required
@admin_required
def create():
    """Create a new data."""
    form = DatatestForm()
    if form.validate_on_submit():
        from datetime import datetime
        dtime = datetime.today()
        datatest = Datatest(
            name=form.name.data,
            d1=form.name.data,
            d2=form.d2.data,
            d3=dtime,
            d4=form.d4.data,
            )
        db.session.add(datatest)
        db.session.commit()
        flash('Datatest {} successfully created'.format(datatest.name), 'form-success')
        return redirect(url_for('datatest.index'))
    return render_template('master/datatest/add-edit.html', form=form)


@datatest.route('/datatest')
@login_required
@admin_required
def all():
    """View all registered datatests."""
    datatest = Datatest.query.all()
    return render_template(
        'master/datatest/index.html', datatests=datatests, roles=roles)


@datatest.route('/edit/<int:id>', methods = ['GET', 'POST'])
# @datatest.route('/datatest/<int:id>/info')
@login_required
@admin_required
def edit(id):
    """edit datatest"""
    
    dbdata = Datatest.query.filter_by(id=id).first()
    form = DatatestForm(obj=dbdata)
    if dbdata is None:
        abort(404)

    if request.method == 'POST':
        form = DatatestForm()
        if form.validate_on_submit():
            dbdata.name = form.name.data
            dbdata.d1 = form.d1.data
            dbdata.d2 = form.d2.data
            
            from datetime import datetime
            dtime = datetime.today()

            # dbdata.d3 = form.d3.data
            dbdata.d3 = dtime
            dbdata.d4 = form.d4.data
            
            db.session.add(dbdata)
            db.session.commit()
            flash('Data successfully changed to {}.'.format(datatest.name, 'form-success'))
            return redirect(url_for('datatest.edit', id=id))
    else:
        return render_template('master/datatest/add-edit.html', 
            datatest=datatest, 
            form=form)
    


@datatest.route('/_delete/<int:id>/')
@login_required
@admin_required
def delete(id):
    """Delete data."""
    datatest = Datatest.query.filter_by(id=id).first()
    db.session.delete(datatest)
    db.session.commit()
    flash('Successfully deleted data %s.' % Datatest.name, 'success')

    return redirect(url_for('datatest.index'))