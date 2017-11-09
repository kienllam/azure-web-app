from flask import Blueprint, request, render_template, _app_ctx_stack, jsonify
from FlaskWebProject1.app.cosmosdb import CosmosDB, DocumentManagement
from config.default import BaseConfig

profile = Blueprint('profile', __name__)


def get_db():
    app_context = _app_ctx_stack
    db = getattr(app_context, "DB", None)
    if db is None:
        db = CosmosDB(BaseConfig.HOST, BaseConfig.MASTER_KEY, BaseConfig.DATABASE_ID)
        app_context.DB = db
    return db


@profile.route('/svoc/<string:id>')
def get_id(id):
    db = get_db()
    document = DocumentManagement.get_document(client=db.client, database_link=db.database_link,
                                               collection=BaseConfig.COLLECTION_ID, id=id)
    return jsonify(document)


@profile.route('/svoc/search', methods=['GET'])
def search():
    params = request.args.to_dict()
    db = get_db()
    params['collection_id'] = BaseConfig.COLLECTION_ID
    if params.get('id') is None:
        params['id'] = 'id'
    documents = DocumentManagement.query_collection(client=db.client, database_link=db.database_link,
                                                      collection=BaseConfig.COLLECTION_ID, params=params)
    return render_template('svoc_dashboard.html', documents=documents)


