"""
Parse Estimation Workflow Markdown to Structured JSON
Categorizes each line and preserves full hierarchy
"""

import re
import json
from typing import Dict, List, Any

def categorize_line(text: str) -> str:
    """Determine category based on content patterns"""
    text_lower = text.lower().strip()
    
    # WARNING patterns (highest priority)
    if any(word in text_lower for word in ['critical', 'warning', 'wrong', 'error', 'risk', 'avoid', 'never']):
        return 'WARNING'
    
    # FORMULA patterns
    if any(char in text for char in ['=', '∑', 'Σ', '±', '×', '÷']) or 'formula' in text_lower:
        return 'FORMULA'
    
    # VALIDATION patterns
    if any(word in text_lower for word in ['check', 'validate', 'verify', 'confirm', 'ensure', 'compare']):
        return 'VALIDATION'
    
    # ACTION patterns
    if text_lower.startswith(('calculate', 'define', 'apply', 'create', 'generate', 'execute', 
                             'perform', 'identify', 'analyze', 'model', 'estimate', 'develop')):
        return 'ACTION'
    
    # PARAMETER patterns
    if re.search(r'\d+[a-z%°]|\d+\s*[-to]\s*\d+|typical:|range:|threshold:', text_lower):
        return 'PARAMETER'
    
    # DOCUMENTATION patterns
    if any(word in text_lower for word in ['document', 'record', 'store', 'archive', 'track', 'log']):
        return 'DOCUMENTATION'
    
    # DELIVERABLE patterns
    if any(word in text_lower for word in ['report', 'presentation', 'output', 'export', 'deliver']):
        return 'DELIVERABLE'
    
    # INPUT patterns
    if any(word in text_lower for word in ['import', 'load', 'input', 'source', 'from']):
        return 'INPUT'
    
    # DECISION patterns
    if any(word in text_lower for word in ['consider', 'decide', 'choose', 'select', 'option', 'if']):
        return 'DECISION'
    
    # OPTION patterns - convert to RATIONALE
    if 'option' in text_lower or text_lower.startswith(('or:', 'alternative')):
        return 'RATIONALE'
    
    # RATIONALE patterns (default for explanatory text)
    if any(word in text_lower for word in ['ensures', 'allows', 'provides', 'enables', 'helps', 'because']):
        return 'RATIONALE'
    
    # Default to RATIONALE for informational content
    return 'RATIONALE'

def parse_markdown_to_json(md_file_path: str) -> Dict[str, Any]:
    """Parse markdown file into structured JSON with categorization"""
    
    with open(md_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    structure = {
        "title": "Estimation Workflow - Mineral Resource Estimation",
        "version": "1.0",
        "date": "2025-11-11",
        "hierarchy_levels": 5,
        "categories": {
            "ACTION": "Tasks to execute",
            "VALIDATION": "Quality control checks",
            "PARAMETER": "Numerical values and thresholds",
            "RATIONALE": "Explanations and justifications",
            "WARNING": "Critical alerts and errors to avoid",
            "DOCUMENTATION": "Recording requirements",
            "FORMULA": "Mathematical equations",
            "DELIVERABLE": "Expected outputs",
            "INPUT": "Required data",
            "DECISION": "Decision points"
        },
        "sections": []
    }
    
    current_section = None
    current_subsection = None
    current_checklist = None
    current_item = None
    
    for line_num, line in enumerate(lines, 1):
        stripped = line.strip()
        
        if not stripped or stripped.startswith('---'):
            continue
        
        # Level 1: ## SECTION
        if stripped.startswith('## ') and not stripped.startswith('###'):
            current_section = {
                "level": 1,
                "line_number": line_num,
                "id": stripped[3:].strip(),
                "title": stripped[3:].strip(),
                "subsections": []
            }
            structure["sections"].append(current_section)
            current_subsection = None
            current_checklist = None
            current_item = None
        
        # Level 2: ### Subsection
        elif stripped.startswith('### ') and not stripped.startswith('####'):
            if current_section:
                current_subsection = {
                    "level": 2,
                    "line_number": line_num,
                    "title": stripped[4:].strip(),
                    "items": []
                }
                current_section["subsections"].append(current_subsection)
                current_checklist = None
                current_item = None
        
        # Level 3: #### Checklist Item
        elif stripped.startswith('#### '):
            if current_subsection:
                # Extract checklist ID (e.g., "1.01")
                match = re.match(r'####\s+(\d+\.\d+)\s*-\s*(.+)', stripped)
                if match:
                    item_id, item_title = match.groups()
                else:
                    item_id = "N/A"
                    item_title = stripped[5:].strip()
                
                current_checklist = {
                    "level": 3,
                    "line_number": line_num,
                    "checklist_id": item_id,
                    "title": item_title,
                    "details": []
                }
                current_subsection["items"].append(current_checklist)
                current_item = None
        
        # Level 4: - Bullet point
        elif stripped.startswith('- ') and not stripped.startswith('  -'):
            content = stripped[2:].strip()
            category = categorize_line(content)
            
            current_item = {
                "level": 4,
                "line_number": line_num,
                "category": category,
                "content": content,
                "sub_items": []
            }
            
            if current_checklist:
                current_checklist["details"].append(current_item)
            elif current_subsection:
                current_subsection["items"].append(current_item)
        
        # Level 5: Sub-bullet (indented)
        elif stripped.startswith('  - ') or (stripped.startswith('-') and line.startswith('  ')):
            content = stripped.lstrip('- ').strip()
            category = categorize_line(content)
            
            sub_item = {
                "level": 5,
                "line_number": line_num,
                "category": category,
                "content": content
            }
            
            if current_item:
                current_item["sub_items"].append(sub_item)
    
    return structure

def normalize_categories(data: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize categories: convert removed categories to RATIONALE, ensure all nodes have category"""
    
    def normalize_node(node):
        if isinstance(node, dict):
            # Normalize category if exists
            if "category" in node and node["category"]:
                category = node["category"]
                # Convert removed categories to RATIONALE
             
            # Recursively process nested structures
            for key, value in node.items():
                if isinstance(value, (list, dict)):
                    normalize_node(value)
        elif isinstance(node, list):
            for item in node:
                normalize_node(item)
    
    normalize_node(data)
    return data

def save_json(data: Dict[str, Any], output_path: str):
    """Save structured data to JSON file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def generate_statistics(data: Dict[str, Any]) -> Dict[str, Any]:
    """Generate statistics about the document"""
    stats = {
        "total_sections": len(data["sections"]),
        "category_counts": {},
        "level_counts": {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
        "checklist_items": 0,
        "total_items": 0
    }
    
    def count_items(node):
        if isinstance(node, dict):
            # Count by level
            if "level" in node:
                level = node["level"]
                stats["level_counts"][level] = stats["level_counts"].get(level, 0) + 1
            
            # Count by category
            if "category" in node:
                category = node["category"]
                stats["category_counts"][category] = stats["category_counts"].get(category, 0) + 1
                stats["total_items"] += 1
            
            # Count checklist items
            if "checklist_id" in node and node["checklist_id"] != "N/A":
                stats["checklist_items"] += 1
            
            for key, value in node.items():
                if isinstance(value, (list, dict)):
                    count_items(value)
        elif isinstance(node, list):
            for item in node:
                count_items(item)
    
    count_items(data)
    return stats

if __name__ == "__main__":
    import sys
    import io
    
    # Fix Windows console encoding for emojis
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    import os
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(base_dir, "estimation_workflow.md")
    output_file = os.path.join(base_dir, "estimation_workflow_structured.json")
    stats_file = os.path.join(base_dir, "estimation_workflow_stats.json")
    
    print("Parsing markdown file...")
    structured_data = parse_markdown_to_json(input_file)
    
    print("Normalizing categories...")
    structured_data = normalize_categories(structured_data)
    
    print("Generating statistics...")
    stats = generate_statistics(structured_data)
    
    print("Saving JSON files...")
    save_json(structured_data, output_file)
    save_json(stats, stats_file)
    
    print(f"\nCompleted!")
    print(f"Structured JSON: {output_file}")
    print(f"Statistics: {stats_file}")
    print(f"\nSummary:")
    print(f"  - Total Sections: {stats['total_sections']}")
    print(f"  - Checklist Items: {stats['checklist_items']}")
    print(f"  - Total Items: {stats['total_items']}")
    
    print(f"\nHierarchy Distribution:")
    print(f"  Level 1 (## Sections): {stats['level_counts'][1]}")
    print(f"  Level 2 (### Subsections): {stats['level_counts'][2]}")
    print(f"  Level 3 (#### Items): {stats['level_counts'][3]}")
    print(f"  Level 4 (- Bullets): {stats['level_counts'][4]}")
    print(f"  Level 5 (  - Sub-bullets): {stats['level_counts'][5]}")
    
    print(f"\nCategory Distribution:")
    for category, count in sorted(stats['category_counts'].items(), key=lambda x: x[1], reverse=True):
        print(f"  {category}: {count}")
