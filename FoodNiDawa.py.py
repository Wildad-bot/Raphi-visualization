from PyQt5 import QtWidgets, QtGui, QtCore
import random

class FoodNiDawaApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Food Ni Dawa")
        self.setGeometry(100, 100, 900, 700)
        self.setStyleSheet("background-color: white; color: black;")

        self.food_data = {
            "Tamarind": {"nutrition": "Rich in Vitamin C, fiber, antioxidants", "conditions": ["Digestion Issues", "Heart Health", "Diabetes", "Blood Pressure"], "benefits": "Improves digestion, reduces blood pressure, supports heart health"},
            "Baobab": {"nutrition": "High in vitamin C, calcium, fiber", "conditions": ["Bone Strength", "Immunity Boost", "Skin Health", "Blood Sugar Regulation"], "benefits": "Strengthens bones, boosts immunity, improves skin health"},
            "Pawpaw": {"nutrition": "Rich in enzymes for digestion, Vitamin A", "conditions": ["Digestion Issues", "Eye Health", "Weight Management", "Cancer Management"], "benefits": "Supports digestion, enhances eye health, aids in weight management"},
            "Ginger": {"nutrition": "Contains gingerol, anti-inflammatory", "conditions": ["Immunity Boost", "Digestion Issues", "Nausea Relief", "Common Cold"], "benefits": "Boosts immunity, relieves nausea, improves digestion"},
            "Green Tea": {"nutrition": "High in antioxidants, metabolism booster", "conditions": ["Weight Management", "Heart Health", "Brain Function", "Prostate Health"], "benefits": "Supports weight management, enhances brain function, improves heart health"},
            "Olive Oil": {"nutrition": "Rich in healthy fats, reduces inflammation", "conditions": ["Heart Health", "Skin Health", "Brain Function", "Blood Pressure"], "benefits": "Supports heart health, improves skin health, reduces inflammation"},
            "Almonds": {"nutrition": "High in vitamin E, good for heart and skin", "conditions": ["Bone Strength", "Heart Health", "Brain Function", "Blood Sugar Regulation"], "benefits": "Strengthens bones, supports heart health, regulates blood sugar"},
            "Spinach": {"nutrition": "Loaded with iron, folate, vitamins", "conditions": ["Eye Health", "Bone Strength", "Skin Health", "Prostate Health"], "benefits": "Enhances eye health, strengthens bones, improves skin health"},
            "Turmeric": {"nutrition": "Contains curcumin, powerful anti-inflammatory", "conditions": ["Immunity Boost", "Brain Function", "Joint Health", "Cancer Management"], "benefits": "Boosts immunity, supports brain function, improves joint health"},
            "Fenugreek": {"nutrition": "Good for digestion and blood sugar control", "conditions": ["Diabetes", "Digestion Issues", "Weight Management", "Blood Sugar Regulation"], "benefits": "Supports digestion, regulates blood sugar, aids in weight management"},
            "Sorghum": {"nutrition": "Rich in fiber, protein, and antioxidants", "conditions": ["Diabetes", "Heart Health", "Weight Management", "Blood Sugar Regulation"], "benefits": "Regulates blood sugar, supports heart health, aids in weight management"},
            "Millet": {"nutrition": "Gluten-free, high in fiber and magnesium", "conditions": ["Diabetes", "Bone Strength", "Weight Management", "Blood Sugar Regulation"], "benefits": "Regulates blood sugar, strengthens bones, aids in weight management"},
            "Fonio": {"nutrition": "Rich in amino acids and fiber", "conditions": ["Brain Function", "Diabetes", "Weight Management", "Blood Pressure"], "benefits": "Supports brain function, regulates blood pressure, aids in weight management"},
            "Dark Leafy Vegetables": {"nutrition": "Loaded with iron, folate, and vitamins", "conditions": ["Bone Strength", "Eye Health", "Heart Health", "Prostate Health"], "benefits": "Strengthens bones, enhances eye health, supports heart health"},
            "Groundnuts": {"nutrition": "High in protein and healthy fats", "conditions": ["Brain Function", "Heart Health", "Weight Management", "Blood Sugar Regulation"], "benefits": "Supports brain function, supports heart health, aids in weight management"},
            "Cashews": {"nutrition": "Rich in magnesium and healthy fats", "conditions": ["Heart Health", "Bone Strength", "Brain Function", "Blood Pressure"], "benefits": "Supports heart health, strengthens bones, regulates blood pressure"},
            "Mango": {"nutrition": "High in Vitamin A and C", "conditions": ["Immunity Boost", "Skin Health", "Eye Health", "Common Cold"], "benefits": "Boosts immunity, enhances skin health, improves eye health"},
            "Avocado": {"nutrition": "Rich in healthy fats and fiber", "conditions": ["Heart Health", "Skin Health", "Brain Function", "Prostate Health"], "benefits": "Supports heart health, improves skin health, supports brain function"},
            "Berries": {"nutrition": "Rich in antioxidants like anthocyanins, ellagic acid, and resveratrol", "conditions": ["Cancer Management"], "benefits": "May help ward off cancer in the digestive tract"},
            "Cruciferous Vegetables": {"nutrition": "Contain indole-3-carbinol, fiber, and vitamins", "conditions": ["Cancer Management"], "benefits": "May lower the risk of many cancers"},
            "Fish": {"nutrition": "High in omega-3 fatty acids", "conditions": ["Cancer Management"], "benefits": "Has anti-inflammatory properties and may help reduce cancer risk"},
            "Whole Grains": {"nutrition": "Contain fiber and essential nutrients", "conditions": ["Cancer Management"], "benefits": "Support overall health and may help reduce cancer risk"},
            "Legumes": {"nutrition": "Excellent sources of plant-based protein and fiber", "conditions": ["Cancer Management"], "benefits": "Beneficial for maintaining a healthy diet during cancer treatment"},
            "Nuts and Seeds": {"nutrition": "Rich in healthy fats, vitamins, and minerals", "conditions": ["Cancer Management"], "benefits": "Support overall health and may help reduce cancer risk"},
            "Fermented Foods": {"nutrition": "Contain probiotics", "conditions": ["Cancer Management"], "benefits": "Support gut health and may have protective effects against cancer"},
            "Blueberries": {"nutrition": "High in antioxidants, vitamins C and K", "conditions": ["Brain Function", "Heart Health", "Cancer Management"], "benefits": "Improves brain function, supports heart health, may reduce cancer risk"},
            "Chia Seeds": {"nutrition": "Rich in omega-3 fatty acids, fiber, protein", "conditions": ["Weight Management", "Heart Health", "Diabetes"], "benefits": "Supports weight management, promotes heart health, regulates blood sugar"},
            "Quinoa": {"nutrition": "High in protein, fiber, essential amino acids", "conditions": ["Weight Management", "Blood Sugar Regulation", "Heart Health"], "benefits": "Supports weight management, regulates blood sugar, promotes heart health"}
        }

        self.food_images = [
            "path/to/image1.jpg",
            "path/to/image2.jpg",
            "path/to/image3.jpg",
            "path/to/image4.jpg",
            "path/to/image5.jpg"
        ]
        
        self.init_ui()
    
    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel("Food Ni Dawa")
        self.label.setFont(QtGui.QFont("Arial", 18, QtGui.QFont.Bold))
        self.label.setStyleSheet("color: orange;")
        layout.addWidget(self.label)

        self.dropdown = QtWidgets.QComboBox()
        self.dropdown.setStyleSheet("color: #4c8e06; background-color: white;")
        self.dropdown.addItem("Select a Category")
        self.dropdown.addItems(["Food Name", "Health Benefit", "Health Condition"])
        self.dropdown.currentTextChanged.connect(self.update_dropdown)
        layout.addWidget(self.dropdown)

        self.secondary_dropdown = QtWidgets.QComboBox()
        self.secondary_dropdown.setStyleSheet("color: #4c8e06; background-color: white;")
        self.secondary_dropdown.currentTextChanged.connect(self.show_info)
        layout.addWidget(self.secondary_dropdown)

        self.result_area = QtWidgets.QTextEdit()
        self.result_area.setReadOnly(True)
        layout.addWidget(self.result_area)

        self.image_label = QtWidgets.QLabel()
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.show_random_image()
        layout.addWidget(self.image_label)

        self.copyright_label = QtWidgets.QLabel("\u00A9 2025 Copyright WildadGroup All Rights Reserved | MWP5+2G9, Aviation Total Road, Embakasi, Nairobi +254712169319, +254773376433")
        self.copyright_label.setStyleSheet("color: gray;")
        layout.addWidget(self.copyright_label)
        
        self.setLayout(layout)
    
    def update_dropdown(self):
        category = self.dropdown.currentText()
        self.secondary_dropdown.clear()
        if category == "Food Name":
            self.secondary_dropdown.addItems(self.food_data.keys())
        elif category == "Health Benefit":
            self.secondary_dropdown.addItems(set([info["nutrition"] for info in self.food_data.values()]))
        elif category == "Health Condition":
            all_conditions = set(condition for info in self.food_data.values() for condition in info["conditions"])
            self.secondary_dropdown.addItems(sorted(all_conditions))
    
    def show_info(self):
        selected = self.secondary_dropdown.currentText()
        category = self.dropdown.currentText()
        info = ""
        if category == "Food Name" and selected in self.food_data:
            food = self.food_data[selected]
            info = f"Food: {selected}\nNutrition: {food['nutrition']}\nConditions: {', '.join(food['conditions'])}\nBenefits: {food['benefits']}"
        elif category == "Health Benefit":
            foods = [food for food, info in self.food_data.items() if info["nutrition"] == selected]
            info = f"Health Benefit: {selected}\nFoods: {', '.join(foods)}"
        elif category == "Health Condition":
            foods = [food for food, info in self.food_data.items() if selected in info["conditions"]]
            info = f"Health Condition: {selected}\nRecommended Foods: {', '.join(foods)}"
        self.result_area.setText(info)
        self.show_random_image()

    def show_random_image(self):
        image_path = random.choice(self.food_images)
        pixmap = QtGui.QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaled(300, 200, QtCore.Qt.KeepAspectRatio))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = FoodNiDawaApp()
    window.show()
    app.exec_()
