import os
from contextlib import asynccontextmanager

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    if not os.path.exists("temp"):
        os.makedirs("temp")

    yield

    print("Shutting down the server")
