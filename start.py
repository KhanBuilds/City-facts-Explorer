import os
from uvicorn import run
from main import app  # make sure this is your FastAPI app

# Railway sets the port in the environment variable PORT
port = int(os.environ.get("PORT", 8000))

# Start the app
run("main:app", host="0.0.0.0", port=port, workers=4)