"""
ClaudeCode - AI-Powered PR Security Audit Tool

A standalone security audit tool that uses Claude Code for comprehensive
security analysis of GitHub pull requests.
"""

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

__version__ = "1.0.0"
__author__ = "Anthropic Security Team"

# Import main components for easier access
from claudecode.github_action_audit import (
    GitHubActionClient,
    SimpleClaudeRunner,
    main
)

__all__ = [
    "GitHubActionClient",
    "SimpleClaudeRunner",
    "main"
]