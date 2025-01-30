import sys
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel,
    QTableWidget, QTableWidgetItem, QComboBox, QMessageBox, QHBoxLayout,
    QSpacerItem, QSizePolicy, QLineEdit
)
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt

class EagleStockJudge(QWidget):
    def __init__(self):
        super().__init__()
        self.stock_data = None
        self.physical_data = None
        self.current_index = 0
        self.currency_rate = 1  # Default conversion rate (1:1, no conversion)
        self.target_currency = "USD"  # Default currency is USD
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Eagle Stock Judge')
        self.setGeometry(100, 100, 1400, 800)
        self.setStyleSheet("background-color: #f4f4f4;")

        layout = QVBoxLayout()

        header_label = QLabel('Eagle Stock Judge', self)
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setFont(QFont('Arial', 28, QFont.Bold))
        layout.addWidget(header_label)

        button_layout = QHBoxLayout()
        button_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.upload_stock_btn = QPushButton('Upload Stock Data', self)
        self.upload_stock_btn.clicked.connect(self.upload_stock_data)
        button_layout.addWidget(self.upload_stock_btn)

        self.upload_physical_btn = QPushButton('Upload Physical Count', self)
        self.upload_physical_btn.clicked.connect(self.upload_physical_count)
        button_layout.addWidget(self.upload_physical_btn)

        self.show_stock_btn = QPushButton('Show Stock Data', self)
        self.show_stock_btn.clicked.connect(self.show_stock_data)
        button_layout.addWidget(self.show_stock_btn)

        self.show_physical_btn = QPushButton('Show Physical Count', self)
        self.show_physical_btn.clicked.connect(self.show_physical_count)
        button_layout.addWidget(self.show_physical_btn)

        self.compare_btn = QPushButton('Compare Data', self)
        self.compare_btn.clicked.connect(self.compare_data)
        button_layout.addWidget(self.compare_btn)

        self.report_type_combo = QComboBox(self)
        self.report_type_combo.addItem("Select Report Type")
        self.report_type_combo.addItem("Total Variance Report")
        self.report_type_combo.addItem("Total Stock Summary Report")
        button_layout.addWidget(self.report_type_combo)

        self.generate_report_btn = QPushButton('Generate Report', self)
        self.generate_report_btn.clicked.connect(self.generate_report)
        button_layout.addWidget(self.generate_report_btn)

        # Currency conversion input
        self.currency_input_label = QLabel("Currency Conversion Rate (1 to new currency):", self)
        button_layout.addWidget(self.currency_input_label)

        self.currency_input = QLineEdit(self)
        self.currency_input.setPlaceholderText("Enter conversion rate (e.g., 1.2 for USD to EUR)")
        self.currency_input.returnPressed.connect(self.update_currency_rate)
        button_layout.addWidget(self.currency_input)

        # Currency selection ComboBox
        self.currency_combo = QComboBox(self)
        self.currency_combo.addItem("USD")
        self.currency_combo.addItem("EUR")
        self.currency_combo.addItem("GBP")
        self.currency_combo.addItem("KSH")  # Kenyan Shilling
        self.currency_combo.addItem("CNY")  # Chinese Yuan
        self.currency_combo.currentTextChanged.connect(self.update_target_currency)
        button_layout.addWidget(self.currency_combo)

        button_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addLayout(button_layout)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        copyright_label = QLabel("© WildadGroup 2025", self)
        copyright_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(copyright_label)

        self.setLayout(layout)

    def upload_stock_data(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Stock Data Excel File", "", "Excel Files (*.xlsx)")
        if file_path:
            self.stock_data = pd.read_excel(file_path)
            required_columns = ['Storage Location', 'Storage Type', 'Storage Bin', 'Pallet ID', 'SKU', 'SKU Description', 'Quantity', 'UoM', 'Unit Price']
            if not all(col in self.stock_data.columns for col in required_columns):
                QMessageBox.warning(self, 'Error', 'Stock data is missing one or more required columns.')
                return
            QMessageBox.information(self, 'Success', 'Stock data uploaded successfully')

    def upload_physical_count(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Physical Count Excel File", "", "Excel Files (*.xlsx)")
        if file_path:
            self.physical_data = pd.read_excel(file_path)
            required_columns = ['Storage Location', 'Storage Type', 'Storage Bin', 'Pallet ID', 'SKU', 'SKU Description', 'Quantity', 'UoM', 'Unit Price']
            if not all(col in self.physical_data.columns for col in required_columns):
                QMessageBox.warning(self, 'Error', 'Physical count data is missing one or more required columns.')
                return
            QMessageBox.information(self, 'Success', 'Physical count data uploaded successfully')

    def show_stock_data(self):
        if self.stock_data is not None:
            self.clear_table()
            self.display_data(self.stock_data)
        else:
            QMessageBox.warning(self, 'Error', 'No stock data uploaded')

    def show_physical_count(self):
        if self.physical_data is not None:
            self.clear_table()
            self.display_data(self.physical_data)
        else:
            QMessageBox.warning(self, 'Error', 'No physical count data uploaded')

    def clear_table(self):
        self.table.setRowCount(0)
        self.table.setColumnCount(0)

    def display_data(self, data):
        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(data.columns))
        self.table.setHorizontalHeaderLabels(data.columns)
        
        for i, row in enumerate(data.itertuples(index=False)):
            for j, col in enumerate(data.columns):
                item = QTableWidgetItem(self.format_cell_value(row[j]))  # Apply format for display
                item.setTextAlignment(Qt.AlignLeft)  # Align the content to the left
                self.table.setItem(i, j, item)
        
        self.add_totals_row(data)  # Add totals row to the displayed data
        self.adjust_column_widths()  # Adjust column widths based on the content

    def compare_data(self):
        if self.stock_data is not None and self.physical_data is not None:
            QMessageBox.information(self, 'Judgement Done!', 'Judgement Done!')
            comparison = self.stock_data.merge(self.physical_data, on=['Storage Location', 'Storage Type', 'Storage Bin', 'Pallet ID', 'SKU', 'SKU Description', 'UoM', 'Unit Price'], suffixes=('_Stock', '_Physical'), how='outer')
            comparison['Variance'] = comparison['Quantity_Stock'].fillna(0) - comparison['Quantity_Physical'].fillna(0)
            self.clear_table()
            self.display_data(comparison)
            self.color_variance_column()  # Apply color changes to the variance column
        else:
            QMessageBox.warning(self, 'Error', 'Please upload both stock data and physical count data before comparing.')

    def generate_report(self):
        report_type = self.report_type_combo.currentText()
        if report_type == "Total Variance Report" and self.stock_data is not None:
            # Calculate the variance and filter out rows with zero variance
            report = self.stock_data.copy()
            report['Variance'] = report['Quantity'] - self.physical_data['Quantity']
            report['Total Value'] = report['Variance'] * report['Unit Price']
            report = report[['SKU', 'SKU Description', 'Variance', 'Unit Price', 'Total Value']]  # Reordered columns
            report = report[report['Variance'] != 0]  # Remove rows with zero variance
            # Aggregate by SKU and SKU Description
            report = report.groupby(['SKU', 'SKU Description'], as_index=False).agg({'Variance': 'sum', 'Unit Price': 'mean', 'Total Value': 'sum'})
        elif report_type == "Total Stock Summary Report" and self.stock_data is not None:
            report = self.stock_data.copy()
            report['Total Value'] = report['Quantity'] * report['Unit Price']
            report = report[['SKU', 'SKU Description', 'Quantity', 'Unit Price', 'Total Value']]  # Reordered columns
            # Remove duplicates by summing the quantities and total values
            report = report.groupby(['SKU', 'SKU Description'], as_index=False).agg({'Quantity': 'sum', 'Unit Price': 'mean', 'Total Value': 'sum'})
        else:
            QMessageBox.warning(self, 'Error', 'Please select a valid report type and ensure stock data is loaded')
            return
        self.clear_table()
        self.display_data(report)

    def add_totals_row(self, data):
        totals_row = {}
        totals_row['SKU'] = 'Total'
        totals_row['SKU Description'] = ''
        totals_row['Quantity'] = data['Quantity'].sum() if 'Quantity' in data.columns else 0
        totals_row['Variance'] = data['Variance'].sum() if 'Variance' in data.columns else 0
        totals_row['Unit Price'] = ''  # No total for unit price
        totals_row['Total Value'] = data['Total Value'].sum() if 'Total Value' in data.columns else 0
        
        # Append the totals row
        self.table.insertRow(self.table.rowCount())
        for col_idx, col_name in enumerate(data.columns):
            item = QTableWidgetItem(self.format_cell_value(totals_row.get(col_name, '')))
            item.setTextAlignment(Qt.AlignLeft)  # Align totals row content to the left
            self.table.setItem(self.table.rowCount() - 1, col_idx, item)

    def format_cell_value(self, value):
        # Check for numeric values and apply round brackets for negatives
        try:
            num_value = float(value)
            if num_value < 0:
                return f"({abs(num_value):,.2f})"
            else:
                return f"{num_value:,.2f}"
        except ValueError:
            return str(value)  # Non-numeric values remain unchanged

    def color_variance_column(self):
        # Ensure that we color only the variance column
        for row in range(self.table.rowCount()):
            variance_item = self.table.item(row, self.table.columnCount() - 1)  # Variance is the last column (zero-indexed)
            if variance_item:
                try:
                    variance_value = variance_item.text()
                    # Check if the variance value is negative or has round brackets
                    if '(' in variance_value or float(variance_value) != 0:
                        variance_item.setBackground(QColor(255, 0, 0))  # Red for negative or non-zero variance
                    elif float(variance_value) == 0:
                        variance_item.setBackground(QColor(0, 255, 0))  # Green for zero variance
                except ValueError:
                    # Skip non-numeric values (like 'Units' or headers)
                    continue

    def adjust_column_widths(self):
        for column in range(self.table.columnCount()):
            self.table.resizeColumnToContents(column)  # Adjust column width based on the longest item

    def update_currency_rate(self):
        # Update the conversion rate from the user input
        try:
            self.currency_rate = float(self.currency_input.text())
            self.convert_values_to_currency()  # Apply conversion immediately
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Invalid currency rate. Please enter a valid number.')

    def update_target_currency(self, new_currency):
        # Update the target currency when the user selects a new one
        self.target_currency = new_currency
        self.convert_values_to_currency()  # Convert values for the selected currency

    def convert_values_to_currency(self):
        # Convert values in 'Unit Price' and 'Total Value' columns by the currency rate
        if self.stock_data is not None:
            self.stock_data['Unit Price'] = self.stock_data['Unit Price'] * self.currency_rate
            self.stock_data['Total Value'] = self.stock_data['Total Value'] * self.currency_rate
            self.clear_table()
            self.display_data(self.stock_data)  # Redisplay the updated data

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EagleStockJudge()
    ex.show()
    sys.exit(app.exec_())
