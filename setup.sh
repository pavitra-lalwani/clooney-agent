#!/bin/bash

echo "🎬 Setting up Clooney Agent..."

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "📥 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Install Playwright browsers
echo "🌐 Installing Playwright browsers..."
playwright install chromium

# Create .env from template
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp env.template .env
    echo "⚠️  Please edit .env and add your OPENAI_API_KEY"
fi

# Create output directory
mkdir -p output/frontend output/backend

echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env and add your OPENAI_API_KEY"
echo "2. Run: python run_agent.py"