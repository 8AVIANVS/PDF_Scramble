#!/usr/bin/env python3
"""
Test script for the DocumentGenerator class.
"""
from generator import DocumentGenerator

def main():
    # Initialize the generator
    generator = DocumentGenerator()
    
    # Generate a single document and QA pairs
    pdf_paths, qa_path = generator.generate_documents(num_documents=1)
    
    print(f"Generated {len(pdf_paths)} PDF documents")
    print(f"QA pairs saved to {qa_path}")

if __name__ == "__main__":
    main()
