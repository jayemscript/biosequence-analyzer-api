# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in the Biosequence Analyzer API, please **DO NOT** create a public GitHub issue. Instead, please report it to us by emailing:

**johnmarkpulmano.dev@gmail.com**

Please include:

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

We will acknowledge receipt within 48 hours and work with you to resolve the issue responsibly.

## Security Guidelines

### For Users

- **Keep dependencies updated**: Run `pip install --upgrade -r requirements.txt` regularly
- **Use environment variables**: Store sensitive data (API keys, database credentials) in `.env` files
- **Validate input**: Always validate user-provided DNA sequences
- **Use HTTPS**: When deploying to production, ensure all connections use HTTPS
- **Restrict access**: Limit API access to authenticated users only

### For Developers

- Run security checks before committing:
  ```bash
  bandit -r app
  safety check
  ```
