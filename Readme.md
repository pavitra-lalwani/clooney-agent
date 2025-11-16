cat > README.md << 'EOF'
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
git clone https://github.com/pavitra-lalwani/clooney-agent.git
cd clooney-agent

# Run setup script
chmod +x setup.sh
./setup.sh

# Edit .env file with your API key
nano .env
# Add: OPENAI_API_KEY=sk-your-key-here
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
```
output/
├── frontend/
│   ├── components/
│   │   ├── HomePage.tsx
│   │   ├── ProjectsPage.tsx
│   │   └── TasksPage.tsx
│   ├── tests/
│   │   └── visual/
│   │       ├── home.spec.ts
│   │       ├── projects.spec.ts
│   │       └── tasks.spec.ts
│   └── package.json
│
└── backend/
    ├── routes/
    │   ├── projects.py
    │   └── tasks.py
    ├── tests/
    │   ├── test_projects.py
    │   └── test_tasks.py
    ├── schema.sql
    └── main.py
```

## 🧪 Running Tests

### Frontend Visual Tests
```bash
cd output/frontend
npm install
npx playwright test
```

### Backend API Tests
```bash
cd output/backend
pip install -r requirements.txt
pytest -v
```

## 🏗️ Architecture

### Analysis Phase
- Playwright automation for DOM extraction
- Computed styles analysis
- Network traffic interception
- Component hierarchy mapping

### Generation Phase
- GPT-4 powered code generation
- Schema inference from API responses
- Test case synthesis
- Fidelity scoring

### Validation Phase
- Pixel-perfect visual regression
- CSS property assertions
- API contract validation
- Edge case coverage

## 📈 Fidelity Metrics

The agent calculates:
- **Visual Similarity**: SSIM comparison of screenshots
- **CSS Match Rate**: Percentage of matching computed styles
- **Component Coverage**: Ratio of replicated to original components
- **API Parity**: Endpoint and schema match percentage

## 🔧 Configuration

Edit `.env` file:
```bash
OPENAI_API_KEY=sk-your-key
TARGET_URL=https://app.asana.com/
PAGES=home,projects,tasks
MODE=both  # Options: frontend, backend, both
```

## 🐳 Docker Support
```bash
# Build and run with Docker
docker-compose up --build

# View output
ls -la output/
```

## 📁 Project Structure
```
clooney-agent/
├── clooney_agent.py          # Main agent orchestrator
├── run_agent.py              # Simple runner script
├── requirements.txt          # Python dependencies
├── setup.sh                  # Setup script
├── env.template              # Environment template
├── README.md                 # This file
├── Dockerfile                # Docker configuration
├── docker-compose.yml        # Docker compose
│
├── generators/               # Code generation modules
│   ├── frontend_generator.py
│   ├── backend_generator.py
│   └── test_generator.py
│
└── utils/                    # Utility modules
    ├── dom_analyzer.py
    └── image_compare.py
```

## 🛠️ Advanced Usage

### Analyze Specific Pages
```python
from clooney_agent import ClooneyAgent
import asyncio

async def main():
    agent = ClooneyAgent(api_key="sk-...", target_url="https://app.asana.com/")
    await agent.run_full_analysis(['home', 'projects', 'tasks', 'dashboard'])

asyncio.run(main())
```

### Custom Configuration

Edit `env.template` for more options:
```bash
VIEWPORT_WIDTH=1920
VIEWPORT_HEIGHT=1080
HEADLESS=false
ASANA_EMAIL=your@email.com
ASANA_PASSWORD=your-password
```

## 🐛 Troubleshooting

### Browser doesn't launch
```bash
playwright install chromium
```

### Import errors
```bash
pip install -r requirements.txt
```

### API rate limits
Add delays in agent configuration or use a higher tier OpenAI account.

## 📝 Implementation Details

### Key Technologies
- **Playwright**: Browser automation and network interception
- **OpenAI GPT-4**: Code generation and analysis
- **Pydantic**: Data validation
- **FastAPI**: Backend framework
- **React + TypeScript**: Frontend framework
- **Tailwind CSS**: Styling
- **Pytest + Playwright Test**: Testing

### Design Decisions

1. **Modular Architecture**: Separate concerns for analysis, generation, and testing
2. **LLM-Powered Generation**: Leverages GPT-4 for context-aware code creation
3. **Comprehensive Testing**: Visual regression and API edge case coverage
4. **Production Ready**: Error handling, logging, and Docker support

## 📊 Expected Results

For Asana Home/Projects/Tasks pages:
- **Generated Files**: 50+ files
- **Lines of Code**: 5000+ lines
- **Test Cases**: 100+ tests
- **Fidelity Score**: 90%+ overall

## ⚠️ Important Notes

- Uses your own OpenAI API key (costs apply)
- Designed for educational and evaluation purposes
- Asana authentication may be required for full access

## 📄 License

MIT License - See LICENSE file for details

## 👨‍💻 Author

Pavitra Lalwani
- GitHub: [@pavitra-lalwani](https://github.com/pavitra-lalwani)



## 📧 Contact

For questions or issues, please open an issue on GitHub or contact through the repository.

---

EOF