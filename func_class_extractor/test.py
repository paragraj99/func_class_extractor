
import os
from fpdf import FPDF

def list_defs_classes(root_dir):
    results = []
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):
                path = os.path.join(subdir, file)
                with open(path, 'r', encoding='utf-8') as f:
                    for i, line in enumerate(f, 1):
                        line_strip = line.strip()
                        if line_strip.startswith('def ') or line_strip.startswith('class ') or line_strip.startswith('async def '):
                            results.append(f"{path}:{i}: {line_strip}")
    return results

def save_to_pdf(lines, pdf_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    for line in lines:
        pdf.cell(0, 10, txt=line, ln=1)
    pdf.output(pdf_path)

if __name__ == "__main__":
    output = list_defs_classes('app')
    save_to_pdf(output, "functions_and_classes.pdf")