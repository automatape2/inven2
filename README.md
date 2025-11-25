# Inven2 Annual Reports Archive

This repository contains the archived annual reports for Inven2, a Norwegian technology transfer company. The archive serves static HTML versions of annual reports from 2016 to 2023.

## About Inven2

Inven2 is a technology transfer office (TTO) that commercializes research from the University of Oslo and Oslo University Hospital. The company helps researchers transform their innovations into commercial products and services.

## Repository Structure

```
├── 2016/          # Annual report 2016
├── 2017/          # Annual report 2017
├── 2018/          # Annual report 2018
├── 2019/          # Annual report 2019
├── 2020/          # Annual report 2020
├── 2021/          # Annual report 2021
├── 2022/          # Annual report 2022
├── 2023/          # Annual report 2023
├── 404.html       # Custom 404 error page
├── search.html    # Search results page
├── Dockerfile     # Docker configuration
├── docker-compose.yml  # Docker Compose configuration
├── nginx.conf     # Nginx server configuration
└── README.md      # This file
```

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) (for containerized deployment)
- Or a web server like nginx, Apache, or any static file server

## Running the Application

### Using Docker Compose (Recommended)

```bash
docker-compose up -d
```

The site will be available at `http://localhost:9002`

### Using Docker directly

**Linux/macOS (bash/zsh):**
```bash
docker run -p 9002:80 -v $(pwd):/usr/share/nginx/html:ro -d nginx
```

**Windows (PowerShell):**
```powershell
docker run -p 9002:80 -v ${PWD}:/usr/share/nginx/html:ro -d nginx
```

### Using the custom Dockerfile

The custom Dockerfile configures nginx with custom error handling. Note that it requires mounting the content volume:

```bash
docker build -t inven2-annual .
docker run -p 9002:80 -v $(pwd):/usr/share/nginx/html:ro -d inven2-annual
```

## Available Annual Reports

| Year | URL Path |
|------|----------|
| 2016 | `/2016/` |
| 2017 | `/2017/` |
| 2018 | `/2018/` |
| 2019 | `/2019/` |
| 2020 | `/2020/` |
| 2021 | `/2021/` |
| 2022 | `/2022/` |
| 2023 | `/2023/` |

Each annual report is available in both Norwegian (default) and English versions.

## Features

- Static HTML archive of annual reports
- Multi-language support (Norwegian and English)
- Custom 404 error page
- Search functionality
- Responsive design using the Flatsome WordPress theme

## Development

This is a static HTML archive. The content was originally generated from WordPress sites using the Flatsome theme. No build process is required - simply serve the files using any web server.