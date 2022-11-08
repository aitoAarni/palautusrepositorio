from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        content_dict = toml.loads(content)
        dependencies = list(content_dict["tool"]["poetry"]["dependencies"])
        dev_dependencies = list(content_dict["tool"]["poetry"]["dev-dependencies"])
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project("Test name", "Test description", dependencies, dev_dependencies)
