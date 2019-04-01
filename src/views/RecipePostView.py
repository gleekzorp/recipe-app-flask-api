from flask import request, g, Blueprint, json, Response
from ..shared.Authentication import Auth
from ..models.RecipepostModel import RecipepostModel, RecipepostSchema

recipepost_api = Blueprint('recipepost_api', __name__)
recipepost_schema = RecipepostSchema()


@recipepost_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
  """
  Create Recipepost Function
  """
  req_data = request.get_json()
  req_data['owner_id'] = g.user.get('id')
  data, error = recipepost_schema.load(req_data)
  if error:
    return custom_response(error, 400)
  post = RecipepostModel(data)
  post.save()
  data = recipepost_schema.dump(post).data
  return custom_response(data, 201)

@recipepost_api.route('/<int:recipepost_id>', methods=['PUT'])
@Auth.auth_required
def update(recipepost_id):
  """
  Update A Repipepost
  """
  req_data = request.get_json()
  post = RecipepostModel.get_one_recipepost(recipepost_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = recipepost_schema.dump(post).data
  if data.get('owner_id') != g.user.get('id'):
    return custom_response({'error': 'permission denied'}, 400)
  
  data, error = recipepost_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)
  post.update(data)
  
  data = recipepost_schema.dump(post).data
  return custom_response(data, 200)

@recipepost_api.route('/<int:recipepost_id>', methods=['DELETE'])
@Auth.auth_required
def delete(recipepost_id):
  """
  Delete A Recipepost
  """
  post = RecipepostModel.get_one_recipepost(recipepost_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = recipepost_schema.dump(post).data
  if data.get('owner_id') != g.user.get('id'):
    return custom_response({'error': 'permission denied'}, 400)

  post.delete()
  return custom_response({'message': 'deleted'}, 204)

# You can add some of the authorization like above if you only want users with access to view all posts
@recipepost_api.route('/', methods=['GET'])
def get_all():
  """
  Get All Recipeposts
  """
  posts = RecipepostModel.get_all_recipeposts()
  data = recipepost_schema.dump(posts, many=True).data
  return custom_response(data, 200)

# You can add some of the authorization like above if you only want users with access to view all posts
@recipepost_api.route('/<int:recipepost_id>', methods=['GET'])
def get_one(recipepost_id):
  """
  Get A Recipepost
  """
  post = RecipepostModel.get_one_recipepost(recipepost_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = recipepost_schema.dump(post).data
  return custom_response(data, 200)

def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )