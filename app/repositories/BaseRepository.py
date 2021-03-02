
class BaseRepository:
    model = None
    db = None
    
    # db.Model type
    insertData = None

    # db.Model type
    updateData = None

    lastData = None
    form = None
    _id = None

    def __init__(self, db = None, model = None):
        """
        model = must be SQLAlchemy db.Model or it's predecessor type
        """
        self.model = model
        self.db = db
    
    def all(self):
        return self.model.query.all()
    
    def single(self, id):
        return self.model.query.filter_by(id=id).first()

    def setId(self, id):
        self._id = id
        return self

    def setForm(self, form):
        self.form = form
        return self

    def setFormData(self, form, _type='insert'):
        if _type == 'insert':
            return self.setForm(form).setInsertData()
        elif _type == 'update':
            return self.setForm(form).setUpdateData()

    def setInsertData(self):
        raise NotImplementedError
    
    def setUpdateData(self):
        raise NotImplementedError

    def insert(self, data = None):
        if not data:
            data = self.insertData
        self.lastData = data
        self.addSessionAndCommit(self.db, data)
        return
    
    def update(self, data = None):
        if not data:
            data = self.updateData
        self.lastData = data
        self.addSessionAndCommit(self.db, data)
        return
    
    def delete(self, id):
        db = self.db
        dbdata = self.model.query.filter_by(id=id).first()
        db.session.delete(dbdata)
        db.session.commit()

        return dbdata
    
    def addSessionAndCommit(self, db, data):
        db.session.add(data)
        db.session.commit()

