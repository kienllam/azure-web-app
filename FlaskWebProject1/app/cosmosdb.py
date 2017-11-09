import pydocumentdb.document_client as documents_client
import pydocumentdb.errors as errors


class CosmosDB(object):

    def __init__(self, host, master_key, database_id):
        self.host = host
        self.master_key = master_key
        self.database_id = database_id
        self.client = documents_client.DocumentClient(host, {'masterKey': master_key})
        self.database_link = 'dbs/' + database_id


class DocumentManagement:

    def generate_sql_statement(params):
        alias = 'c'
        fields = "SELECT {0}.{1}, ".format(alias, params['id']) + ", ".join(map(lambda x: alias + "." + x, params.get('fields').split(","))) if params.get(
            'fields') else 'SELECT *'
        condition = "WHERE {0}.{1} {2} '{3}'".format(alias, params.get('condition'), params.get('operator'),
                                                   params.get('target')) if params.get('condition') else ''
        return "{0} FROM {1} {2} {3}".format(fields, params.get('collection_id'), alias, condition)


    @staticmethod
    def query_collection(**kwargs):
        print("--INFO-- Start Query the Collection with id: {0} --INFO--".format(id))
        client = kwargs.get('client')
        coll_links = "{0}/colls/{1}/".format(kwargs.get('database_link'), kwargs.get('collection'))
        sql_statement = DocumentManagement.generate_sql_statement(kwargs.get('params'))
        print(sql_statement)

        if (kwargs.get('partition')):
            query_options = {'partitionKey': kwargs.get('partition')}
            documents = client.QueryDocuments(coll_links, sql_statement, query_options)
        else:
            documents = client.QueryDocuments(coll_links, sql_statement)

        return list(documents)


    @staticmethod
    def get_document(**kwargs):
        print("--INFO-- Start Getting Document with id: {0}".format(kwargs.get('id')))

        client = kwargs.get('client')

        doc_link = "{0}/colls/{1}/docs/{2}".format(kwargs.get('database_link'), kwargs.get('collection'), kwargs.get('id'))
        print(doc_link)
        try:
            result = client.ReadDocument(doc_link)
        except errors.HTTPFailure as error:
            print("--ERROR-- {0} --ERROR--".format(error.status_code))
            result = errors
        return result
