from app.dal.repo.interface import IRepository

class RepositoryRegistry:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(RepositoryRegistry, cls).__new__(cls)
        return cls.__instance

    def __init__(self, session):
        if not hasattr(self, 'initialized'):
            self.repositories = {}
            self.session = session
            self.initialized = True

    def add(self, repo_name: str, repo_class: IRepository) -> None:
        if repo_name in self.repositories:
            raise ValueError(f"'{repo_name}' already is in the registry.")
        self.repositories[repo_name] = repo_class

    def get(self, repo_name: str) -> IRepository:
        if repo_name not in self.repositories:
            available_repos = ", ".join(self.repositories.keys())
            raise ValueError(f"'{repo_name}' not found in the registry. Available repositories: {available_repos}")
        repo_class = self.repositories[repo_name]
        return repo_class(self.session)