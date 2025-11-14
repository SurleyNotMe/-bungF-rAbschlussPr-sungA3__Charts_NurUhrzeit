from PyQt6.QtWidgets import QWidget
from PyQt6.QtCharts import QDateTimeAxis
from PyQt6.QtCore import QDateTime, QDate, QTime

class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        basis_datum = QDate(2000, 1, 1)
        axis_date_time = QDateTimeAxis()
        axis_date_time.setTitleText("Datum")
        axis_date_time.setFormat("hh:mm")
        date_time_start = QDateTime(basis_datum, QTime(8, 0, 0))
        date_time_end = QDateTime(basis_datum, QTime(17, 0, 0))
        axis_date_time.setRange(date_time_start, date_time_end)


