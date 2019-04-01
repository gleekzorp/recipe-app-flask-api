from . import db
import datetime
from marshmallow import fields, Schema

class RecipepostModel(db.Model):
  """
  Recipepost Model
  """

  __tablename__ = 'recipeposts'

  id = db.Column(db.Integer, primary_key=True)
  recipe_name = db.Column(db.String(128), nullable=False)
  cook_time = db.Column(db.Integer, nullable=False)
  recipe_link = db.Column(db.String, nullable=False)
  image_url = db.Column(db.String, nullable=False)
  main_ingredient = db.Column(db.String, nullable=False)
  description = db.Column(db.Text, nullable=False)
  owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)

  def __init__(self, data):
    self.recipe_name = data.get('recipe_name')
    self.cook_time = data.get('cook_time')
    self.recipe_link = data.get('recipe_link')
    self.image_url = data.get('image_url')
    self.main_ingredient = data.get('main_ingredient')
    self.description = data.get('description')
    self.owner_id = data.get('owner_id')
    self.created_at = datetime.datetime.utcnow()
    self.modified_at = datetime.datetime.utcnow()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    self.modified_at = datetime.datetime.utcnow()
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  @staticmethod
  def get_all_recipeposts():
    return RecipepostModel.query.all()
  
  @staticmethod
  def get_one_recipepost(id):
    return RecipepostModel.query.get(id)

  def __repr__(self):
    return '<id {}>'.format(self.id)

class RecipepostSchema(Schema):
  """
  Recipepost Schema
  """
  id = fields.Int(dump_only=True)
  recipe_name = fields.Str(required=True)
  cook_time = fields.Int(required=True)
  recipe_link = fields.Str(required=True)
  image_url = fields.Str(required=True)
  main_ingredient = fields.Str(required=True)
  description = fields.Str(required=True)
  owner_id = fields.Int(required=True)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)