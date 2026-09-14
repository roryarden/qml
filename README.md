Resources and materials for quantum machine learning research.

## Prerequisites

Python dependencies are managed by [uv](https://docs.astral.sh/uv/):

```sh
uv sync
```

Adding papers to the library with `scripts/sync_library.py` converts arXiv HTML
to Markdown using **pandoc**. Install the system tools with Homebrew:

```sh
brew bundle      # installs uv + pandoc from the Brewfile
```
