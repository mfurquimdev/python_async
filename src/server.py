import asyncio
from typing import Annotated

import uvicorn
from fastapi import FastAPI
from fastapi import Path
from fastapi import Query

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from Server"}


@app.get("/test/{name}")
async def test_name(
    name: Annotated[str, Path(..., title="Name path")],
    number: Annotated[int, Query(..., title="Number query", gt=0, le=10)],
):
    await asyncio.sleep(number / 10)

    return {name: number}


def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
