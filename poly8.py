class Report:
    def generate(self):
        pass

class PDFReport(Report):
    def generate(self):
        print("Generating PDF Report")

class ExcelReport(Report):
    def generate(self):
        print("Generating Excel Report")

class HTMLReport(Report):
    def generate(self):
        print("Generating HTML Report")

def show_report(report):
    report.generate()

show_report(PDFReport())
show_report(ExcelReport())
show_report(HTMLReport())