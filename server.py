import xml.etree.ElementTree as ET
from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("drawio")


OUTPUT_DIR = Path.home() /"drawio-diagrams"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def validate_xml(xml_string: str) -> tuple[bool,str]:
    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError as e:
        return False, f"XML parse error: {e}"
    
    if root.tag not in ("mxfile", "mxGraphModel"):
        return False, f"Expected <mxfile> or <mxGraphModel>, got <{root.tag}>"
    
    return True, "Valid"

@mcp.tool()
def save_diagram(xml:str, filename: str = "diagram") -> dict:
    """Validate draw.io XML and save it as a .drawio file.

    Args:
        xml: Complete draw.io XML string with mxfile or mxGraphModel root.
        filename: Name for the file (without extension).
    """   
    is_valid, error = validate_xml(xml)
    if not is_valid:
        return {"error": error}
    
    if not filename.endswith(".drawio"):
        filename += ".drawio"

    path = OUTPUT_DIR/filename
    path.write_text(xml, encoding="utf-8")

    return {"file_path": str(path), "message": f"Saved to {path}"}

mcp.run()