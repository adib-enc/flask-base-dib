from .BaseRepository import BaseRepository
from app.models import Datatest
from app import db
from datetime import datetime

class DatatestRepository(BaseRepository):
    def __init__(self, db = None, model = None):
        self.model = Datatest
        self.db = db
    
    def setInsertData(self):
        # dataRepo.setForm(form).insert()
        dtime = datetime.today()
        form = self.form

        self.insertData = Datatest(
            name=form.name.data,
            d1=form.name.data,
            d2=form.d2.data,
            d3=dtime,
            d4=form.d4.data,
            )
        return self
    
    def setUpdateData(self):
        dtime = datetime.today()
        form = self.form
        dbdata = self.single(self._id)
        
        if dbdata:
            dbdata.name=form.name.data
            dbdata.d1=form.d1.data
            dbdata.d2=form.d2.data
            dbdata.d3=dtime
            dbdata.d4=form.d4.data
            
            print(dbdata.d1)

            self.updateData = dbdata
        
        return self