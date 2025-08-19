# Security Guidelines for Current of Thoughts

## 🔒 API Key and Secret Management

This document outlines security best practices for maintaining the Current of Thoughts repository.

### ✅ Current Security Status
- **No hardcoded API keys found** - Repository is clean ✅
- Security scanning workflow implemented
- Git hooks for secret detection available

### 🚫 What NOT to Commit

**Never commit these types of sensitive data:**
- API keys (`API_KEY=abc123...`)
- Secret keys (`SECRET_KEY=xyz789...`)
- Database passwords
- Private keys (SSH, TLS, etc.)
- Access tokens
- Authentication credentials
- Connection strings with embedded passwords

### ✅ Security Best Practices

#### 1. Use Environment Variables
```bash
# ❌ Don't do this in code:
API_KEY = "sk-1234567890abcdef"

# ✅ Do this instead:
API_KEY = os.getenv('API_KEY')
```

#### 2. Use .env Files (Locally Only)
- Copy `.env.example` to `.env`
- Add your actual values to `.env`
- **Never commit `.env` files** (they're gitignored)

#### 3. Use GitHub Secrets for CI/CD
For GitHub Actions workflows:
1. Go to repository Settings → Secrets and variables → Actions
2. Add secrets there
3. Reference them as `${{ secrets.SECRET_NAME }}`

#### 4. Regular Security Scanning
- The repository now includes automated secret scanning
- Gitleaks runs on every push and pull request
- Review and fix any alerts promptly

### 🛠️ Tools and Workflows

#### Automated Security Scanning
- **Gitleaks**: Scans for secrets in code and git history
- **GitHub Security Advisories**: Monitors for vulnerable dependencies
- **GitHub Secret Scanning**: Platform-level secret detection

#### Manual Security Checks
```bash
# Install gitleaks locally for manual scanning
brew install gitleaks  # macOS
# or download from https://github.com/gitleaks/gitleaks/releases

# Run local scan
gitleaks detect --source . --verbose
```

### 🚨 If You Accidentally Commit a Secret

1. **Immediately revoke/regenerate** the compromised secret
2. **Remove from git history** (if recently committed):
   ```bash
   git reset --soft HEAD~1  # Remove last commit
   git reset HEAD .         # Unstage files
   # Edit files to remove secret
   git add .
   git commit -m "Remove sensitive data"
   ```
3. **For older commits**, use tools like `git-filter-repo` or contact repository admins

### 📚 Additional Resources

- [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-scanning)
- [Gitleaks Documentation](https://github.com/gitleaks/gitleaks)
- [OWASP API Security](https://owasp.org/www-project-api-security/)
- [Git Secrets](https://github.com/awslabs/git-secrets)

### 💡 Hugo-Specific Security

Since this is a Hugo static site:
- Most secrets would be for external integrations (analytics, comments, etc.)
- Use Hugo's environment functions: `{{ getenv "API_KEY" }}`
- Consider using Hugo modules for third-party integrations
- Be careful with JavaScript that might expose API endpoints

---

**Remember**: Security is everyone's responsibility. When in doubt, ask!