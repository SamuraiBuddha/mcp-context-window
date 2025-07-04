# Security Policy

## Overview

The mcp-context-window project implements a Model Context Protocol (MCP) server for tracking remaining token counts in Claude conversations. This document outlines security measures, vulnerability reporting procedures, and best practices for safe deployment.

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| main    | :white_check_mark: |

## Reporting Security Vulnerabilities

**DO NOT** create public GitHub issues for security vulnerabilities.

Instead, please report security vulnerabilities to:
- **Email**: [Your security contact email]
- **Private GitHub Security Advisory**: Use GitHub's private vulnerability reporting feature

### What to Include in Reports
- Description of the vulnerability
- Steps to reproduce the issue
- Potential impact assessment
- Suggested mitigation (if known)

## Security Considerations

### MCP Server Security
- **Port Binding**: MCP server should only bind to localhost/127.0.0.1
- **Authentication**: Implement proper authentication for multi-user environments
- **Input Validation**: All HTTP requests and MCP messages are validated
- **Resource Limits**: Implement rate limiting and resource constraints

### Python Environment Security
- **Dependencies**: Regularly update Python dependencies using `pip audit`
- **Virtual Environment**: Always run in isolated virtual environment
- **Permissions**: Run with minimal required system permissions
- **Logging**: Avoid logging sensitive information (tokens, auth data)

### Data Protection
- **Token Data**: Never log or persist actual conversation tokens
- **Memory Management**: Clear sensitive data from memory after use
- **File Permissions**: Ensure log files have restricted permissions
- **Network Security**: Use HTTPS for any external communications

### Deployment Security Checklist

#### Local Development
- [ ] Use virtual environment (venv/conda)
- [ ] Keep dependencies updated
- [ ] Review .gitignore for sensitive files
- [ ] Never commit credentials or tokens

#### Production Deployment
- [ ] Run as non-root user
- [ ] Implement proper logging (without sensitive data)
- [ ] Set up monitoring and alerting
- [ ] Regular security updates
- [ ] Network isolation (firewall rules)
- [ ] Backup and recovery procedures

## Known Security Considerations

### Context Window Tracking
- **Privacy**: This tool tracks token usage patterns - ensure compliance with privacy policies
- **Data Retention**: Token count data should have defined retention periods
- **Access Control**: Restrict access to token usage analytics

### MCP Protocol Security
- **Transport Security**: MCP protocol should use secure transport (stdio/SSH)
- **Message Validation**: All MCP messages are validated against schema
- **Error Handling**: Errors should not leak system information

## Incident Response

### Response Timeline
- **Acknowledgment**: Within 24 hours of report
- **Initial Assessment**: Within 72 hours
- **Fix Development**: Varies by severity
- **Public Disclosure**: After fix deployment (coordinated disclosure)

### Severity Classification
- **Critical**: Remote code execution, privilege escalation
- **High**: Information disclosure, authentication bypass
- **Medium**: Denial of service, input validation issues
- **Low**: Minor information leaks, configuration issues

## Security Updates

Security updates will be published through:
- GitHub Releases with security advisory
- Commit messages tagged with "Security:"
- Documentation updates in this file

## Compliance

This project follows:
- OWASP Top 10 security guidelines
- Python security best practices
- MCP protocol security recommendations
- Secure coding standards for AI tools

## Contact

For security-related questions or concerns:
- Create a private security advisory on GitHub
- Review our public security documentation
- Follow responsible disclosure practices

---

**Note**: This security policy is part of the MAGI infrastructure security initiative and follows established security templates for MCP tools.

Last Updated: July 2025