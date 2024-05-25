from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.modules.auth.services import AuthService
from app.modules.roles.models import Role
from app.modules.tasks.models import Task
from app.modules.users.adapters import UserRepositoryAdapter
from app.modules.users.models import User
from app.modules.users.use_cases import UserSignUp

sql_user = "victor"
sql_pass = "password"
sql_host = "localhost"
sql_port = "5432"
SQLALCHEMY_DATABASE_URI = (
    f"postgresql+psycopg2://{sql_user}:{sql_pass}@{sql_host}:{sql_port}/task_master"
)

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

with SessionLocal() as session:
    task = Task()
    role = Role()
    user_repository = UserRepositoryAdapter(session, User)
    auth_service = AuthService()
    use_case = UserSignUp(auth_service=auth_service, user_repository=user_repository)
    login = use_case.execute(
        user_data={"email": "victormalsx@gmail.com", "password": "password"}
    )
    print(login)
