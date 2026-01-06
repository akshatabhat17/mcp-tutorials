from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
        return a + b
        @mcp.tool
        def weather(city: str) -> str:
            """Get the current weather for a city."""
                # Dummy implementation for illustration
                    return f"The current weather in {city} is sunny with a temperature of 25°C."

                    if __name__ == "__main__":
                        mcp.run(transport="stdio")
                        
