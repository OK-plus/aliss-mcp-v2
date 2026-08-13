import os
import logging

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
    """
    Search ALISS for local community services.
    """
    return await search_aliss(postcode, keyword, radius)


# IMPORTANT:
# Cloud Run serves this ASGI application.
# Stateless HTTP is configured HERE, on the app that is actually served.
app = mcp.http_app(
    path="/mcp",
    stateless_http=True,
)
