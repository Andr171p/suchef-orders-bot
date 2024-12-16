from fastapi import FastAPI

from contextlib import AbstractAsyncContextManager
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI) -> AbstractAsyncContextManager[None]:
    pass
