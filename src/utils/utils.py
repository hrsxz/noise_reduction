import os
from nbconvert import HTMLExporter, PDFExporter
from traitlets.config import Config


class NotebookConverter:
    def __init__(self, source_notebook, target_folder, additional_pdf=False):
        self.source_notebook = source_notebook
        self.target_folder = target_folder
        self.additional_pdf = additional_pdf

        # 确保目标文件夹存在
        os.makedirs(target_folder, exist_ok=True)

    def convert(self):
        # 获取文件名（无扩展名）
        notebook_name = os.path.splitext(os.path.basename(self.source_notebook))[0]

        # 转换为 HTML
        html_output_path = os.path.join(self.target_folder, f"{notebook_name}.html")
        self.convert_to_html(html_output_path)

        # 如果需要，转换为 PDF
        if self.additional_pdf:
            pdf_output_path = os.path.join(self.target_folder, f"{notebook_name}.pdf")
            self.convert_to_pdf(pdf_output_path)

    def convert_to_html(self, output_path):
        print(f"Converting {self.source_notebook} to HTML...")
        exporter = HTMLExporter()
        config = Config()
        config.HTMLExporter.preprocessors = ["nbconvert.preprocessors.ExecutePreprocessor"]
        exporter.config = config
        body, _ = exporter.from_filename(self.source_notebook)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(body)
        print(f"HTML file saved to {output_path}")

    def convert_to_pdf(self, output_path):
        print(f"Converting {self.source_notebook} to PDF...")
        exporter = PDFExporter()
        config = Config()
        exporter.config = config
        body, _ = exporter.from_filename(self.source_notebook)
        with open(output_path, "wb") as f:
            f.write(body)
        print(f"PDF file saved to {output_path}")


def get_notebook_converter(source_notebook, target_folder, additional_pdf=False):
    return NotebookConverter(source_notebook, target_folder, additional_pdf)
