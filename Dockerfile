FROM python:3.12.5-slim as build
RUN pip install poetry==1.8.3
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
COPY poetry.lock pyproject.toml README.md /app/
COPY devops_tech_interviews /app/devops_tech_interview
WORKDIR /app
RUN poetry install --only main
RUN poetry build
RUN poetry run pip install dist/*.whl
FROM python:3.12.5-slim as runtime
ENV PATH="/app/.venv/bin:$PATH"
COPY --from=build /app/.venv /app/.venv
WORKDIR /
ENTRYPOINT ["/bin/bash", "-c"]
CMD ["python -m devops_tech_interview.server"]
