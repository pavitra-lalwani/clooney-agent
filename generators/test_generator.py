"""
Test generation for both frontend (Playwright) and backend (pytest)
"""

from typing import Dict, List
from openai import AsyncOpenAI

class TestGenerator:
    """Generates comprehensive test suites"""
    
    def __init__(self, client: AsyncOpenAI):
        self.client = client
        
    async def generate_visual_tests(
        self, 
        component_name: str,
        screenshot_path: str,
        css_properties: Dict[str, Dict[str, str]]
    ) -> str:
        """Generate Playwright visual regression tests"""
        
        prompt = f"""Generate comprehensive Playwright tests for visual regression testing.

Component: {component_name}
Reference Screenshot: {screenshot_path}

CSS Properties to Assert:
{self._format_css_assertions(css_properties)}

Generate tests that:
1. Take screenshots and compare with baseline (mask dynamic content)
2. Assert EXACT CSS property values using toHaveCSS()
3. Test responsive breakpoints (mobile: 375px, tablet: 768px, desktop: 1920px)
4. Test hover states for interactive elements
5. Test loading states
6. Test error states
7. Verify accessibility (aria labels, roles)

CRITICAL: 
- Use toHaveCSS() for exact color matching: expect(button).toHaveCSS('background-color', 'rgb(58, 37, 142)')
- Mask dynamic content: text, timestamps, user names
- Use data-testid for reliable selectors

Return TypeScript Playwright test file.
"""
        
        response = await self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are an expert in test automation with Playwright."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        
        return self._clean_code(response.choices[0].message.content)
    
    async def generate_api_tests(
        self,
        endpoint_path: str,
        method: str,
        request_schema: Dict,
        response_schema: Dict
    ) -> str:
        """Generate pytest API tests with edge cases"""
        
        prompt = f"""Generate comprehensive pytest tests for this API endpoint.

Endpoint: {method} {endpoint_path}
Request Schema: {request_schema}
Response Schema: {response_schema}

Generate test cases for:

HAPPY PATH:
1. Valid request with all fields
2. Valid request with only required fields
3. Multiple successful requests

VALIDATION TESTS:
4. Missing required fields (test each one)
5. Empty strings where not allowed
6. Null values where not allowed
7. Wrong data types (string instead of int, etc.)
8. Extra unexpected fields

EDGE CASES:
9. Very long strings (10000+ chars)
10. Special characters in strings
11. Unicode characters
12. Negative numbers where not expected
13. Zero values
14. Boundary values (min/max)

SECURITY TESTS:
15. SQL injection attempts
16. XSS attempts
17. Path traversal attempts
18. Command injection

Use:
- pytest
- httpx for requests
- pytest.mark.parametrize for multiple cases
- Fixtures for common setup
- Clear test names: test_endpoint_scenario

Return pytest test file with all test functions.
"""
        
        response = await self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are an expert in API testing and security."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        
        return self._clean_code(response.choices[0].message.content)
    
    def _format_css_assertions(self, css_props: Dict) -> str:
        """Format CSS properties for test generation"""
        result = []
        for selector, props in css_props.items():
            result.append(f"\n{selector}:")
            for prop, value in props.items():
                result.append(f"  - {prop}: {value}")
        return "\n".join(result)
    
    def _clean_code(self, code: str) -> str:
        """Clean up generated code"""
        if code.startswith('```'):
            lines = code.split('\n')
            code = '\n'.join(lines[1:-1])
        return code.strip()