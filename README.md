
# Containerised Data Warehouse & BI Platform — System Architecture
**An End-to-End Data Engineering and Analytics Platform for Higher Education**

<img width="882" height="791" alt="DW and BI ETL drawio" src="https://github.com/user-attachments/assets/1aadf102-cc3b-4f7c-8b20-08ca54d5356e" />


## Overview

The Education Intelligence Platform is an open-source data engineering and business intelligence project designed to transform student academic records into reliable, actionable insights for institutional decision-making.

The platform demonstrates an end-to-end analytics workflow, from synthetic data generation and ingestion to data validation, transformation, dimensional modelling, and interactive reporting. It provides a foundation for monitoring academic performance, evaluating student progression, and supporting evidence-based decisions in higher education.

The project is being developed as part of my MSc in Information Technology, with an emphasis on building a modular, reproducible, and containerized data platform using open-source technologies.

## Objectives

- Build an end-to-end ETL/ELT pipeline for academic data.
- Implement structured data layers for staging, warehousing, and reporting.
- Apply data quality checks and transformation best practices.
- Develop analytical data models for student performance and institutional reporting.
- Build interactive dashboards to support academic performance monitoring.
- Demonstrate data orchestration, containerization, and reproducible deployment.

## Architecture

The platform follows a layered data architecture:

```text
Synthetic Academic Data
          |
          v
   Data Generation
          |
          v
   Data Ingestion
          |
          v
 PostgreSQL Database
          |
          v
   Staging Layer
          |
          v
 Data Quality Checks
          |
          v
   dbt Transformations
          |
          v
 Warehouse / Reporting
          |
          v
 Apache Superset
          |
          v
 Interactive Dashboards
```

Apache Airflow is used to orchestrate pipeline tasks, while Docker and Docker Compose provide a containerized development environment.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data generation, ingestion, and validation |
| PostgreSQL | Relational database and analytical data storage |
| dbt | SQL transformations and data modelling |
| Apache Airflow | Workflow orchestration |
| Apache Superset | Interactive dashboards and reporting |
| Docker | Containerization and service deployment |
| Redis | Supporting service for the orchestration environment |
| Git and GitHub | Version control and project documentation |

## Data Model and Scope

The platform uses synthetic academic data to simulate a university environment without exposing real student information.

The initial dataset covers:

- **3 faculties**
- **9 departments**
- **45 courses**, with five courses per department across Levels 100–500
- **1,000 students**
- **7,088 academic result records** generated for pipeline testing

The academic results include scores that can be used to evaluate performance, identify students at risk of failing, and support institution-level reporting.

The data model is designed to support analysis across faculties, departments, courses, student populations, and academic performance categories.

## Analytics and Reporting

The reporting layer is designed to support higher-education performance monitoring through metrics such as:

- Student population and distribution by faculty and department
- Academic performance by course, department, and faculty
- Score distributions and pass/fail rates
- Student performance classifications
- Semester GPA and cumulative GPA analysis
- Identification of students requiring academic support

The analytical models are intended to provide consistent, reusable datasets for dashboards and further analysis.

## Data Engineering Workflow

The project implements the following core stages:

1. **Data generation:** Create synthetic student, course, faculty, department, and academic result datasets.
2. **Data ingestion:** Load source datasets into PostgreSQL.
3. **Data validation:** Apply checks to identify missing, invalid, or inconsistent records.
4. **Data transformation:** Use dbt to organize data into staging, warehouse, and reporting models.
5. **Workflow orchestration:** Use Airflow to coordinate pipeline execution and dependencies.
6. **Data visualization:** Connect Apache Superset to the database to build interactive analytical dashboards.

## Project Structure

The repository is organized around the following components:

```text
edu-intelligence-platform/
├── data/
│   └── sample/
├── scripts/
│   ├── generate_data.py
│   ├── load_staging.py
│   └── validate_results.py
├── postgres/
│   └── init/
├── education_dbt/
├── dags/
├── superset/
├── docker-compose.yml
├── .env
├── .gitignore
└── README.md
```

*Directory names may evolve as the project develops.*

## Getting Started

### Prerequisites

Install the following tools:

- Git
- Docker
- Docker Compose
- WSL 2 with Ubuntu, or another supported Linux environment

### Installation

Clone the repository:

```bash
git clone https://github.com/philipebuka/edu-intelligence-platform.git
cd edu-intelligence-platform
```

Configure the environment variables in your local `.env` file using the variables required by your Docker Compose configuration.

Start the containers:

```bash
docker compose up -d --build
```

Check the running services:

```bash
docker compose ps
```

Use the service ports and credentials configured in your local environment to access the database, orchestration interface, and dashboard application.

> **Security:** Do not commit `.env` files, database passwords, secret keys, or other credentials to GitHub.

## Project Status

The platform is under active development. Core components include the PostgreSQL database, dbt transformation project, Docker-based environment, Airflow orchestration, and Apache Superset reporting layer.

Ongoing development focuses on strengthening pipeline reliability, validating data quality, refining analytical models, and expanding dashboard functionality.

## Future Enhancements

- Implement automated data quality testing across transformation layers.
- Improve pipeline monitoring, logging, and failure recovery.
- Expand student progression and academic risk analytics.
- Implement role-based access control for faculty and departmental users.
- Add row-level security to restrict access to relevant institutional data.
- Introduce automated testing and continuous integration.
- Explore predictive analytics for identifying students at risk of poor academic performance.

## Author

**Ebuka Philips**

MSc Information Technology | Business Intelligence | Data Engineering | Analytics

GitHub: [@philipebuka](https://github.com/philipebuka)

## License

This project is intended as an open-source educational and portfolio project. A license can be added to the repository to define the terms under which others may use, modify, and distribute the code.
