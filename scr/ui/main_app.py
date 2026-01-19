import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from scr.algorithms.run_algorithms import run_algorithms

class main_app():

    canvas = None
    figure = None
    ax= None

    markers = [".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "D", "d"]

    algorithm_manager = run_algorithms()

    def set_min_value(self, value):
        try:
            self.algorithm_manager.min_value = int(value)
            print('set_min_value={value}')
        except ValueError as e:
            print('ValueError={e}')

    def set_max_value(self, value):
        try:
            self.algorithm_manager.max_value = int(value)
            print('max_value={value}')
        except ValueError as e:
            print('ValueError={e}')

    def set_min_power(self, value):
        try:
            self.algorithm_manager.min_array_size = int(value)
            print('min_array_size={value}')
        except ValueError as e:
            print('ValueError={e}')

    def set_max_power(self, value):
        try:
            self.algorithm_manager.max_array_size = int(value)
            print('max_array_size={value}')
        except ValueError as e:
            print('ValueError={e}')

    def set_max_time(self, value):
        try:
            self.algorithm_manager.max_time = int(value)
            print('max_time={value}')
        except ValueError as e:
            print('ValueError={e}')

    def print_plot(self,x_vals,y_vals,title):
        self.ax.plot(
            x_vals, y_vals,
            color='blue',        # blaue Linie
            linestyle='-',       # durchgezogene Linie
            linewidth=2,
            marker=self.markers.pop(),
            label=title,
            markerfacecolor='red',   # rote Füllung
            markeredgecolor='black', # schwarze Kontur
            markersize=10
        )
        self.ax.legend()

    def on_run_click(self):
        print("Button pressed")
        results = self.algorithm_manager.easy_compare()

        for algo_name, data in results.items():
            self.print_plot(data.keys(),data.values(), algo_name)
        self.canvas.draw()
            
    def create_QPushButton(self,label):
        button = QPushButton(label)
        button.setStyleSheet("""
            QPushButton {
                background-color: #4a90e2;   /* modern blue */
                color: white;                 /* text color */
                font-size: 18px;              /* font size */
                padding: 10px 25px;           /* top/bottom 10px, left/right 20px */
                border-radius: 8px;           /* rounded corners */
            }
            QPushButton:hover {
                background-color: #357ab8;   /* hover effect */
            }
            QPushButton:pressed {
                background-color: #2d5d8f;   /* pressed effect */
            }
        """)

        button.setMaximumSize(270,80)
        return button

    def create_plot(self):
        container = QWidget()
        container.setMinimumSize(1000,1000) #setMaximumSize(900, 600)
        holder = QVBoxLayout(container)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.setMinimumHeight(1000)
        self.canvas.setMaximumHeight(2000)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("Sorting times for different sized lists")
        self.ax.set_xscale('log')
        self.ax.set_xlabel("Array size")
        self.ax.set_ylabel("Execution Time in s")
        self.ax.legend(loc='upper left', fontsize=10, frameon=True)

        self.ax.grid(
            True,             # enable grid
            which='both',     # 'major', 'minor', or 'both'
            linestyle='--',   # '-', '--', '-.', ':'
            linewidth=0.8,    # thickness
            color='gray',     # color
            alpha=0.7         # transparency
        )
        holder.addWidget(self.canvas)

        return container

    def create_top_command_buttons(self):
        # Comand buttons
        command_button_layout = QHBoxLayout()
        run_btn = self.create_QPushButton('Run')
        run_btn.clicked.connect(self.on_run_click)
        command_button_layout.addWidget(run_btn,alignment=Qt.AlignCenter)
        command_button_layout.addWidget(self.create_QPushButton('Stop'),alignment=Qt.AlignCenter)
        return command_button_layout

    def create_label(self, text):
        label = QLabel(text)
        label.setStyleSheet("""
            QLabel {
                color: white;
                min-width: 300px;
                max-width: 300px;
                min-height: 70px;
                max-height: 70px;
                background-color: darkgrey;
                font-family: Arial;
                font-size: 28px;
                font-weight: bold;
                qproperty-alignment: 'AlignCenter';
            }
        """)
        return label

    def create_line_edit_control(self, binding_func, default_value=10):
        line_edit = QLineEdit()
        line_edit.setStyleSheet("""
            QLineEdit {
                color: white;
                min-height: 70px;
                max-height: 70px;
                max-width: 700px;
                background-color: darkgrey;
                font-family: Arial;
                font-size: 28px;
                font-weight: bold;
                qproperty-alignment: 'AlignLeft';
            }
        """)
        line_edit.setText(str(default_value))
        line_edit.textChanged.connect(binding_func)
        return line_edit

    def create_control_row(self, parent_layout, text, binding_func,default_value):
        container = QWidget()
        row = QHBoxLayout(container)
        row.addWidget(self.create_label(text))
        row.addWidget(self.create_line_edit_control(binding_func,default_value))
        parent_layout.addWidget(container)
        return container

    def create_control_panel(self):
        container = QWidget()
        layout = QVBoxLayout(container)
        controls = [
            ('Min Power',self.set_min_power, self.algorithm_manager.min_array_size), 
            ('Max Power',self.set_max_power, self.algorithm_manager.min_array_size), 
            ('Min number',self.set_min_value, self.algorithm_manager.min_value), 
            ('Max number', self.set_max_value, self.algorithm_manager.max_value),
            ('Max time', self.set_max_time, self.algorithm_manager.max_time)
            ]
        for control in controls:
            self.create_control_row(layout, control[0], control[1], control[2])
        return container

    def create_work_layout(self):
        work_layout = QHBoxLayout()
        work_layout.addWidget(self.create_control_panel())
        work_layout.addWidget(self.create_plot())
        return work_layout

    def create_window(self):
        app = QApplication(sys.argv)
        window = QWidget()
        window.setWindowTitle("Compare Sorting Algorithm")
        window.setStyleSheet("background-color: #272726;")

        master_layout = QVBoxLayout()
        master_layout.addLayout(self.create_top_command_buttons())
        master_layout.addLayout(self.create_work_layout())
        master_layout.addStretch()
        window.setLayout(master_layout)

        #Show the appliaction
        window.showMaximized()
        
        sys.exit(app.exec_())