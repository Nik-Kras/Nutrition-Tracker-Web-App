# Nutrition-Tracker-Web-App
This is a web-application that allowes you to get recommendations on daily nutrition intake and helps you to keep track of food you consume daily. These records could be used for self-analysis during weight dropping or muscular mass gaining

# General UI design

Main page sould include:
1.	To the left you see your statistics: weight, height, age, BMI (one line)
2.	Then a bit lower you see recommended nutritions in a list (multiple lines)
3.	Somewhere in the middle you can see your recorded Food and a form to fill a new food intake. They look like big horizontal blocks (like MoFish) 
4.	Right after recorded food you see a form to record a new dish
5.	Lower the form you see a table
    - Total for today: (one line nutrition)
    - Recommended: (one line nutrition)
    - Result: (one line nutrition) + comment if you are gaining / dropping weight. 

![image](https://user-images.githubusercontent.com/26204187/218183704-9c75f4db-28f4-4a29-828a-0f49b97efd33.png)

# User abilities

1.	Calculate recommended daily nutrition intake (kcal, protein, fibra, fat, etc) depending on age, height, weight, how much does a person do sport
  - You will be given with BMI and other body data
  - You will be given with recommended daily nutritions
2.	Record your food:
  - With manual writing of nutritions: kcal, fats, fibra, protein
  - With given DataBase of ingredients / dishes
  - With AI that can estimate your dish to disassemble it to nutritions
3.	View total daily intake, indicating whether it is lower than recommended or not
  - View analysis whether you are going to drop weight or gain weight with such food intake
