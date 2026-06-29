print('3')

"""import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QHeaderView, QTableWidgetItem
import pymysql

class Window(QMainWindow):
def __init__(self):
super().__init__()
self.text = QTextEdit()
self.setCentralWidget(self.text)
self.load_data()

def load_data(self):
try:
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='fuel_stations')
cursor = conn.cursor()
cursor.execute("select * from sales")
for row in cursor:
self.text.append(" | ".join(map(str, row)))
cursor.close()
conn.close()
except Exception as e:
self.text.append(f"Error: {e}")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())




CREATE TABLE Clients (
id INT PRIMARY KEY IDENTITY(1,1),
name VARCHAR(100) NOT NULL,
phone VARCHAR(20) NOT NULL
);

CREATE TABLE Models (
id INT PRIMARY KEY IDENTITY(1,1),
name VARCHAR(50) NOT NULL,
depth_m DECIMAL(10,2),
height_m DECIMAL(10,2),
length_m DECIMAL(10,2)
);

CREATE TABLE Materials (
id INT PRIMARY KEY IDENTITY(1,1),
name VARCHAR(50) NOT NULL,
price_per_m2 DECIMAL(10,2)
);

CREATE TABLE Orders (
id INT PRIMARY KEY IDENTITY(1,1),
client_id INT NOT NULL,
model_id INT NOT NULL,
order_date DATETIME DEFAULT GETDATE(),
quantity INT NOT NULL,
status VARCHAR(20) DEFAULT 'новый',
material_id INT NOT NULL,
FOREIGN KEY (client_id) REFERENCES Clients(id),
FOREIGN KEY (model_id) REFERENCES Models(id),
FOREIGN KEY (material_id) REFERENCES Materials(id)
);

CREATE TABLE Fittings (
id INT PRIMARY KEY IDENTITY(1,1),
name VARCHAR(50) NOT NULL,
price_per_unit DECIMAL(10,2)
);

CREATE TABLE OrderFittings (
id INT PRIMARY KEY IDENTITY(1,1),
order_id INT NOT NULL,
fitting_id INT NOT NULL,
quantity INT NOT NULL,
FOREIGN KEY (order_id) REFERENCES Orders(id),
FOREIGN KEY (fitting_id) REFERENCES Fittings(id)
);"""
