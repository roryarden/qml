Resources and materials for quantum machine learning research.

## Prerequisites

Python dependencies are managed by [uv](https://docs.astral.sh/uv/) (`uv sync`).
In addition, PDF conversion (via [marker-pdf](https://github.com/datalab-to/marker))
needs a **system-level inference server** to run its VLM. The backend differs by
platform:

### macOS (CPU / Apple Silicon)

marker runs the VLM through **llama.cpp**, which provides the `llama-server`
binary. Install the system dependencies with Homebrew:

```sh
brew bundle      # installs uv + llama.cpp from the Brewfile
uv sync          # installs Python dependencies
```

### PC with NVIDIA GPU (Windows / Linux)

marker runs the VLM through **vLLM**, served in a container. Install:

- [Docker](https://docs.docker.com/get-docker/)
- [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

Then install the Python dependencies:

```sh
uv sync
```

marker auto-spawns the correct inference server on first use and downloads model
weights (a one-time cost). On the GPU machine, conversions run in `balanced`
mode automatically; on macOS they fall back to `fast` mode.

### Running the converter

```sh
uv run scripts/convert_pdfs.py          # convert new/changed PDFs
uv run scripts/convert_pdfs.py --force  # reconvert everything
```
