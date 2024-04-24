from fastapi import FastAPI
from config.database import engine, Base
from dotenv import load_dotenv
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

Base.metadata.create_all(bind=engine)

load_dotenv()

app = FastAPI()
app.title = 'Movies APIz'
app.version = '0.0.1'
app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)
