import asyncio
import time
from random import randint
from typing import Annotated

import httpx
import uvicorn
from fastapi import FastAPI
from fastapi import Path
from fastapi import Query

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from Client"}


@app.get("/fetch/{name}")
async def fetch_name(
    name: Annotated[str, Path(..., title="Name path")],
    number: Annotated[int, Query(..., title="Number query", gt=0, le=10)],
):
    start_time = time.perf_counter()
    async with httpx.AsyncClient() as client:
        async with asyncio.TaskGroup() as tg:
            tasks = [
                tg.create_task(
                    client.get(
                        f"http://127.0.0.1:8000/test/{name}", params={"number": randint(1, 10)}
                    )
                )
                for _ in range(number)
            ]

    results = [task.result().json() for task in tasks]

    elapsed = time.perf_counter() - start_time

    sum_time = sum([result.get(name) for result in results])

    return {
        "elapsed": elapsed,
        "sum_time": f"{sum_time / 10:.1f}",
        "results": results,
    }


def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8001)


if __name__ == "__main__":
    main()
