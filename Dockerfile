FROM debian:12-slim
WORKDIR /valgrind-tests
# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    valgrind \
    nano \
    && rm -rf /var/lib/apt/lists/*

COPY van_emde_boas_tree.py . 
COPY binary_search_tree.py .

RUN chmod u+x van_emde_boas_tree.py
RUN chmod u+x binary_search_tree.py