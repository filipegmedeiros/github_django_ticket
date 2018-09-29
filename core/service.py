import json
import requests

class GitHub:

    def __init__(self, username, password):

        self.username = username
        self.password = password

        self.repository = None
        self.owner_repository = None

        self.url_api = 'https://api.github.com/repos/{}/{}/issues'

        self.session = requests.Session()
        self.session.auth = (self.username, self.password)

    def access(self, repository, owner_repository):
        self.repository = repository
        self.owner_repository = owner_repository

        self.url_api = self.url_api.format(self.owner_repository, self.repository)

    def create_issue(self, title=None, autor=None, setor=None, conteudo=None, labels=[]):

        self.__verify_errors()

        TEMPLATE_CHAMADO = "**Aberto por:**\n\r >{autor}\n\r**Setor:** \n\r>{setor} \n\r--- \n\r{conteudo}"
    
        issue_data = {
            "autor":autor,
            "setor":setor,
            "conteudo":conteudo
        }

        api_data = {
            'title': title,
            'body': TEMPLATE_CHAMADO.format(**issue_data),
            'labels': labels or ["Não Vista"]
        }

        response = self.session.post(self.url_api, json.dumps(api_data))
        
        response_api = None

        if response.status_code == 201:
            
            response = json.loads(response.content.decode('utf-8'))
            
            response_api = {
                "status": "success",
                "message": "Chamado criado com sucesso.",
                "data": "https://github.com/{}/{}/issues/{}".format(self.owner_repository,self.repository,response.get('number'))
            }

        else:

            response_api = {
                "status": "error",
                "message": "Não foi possível criar o chamado. Contacte o Administrador",
                "data": None
            }

        return response_api

    def __verify_errors(self):

        if ( self.username is None):
            raise Exception("The username must be filled")

        elif ( self.password is None):
            raise Exception("The password must be filled")

        elif (self.repository is None):
            raise Exception("The repository must be filled")

        elif ( self.owner_repository is None):
            raise Exception("The owner_repository must be filled")


if __name__ == "__main__":

    TITULO = None

    USERNAME = None
    PASSWORD = None

    OWNER = None
    REPOSITORY = None

    github = GitHub(USERNAME,PASSWORD)
    github.access(REPOSITORY,OWNER)

    retorno = github.create_issue(
                title=None, 
                autor=None,
                setor=None,
                conteudo=None
            )