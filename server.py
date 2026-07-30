import asyncio
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

    logging.info(
        f"Starting ALISS MCP on port {os.getenv('PORT', 8080)}"
    )

    asyncio.run(
        mcp.run_async(
            transport="streamable-http",
            host="0.0.0.0",
            port=int(os.getenv("PORT", "8080")),
        )
    )
