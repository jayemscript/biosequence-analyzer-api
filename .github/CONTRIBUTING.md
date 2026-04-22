# Contributing to Biosequence Analyzer API

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/jayemscript/biosequence-analyzer-api.git`
3. Create a virtual environment: `python -m venv .venv`
4. Activate it:
   - Windows: `.\.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`

## Development Workflow

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes
3. Run tests: `pytest tests/`
4. Run linting: `flake8 app` and `black app`
5. Commit: `git commit -am 'Add your feature'`
6. Push: `git push origin feature/your-feature`
7. Create a Pull Request

## Code Standards

- Use **Black** for code formatting
- Use **isort** for import sorting
- Use **flake8** for linting
- Write tests for all new features
- Maintain test coverage above 80%

## Running Tests

```bash
pytest tests/ -v --cov=app