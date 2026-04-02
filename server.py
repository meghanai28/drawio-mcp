import xml.etree.ElementTree as ET
from pathlib import Path
import webbrowser
import zlib
import base64
import urllib.parse
from mcp.server.fastmcp import FastMCP
from format_reference import DRAWIO_FORMAT_REFERENCE

mcp = FastMCP("drawio")


OUTPUT_DIR = Path.cwd() /"drawio-diagrams"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def validate_xml(xml_string: str) -> tuple[bool,str]:
    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError as e:
        return False, f"XML parse error: {e}"
    
    if root.tag not in ("mxfile", "mxGraphModel"):
        return False, f"Expected <mxfile> or <mxGraphModel>, got <{root.tag}>"
    
    return True, "Valid"

def make_drawio_url(xml:str) -> str:
    """ Compress XML into draw.io broswer URL
    
    draw.io expects: encodeURIComponent(base64(raw_deflate(xml)))
    """

    compressed = zlib.compress(xml.encode("utf-8"))[2:-4] # removing the zlib header + the trailer
    b64 = base64.b64encode(compressed).decode("ascii")
    encoded = urllib.parse.quote(b64, safe="")
    return f"https://app.diagrams.net/#R{encoded}"


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

@mcp.tool()
def open_in_browser(xml: str) -> dict:
    """Encode draw.io XML into a URL for the web editor, without saving a file.
    
    Args:
        xml: Valid draw.io XML string
    """
    is_valid, error = validate_xml(xml)
    if not is_valid:
        return {"error": error}
    
    url = make_drawio_url(xml)
    webbrowser.open(url)
    return {"drawio_rl" : url, "message": f"Open in browser: {url}"}

@mcp.tool()
def list_diagrams() -> dict:
    """ List all saved .drawio files. 
    
    Returns the output directory and a list of diagram filenames
    """
    files = sorted(OUTPUT_DIR.glob("*.drawio"))
    return {"output_dir": str(OUTPUT_DIR), "diagrams": [f.name for f in files], "count": len(files)}

@mcp.tool()
def get_diagram(filename: str) -> dict:
    """Read an existing .drawio file so it can be modified and re-saved
    
    Args:
        filename: Name of the file (with or without .drawio extension).
    """

    if not filename.endswith(".drawio"):
        filename += ".drawio"

    path = OUTPUT_DIR/filename
    if not path.exists():
        return {"error": f"File not found: {filename}", "available": [f.name for f in OUTPUT_DIR.glob("*.drawio")]}
    
    xml = path.read_text(encoding="utf-8")
    return {"xml": xml, "file_path": str(path), "message": f"Loaded {filename}. Edit the XML and call save_diagram to save."}

@mcp.prompt()
def drawio_format_reference() -> str:
    """draw.io XML format reference — shapes, edges, styles, colors, and examples."""
    return DRAWIO_FORMAT_REFERENCE

mcp.run()