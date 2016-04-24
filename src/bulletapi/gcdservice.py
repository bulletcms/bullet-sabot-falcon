from gcloud import datastore

##########################################
##    Google Datastore Service          ##
##########################################

class GCDService:
    def __init__(self, project_id):
        self._project_id = project_id
        self._client = datastore.Client()

    @property
    def project_id(self):
        return self._project_id

    def add_page(self, path, title, content):
        self._client.put(
            datastore.Entity(
                self._client.key('Page', path),
                exclude_from_indexes=['title', 'content']
            ).update({
                'path': path,
                'title': title,
                'content': content
            })
        )

    def update_page(self, ):
        pass
