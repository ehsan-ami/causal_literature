import arxiv
import requests
import os

# Function to sanitize filenames
def sanitize_filename(title):
    invalid = '<>:"/\|?*'
    for char in invalid:
        title = title.replace(char, '')
    return title

# Function to search and download papers from arXiv
def search_and_download(title):
    # Use the arxiv library to query for the title
    search = arxiv.Search(
        query = f"ti:\"{title}\"", # Search by title
        max_results = 1
    )
    results = list(search.results())

    if not results:
        # print(f"No results found for '{title}'")
        print(title)
        return
    
    paper = results[0]
    # print(f"Found '{paper.title}', downloading...")
    # Generate a sanitized filename for the PDF
    filename = f"{sanitize_filename(paper.title)}.pdf"
    
    # Get the PDF URL and download the file
    pdf_url = paper.pdf_url
    response = requests.get(pdf_url)
    
    if response.status_code == 200:
        return
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Saved as {filename}")
    else:
        print(title)
        # print(f"Failed to download the PDF for '{title}'")

# Define the list of titles to search and download
paper_titles = [
    "CausalAgents: A Robustness Benchmark for Motion Forecasting using Causal Relationships",
    "Amortized Inference for Causal Structure Learning",
    "Amortized causal discovery: Learning to infer causal graphs from time-series data",
    "Neural Relational Inference for Interacting Systems",
    "Dynamic Neural Relational Inference",
    "Differentiable graph module (DGM) for graph convolutional networks",
    "Pointer Graph Networks",
    "SLAPS: Self-Supervision Improves Structure Learning for Graph Neural Networks",
    "Towards Unsupervised Deep Graph Structure Learning",
    "SE(3)-Transformers: 3D Roto-Translation Equivariant Attention Networks",
    "SE(3) Equivariant Graph Neural Networks with Complete Local Frames",
    "SPAGNN: Spatially-aware graph neural networks for relational behavior forecasting from sensor data",
    "Principal Neighbourhood Aggregation for Graph Nets",
    "Position-aware Graph Neural Networks",
    "Identity-aware Graph Neural Networks",
    "Do Transformers Really Perform Badly for Graph Representation?",
    "Graph Attention Networks",
    "How Attentive are Graph Attention Networks?",
    "Neural Message Passing for Quantum Chemistry",
    "Heterogeneous Graph Transformer",
    "Mixture-of-Experts with Expert Choice Routing",
    "From Sparse to Soft Mixtures of Experts",
    "Fuzzy Tiling Activations: A Simple Approach to Learning Sparse Representations Online",
    "Towards Robust and Adaptive Motion Forecasting: A Causal Representation Perspective",
    "Sequential Causal Imitation Learning with Unobserved Confounders",
    "Causal Imitative Model for Autonomous Driving",
    "Toward Causal Representation Learning",
    "AZ-whiteness test: a test for signal uncorrelation on spatio-temporal graphs",
    "Causal Effect Inference with Deep Latent-Variable Models",
    "Sharpness-aware Minimization for Efficiently Improving Generalization",
    "Ignorance is Bliss: Robust Control via Information Gating",
    "Motion Transformer with Global Intention Localization and Local Movement Refinement",
    "GoRela: Go Relative for Viewpoint-Invariant Motion Forecasting",
    "An investigation of why overparameterization exacerbates spurious correlations",
    "Invariant risk minimization",
    "Invariant risk minimization games",
    "Learning Unforeseen Robustness from Out-of-distribution Data Using Equivariant Domain Translator",
    "Adversarially robust generalization requires more data",
    "Learning Causal Semantic Representation for Out-of-Distribution Prediction",
    "Generative Causal Representation Learning for Out-of-Distribution Motion Forecasting",
    "A survey on graph structure learning: Progress and opportunities",
    "Attention is all you need",
    "Energy-based Out-of-Distribution Detection for Graph Neural Networks",
    "IS-GGT: Iterative Scene Graph Generation With Generative Transformers",
    "Relationformer: A Unified Framework for Image-to-Graph Generation",
    "Transparency and explanation in deep reinforcement learning neural networks",
    "Large scale interactive motion forecasting for autonomous driving: The waymo open motion dataset",
]

# Iterate through the list of paper titles and attempt to download each
for title in paper_titles:
    search_and_download(title)

