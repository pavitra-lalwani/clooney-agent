"""
Backend API and schema generation
"""

from typing import Dict, List
from openai import AsyncOpenAI

class BackendGenerator:
    """Generates FastAPI backend code"""
    
    def __init__(self, client: AsyncOpenAI):
        self.client = client
        
    async def generate_fastapi_route(
        self,
        path: str,
        method: str,
        request_schema: Dict,
        response_schema: Dict,
        business_logic_notes: str = ""
    ) -> str:
        """Generate FastAPI route with full implementation"""
        
        prompt = f"""Generate a production-ready FastAPI route.

Path: {path}
Method: {method}
Request Schema: {request_schema}
Response Schema: {response_schema}
Business Logic Notes: {business_logic_notes}

Requirements:
1. Create Pydantic models for request/response with validation
2. Implement the route handler with proper type hints
3. Add comprehensive input validation
4. Handle all edge cases gracefully
5. Return appropriate HTTP status codes
6. Add detailed docstrings
7. Include error handling with try/except
8. Add logging statements
9. Validate business logic constraints
10. Add rate limiting hints

Use:
- from fastapi import APIRouter, HTTPException, status
- from pydantic import BaseModel, Field, validator
- Proper HTTP status codes (200, 201, 400, 404, 500)
- Custom validators for complex validation

Return complete Python file with router, models, and handler.
"""
        
        response = await self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are an expert FastAPI developer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        
        return self._clean_code(response.choices[0].message.content)
    
    async def generate_database_schema(self, api_schemas: List[Dict]) -> str:
        """Generate PostgreSQL schema from API analysis"""
        
        prompt = f"""Generate a complete PostgreSQL database schema.

API Response Schemas:
{api_schemas}

Requirements:
1. Infer table structure from API schemas
2. Create proper relationships (foreign keys)
3. Add indexes for common queries
4. Include timestamps (created_at, updated_at)
5. Use appropriate data types
6. Add NOT NULL constraints where appropriate
7. Add CHECK constraints for validation
8. Include comments for documentation
9. Create enum types where needed
10. Add sample data INSERT statements

Return schema.sql with:
- CREATE TYPE statements
- CREATE TABLE statements
- CREATE INDEX statements
- COMMENT ON statements
- Sample INSERT statements

Format as production-ready SQL.
"""
        
        response = await self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a database architect expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        
        return self._clean_code(response.choices[0].message.content)
    
    async def generate_openapi_spec(self, endpoints: List[Dict]) -> str:
        """Generate OpenAPI specification"""
        
        prompt = f"""Generate a complete OpenAPI 3.0 specification.

Endpoints:
{endpoints}

Requirements:
1. Complete OpenAPI 3.0 YAML format
2. Include all endpoints with full documentation
3. Define all schemas with proper types
4. Add examples for requests/responses
5. Include error responses
6. Add security schemes
7. Document query parameters
8. Add tags for organization

Return api.yml in OpenAPI 3.0 format.
"""
        
        response = await self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are an API documentation expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        
        return self._clean_code(response.choices[0].message.content)
    
    def _clean_code(self, code: str) -> str:
        """Clean up generated code"""
        if code.startswith('```'):
            lines = code.split('\n')
            code = '\n'.join(lines[1:-1])
        return code.strip()