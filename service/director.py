from models.director import Director as DirectorModel
from schemas.director import Director

class DirectorService():

    def __init__(self,db) -> None:
        self.db = db

    def get_director(self):
        result = self.db.query(DirectorModel).all()
        return result

    def get_director_by_id(self, id:int):
        result = self.db.query(DirectorModel).filter(DirectorModel.id == id).first() 
        return result
    
    def get_director_by_fname(self, fname:str):
        result = self.db.query(DirectorModel).filter(DirectorModel.fname == fname).all() 
        return result

    def get_director_by_lname(self, lname:str):
        result = self.db.query(DirectorModel).filter(DirectorModel.lname == lname).all() 
        return result

    # crear
    def create_director(self, director:Director):
        new_director = DirectorModel(
            id = director.id,
            fname = director.fname,
            lname = director.lname,
        )
        self.db.add(new_director)
        self.db.commit()
        return 

    # actualizar
    def update_director(self, fname:str, data:Director):
        director.id = data.id
        director = self.db.query(DirectorModel).filter(DirectorModel.fname == fname).first()
        director.lname = data.lname
        self.db.commit()
        return
        
    # eliminar
    def delete_director(self,id:int):
        self.db.query(DirectorModel).filter(DirectorModel.id == id).delete()
        self.db.commit()
        return


