"""
Simple runner script for Clooney Agent
Usage: python run_agent.py
"""

import asyncio
import os
from dotenv import load_dotenv
from clooney_agent import ClooneyAgent

async def main():
    # Load environment variables
    load_dotenv()
    
    api_key = os.getenv('OPENAI_API_KEY')
    target_url = os.getenv('TARGET_URL', 'https://app.asana.com/')
    output_dir = os.getenv('OUTPUT_DIR', './output')
    pages = os.getenv('PAGES', 'home,projects,tasks').split(',')
    
    if not api_key:
        print("❌ Error: OPENAI_API_KEY not found in environment")
        print("Please copy env.template to .env and add your API key")
        return
    
    print(f"""
    🎬 Clooney Agent Starting...
    
    Target: {target_url}
    Pages: {', '.join(pages)}
    Output: {output_dir}
    """)
    
    agent = ClooneyAgent(api_key, target_url, output_dir)
    await agent.run_full_analysis(pages)
    
    print(f"""
    ✅ Analysis Complete!
    
    Generated files are in: {output_dir}
    
    Next steps:
    1. Review generated components in {output_dir}/frontend/components/
    2. Review API routes in {output_dir}/backend/routes/
    3. Run tests: cd {output_dir}/frontend && npx playwright test
    """)

if __name__ == "__main__":
    asyncio.run(main())