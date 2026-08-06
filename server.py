import os
import logging

from fastapi import FastAPI, Request
from fastmcp import FastMCP
from aliss_client import search_aliss

logging.basicConfig(level=logging.INFO)

mcp = FastMCP("ALISS Community Services")


@mcp.tool()
async def find_aliss_services(
    postcode: str,
    keyword: str,
    radius: int = 10,
):
    return await search_aliss(postcode, keyword, radius)


app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):

    body = await request.body()

    logging.info("========== NEW REQUEST ==========")
    logging.info(f"Path: {request.url.path}")
    logging.info(f"Method: {request.method}")

    auth = request.headers.get("authorization")

    if auth:
        logging.info("Authorization header present")
    else:
        logging.info("No Authorization header")

    logging.info(f"Body: {body.decode('utf-8')}")

    response = await call_next(request)

    logging.info(f"Response status: {response.status_code}")
    logging.info("=================================")

    return response


app.mount("/", mcp.http_app(path="/mcp", stateless_http=True))


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.getenv("PORT", "8080")),
    )
