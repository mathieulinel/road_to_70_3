# road_to_70_3
Ironman 70.3 training repo

# To Do

### ELT
- [ ] Extract:
    - [ ] Check payload for one activity
    - [ ] Add a cooldown or a limit to avoid reaching daily limit too fast
- [ ] Load into duckDB
- [ ] Transform with dbt

### Orchestration
- [ ] Create dag to execute in Dagster


# Project structure
road_to_70_3/
│
├── .env                    # Environment variables (e.g., API keys, DB credentials)
├── .gitignore              # Files/folders to ignore in version control
├── README.md               # Project overview, setup, and usage instructions
├── docker-compose.yml      # Docker Compose configuration
│
├── data/                   # Raw and processed data (optional, can be mounted as volume)
│   ├── raw/                # Raw data from the API
│   └── processed/          # Processed data after transformation
│
├── scripts/                # Utility scripts (e.g., data extraction, setup)
│   ├── extract_data.py     # Script to extract data from the API
│   └── ...
│
├── dbt/                    # dbt project for transformation
│   ├── dbt_project.yml     # dbt project configuration
│   ├── models/             # dbt models (SQL files)
│   │   ├── staging/        # Staging models
│   │   └── marts/          # Marts (business logic)
│   ├── seeds/              # CSV files for static data
│   └── ...
│
├── dagster/                # Dagster project for orchestration
│   ├── __init__.py         # Python package initialization
│   ├── assets/             # Dagster assets (e.g., tables, files)
│   ├── jobs/               # Dagster jobs (orchestration logic)
│   ├── schedules/          # Schedules for jobs
│   ├── sensors/            # Sensors for event-based triggers
│   └── ...
│
├── docker/                 # Docker-related files
│   ├── Dockerfile          # Dockerfile for the main application
│   └── ...
│
└── tests/                  # Unit and integration tests
    ├── unit/               # Unit tests
    └── integration/        # Integration tests
