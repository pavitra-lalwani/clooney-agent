"""
DOM Analysis Utilities
Extracts and analyzes DOM structure and computed styles
"""

from typing import Dict, List, Optional
from playwright.async_api import Page

class DOMAnalyzer:
    """Analyzes DOM structure and computed styles"""
    
    @staticmethod
    async def extract_component_tree(page: Page, selector: str = 'main') -> Dict:
        """Extract hierarchical component tree with styles"""
        
        script = """
        (selector) => {
            function analyzeElement(el, depth = 0) {
                if (depth > 5) return null; // Limit depth
                
                const styles = window.getComputedStyle(el);
                const rect = el.getBoundingClientRect();
                
                // Skip invisible elements
                if (rect.width === 0 || rect.height === 0) return null;
                
                return {
                    tag: el.tagName.toLowerCase(),
                    id: el.id,
                    classes: Array.from(el.classList),
                    text: el.childNodes.length === 1 && el.childNodes[0].nodeType === 3 
                        ? el.textContent.trim().substring(0, 100) 
                        : null,
                    attributes: {
                        role: el.getAttribute('role'),
                        ariaLabel: el.getAttribute('aria-label'),
                        dataTestId: el.getAttribute('data-test-id')
                    },
                    styles: {
                        // Layout
                        display: styles.display,
                        position: styles.position,
                        flexDirection: styles.flexDirection,
                        justifyContent: styles.justifyContent,
                        alignItems: styles.alignItems,
                        gridTemplateColumns: styles.gridTemplateColumns,
                        
                        // Box model
                        width: styles.width,
                        height: styles.height,
                        margin: styles.margin,
                        padding: styles.padding,
                        
                        // Typography
                        fontSize: styles.fontSize,
                        fontWeight: styles.fontWeight,
                        fontFamily: styles.fontFamily,
                        lineHeight: styles.lineHeight,
                        textAlign: styles.textAlign,
                        color: styles.color,
                        
                        // Visual
                        backgroundColor: styles.backgroundColor,
                        border: styles.border,
                        borderRadius: styles.borderRadius,
                        boxShadow: styles.boxShadow,
                        opacity: styles.opacity,
                        
                        // Transform
                        transform: styles.transform,
                        transition: styles.transition
                    },
                    rect: {
                        x: rect.x,
                        y: rect.y,
                        width: rect.width,
                        height: rect.height
                    },
                    children: Array.from(el.children)
                        .map(child => analyzeElement(child, depth + 1))
                        .filter(Boolean)
                };
            }
            
            const root = document.querySelector(selector);
            return root ? analyzeElement(root) : null;
        }
        """
        
        return await page.evaluate(script, selector)
    
    @staticmethod
    async def extract_interactive_elements(page: Page) -> List[Dict]:
        """Extract all interactive elements with their properties"""
        
        script = """
        () => {
            const interactiveSelectors = [
                'button',
                'a',
                'input',
                'textarea',
                'select',
                '[role="button"]',
                '[role="link"]',
                '[role="tab"]',
                '[tabindex="0"]',
                '[onclick]'
            ];
            
            const elements = [];
            interactiveSelectors.forEach(selector => {
                document.querySelectorAll(selector).forEach(el => {
                    const styles = window.getComputedStyle(el);
                    const rect = el.getBoundingClientRect();
                    
                    if (rect.width > 0 && rect.height > 0) {
                        elements.push({
                            type: el.tagName.toLowerCase(),
                            text: el.textContent.trim().substring(0, 50),
                            selector: el.id ? `#${el.id}` : `.${Array.from(el.classList).join('.')}`,
                            styles: {
                                color: styles.color,
                                backgroundColor: styles.backgroundColor,
                                fontSize: styles.fontSize,
                                padding: styles.padding,
                                border: styles.border,
                                borderRadius: styles.borderRadius,
                                cursor: styles.cursor
                            },
                            rect: rect.toJSON(),
                            events: {
                                hasOnClick: el.onclick !== null,
                                hasHref: el.hasAttribute('href'),
                                isDisabled: el.disabled
                            }
                        });
                    }
                });
            });
            
            return elements;
        }
        """
        
        return await page.evaluate(script)
    
    @staticmethod
    async def extract_color_palette(page: Page) -> Dict[str, List[str]]:
        """Extract color palette used in the application"""
        
        script = """
        () => {
            const colors = {
                text: new Set(),
                background: new Set(),
                border: new Set()
            };
            
            document.querySelectorAll('*').forEach(el => {
                const styles = window.getComputedStyle(el);
                
                if (styles.color !== 'rgba(0, 0, 0, 0)') {
                    colors.text.add(styles.color);
                }
                if (styles.backgroundColor !== 'rgba(0, 0, 0, 0)') {
                    colors.background.add(styles.backgroundColor);
                }
                if (styles.borderColor && styles.borderColor !== 'rgba(0, 0, 0, 0)') {
                    colors.border.add(styles.borderColor);
                }
            });
            
            return {
                text: Array.from(colors.text),
                background: Array.from(colors.background),
                border: Array.from(colors.border)
            };
        }
        """
        
        return await page.evaluate(script)