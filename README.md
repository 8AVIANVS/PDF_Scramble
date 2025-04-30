# RAG Benchmarking Pipeline

A tool for benchmarking Retrieval-Augmented Generation (RAG) systems. This pipeline generates test documents in PDF format and corresponding question-answer pairs.

## Overview

This pipeline generates PDF documents with controlled content and corresponding question-answer pairs

## Directory Structure

```
.
├── main.py          # Main orchestration script
├── generator.py     # Document and QA pair generator
├── unpack.py        # Helper for unpacking content
├── pdf/             # Generated PDF documents (gitignored)
├── md/              # Extracted markdown files (gitignored)
└── qa/              # Question-answer pairs (gitignored)
```

## Setup

### Prerequisites

- Python 3.8+
- Required Python packages (install via pip):
  ```
  pip install -r requirements.txt
  ```

### Environment Setup

Create a `.env` file in the project root with the following configurations:

```
# Add any environment variables needed for the pipeline
```

## Usage

Generates PDF documents and QA pairs by editing the decompressed PDF stream via direct hex manipulation. The net income row of each generated PDF file will have randomized numbers corresponding to the QA pair.
