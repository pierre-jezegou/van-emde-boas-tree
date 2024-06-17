# Cache-Oblivious Van Emde-Boas Trees

## Overview

This repository contains the implementation and performance analysis of Van Emde-Boas (vEB) trees and Binary Search Trees (BSTs), focusing on their cache performance.

## Contents

- `van_emde_boas_tree.py`: Van Emde-Boas tree implementation.
- `binary_search_tree.py`: Binary Search Tree implementation.
- `Dockerfile`: Docker setup with Valgrind for cache performance measurement.
- `performance_analysis.py`: Script for performance tests.
- `results/`: Experimental results and plots.
- `README.md`: Project documentation.

## How to Use

### Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/pierre-jezegou/van-emde-boas-tree.git
    cd van-emde-boas-tree
    ```

2. **Build and run the Docker container:**
    ```sh
    docker build -t valgrind .
    docker run -it --rm valgrind
    ```

### Running Performance Tests

1. **Van Emde-Boas tree:**
    ```sh
    valgrind --tool=cachegrind --cachegrind-out-file=output-veb --trace-children=yes /usr/bin/python3 ./van_emde_boas_tree.py
    ```

2. **Binary Search Tree:**
    ```sh
    valgrind --tool=cachegrind --cachegrind-out-file=output-bst --trace-children=yes /usr/bin/python3 ./binary_search_tree.py
    ```

### Analyzing Results

1. **Generate reports:**
    ```sh
    cg_annotate output-veb > report-veb.txt
    cg_annotate output-bst > report-bst.txt
    ```

## Observations

Van Emde-Boas trees had more cache misses compared to Binary Search Trees. Despite their complexity, BSTs showed better cache performance in practical scenarios.

For more details, refer to the `main.pdf` file in the repository, or the PDF in the releases section.