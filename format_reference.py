DRAWIO_FORMAT_REFERENCE = r"""# draw.io XML format reference

## File structure

<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="drawio-mcp" agent="drawio-mcp-server" version="1.0.0" type="device">
  <diagram name="Page-1" id="page1">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1"
      tooltips="1" connect="1" arrows="1" fold="1" page="1"
      pageScale="1" pageWidth="1100" pageHeight="850" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>

## Rules

- id="0" is root, id="1" is default parent layer. Your cells start at id="2".
- Vertices (shapes): <mxCell id="2" value="Label" style="..." vertex="1" parent="1"><mxGeometry x="100" y="100" width="120" height="60" as="geometry"/></mxCell>
- Edges (connectors): <mxCell id="10" value="" style="..." edge="1" parent="1" source="2" target="3"><mxGeometry relative="1" as="geometry"/></mxCell>
- Always include as="geometry". Vertices use absolute x/y/width/height. Edges use relative="1".
- Use &#xa; for line breaks inside labels.
- Use math="1" in mxGraphModel and $$ $$ in values for LaTeX math notation.

## Style rules — follow these strictly

- Prefer card/grid layouts over flowcharts unless a flow is specifically requested.
- Each concept gets its own color-coded card with a bold colored header bar.
- Use rich, saturated fill colors — not default pastel draw.io colors.
- Group related concepts spatially — left to right or top to bottom by logic flow.
- Use bullet lists inside cards for details (html=1 with <ul><li> tags).
- Keep consistent card sizes within the same row.
- Bold headers at the top of each card using colored rectangle + overlaid text.
- Support math notation in labels when relevant using $$ LaTeX $$.

## Shape styles

- Card: rounded=0;whiteSpace=wrap;html=1;
- Rounded card: rounded=1;whiteSpace=wrap;html=1;arcSize=20;strokeWidth=1;
- Pill / button: rounded=1;whiteSpace=wrap;html=1;arcSize=50;
- Circle / avatar: ellipse;whiteSpace=wrap;html=1;aspect=fixed;
- Diamond: rhombus;whiteSpace=wrap;html=1;
- Database: shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;
- Cloud: ellipse;shape=cloud;whiteSpace=wrap;html=1;
- Person: shape=mxgraph.basic.person;whiteSpace=wrap;html=1;
- Text label (no border): text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;
- Header bar: rounded=0;whiteSpace=wrap;html=1;fillColor=#DARK_COLOR;strokeColor=#DARK_COLOR; (with white text overlaid)
- Swimlane: swimlane;startSize=23;

## Edge styles

- Orthogonal: edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;
- Simple arrow: endArrow=classic;html=1;rounded=0;
- Curved: curved=1;html=1;
- Dashed: dashed=1;html=1;
- Bidirectional: html=1;startArrow=classic;endArrow=classic;
- No arrow: html=1;endArrow=none;endFill=0;

## Color palette

### Card fills with matching strokes
- Salmon/pink: fillColor=#fad9d5;strokeColor=#ae4132;
- Orange/peach: fillColor=#ffe6cc;strokeColor=#d79b00;
- Teal: fillColor=#b0e3e6;strokeColor=#0e8088;
- Light purple: fillColor=#d0cee2;strokeColor=#56517e;
- Light blue: fillColor=#dae8fc;strokeColor=#6c8ebf;
- Blue accent: fillColor=#b1ddf0;strokeColor=#10739e;

### Header bar fills (solid dark, white text on top)
- Dark teal: fillColor=#0E8088;strokeColor=#0E8088;
- Dark purple: fillColor=#56517E;strokeColor=#56517e;
- Medium blue: fillColor=#6C8EBF;strokeColor=#56517e;

### Text colors
- White text on dark: fontColor=#FFFFFF; or use font color="rgb(255, 255, 255)" in HTML
- Dark text on light: fontColor=#000000;

## Font options

- fontSize=15; (body/list items)
- fontSize=20; (card headers and labels)
- fontStyle=1; (bold=1, italic=2, underline=4, bold+italic=3)

## Layout tips

- Space cards ~20px apart.
- Use consistent card heights within a row (e.g. all 140px tall).
- Header bars: same width as card, ~30px tall, positioned at top of card.
- Overlay text on header bars using text cells with fillColor=none;strokeColor=none;
- Cards typically 200-400px wide, 140-240px tall.
- Keep coordinates positive, 0-1200 range.
- For card grids: align tops of cards in each row.
- For technical content: include math notation, bullet lists, and subscripts.

## Example 1 — architecture diagram 

<mxGraphModel dx="1389" dy="703" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="970" pageHeight="700" math="0" shadow="0">
  <root>
    <mxCell id="0" />
    <mxCell id="1" parent="0" />
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-5" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fad7ac;strokeColor=#b46504;" value="" vertex="1">
      <mxGeometry height="300" width="190" x="20" y="20" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-6" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fad7ac;strokeColor=#b46504;" value="" vertex="1">
      <mxGeometry height="90" width="190" x="20" y="340" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-7" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fad7ac;strokeColor=#b46504;" value="" vertex="1">
      <mxGeometry height="230" width="190" x="20" y="450" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-8" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#b0e3e6;strokeColor=#0e8088;" value="" vertex="1">
      <mxGeometry height="240" width="350" x="260" y="20" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-9" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#b1ddf0;strokeColor=#10739e;" value="" vertex="1">
      <mxGeometry height="660" width="290" x="660" y="20" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-10" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#b0e3e6;strokeColor=#0e8088;" value="" vertex="1">
      <mxGeometry height="400" width="350" x="260" y="280" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-12" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFB570;strokeColor=#b46504;" value="" vertex="1">
      <mxGeometry height="40" width="190" x="20" y="20" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-11" parent="1" style="text;html=1;whiteSpace=wrap;overflow=hidden;rounded=0;fontSize=9;" value="&lt;h1 style=&quot;margin-top: 0px;&quot;&gt;&lt;font style=&quot;font-size: 20px;&quot;&gt;Feature Extraction&lt;/font&gt;&lt;/h1&gt;" vertex="1">
      <mxGeometry height="27" width="210" x="25" y="23" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-13" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFB570;strokeColor=#b46504;" value="" vertex="1">
      <mxGeometry height="40" width="190" x="20" y="450" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-14" parent="1" style="text;html=1;whiteSpace=wrap;overflow=hidden;rounded=0;fontSize=9;" value="&lt;h1 style=&quot;margin-top: 0px;&quot;&gt;&lt;font style=&quot;font-size: 20px;&quot;&gt;Sliding Windows&lt;/font&gt;&lt;/h1&gt;" vertex="1">
      <mxGeometry height="27" width="210" x="30" y="453" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-15" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;" value="&lt;font style=&quot;font-size: 15px;&quot;&gt;&lt;u&gt;Web Application Telemetry Steam&lt;/u&gt;&lt;/font&gt;" vertex="1">
      <mxGeometry height="30" width="190" x="21.25" y="70" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-16" parent="1" style="sketch=0;pointerEvents=1;shadow=0;dashed=0;html=1;strokeColor=none;fillColor=#000000;aspect=fixed;labelPosition=center;verticalLabelPosition=bottom;verticalAlign=top;align=center;outlineConnect=0;shape=mxgraph.vvd.mouse;" value="" vertex="1">
      <mxGeometry height="40" width="19.6" x="41.94" y="110" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-22" parent="1" style="sketch=0;pointerEvents=1;shadow=0;dashed=0;html=1;strokeColor=none;fillColor=#000000;aspect=fixed;labelPosition=center;verticalLabelPosition=bottom;verticalAlign=top;align=center;outlineConnect=0;shape=mxgraph.vvd.web_browser;" value="" vertex="1">
      <mxGeometry height="20" width="28.17" x="37.65" y="160" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-27" parent="1" style="verticalLabelPosition=bottom;shadow=0;dashed=0;align=center;html=1;verticalAlign=top;strokeWidth=1;shape=mxgraph.mockup.navigation.scrollBar;strokeColor=#000000;barPos=20;fillColor2=#000000;strokeColor2=none;direction=north;fillColor=none;" value="" vertex="1">
      <mxGeometry height="120" width="8.06" x="41.94" y="190" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-31" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;rounded=0;" value="&lt;font style=&quot;font-size: 15px;&quot;&gt;&lt;b&gt;Mouse Movement&lt;/b&gt;&lt;/font&gt;&lt;div&gt;&lt;font style=&quot;font-size: 15px;&quot;&gt;&lt;b&gt;Mouse Clicks&lt;/b&gt;&lt;/font&gt;&lt;/div&gt;&lt;div&gt;&lt;font style=&quot;font-size: 15px;&quot;&gt;&lt;b&gt;Scrolling Events&lt;/b&gt;&lt;/font&gt;&lt;/div&gt;&lt;div&gt;&lt;font style=&quot;font-size: 15px;&quot;&gt;&lt;b&gt;Keystrokes&lt;/b&gt;&lt;/font&gt;&lt;/div&gt;" vertex="1">
      <mxGeometry height="30" width="127.5" x="76.25" y="145" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-32" parent="1" style="rounded=1;whiteSpace=wrap;html=1;strokeColor=none;" value="" vertex="1">
      <mxGeometry height="40" width="120" x="76.25" y="210" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-33" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;" value="&lt;font style=&quot;font-size: 15px;&quot;&gt;&lt;b&gt;Initial State:&lt;/b&gt; Home Page&lt;/font&gt;" vertex="1">
      <mxGeometry height="30" width="100" x="86.25" y="215" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-34" parent="1" style="rounded=1;whiteSpace=wrap;html=1;strokeColor=none;" value="" vertex="1">
      <mxGeometry height="40" width="120" x="76.25" y="260" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-35" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;" value="&lt;font style=&quot;font-size: 15px;&quot;&gt;&lt;b&gt;Terminal State:&lt;/b&gt; Checkout Click&lt;/font&gt;" vertex="1">
      <mxGeometry height="30" width="118.75" x="77.5" y="265" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-36" edge="1" parent="1" source="xJ0yeJP-ojD9ltWxKH4l-5" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" target="xJ0yeJP-ojD9ltWxKH4l-6" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <mxPoint x="340" y="310" as="sourcePoint" />
        <mxPoint x="390" y="260" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-37" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;" value="&lt;font style=&quot;font-size: 20px;&quot;&gt;&lt;b style=&quot;&quot;&gt;Subsampling&lt;/b&gt;&amp;nbsp;&lt;/font&gt;&lt;div&gt;&lt;font style=&quot;font-size: 20px;&quot;&gt;(1/5 of mouse movement events)&lt;/font&gt;&lt;/div&gt;" vertex="1">
      <mxGeometry height="30" width="172.5" x="30" y="370" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-38" edge="1" parent="1" source="xJ0yeJP-ojD9ltWxKH4l-6" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <mxPoint x="420" y="440" as="sourcePoint" />
        <mxPoint x="115" y="450" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-39" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" value="" vertex="1">
      <mxGeometry height="20" width="70" x="30" y="510" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-41" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" value="" vertex="1">
      <mxGeometry height="20" width="70" x="61.54" y="540" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-42" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" value="" vertex="1">
      <mxGeometry height="20" width="70" x="92.5" y="570" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-43" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#bac8d3;strokeColor=#23445d;" value="" vertex="1">
      <mxGeometry height="20" width="70" x="130" y="600" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-46" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=15;" value="15 event stride" vertex="1">
      <mxGeometry height="30" width="62.82" x="27.18" y="590" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-47" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;" value="&lt;b&gt;&lt;font style=&quot;font-size: 15px;&quot;&gt;30 events each window, 50% overlap&lt;/font&gt;&lt;/b&gt;" vertex="1">
      <mxGeometry height="30" width="162.5" x="37.5" y="640" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-49" edge="1" parent="1" style="endArrow=classic;html=1;rounded=0;fillColor=#fad7ac;strokeColor=#b46504;exitX=0.75;exitY=0;exitDx=0;exitDy=0;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <mxPoint x="30" y="550.08" as="sourcePoint" />
        <mxPoint x="59" y="549.74" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-50" edge="1" parent="1" style="endArrow=classic;html=1;rounded=0;fillColor=#fad7ac;strokeColor=#b46504;exitX=0.75;exitY=0;exitDx=0;exitDy=0;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <mxPoint x="61.54" y="580.08" as="sourcePoint" />
        <mxPoint x="90.53999999999999" y="579.74" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-52" edge="1" parent="1" style="endArrow=classic;html=1;rounded=0;fillColor=#fad7ac;strokeColor=#b46504;exitX=0.75;exitY=0;exitDx=0;exitDy=0;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <mxPoint x="92.5" y="609.83" as="sourcePoint" />
        <mxPoint x="121.5" y="609.49" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-53" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#cce5ff;strokeColor=#36393d;" value="" vertex="1">
      <mxGeometry height="20" width="20" x="30" y="510" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-54" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#cce5ff;strokeColor=#36393d;" value="" vertex="1">
      <mxGeometry height="20" width="20" x="50" y="510" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-55" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#cce5ff;strokeColor=#36393d;" value="" vertex="1">
      <mxGeometry height="20" width="20" x="90" y="510" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-56" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#cce5ff;strokeColor=#36393d;" value="" vertex="1">
      <mxGeometry height="20" width="20" x="70" y="510" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-57" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" value="" vertex="1">
      <mxGeometry height="20" width="20" x="61.54" y="540" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-58" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" value="" vertex="1">
      <mxGeometry height="20" width="20" x="81.54" y="540" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-59" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" value="" vertex="1">
      <mxGeometry height="20" width="20" x="100" y="540" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-60" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" value="" vertex="1">
      <mxGeometry height="20" width="20" x="120" y="540" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-61" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" value="" vertex="1">
      <mxGeometry height="20" width="20" x="92.5" y="570" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-62" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" value="" vertex="1">
      <mxGeometry height="20" width="20" x="112.5" y="570" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-63" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" value="" vertex="1">
      <mxGeometry height="20" width="20" x="132.5" y="570" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-64" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" value="" vertex="1">
      <mxGeometry height="20" width="20" x="152.5" y="570" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-65" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#bac8d3;strokeColor=#23445d;" value="" vertex="1">
      <mxGeometry height="20" width="20" x="130" y="600" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-66" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#bac8d3;strokeColor=#23445d;" value="" vertex="1">
      <mxGeometry height="20" width="20" x="150" y="600" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-69" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#bac8d3;strokeColor=#23445d;" value="" vertex="1">
      <mxGeometry height="20" width="20" x="170" y="600" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-70" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#bac8d3;strokeColor=#23445d;" value="" vertex="1">
      <mxGeometry height="20" width="10" x="190" y="600" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-71" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;" value="&lt;font style=&quot;font-size: 15px;&quot;&gt;W&lt;sub style=&quot;&quot;&gt;1&lt;/sub&gt;&amp;nbsp;(30)&lt;/font&gt;" vertex="1">
      <mxGeometry height="30" width="60" x="120" y="505" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-72" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;" value="&lt;font style=&quot;font-size: 15px;&quot;&gt;W&lt;sub style=&quot;&quot;&gt;2&lt;/sub&gt;&amp;nbsp;(30)&lt;/font&gt;" vertex="1">
      <mxGeometry height="30" width="60" x="142.5" y="535" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-73" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#0E8088;strokeColor=#0e8088;" value="" vertex="1">
      <mxGeometry height="40" width="350" x="260" y="20" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-74" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#0E8088;strokeColor=#0e8088;" value="" vertex="1">
      <mxGeometry height="40" width="350" x="260" y="280" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-75" parent="1" style="text;html=1;whiteSpace=wrap;overflow=hidden;rounded=0;fontSize=9;fontColor=#FFFFFF;" value="&lt;h1 style=&quot;margin-top: 0px;&quot;&gt;&lt;font style=&quot;font-size: 20px;&quot;&gt;RL Decision Policy&lt;/font&gt;&lt;/h1&gt;" vertex="1">
      <mxGeometry height="27" width="210" x="275" y="23" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-76" parent="1" style="text;html=1;whiteSpace=wrap;overflow=hidden;rounded=0;fontSize=9;fontColor=#FFFFFF;" value="&lt;h1 style=&quot;margin-top: 0px;&quot;&gt;&lt;font style=&quot;font-size: 20px;&quot;&gt;26 Dimension Feature Vectors&lt;/font&gt;&lt;/h1&gt;" vertex="1">
      <mxGeometry height="27" width="305" x="275" y="283" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-77" edge="1" parent="1" source="xJ0yeJP-ojD9ltWxKH4l-7" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <mxPoint x="270" y="610" as="sourcePoint" />
        <mxPoint x="260" y="565" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-78" edge="1" parent="1" source="xJ0yeJP-ojD9ltWxKH4l-74" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" target="xJ0yeJP-ojD9ltWxKH4l-8" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <mxPoint x="270" y="330" as="sourcePoint" />
        <mxPoint x="320" y="280" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-79" edge="1" parent="1" source="xJ0yeJP-ojD9ltWxKH4l-9" style="endArrow=classic;html=1;rounded=0;exitX=0;exitY=0.25;exitDx=0;exitDy=0;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <mxPoint x="40" y="250" as="sourcePoint" />
        <mxPoint x="610" y="185" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-80" parent="1" style="text;html=1;whiteSpace=wrap;overflow=hidden;rounded=0;" value="&lt;h1 style=&quot;margin-top: 0px;&quot;&gt;Policy&amp;nbsp;π&lt;/h1&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;" vertex="1">
      <mxGeometry height="50" width="225" x="275" y="70" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-81" parent="1" style="rounded=1;whiteSpace=wrap;html=1;align=left;" value="&lt;font style=&quot;font-size: 18px;&quot;&gt;&amp;nbsp; State: 26 Dimension Feature Vectors&lt;/font&gt;" vertex="1">
      <mxGeometry height="25" width="315" x="275" y="115" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-82" parent="1" style="rounded=1;whiteSpace=wrap;html=1;align=left;" value="&lt;font style=&quot;font-size: 18px;&quot;&gt;&amp;nbsp; Action Space: 7 Discrete Actions&lt;/font&gt;" vertex="1">
      <mxGeometry height="25" width="315" x="275" y="150" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-83" parent="1" style="rounded=1;whiteSpace=wrap;html=1;align=left;" value="&lt;font style=&quot;font-size: 18px;&quot;&gt;&amp;nbsp; Invalid Action Masking&lt;/font&gt;" vertex="1">
      <mxGeometry height="25" width="315" x="275" y="185" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-84" parent="1" style="rounded=1;whiteSpace=wrap;html=1;align=left;" value="&lt;font style=&quot;font-size: 18px;&quot;&gt;&amp;nbsp; Confidence-based Decision&lt;/font&gt;" vertex="1">
      <mxGeometry height="25" width="315" x="275" y="217.5" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-85" parent="1" style="rounded=0;whiteSpace=wrap;html=1;" value="" vertex="1">
      <mxGeometry height="30" width="300" x="280" y="340" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-86" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fad7ac;strokeColor=#b46504;" value="" vertex="1">
      <mxGeometry height="90" width="20" x="280" y="340" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-87" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#bac8d3;strokeColor=#23445d;" value="" vertex="1">
      <mxGeometry height="90" width="20" x="300" y="340" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-88" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fad9d5;strokeColor=#ae4132;" value="" vertex="1">
      <mxGeometry height="90" width="20" x="320" y="340" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-89" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffcccc;strokeColor=#36393d;" value="" vertex="1">
      <mxGeometry height="90" width="20" x="340" y="340" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-90" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#cdeb8b;strokeColor=#36393d;" value="" vertex="1">
      <mxGeometry height="90" width="20" x="360" y="340" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-91" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffff88;strokeColor=#36393d;" value="" vertex="1">
      <mxGeometry height="90" width="20" x="380" y="340" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-92" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#cce5ff;strokeColor=#36393d;" value="" vertex="1">
      <mxGeometry height="90" width="20" x="400" y="340" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-93" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffcc99;strokeColor=#36393d;" value="" vertex="1">
      <mxGeometry height="90" width="20" x="420" y="340" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-94" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f9f7ed;strokeColor=#36393d;" value="" vertex="1">
      <mxGeometry height="90" width="20" x="440" y="340" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-95" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#eeeeee;strokeColor=#36393d;" value="" vertex="1">
      <mxGeometry height="90" width="20" x="460" y="340" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-96" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#bac8d3;strokeColor=#23445d;" value="" vertex="1">
      <mxGeometry height="90" width="20" x="480" y="340" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-97" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fad9d5;strokeColor=#ae4132;" value="" vertex="1">
      <mxGeometry height="90" width="20" x="500" y="340" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-98" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fad7ac;strokeColor=#b46504;" value="" vertex="1">
      <mxGeometry height="90" width="20" x="520" y="340" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-99" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d0cee2;strokeColor=#56517e;" value="" vertex="1">
      <mxGeometry height="90" width="20" x="540" y="340" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-100" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#b1ddf0;strokeColor=#10739e;" value="" vertex="1">
      <mxGeometry height="90" width="20" x="560" y="340" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-103" parent="1" style="strokeWidth=2;html=1;shape=mxgraph.flowchart.annotation_2;align=left;labelPosition=right;pointerEvents=1;rotation=-90;" value="" vertex="1">
      <mxGeometry height="70" width="40" x="300" y="430" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-104" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=15;" value="Features 0-7: Motor Dynamics" vertex="1">
      <mxGeometry height="30" width="60" x="290" y="517" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-105" parent="1" style="strokeWidth=2;html=1;shape=mxgraph.flowchart.annotation_2;align=left;labelPosition=right;pointerEvents=1;rotation=-90;" value="" vertex="1">
      <mxGeometry height="90" width="40" x="390" y="420" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-106" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=15;" value="Features 8-16: Temporal Dynamics" vertex="1">
      <mxGeometry height="30" width="80" x="370" y="517" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-107" parent="1" style="strokeWidth=2;html=1;shape=mxgraph.flowchart.annotation_2;align=left;labelPosition=right;pointerEvents=1;rotation=-90;" value="" vertex="1">
      <mxGeometry height="62.5" width="40" x="473.75" y="433.75" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-108" parent="1" style="strokeWidth=2;html=1;shape=mxgraph.flowchart.annotation_2;align=left;labelPosition=right;pointerEvents=1;rotation=-90;" value="" vertex="1">
      <mxGeometry height="42.5" width="40" x="537.5" y="443.75" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-109" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=15;" value="Features 17-22: Spatial Coverage" vertex="1">
      <mxGeometry height="30" width="76.25" x="455.62" y="517" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-110" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=15;" value="Features 23-25: Metadata" vertex="1">
      <mxGeometry height="47" width="35" x="550" y="500" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-112" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fontSize=11;align=center;" value="" vertex="1">
      <mxGeometry height="70" width="325" x="275" y="590" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-111" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=15;" value="The observation space is defined as a vector with each value bounded to [−10, 10] in ℝ²⁶" vertex="1">
      <mxGeometry height="30" width="317.5" x="280" y="620" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-116" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=15;" value="&lt;font&gt;&lt;b&gt;&lt;font&gt;&lt;font&gt;Statistics computed from raw events&amp;nbsp;&lt;/font&gt;&lt;/font&gt;&amp;nbsp;&lt;/b&gt;&lt;/font&gt;" vertex="1">
      <mxGeometry height="30" width="320" x="280" y="590" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-117" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#10739E;strokeColor=#10739e;align=left;" value="&lt;font style=&quot;color: rgb(255, 255, 255); font-size: 20px;&quot;&gt;&lt;b style=&quot;&quot;&gt;&amp;nbsp; &amp;nbsp;Actions and Rewards&lt;/b&gt;&lt;/font&gt;" vertex="1">
      <mxGeometry height="40" width="290" x="660" y="20" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-118" parent="1" style="rounded=0;whiteSpace=wrap;html=1;" value="" vertex="1">
      <mxGeometry height="250" width="250" x="680" y="80" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-119" parent="1" style="text;html=1;whiteSpace=wrap;overflow=hidden;rounded=0;" value="&lt;div style=&quot;line-height: 90%;&quot;&gt;&lt;h1 style=&quot;margin-top: 0px; line-height: 90%;&quot;&gt;&lt;span style=&quot;background-color: transparent; color: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));&quot;&gt;&lt;font style=&quot;font-size: 20px; line-height: 70%;&quot; face=&quot;Helvetica&quot;&gt;&lt;u&gt;Non Terminal Actions&lt;/u&gt;&lt;/font&gt;&lt;/span&gt;&lt;/h1&gt;&lt;p&gt;&lt;font style=&quot;font-size: 15px; line-height: 90%;&quot; face=&quot;Helvetica&quot;&gt;- Continue Observing&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font style=&quot;font-size: 15px; line-height: 90%;&quot; face=&quot;Helvetica&quot;&gt;- Deploy Honeypot&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;span style=&quot;background-color: transparent; color: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));&quot;&gt;&lt;font style=&quot;line-height: 90%; font-size: 20px;&quot; face=&quot;Helvetica&quot;&gt;&lt;b style=&quot;&quot;&gt;&lt;u&gt;Terminal Actions&lt;/u&gt;&lt;/b&gt;&lt;/font&gt;&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;span style=&quot;background-color: transparent; color: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));&quot;&gt;&lt;font style=&quot;font-size: 15px; line-height: 90%;&quot; face=&quot;Helvetica&quot;&gt;- Easy CAPTCHA (0.1 Cost)&lt;/font&gt;&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;span style=&quot;background-color: transparent; color: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));&quot;&gt;&lt;font style=&quot;font-size: 15px; line-height: 90%;&quot; face=&quot;Helvetica&quot;&gt;- Medium CAPTCHA (0.3 Cost)&lt;/font&gt;&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;span style=&quot;background-color: transparent; color: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));&quot;&gt;&lt;font style=&quot;font-size: 15px; line-height: 90%;&quot; face=&quot;Helvetica&quot;&gt;- Hard CAPTCHA (0.5 Cost)&lt;/font&gt;&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;span style=&quot;background-color: transparent; color: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));&quot;&gt;&lt;font style=&quot;font-size: 15px; line-height: 90%;&quot; face=&quot;Helvetica&quot;&gt;- Block User&lt;/font&gt;&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;font style=&quot;font-size: 15px; line-height: 90%;&quot; face=&quot;Helvetica&quot;&gt;- Allow User&lt;/font&gt;&lt;/p&gt;&lt;/div&gt;" vertex="1">
      <mxGeometry height="240" width="220" x="690" y="80" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-121" parent="1" style="rounded=0;whiteSpace=wrap;html=1;" value="" vertex="1">
      <mxGeometry height="190" width="250" x="680" y="340" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-122" parent="1" style="text;html=1;whiteSpace=wrap;overflow=hidden;rounded=0;fontSize=10;" value="&lt;h1 style=&quot;margin-top: 0px;&quot;&gt;Reward Function&lt;/h1&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;" vertex="1">
      <mxGeometry height="32" width="210" x="690" y="340" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-134" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fontSize=15;fillColor=#ffe6cc;strokeColor=#000000;" value="Outcome" vertex="1">
      <mxGeometry height="20" width="180" x="690" y="380" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-136" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#000000;" value="Reward" vertex="1">
      <mxGeometry height="20" width="50" x="870" y="380" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-137" parent="1" style="rounded=0;whiteSpace=wrap;html=1;" value="&lt;font style=&quot;font-size: 15px;&quot;&gt;Correct Block&lt;/font&gt;&amp;nbsp;" vertex="1">
      <mxGeometry height="20" width="180" x="690" y="400" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-138" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fontSize=15;" value="Correct Allow&amp;nbsp;" vertex="1">
      <mxGeometry height="20" width="180" x="690" y="420" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-139" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fontSize=15;" value="False Postive" vertex="1">
      <mxGeometry height="20" width="180" x="690" y="440" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-140" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fontSize=15;" value="False Negative" vertex="1">
      <mxGeometry height="20" width="180" x="690" y="460" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-141" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fontSize=15;" value="Honeypot Info Bonus" vertex="1">
      <mxGeometry height="20" width="180" x="690" y="480" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-142" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fontSize=15;" value="Continue (per window)" vertex="1">
      <mxGeometry height="20" width="180" x="690" y="500" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-144" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#000000;" value="+1.0" vertex="1">
      <mxGeometry height="20" width="50" x="870" y="400" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-145" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#000000;" value="+0.5" vertex="1">
      <mxGeometry height="20" width="50" x="870" y="420" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-146" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#000000;" value="-1.0" vertex="1">
      <mxGeometry height="20" width="50" x="870" y="440" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-147" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#000000;" value="-0.8" vertex="1">
      <mxGeometry height="20" width="50" x="870" y="460" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-148" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#000000;" value="+0.3" vertex="1">
      <mxGeometry height="20" width="50" x="870" y="480" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-149" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#000000;" value="-0.001" vertex="1">
      <mxGeometry height="20" width="50" x="870" y="500" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-151" parent="1" style="rounded=0;whiteSpace=wrap;html=1;" value="" vertex="1">
      <mxGeometry height="120" width="250" x="680" y="540" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-152" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=default;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=10;" value="&lt;font style=&quot;font-size: 14px;&quot;&gt;Easy CAPTCHA&amp;nbsp;- 95% Human, 40% Bot Pass Rates&lt;/font&gt;" vertex="1">
      <mxGeometry height="40" width="250" x="680" y="540" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-153" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=default;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=10;" value="&lt;font style=&quot;font-size: 15px;&quot;&gt;Med CAPTCHA - 85% Human, 15% Bot Pass Rates&lt;/font&gt;" vertex="1">
      <mxGeometry height="40" width="250" x="680" y="580" as="geometry" />
    </mxCell>
    <mxCell id="xJ0yeJP-ojD9ltWxKH4l-154" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=default;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=10;" value="&lt;font style=&quot;font-size: 15px;&quot;&gt;Hard CAPTCHA&amp;nbsp;- 70% Human, 5% Bot Pass Rates&lt;/font&gt;" vertex="1">
      <mxGeometry height="40" width="250" x="680" y="620" as="geometry" />
    </mxCell>
  </root>
</mxGraphModel>


## Example 2 — RL bot detection system (mixed layout with icons and decision flow)

<mxGraphModel dx="1042" dy="527" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="970" pageHeight="500" math="0" shadow="0">
  <root>
    <mxCell id="0" />
    <mxCell id="1" parent="0" />
    <mxCell id="AqnNnLGgXoHwOnxmoKHe-4" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" value="" vertex="1">
      <mxGeometry height="232.85" width="400" x="560" y="7.15" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-2" parent="1" style="verticalLabelPosition=bottom;shadow=0;dashed=0;align=center;html=1;verticalAlign=top;strokeWidth=1;shape=mxgraph.mockup.containers.userFemale;strokeColor2=#67AB9F;" value="" vertex="1">
      <mxGeometry height="120" width="120" x="10" y="20" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-3" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=20;" value="User (human or bot)" vertex="1">
      <mxGeometry height="30" width="190" y="210" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-4" edge="1" parent="1" style="endArrow=classic;html=1;rounded=0;exitX=1.005;exitY=0.51;exitDx=0;exitDy=0;exitPerimeter=0;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <mxPoint x="179.99999999999991" y="123.32999999999996" as="sourcePoint" />
        <mxPoint x="289.15" y="123.53" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-5" parent="1" style="points=[];aspect=fixed;html=1;align=center;shadow=0;dashed=0;shape=mxgraph.alibaba_cloud.domain_and_website;fillColor=#b0e3e6;strokeColor=#0e8088;" value="" vertex="1">
      <mxGeometry height="111.4" width="138.04" x="320" y="20" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-6" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=20;" value="Navigation Flow and Telemetry Stream&lt;div&gt;(Behavioral Signals)&lt;/div&gt;" vertex="1">
      <mxGeometry height="30" width="230" x="274.02" y="190" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-7" parent="1" style="sketch=0;pointerEvents=1;shadow=0;dashed=0;html=1;strokeColor=#0e8088;fillColor=#b0e3e6;aspect=fixed;labelPosition=center;verticalLabelPosition=bottom;verticalAlign=top;align=center;outlineConnect=0;shape=mxgraph.vvd.mouse;" value="" vertex="1">
      <mxGeometry height="50" width="24.5" x="310" y="110" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-9" edge="1" parent="1" style="endArrow=classic;html=1;rounded=0;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <mxPoint x="480" y="123.89" as="sourcePoint" />
        <mxPoint x="550" y="123.89" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-10" parent="1" style="shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;darkOpacity=0.05;size=25;" value="" vertex="1">
      <mxGeometry height="64.3" width="45" x="580" y="20.000000000000004" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-11" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=20;" value="JSON Logs" vertex="1">
      <mxGeometry height="30" width="110" x="640" y="40" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-12" parent="1" style="rounded=1;whiteSpace=wrap;html=1;" value="" vertex="1">
      <mxGeometry height="60" width="360" x="580" y="110" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-14" edge="1" parent="1" style="endArrow=none;html=1;rounded=0;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <Array as="points" />
        <mxPoint x="630" y="120" as="sourcePoint" />
        <mxPoint x="630" y="160" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-15" edge="1" parent="1" style="endArrow=none;html=1;rounded=0;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <Array as="points" />
        <mxPoint x="684.8100000000001" y="120" as="sourcePoint" />
        <mxPoint x="684.8100000000001" y="160" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-16" edge="1" parent="1" style="endArrow=none;html=1;rounded=0;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <Array as="points" />
        <mxPoint x="740" y="120" as="sourcePoint" />
        <mxPoint x="740" y="160" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-17" edge="1" parent="1" style="endArrow=none;html=1;rounded=0;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <Array as="points" />
        <mxPoint x="790" y="120" as="sourcePoint" />
        <mxPoint x="790" y="160" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-18" edge="1" parent="1" style="endArrow=none;html=1;rounded=0;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <Array as="points" />
        <mxPoint x="580" y="120" as="sourcePoint" />
        <mxPoint x="580" y="160" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-19" edge="1" parent="1" style="endArrow=none;html=1;rounded=0;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <Array as="points" />
        <mxPoint x="840" y="120" as="sourcePoint" />
        <mxPoint x="840" y="160" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-20" edge="1" parent="1" style="endArrow=none;html=1;rounded=0;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <Array as="points" />
        <mxPoint x="890" y="120" as="sourcePoint" />
        <mxPoint x="890" y="160" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-21" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=20;" value="W&lt;span style=&quot;font-size: 16.6667px;&quot;&gt;&lt;sub&gt;1&lt;/sub&gt;&lt;/span&gt;" vertex="1">
      <mxGeometry height="30" width="110" x="550" y="125" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-22" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=20;" value="W&lt;span style=&quot;font-size: 16.6667px;&quot;&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/span&gt;" vertex="1">
      <mxGeometry height="30" width="110" x="600" y="125" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-23" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=20;" value="W&lt;sub&gt;3&lt;/sub&gt;" vertex="1">
      <mxGeometry height="30" width="110" x="660" y="125" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-24" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=20;" value="W&lt;sub&gt;4&lt;/sub&gt;" vertex="1">
      <mxGeometry height="30" width="110" x="710" y="125" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-25" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=20;" value="W&lt;span style=&quot;font-size: 16.6667px;&quot;&gt;&lt;sub&gt;T&lt;/sub&gt;&lt;/span&gt;" vertex="1">
      <mxGeometry height="30" width="110" x="810" y="125" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-27" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=20;" value="W&lt;sub&gt;n&lt;/sub&gt;" vertex="1">
      <mxGeometry height="30" width="110" x="860" y="125" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-28" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=default;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=20;" value="Telemetry&amp;nbsp;&lt;div&gt;Windows&lt;/div&gt;" vertex="1">
      <mxGeometry height="50" width="110" x="580" y="180" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-31" parent="1" style="strokeWidth=2;html=1;shape=mxgraph.flowchart.annotation_2;align=left;labelPosition=right;pointerEvents=1;direction=north;" value="" vertex="1">
      <mxGeometry height="35" width="160" x="710" y="160" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-32" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=20;" value="Non-Terminal Windows" vertex="1">
      <mxGeometry height="30" width="210" x="710" y="195" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-34" edge="1" parent="1" source="7vmrfwgSSJ4PBpgQQonu-12" style="endArrow=classic;html=1;rounded=0;edgeStyle=orthogonalEdgeStyle;exitX=0.933;exitY=-0.053;exitDx=0;exitDy=0;exitPerimeter=0;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <mxPoint x="840" y="90" as="sourcePoint" />
        <mxPoint x="860" y="80" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-35" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=20;" value="Terminal Window" vertex="1">
      <mxGeometry height="30" width="120" x="800" y="37.15" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-37" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#b0e3e6;strokeColor=#0e8088;" value="" vertex="1">
      <mxGeometry height="205" width="120" x="180" y="285" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-38" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=20;" value="RL Agent" vertex="1">
      <mxGeometry height="30" width="120" x="180" y="297.15" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-42" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=15;strokeWidth=0;" value="&lt;font&gt;&amp;nbsp;Policy:&amp;nbsp;&lt;span class=&quot;katex&quot; style=&quot;&quot;&gt;&lt;span class=&quot;katex-mathml&quot;&gt;&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mrow&gt;&lt;mi&gt;π&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;/msub&gt;&lt;mo&gt;∣&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;h&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;/msub&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/mrow&gt;&lt;/math&gt;&lt;/span&gt;&lt;span class=&quot;katex-html&quot; aria-hidden=&quot;true&quot;&gt;&lt;span class=&quot;base&quot;&gt;&lt;span class=&quot;mord&quot;&gt;&lt;span class=&quot;msupsub&quot;&gt;&lt;span class=&quot;vlist-t vlist-t2&quot;&gt;&lt;span class=&quot;vlist-r&quot;&gt;&lt;span class=&quot;vlist-s&quot;&gt;​&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;, where the agent selects action&amp;nbsp;&lt;span class=&quot;katex&quot; style=&quot;&quot;&gt;&lt;span class=&quot;katex-mathml&quot;&gt;&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mrow&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;/msub&gt;&lt;/mrow&gt;&lt;/math&gt;&lt;/span&gt;&lt;/span&gt;&amp;nbsp;at time&amp;nbsp;&lt;span class=&quot;katex&quot; style=&quot;&quot;&gt;&lt;span class=&quot;katex-mathml&quot;&gt;&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mrow&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;/mrow&gt;&lt;/math&gt;&lt;/span&gt;&lt;/span&gt;&amp;nbsp;based on the history of events so far&amp;nbsp;&lt;/font&gt;&lt;span class=&quot;katex&quot; style=&quot;&quot;&gt;&lt;span class=&quot;katex-mathml&quot; style=&quot;&quot;&gt;&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mrow&gt;&lt;msub&gt;&lt;/msub&gt;&lt;/mrow&gt;&lt;/math&gt;&lt;div&gt;&lt;br&gt;&lt;/div&gt;&lt;/span&gt;&lt;/span&gt;&lt;span style=&quot;font-size: 12px;&quot;&gt;&lt;/span&gt;" vertex="1">
      <mxGeometry height="30" width="120" x="180" y="400" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-44" parent="1" style="rhombus;whiteSpace=wrap;html=1;" value="&lt;font style=&quot;font-size: 20px;&quot;&gt;Is checkout reached?&lt;/font&gt;" vertex="1">
      <mxGeometry height="140" width="140" x="334.5" y="310" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-45" edge="1" parent="1" style="endArrow=classic;html=1;rounded=0;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <mxPoint x="300" y="380" as="sourcePoint" />
        <mxPoint x="330" y="380" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-46" edge="1" parent="1" source="7vmrfwgSSJ4PBpgQQonu-44" style="endArrow=classic;html=1;rounded=0;edgeStyle=orthogonalEdgeStyle;entryX=0.603;entryY=0.01;entryDx=0;entryDy=0;entryPerimeter=0;exitX=0.825;exitY=0.305;exitDx=0;exitDy=0;exitPerimeter=0;" target="7vmrfwgSSJ4PBpgQQonu-89" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <Array as="points">
          <mxPoint x="450" y="270" />
          <mxPoint x="861" y="270" />
        </Array>
        <mxPoint x="450" y="340" as="sourcePoint" />
        <mxPoint x="860" y="290" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-47" edge="1" parent="1" source="7vmrfwgSSJ4PBpgQQonu-44" style="endArrow=classic;html=1;rounded=0;edgeStyle=orthogonalEdgeStyle;exitX=0.833;exitY=0.694;exitDx=0;exitDy=0;exitPerimeter=0;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <Array as="points">
          <mxPoint x="451" y="480" />
        </Array>
        <mxPoint x="450" y="420" as="sourcePoint" />
        <mxPoint x="500" y="480" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-49" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=20;" value="Yes" vertex="1">
      <mxGeometry height="30" width="120" x="354.5" y="280" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-50" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=20;" value="No" vertex="1">
      <mxGeometry height="30" width="120" x="370" y="455" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-59" parent="1" style="shape=image;html=1;verticalAlign=top;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;imageAspect=0;aspect=fixed;image=https://icons.diagrams.net/icon-cache1/Tweet_Scotty-2186/twitterbot-561.png;imageBackground=default;imageBorder=default;" value="" vertex="1">
      <mxGeometry height="95.5" width="95.5" x="70" y="107.25" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-60" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#b0e3e6;strokeColor=#0e8088;" value="" vertex="1">
      <mxGeometry height="21.25" width="17.25" x="109.13" y="148.75" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-61" parent="1" style="rounded=1;whiteSpace=wrap;html=1;" value="" vertex="1">
      <mxGeometry height="220" width="200" x="510" y="280" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-63" parent="1" style="text;html=1;whiteSpace=wrap;overflow=hidden;rounded=0;" value="&lt;h1 style=&quot;margin-top: 0px;&quot;&gt;Non-Terminal State&lt;br&gt;&lt;/h1&gt;&lt;div&gt;&lt;br&gt;&lt;/div&gt;" vertex="1">
      <mxGeometry height="120" width="180" x="520" y="288.75" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-64" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#b0e3e6;strokeColor=#0e8088;" value="" vertex="1">
      <mxGeometry height="40" width="180" x="520" y="360" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-65" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;" value="&lt;font style=&quot;font-size: 15px;&quot;&gt;Action: Continue Observing (W&lt;sub style=&quot;&quot;&gt;T+1&lt;/sub&gt;)&lt;/font&gt;" vertex="1">
      <mxGeometry height="30" width="150" x="530" y="365" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-66" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#b0e3e6;strokeColor=#0e8088;" value="" vertex="1">
      <mxGeometry height="40" width="180" x="520" y="408.75" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-67" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=15;" value="Action: Deploy Honeypot" vertex="1">
      <mxGeometry height="30" width="150" x="530" y="413.75" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-69" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=20;" value="..." vertex="1">
      <mxGeometry height="30" width="110" x="760" y="120" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-74" parent="1" style="fillColor=none;strokeColor=none;html=1;fontSize=11;fontStyle=0;align=left;fontColor=#596780;fontStyle=1;fontSize=11" value="Company Fax" vertex="1">
      <mxGeometry height="20" width="150" x="520" y="450" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-75" parent="1" style="rounded=1;arcSize=9;align=left;spacingLeft=5;strokeColor=#FFAB00;html=1;strokeWidth=2;fontSize=12" value="1234" vertex="1">
      <mxGeometry height="15" width="150" x="530" y="470" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-76" parent="7vmrfwgSSJ4PBpgQQonu-75" style="shape=mxgraph.azure.azure_alert;fillColor=#FFAB00;strokeColor=none;html=1;sketch=0;" value="" vertex="1">
      <mxGeometry height="9.5" relative="1" width="9" x="1" y="0.5" as="geometry">
        <mxPoint x="-20" y="-5" as="offset" />
      </mxGeometry>
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-79" edge="1" parent="1" source="7vmrfwgSSJ4PBpgQQonu-67" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.75;exitDx=0;exitDy=0;startSize=6;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <mxPoint x="570" y="410" as="sourcePoint" />
        <mxPoint x="680" y="468" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-89" parent="1" style="rounded=1;whiteSpace=wrap;html=1;" value="" vertex="1">
      <mxGeometry height="220" width="200" x="740" y="280" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-90" parent="1" style="text;html=1;whiteSpace=wrap;overflow=hidden;rounded=0;" value="&lt;h1 style=&quot;margin-top: 0px;&quot;&gt;Terminal State&lt;/h1&gt;" vertex="1">
      <mxGeometry height="120" width="180" x="750" y="288.75" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-93" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#b0e3e6;strokeColor=#0e8088;" value="&lt;font style=&quot;font-size: 15px;&quot;&gt;Action: CAPTCHA (Easy, Medium, Hard)&lt;/font&gt;" vertex="1">
      <mxGeometry height="42.5" width="180" x="750" y="337.5" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-99" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#b0e3e6;strokeColor=#0e8088;" value="&lt;font style=&quot;font-size: 15px;&quot;&gt;Action: Block&lt;/font&gt;" vertex="1">
      <mxGeometry height="40" width="180" x="750" y="390" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-100" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#b0e3e6;strokeColor=#0e8088;" value="&lt;font style=&quot;font-size: 15px;&quot;&gt;Action: Allow&lt;/font&gt;" vertex="1">
      <mxGeometry height="40" width="180" x="750" y="437.5" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-101" edge="1" parent="1" source="AqnNnLGgXoHwOnxmoKHe-4" style="endArrow=classic;html=1;rounded=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;edgeStyle=orthogonalEdgeStyle;exitX=0.188;exitY=1.013;exitDx=0;exitDy=0;exitPerimeter=0;" target="7vmrfwgSSJ4PBpgQQonu-37" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <Array as="points">
          <mxPoint x="635" y="260" />
          <mxPoint x="240" y="260" />
        </Array>
        <mxPoint x="635" y="250" as="sourcePoint" />
        <mxPoint x="470" y="330" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-102" edge="1" parent="1" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <mxPoint x="84.52" y="240" as="sourcePoint" />
        <mxPoint x="85" y="310" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-104" parent="1" style="rounded=0;whiteSpace=wrap;html=1;" value="" vertex="1">
      <mxGeometry height="122.85" width="140" x="20" y="327.15" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-105" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;" value="&lt;font style=&quot;font-size: 20px;&quot;&gt;True User Type&amp;nbsp;&lt;/font&gt;&lt;div&gt;&lt;br&gt;&lt;/div&gt;" vertex="1">
      <mxGeometry height="30" width="140" x="20" y="350" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-106" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontSize=20;" value="[Not Directly Observable]" vertex="1">
      <mxGeometry height="30" width="130" x="25" y="400" as="geometry" />
    </mxCell>
    <mxCell id="7vmrfwgSSJ4PBpgQQonu-107" edge="1" parent="1" source="7vmrfwgSSJ4PBpgQQonu-104" style="endArrow=classic;html=1;rounded=0;edgeStyle=orthogonalEdgeStyle;exitX=0.427;exitY=1.022;exitDx=0;exitDy=0;exitPerimeter=0;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <Array as="points">
          <mxPoint x="80" y="470" />
          <mxPoint x="170" y="470" />
        </Array>
        <mxPoint x="80" y="457.15" as="sourcePoint" />
        <mxPoint x="170" y="471" as="targetPoint" />
      </mxGeometry>
    </mxCell>
    <mxCell id="AqnNnLGgXoHwOnxmoKHe-5" edge="1" parent="1" style="endArrow=classic;html=1;rounded=0;entryX=2.872;entryY=0.486;entryDx=0;entryDy=0;entryPerimeter=0;" value="">
      <mxGeometry height="50" relative="1" width="50" as="geometry">
        <Array as="points">
          <mxPoint x="798" y="56.96" />
        </Array>
        <mxPoint x="760" y="57.11000000000001" as="sourcePoint" />
        <mxPoint x="797.76" y="94.4399999999999" as="targetPoint" />
      </mxGeometry>
    </mxCell>
  </root>
</mxGraphModel>
"""