# AGENTS.md

## Project Overview

`django-rest-framework-gis` adds GIS fields, serializers, filters, pagination, and schema helpers to Django REST Framework.

Core code lives in `rest_framework_gis/`:

- `fields.py`, `serializers.py`, `filters.py`, `filterset.py`, `pagination.py`, `schema.py`, and `tilenames.py` implement GIS API helpers.
- Tests live in `tests/`.

## Source of Truth

- Use `README.rst`, `CHANGES.rst`, and `performance_tests.rst` for setup, package usage, and performance context.
- Use `.github/workflows/ci.yml` and `tox.ini` for CI-tested dependencies, QA/test commands, env vars, and supported Python/Django/DRF versions.
- Use GitHub issue/PR templates when asked to open issues or PRs.

If instructions conflict, repository config and CI workflows win first, docs next, and this file is supplemental.

## Development Notes

- Keep changes focused. Avoid unrelated refactors and formatting churn.
- Preserve public APIs, serializer output formats, GeoJSON compatibility, filter semantics, and pagination behavior unless explicitly required.
- Avoid unnecessary blank lines inside function and method bodies.
- Update docs when behavior, settings, public APIs, setup steps, or supported versions change.

## Testing and QA

- Add or update tests for every behavior change.
- For bug fixes, write the regression test first, run it against the unfixed code, confirm it fails for the expected reason, then implement the fix.
- Use targeted tests while iterating, then run the documented full test command before considering the change complete.
- Run `openwisp-qa-format` after editing when available.
- Run `./run-qa-checks` when present. Treat failures as blocking unless confirmed unrelated and reported.
- Prefer in-process tests so coverage tools can measure changed code.

## Security and API Notes

- Watch for invalid geometry handling, excessive query costs, unsafe user-controlled filters, and compatibility regressions across Django, DRF, GEOS, and GDAL.
- Preserve validation around GeoJSON, bounding boxes, distance filters, tile names, pagination links, and schema output.
- Write comments and docstrings only when they explain why code is shaped a certain way. Put comments before the relevant code block instead of scattering them inside it.

## Troubleshooting

- If setup, QA, or tests fail, check docs first, then compare with CI. If commands diverge, follow CI.
