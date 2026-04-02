# drawio-mcp

Turn natural language into draw.io diagrams using Claude Code. No API key needed.

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/drawio-mcp.git
cd drawio-mcp
uv sync
```

Don't have uv? Install it first:
- Mac/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

## Connect to Claude Code

**Global (use from any repo):**
```bash
claude mcp add --scope global drawio -- uv run --directory /path/to/drawio-mcp python server.py
```

**Single project:**
```bash
claude mcp add drawio -- uv run --directory /path/to/drawio-mcp python server.py
```

## Usage

Open Claude Code and ask:

```
Read the drawio_format_reference prompt first, then create a draw.io diagram
showing [whatever you want]. Save it as [name] and open it in the browser.
```

### Example prompts

- `Create a card grid diagram explaining how transformers work. Save it as transformers and open in browser.`
- `Read my codebase and create an architecture diagram. Save it as architecture.`
- `Make a flowchart for user authentication with OAuth. Save it as auth-flow and open in browser.`

## Tools

| Tool | What it does |
|---|---|
| `save_diagram` | Validates XML, saves `.drawio` file, returns browser URL |
| `open_in_browser` | Opens diagram in draw.io web editor |
| `get_diagram` | Loads an existing `.drawio` file for editing |
| `list_diagrams` | Lists all saved diagrams |

Diagrams save to a `drawio-diagrams/` folder in whatever repo you run Claude from.

## Customize the style

Edit `format_reference.py` to change the color palette, layout preferences, and example diagrams. Claude reads this before generating — your examples are its style guide. Currently using some of my human-made diagrams which helps generates diagrams that match my aesthetic.

## License

MIT
