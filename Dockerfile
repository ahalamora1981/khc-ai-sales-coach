FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# Copy dependency files first for better caching
COPY pyproject.toml uv.lock ./

# Copy application code and data
COPY .streamlit/ .streamlit/
COPY data/ data/
COPY sample-menus/ sample-menus/
COPY app.py main.py ./

# Install production dependencies
RUN uv sync --frozen --no-dev

# Expose Streamlit default port
EXPOSE 8501

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \
    CMD uv run python -c "import urllib.request; urllib.request.urlopen('http://localhost:8501/ai-sales-coach/_stcore/health')" || exit 1

CMD ["uv", "run", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
