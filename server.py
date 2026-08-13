import logging
import os

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


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))

    logging.info(
        "Starting ALISS MCP server on port %s",
        port,
    )

    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=port,
        path="/mcp",
        stateless_http=True,
    )
