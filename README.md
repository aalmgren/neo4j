# Geological Workflow Visualizations

Interactive D3.js visualizations for mineral deposit inference and estimation workflows.

## Visualizations

### 1. Heuristic Reasoning Simulation
**File:** `simple_growth.html`

Simulates the mental shortcuts that an experienced geologist uses to infer mineral deposit characteristics from assay data. Features:

- Progressive animation showing reasoning flow
- Score-based node and link coloring
- Action nodes for automated workflow steps
- Fading of lower-probability paths
- Interactive tooltips with detailed explanations

### 2. Neo4j Graph Explorer
**File:** `neo4j_graphs.html`

Interactive exploration of geological workflow graphs with hierarchical structure. Features:

- Multi-level hierarchical graph visualization
- Color coding by category or level
- Interactive node dragging and zooming
- Dynamic legend
- Tooltips with node information

## Usage

### Local Development

1. Start a local server:
```bash
python serve_local.py
```

2. Open in browser:
- Main page: `http://localhost:8000/index.html`
- Heuristic Reasoning: `http://localhost:8000/simple_growth.html`
- Neo4j Graph Explorer: `http://localhost:8000/neo4j_graphs.html`

### GitHub Pages

The visualizations are available at:
- Main page: `https://[your-username].github.io/[repo-name]/index.html`
- Or simply: `https://[your-username].github.io/[repo-name]/`

## Files

- `index.html` - Main landing page with tab navigation
- `simple_growth.html` - Heuristic reasoning visualization
- `neo4j_graphs.html` - Neo4j graph explorer
- `simple_growth_graph.json` - Data for heuristic reasoning workflow
- `estimation_workflow_structured.json` - Data for Neo4j graph explorer

## Technologies

- D3.js v7
- HTML5/CSS3
- JavaScript (ES6+)

## License

MIT License
