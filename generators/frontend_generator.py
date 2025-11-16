"""
Frontend code generation using LLM
Specialized prompts for React/TypeScript/Tailwind generation
"""

from typing import Dict, Optional
from openai import AsyncOpenAI

class FrontendGenerator:
    """Generates React components from DOM analysis"""
    
    def __init__(self, client: AsyncOpenAI):
        self.client = client
        
    async def generate_component(
        self, 
        component_name: str, 
        dom_tree: Dict, 
        color_palette: Dict,
        interactions: list
    ) -> str:
        """Generate a complete React component"""
        
        prompt = f"""You are an expert React/TypeScript developer specializing in pixel-perfect UI replication.

Generate a production-ready React component based on this analysis:

Component Name: {component_name}
DOM Structure:
{self._format_dom_tree(dom_tree)}

Color Palette:
- Text colors: {', '.join(color_palette.get('text', [])[:5])}
- Background colors: {', '.join(color_palette.get('background', [])[:5])}

Interactive Elements:
{self._format_interactions(interactions[:10])}

REQUIREMENTS:
1. Use TypeScript with strict types
2. Use ONLY Tailwind CSS utility classes (no custom CSS)
3. Match EXACT colors from the palette using arbitrary values like bg-[#hex]
4. Include all interactive elements (buttons, inputs, etc.)
5. Add proper event handlers (onClick, onChange, etc.)
6. Use React hooks (useState, useEffect) where needed
7. Add loading states and error handling
8. Make it responsive (mobile, tablet, desktop)
9. Add proper accessibility attributes (aria-label, role, etc.)
10. Include TypeScript interfaces for all data

IMPORTANT COLOR MATCHING:
- Extract exact hex colors from rgb() values
- Use Tailwind arbitrary values: className="bg-[#3a258e]"
- Do not approximate colors

Format: Return ONLY the .tsx file content, no explanations.
Include imports, component, and export default.
"""
        
        response = await self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are an expert React developer who creates pixel-perfect UI replicas."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=4000
        )
        
        return self._clean_code(response.choices[0].message.content)
    
    async def generate_types(self, api_schemas: list) -> str:
        """Generate TypeScript types from API schemas"""
        
        prompt = f"""Generate TypeScript interfaces for these API schemas:

{api_schemas}

Requirements:
1. Create interfaces for all entities
2. Include optional fields with ?
3. Add JSDoc comments
4. Export all interfaces
5. Use proper TypeScript types (string, number, boolean, Date, etc.)

Return ONLY the types.ts file content.
"""
        
        response = await self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a TypeScript expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1
        )
        
        return self._clean_code(response.choices[0].message.content)
    
    def _format_dom_tree(self, tree: Dict, indent: int = 0) -> str:
        """Format DOM tree for prompt"""
        if not tree:
            return ""
            
        result = "  " * indent + f"<{tree['tag']}"
        if tree.get('classes'):
            result += f" class='{' '.join(tree['classes'][:3])}'"
        result += ">\n"
        
        if tree.get('text'):
            result += "  " * (indent + 1) + f"{tree['text'][:50]}\n"
            
        # Include key styles
        styles = tree.get('styles', {})
        important_styles = ['color', 'backgroundColor', 'fontSize', 'padding', 'display']
        style_str = "; ".join([f"{k}: {styles[k]}" for k in important_styles if k in styles])
        if style_str:
            result += "  " * (indent + 1) + f"/* {style_str} */\n"
        
        return result
    
    def _format_interactions(self, interactions: list) -> str:
        """Format interaction elements for prompt"""
        result = []
        for item in interactions:
            result.append(f"- {item['type']}: {item.get('text', 'N/A')[:30]}")
        return "\n".join(result)
    
    def _clean_code(self, code: str) -> str:
        """Remove markdown code blocks and clean up"""
        if code.startswith('```'):
            lines = code.split('\n')
            code = '\n'.join(lines[1:-1])
        return code.strip()