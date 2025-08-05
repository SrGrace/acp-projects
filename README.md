# acp-projects
Projects repo for ACP (Agent Communication Protocol)

---
## Setup

**Prerequisite:** Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/) (a fast Python package manager).

### 1. Clone the Repository
```bash
git clone https://github.com/SrGrace/acp-projects.git
```

### 2. Install Dependencies

**Sync dependencies from pyproject.toml and uv.lock**

```bash
uv sync
```

### 3. Run the server:

```bash
uv run <project_folder>agent.py
```

The server will be available at:  
`http://localhost:8000`

### 4. Run the client:

```bash
uv run <project_folder>client.py
```

---

## License

This project is licensed under the terms of the [MIT License](./LICENSE).
