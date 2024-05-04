# git_assignment_HeroVired
Question:
Q.1: You are part of a development team working on a Python application called "CalculatorPlus." The application provides basic arithmetic operations, such as addition, subtraction, multiplication, and division. Your task is to implement a new feature that adds support for calculating the square root of a number.

a. Create a repository name: git_assignment_HeroVired
```
steps:  Go to GitHub and log in.
        Click on the "+" icon in the top right corner of the page and select "New repository".
        Enter "git_assignment_HeroVired" in the "Repository name" field.
        Choose the visibility as private.
        Initialize this repository with a README.
        Click on "Create repository".
```
        
b. Create a ‘dev’ branch and add this code.
```

import math

class Calculator:

    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b
    # TODO: Implement the following function to calculate the square root of a number.
    # def square_root(self, x):
        # return math.sqrt(x)
    # You need to uncomment the above function and complete its implementation to add the square root feature. 

if __name__ == "__main__":

    calculator = Calculator()
    num1 = 16
    num2 = 4
    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}") 
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")
    # TODO: Uncomment and test the square root feature.
    # num3 = 25
    # print(f"The square root of {num3} = {calculator.square_root(num3)}") 

```
```
steps:
    Clone the repository:
        git clone https://github.com/Sukhilnair/git_assignment_HeroVired.git
        cd git_assignment_HeroVired
    Create a new branch named dev and switch to it:
        git checkout -b dev
    Create a file calculator.py and update calculator.py with the code provided.
    Add and commit the changes:
        git add calculator.py
        git commit -m "Added code for doing basic calucation of two numbers (16 and 4)"
```

c. Merge this branch with the main branch and make a release of version 1 of the ‘calculator plus app’.
```
steps:
    Switch to the main branch:
        git checkout main
    Merge dev branch into main branch:
        git merge dev
    Tag version 1 release:
        git tag -a v1.0 -m "Version 1.0 release"
    Push changes and tags to GitHub:
        git push origin main --tags
```

        
d. Add any of your classmates as collaborators.
```
steps:
    Go to repository settings on GitHub.
    Click on "Manage access".
    Click on "Invite a collaborator" and add your collaborator.
``` 

e. Implement a feature by creating a new branch called ‘feature/sqrt’. 
```
steps:
    Create a new branch named feature/sqrt and switch to it:
        git checkout -b feature/sqrt
```
        
f. Add the ‘sqrt’ code to it.
```
steps:
    Update calculator.py with the sqrt feature. Uncomment the code which were added in the previos step.
    Add and commit the changes:
        git add calculator.py
        git commit -m "Implemented square root feature in calculator"
```
        
g. While you are working on this feature, imagine that one critical bug is reported in the main branch, and you need to switch back to the ‘dev’ branch, create fixes, and apply them while keeping your ‘feature/sqrt’ branch up-to-date. For this, you need to create

The bug fixation is in the divide function and the new function should be: def divide(self, a, b):

if b == 0:

raise ValueError("Cannot divide by zero.")

return a / b
```
steps:
    Switch back to the dev branch:
        git checkout dev
    Update the divide function with the provided fix.
    Add and commit the changes:
        git add calculator.py
        git commit -m "Fixed divide function bug"
    Merge the changes into the feature/sqrt branch:
        git checkout feature/sqrt
        git merge dev
```

h. After completing the feature implementation and ensuring that the application works correctly, create a pull request targeting the main branch.
```
steps:
    Push the feature/sqrt branch to GitHub:
        git push origin feature/sqrt
    Create a pull request on GitHub:
        Title: Implement Square Root Feature
        Description: Added square root feature to the Calculator class.
        Target branch: main
```


i. Request a code review from a team member and make any necessary improvements based on the review feedback.

j. Once the code reviewer approves your pull request, merge the "feature/sqrt" branch into the ‘dev’ branch.

k. Finally, do the testing in the ‘dev’ branch itself and merge it into the ‘main’ branch and create a ‘version 2’ release.
```
steps:
    Switch to the dev branch:
        git checkout dev
    Test the changes:
        python3 calculator.py
    Switch to the main branch:
        git checkout main
    Merge the dev branch into the main branch:
        git merge dev
    Tag version 2 release:
        git tag -a v2.0 -m "Version 2.0 release"
    Push changes and tags to GitHub:
        git push origin main --tags
```
Q.2: For a project that deals with large binary files, integrate Git LFS (Large File Storage) to handle these files efficiently. Demonstrate how to add, commit, and push binary files to the repository, ensuring they are tracked by Git LFS correctly. Clone the repository on another machine to verify that the binary files are downloaded correctly.

In the repository ‘git_assignment_HeroVired’, create a branch ‘lfs’. Upload any large file whose size is over ‘200mb’ and try to push this file into the repository.

```
Step 1: Install Git LFS
    Install git lfs from it's official website.
```
```
Step 2: Create a lfs branch and initialize Git LFS in your repository.
    Clone the Repository:
        git clone https://github.com/Sukhilnair/git_assignment_HeroVired.git
    Navigate to your repository directory
        cd git_assignment_HeroVired
    Create a new branch named lfs and switch to it:
        git checkout -b lfs
    Initialize Git LFS by running:
        git lfs install
```
```
Step 3: Track large files using Git LFS
    To track large files, you need to specify the file extensions you want Git LFS to manage:
        git lfs track "*.mkv"
```
```
Step 4: Add, commit, and push large files
    Now, you can add, commit, and push your large binary files.
        git add Complete_Git_and_GitHub_Tutorial_for_Beginners.mkv
        git commit -m "Add large binary file"
        git push origin lfs
```
```
Step 5: Clone the repository on another machine
    To verify that the binary files are downloaded correctly, clone the repository on another machine:
        git clone https://github.com/Sukhilnair/git_assignment_HeroVired.git
        git checkout lfs
```

Q.3: In this same GitHub repository, create a new branch ‘geometry-calculator’, we'll work on a simple Python program that calculates the area of a circle and the area of a rectangle. We'll use Git stash to switch between working on multiple features (calculating circle area and calculating rectangle area) without committing incomplete changes.

```
import math

class GeometryCalculator:

    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2

    def calculate_rectangle_area(self, length, width):
        return length * width

if __name__ == "__main__":
calculator = GeometryCalculator()
# TODO: Implement the feature to calculate the area of a circle
# radius = 5
# print(f"The area of the circle with radius {radius} = {calculator.calculate_circle_area(radius)}")

# TODO: Implement the feature to calculate the area of a rectangle # length = 10
# width = 6
# print(f"The area of the rectangle with length {length} and width {width} ={calculator.calculate_rectangle_area(length, width)}")
```

Workflow Steps:

a. Create a New Branch:

- Create a new branch named "feature/circle-area" to work on the circle area feature

```
    git checkout -b feature/circle-area
```

b. Stash Changes for Circle Area Feature:

- Before committing the changes, stash them using git stash to save the incomplete feature implementation.

- Verify that the working directory is clean

```
    git stash
    git status
```

c. Create a New Branch for Rectangle Area Feature:

- Create a new branch named "feature/rectangle-area" to work on the rectangle area
```
    git checkout -b feature/rectangle-area
```

d. Stash Changes for Rectangle Area Feature:

- Before committing the changes, stash them using git stash to save the incomplete feature implementation.

- Verify that the working directory is clean

```
    git stash
    git status 

```

e. Switch Back to Circle Area Branch:

- Switch back to the "feature/circle-area" branch to continue working on the circle area feature.

- Retrieve the stashed changes

- Complete the circle area feature implementation and save the changes. f. Commit and Push Circle Area Feature:

```
    git checkout feature/circle-area
    git stash pop
    Modifiy the above code for circle area feature.
    git add .
    git commit -m "Implemented circle area feature"
    git push origin feature/circle-area
```
g. Switch Back to Rectangle Area Branch:

- Switch back to the "feature/rectangle-area" branch to continue working on the rectangle area feature.

- Retrieve the stashed changes

- Complete the rectangle area feature implementation and save the changes. h. Commit and Push Rectangle Area Feature
```
    git checkout feature/circle-area
    git stash pop
    Modifiy the above code for rectangle area feature.
    git add .
    git commit -m "Implemented circle area feature"
    git push origin feature/circle-area
```


i. Create Pull Requests:

- Create a pull request to the ‘dev’ branch.
```
1. Create a pull request for the circle area feature (`feature/circle-area`) into the `dev` branch.
    - Navigate to your repository on GitHub and click on the "Pull Requests" tab.
    - Click on "New pull request".
    - Choose the `dev` branch as the base branch and `feature/circle-area` as the compare branch.
    - Click on "Create pull request".
    - Provide a title and description for your pull request.
    - Click on "Create pull request" to finalize.

2. Create a pull request for the rectangle area feature (`feature/rectangle-area`) into the `dev` branch.
    - Navigate to your repository on GitHub and click on the "Pull Requests" tab.
    - Click on "New pull request".
    - Choose the `dev` branch as the base branch and `feature/rectangle-area` as the compare branch.
    - Click on "Create pull request".
    - Provide a title and description for your pull request.
    - Click on "Create pull request" to finalize.

```

j. Review and Merge

- Have another team member or reviewer review your pull requests. - After receiving approval, merge both pull requests into the main branch.