cd private-gpt-9-oct
 python --version 3.11
 python -m venv mvenv
 activate
curl -sSL https://install.python-poetry.org | python3 -
poetry install --extras "ui embeddings-huggingface llms-llama-cpp vector-stores-qdrant"
CMAKE_ARGS='-DLLAMA_CUBLAS=on' poetry run pip install --force-reinstall --no-cache-dir llama-cpp-python
poetry run python scripts/setup
make run