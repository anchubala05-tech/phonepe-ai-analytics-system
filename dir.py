import os

folders = [
    'data/raw',
    'data/processed',
    'data/backup',
    'notebooks/eda',
    'notebooks/model_building',
    'notebooks/sql_analysis',
    'database/schema',
    'database/sql_queries',
    'database/db_connection',
    'src/extraction',
    'src/preprocessing',
    'src/feature_engineering',
    'src/visualization',
    'src/machine_learning',
    'src/forecasting',
    'src/fraud_detection',
    'src/utils',
    'models',
    'dashboard/pages',
    'dashboard/assets',
    'dashboard/components',
    'reports/charts',
    'reports/insights',
    'reports/presentation',
    'screenshots',
    'tests'
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f'Created: {folder}')

files = [
    'requirements.txt',
    'README.md',
    'main.py',
    'app.py',
    '.gitignore'
]

for file in files:
    open(file, 'a').close()
    print(f'Created file: {file}')

print('\nProject Structure Created Successfully!')
