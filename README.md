# python_api_dev

## This is a python API using FastAPI

1. Install python plugin
2. Create main.py
3. Create virtual environment - python3 -m venv venv
4. Activating virtual environment - source venv/bin/activate
5. Install fastapi - pip install "fastapi[all]"
6. Run uvicorn server - uvicorn main:app --reload (Because uvicorn is name of server, main is name of file and in main app is name of FastAPI instance) (--reload allows for reloads on detected changes)
7. Making get requests to paths - @app.get("/") async def root(): "function" 
8. 