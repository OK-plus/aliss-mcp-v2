import os
import logging

from fastmcp import FastMCP
from aliss_client import search_aliss

logging.basicConfig(level=logging.INFO)

# IMPORTANT:
# Set stateless_http=True here AND on http_app below.
mcp = FastMCP(
    "ALISS Community Services",
    stateless_http=True,
)


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
# This is the actual ASGI application Cloud Run will serve.
app = mcp.http_app(
    path="/mcp",
    stateless_http=True,
)
