from fastapi import FastAPI

from datetime import datetime
from core.dependencies import setup_dependencies

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Log format
logger = logging.getLogger(__name__)
from fastapi.middleware.cors import CORSMiddleware

# pip install cloud-sql-python-connector[pymysql] SQLAlchemy==2.0.7


from apis.chat_api import router as ChatApiRouter
from apis.info_api import router as InfoApiRouter
from apis.task_api import router as TaskApiRouter
from apis.user_api import router as UserApiRouter

app = FastAPI(
    title="FastAPI Application",
    description="API for LLMQueryExecutor and LLMVisualisationManager functionality, with user management.",
    version="1.0.0",
)

# origins = [
#     "http://localhost:5173",  # Add specific origins here
#     "https://enes-talk-w-sql.vercel.app",
#     "https://api.budgety.ai",
#     "https://wwww.budgety.ai",
#     "https://editor.swagger.io/"
# ]


origins = [
    "http://localhost:5173",  # Add specific origins here
    "http://localhost:5174",  # Add specific origins here
    "https://enes-talk-w-sql.vercel.app",
    "https://db-whisperer.vercel.app",
    "https://api.budgety.ai",
    "https://api.budgety.ai:3000",
    "https://editor.swagger.io/" ,
    "https://editor.swagger.io"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins , # Adjust this to more specific domains for security
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],
    expose_headers=["*"]
)


app.include_router(ChatApiRouter)
app.include_router(InfoApiRouter)
app.include_router(TaskApiRouter)
app.include_router(UserApiRouter)


from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import Request
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"Validation error: {exc}")
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body},
    )


@app.exception_handler(Exception)
async def internal_server_error_handler(request: Request, exc: Exception):
    logger.error(f"Internal Server Error: {str(exc)}", exc_info=True)  # Log the exception details
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error", "message": str(exc)},
    )

CORRECT_PASSCODE = "supersecretpasscode"

total_cost_since_dict = {"date": datetime.now(),
                         "input_cost": 0,
                         "output_cost": 0}


# Configure logging
logger = logging.getLogger("Analyser")
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize DI containers
services = setup_dependencies()

@app.on_event("startup")
async def startup_event():
    app.state.services = services
    logger.info("Configurations loaded and services initialized")







