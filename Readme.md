# 🎬 Clooney - Web App Cloning Agent

An autonomous agent that creates high-fidelity replicas of web applications by analyzing UI, APIs, and generating production-ready code.

## 🌟 Features

- **Frontend Replication**: Pixel-perfect React/TypeScript components with Tailwind CSS
- **Backend Replication**: FastAPI routes with Pydantic validation
- **Database Schema**: Inferred SQL schemas with relationships
- **Visual Testing**: Playwright tests with screenshot comparison and CSS assertions
- **API Testing**: Comprehensive edge case coverage
- **Fidelity Scoring**: Quantitative measurement of replica accuracy

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Node.js 18+ (for running generated frontend)
- OpenAI API key

### Installation
```bash
# Clone repository
git clone <your-repo-url>
cd clooney-agent

# Run setup script
chmod +x setup.sh
./setup.sh

# Edit .env file with your API key
nano .env
```

### Usage
```bash
# Activate virtual environment
source venv/bin/activate

# Run the agent
python run_agent.py
```

The agent will:
1. Launch a browser and navigate to Asana
2. Analyze DOM structure and computed styles
3. Capture network traffic and API calls
4. Generate React components
5. Generate FastAPI routes
6. Create database schema
7. Generate comprehensive tests

## 📊 Output Structure