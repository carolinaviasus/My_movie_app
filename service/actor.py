from models.actor import Actor as ActorMoldel
from schemas.actor import Actor

class ActorService():

    def __init__(self,db) -> None:
        self.db = db

    def get_actor(self): 
        result = self.db.query(ActorMoldel).all()
        return result

     # id = Column(Integer,primary_key = True)
    # actor_first_name = Column(String)
    # actor_last_name = Column(String)
    # actor_gender = Column(String)

    def get_actor_by_id(self,id:int):
        result = self.db.query(ActorMoldel).filter(ActorMoldel.id == id).first()
        return result

    def get_actor_by_actor_first_name(self,actor_first_name:str):
        result = self.db.query(ActorMoldel).filter(ActorMoldel.actor_first_name == actor_first_name).all()
        return result

    def get_actor_by_actor_last_name(self,actor_last_name:str):
        result = self.db.query(ActorMoldel).filter(ActorMoldel.actor_last_name == actor_last_name).all()
        return result

    def get_actor_by_actor_gender(self,actor_gender:str):
        result = self.db.query(ActorMoldel).filter(ActorMoldel.actor_gender == actor_gender).all()
        return result

    def create_actor(self,actor:ActorMoldel):
        new_actor = ActorMoldel(
        actor_first_name = actor.actor_first_name ,
        actor_last_name = actor.actor_last_name,
        actor_gender = actor.actor_gender,    
        )
        self.db.add(new_actor)
        self.db.commit()
        return