# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an experimental/learning repository for working with the Anthropic Claude API. It contains simple Python scripts and Jupyter notebooks to test API interactions.

## Environment Setup

This project requires an Anthropic API key stored in a `.env` file:
```
ANTHROPIC_API_KEY=your_api_key_here
```

The `.env` file is gitignored and should never be committed.

## Development Commands

**Initial Setup:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

**Running the Code:**
```bash
# Run the test script
python test_claude.py

# Run Jupyter notebook
jupyter notebook 001_requests.ipynb
```

## Project Structure

- `test_claude.py` - Simple Python script demonstrating basic API calls to Claude
- `001_requests.ipynb` - Jupyter notebook with interactive API examples
- `requirements.txt` - Python dependencies (anthropic, python-dotenv)
- `.env` - API credentials (gitignored)
- `venv/` - Python virtual environment (gitignored)

## Dependencies

- `anthropic` - Official Anthropic Python SDK
- `python-dotenv` - For loading environment variables from .env file
