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
from app.repositories.DatatestRepository import DatatestRepository
dataRepo = DatatestRepository(db)

@datatest.route('/')
@login_required
@admin_required
def index():
    """Admin dashboard page."""
    datas = dataRepo.all()
    return render_template('master/datatest/index.html', datas=datas)


@datatest.route('/create', methods=['GET', 'POST'])
@login_required
@admin_required
def create():
    """Create a new data."""
    form = DatatestForm()
    if form.validate_on_submit():
        dataRepo.setFormData(form).insert()
        flash('Datatest {} successfully created'.format(dataRepo.lastData.name), 'form-success')
        return redirect(url_for('datatest.index'))
    return render_template('master/datatest/add-edit.html', form=form)


@datatest.route('/datatest')
@login_required
@admin_required
def all():
    """View all registered datatests."""
    datatests = Datatest.query.all()
    return render_template(
        'master/datatest/index.html', datatests=datatests, roles=roles)


@datatest.route('/edit/<int:id>', methods = ['GET', 'POST'])
# @datatest.route('/datatest/<int:id>/info')
@login_required
@admin_required
def edit(id):
    """edit datatest"""
    
    dbdata = dataRepo.single(id)
    form = DatatestForm(obj=dbdata)
    if dbdata is None:
        abort(404)

    if request.method == 'POST':
        form = DatatestForm()
        if form.validate_on_submit():
            dataRepo.setId(id).setFormData(form, 'update').update()
            flash('Data successfully changed to {}.'.format(dataRepo.lastData.name, 'form-success'))
            return redirect(url_for('datatest.edit', id=id))
    else:
        return render_template('master/datatest/add-edit.html', 
            data=dbdata, 
            form=form)
    


@datatest.route('/_delete/<int:id>/')
@login_required
@admin_required
def delete(id):
    """Delete data."""
    data = dataRepo.delete(id)
    flash('Successfully deleted data %s.' % data.name, 'success')

    return redirect(url_for('datatest.index'))