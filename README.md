# biosequence-analyzer-api

## Overview

biosequence-analyzer-api is a REST API built with FastAPI and Biopython for DNA and RNA sequence analysis. It provides core bioinformatics utilities such as sequence transformation, GC content calculation, reverse complement generation, transcription, translation, and FASTA parsing.

The project is designed as a backend-only service intended for integration into other applications, pipelines, or bioinformatics tools.

## Features

* DNA/RNA sequence analysis
* GC content calculation
* Reverse complement generation
* DNA transcription (DNA → RNA)
* RNA/DNA translation (RNA → protein)
* FASTA file parsing support
* RESTful API design for easy integration

## Tech Stack

* Python
* FastAPI
* Biopython
* Uvicorn (ASGI server)

## Project Structure

app/
main.py              # Application entry point
routes/              # API route definitions
services/            # Core sequence processing logic
schemas/             # Request and response models

## Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/biosequence-analyzer-api.git
cd biosequence-analyzer-api
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

## Running the API

Start the development server:

```
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

### Analyze Sequence

**POST** `/analyze`

Request body:

```
{
  "sequence": "ATGCATGC"
}
```

Response:

```
{
  "gc_content": 50.0,
  "reverse_complement": "GCATGCAT",
  "rna": "AUGCAUGC",
  "protein": "MHA"
}
```

## Planned Improvements

* FASTA file upload support
* Batch sequence processing
* Authentication layer (optional)
* Rate limiting
* Docker support
* Cloud deployment configuration

## Use Cases

* Bioinformatics research tools
* Educational platforms for molecular biology
* Backend service for genomics applications
* Integration into scientific data pipelines

## License

MIT License

## Notes

This project focuses on backend processing and does not include a frontend. It is intended to be consumed as a standalone API service.
