from typing import Dict, Any

def validate_and_map_data(data: Dict[str, Any]) -> Dict[str, Any]:
    # Define expected keys and their types
    expected_keys = {
        'job_title': str,
        'company_name': str,
        'location': str,
        'required_skills': list,
        'desired_experience_years': int,
        'salary_range': str,
        'technologies_required': list,
        'deployment_platforms': list,
        'additional_requirements': str
    }

    # Validate and map data
    mapped_data = {}
    for key, expected_type in expected_keys.items():
        if key not in data:
            raise ValueError(f"Missing required key: {key}")
        if not isinstance(data[key], expected_type):
            raise TypeError(f"Invalid type for key '{key}': Expected {expected_type.__name__}, got {type(data[key]).__name__}")
        mapped_data[key] = data[key]

    return mapped_data

# Example usage
data = {
    'job_title': '追加開発エンジニア',
    'company_name': 'AI解析アプリ',
    'location': 'デスクトップアプリ',
    'required_skills': ['Python', 'RunPod'],
    'desired_experience_years': 3,
    'salary_range': '未設定',
    'technologies_required': ['AI解析'],
    'deployment_platforms': ['AWS', 'Azure'],
    'additional_requirements': '詳細な仕様書を参照'
}

try:
    validated_data = validate_and_map_data(data)
    print("Validated and mapped data:", validated_data)
except (ValueError, TypeError) as e:
    print(e)