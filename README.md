# comfy‑api‑nodes

Official **API Nodes** for **ComfyUI**.

> This is a Python package of nodes, **not** ComfyUI itself.

---

## Install & Update

**Most users:** no action needed. 

Recent ComfyUI builds ensure `comfy-core==<your ComfyUI version>` is installed and then upgrade **comfy‑api‑nodes** to the latest compatible release on startup.

**Manual install/update:**

```bash
python -m pip install -U comfy-api-nodes
```

**Pin a specific version:**

```bash
python -m pip install "comfy-api-nodes==X.Y.Z"
```

> You can disable loading API nodes in ComfyUI with `--disable-api-nodes`.

TODO: flag in ComfyUI to skip autoupdate of api-nodes to allow pinning old versions

---

## Compatibility model

This package declares a dependency on **`comfy-core`** using a version **range** (e.g. `>=0.3.60,<0.4.0`).
On startup, ComfyUI installs `comfy-core` that matches its own version; **pip** or **uv** then resolves the **newest compatible** `comfy‑api‑nodes` automatically.
