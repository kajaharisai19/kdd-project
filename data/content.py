"""
Static content: topic questions and flawed AI explanations.
"""

TOPICS = {
    "Algebra": {
        "icon": "📐",
        "concepts": ["Linear Equations", "Quadratic Equations", "Inequalities", "Functions", "Polynomials"],
        "questions": [
            {
                "q": "Solve for x: 2x + 5 = 13",
                "answer": "x = 4",
                "hint": "Subtract 5 from both sides first, then divide by 2.",
                "concept": "Linear Equations",
                "difficulty": 1,
                "common_errors": ["forgetting to divide by 2", "arithmetic error with subtraction"],
            },
            {
                "q": "Factor the expression: x² + 5x + 6",
                "answer": "(x + 2)(x + 3)",
                "hint": "Find two numbers that multiply to 6 and add to 5.",
                "concept": "Polynomials",
                "difficulty": 2,
                "common_errors": ["wrong sign in factors", "not checking by expanding"],
            },
            {
                "q": "Solve: x² - 4x - 12 = 0",
                "answer": "x = 6 or x = -2",
                "hint": "Factor first, or use the quadratic formula.",
                "concept": "Quadratic Equations",
                "difficulty": 3,
                "common_errors": ["sign error in factoring", "forgetting the negative root"],
            },
            {
                "q": "If f(x) = 3x - 2, find f(f(3))",
                "answer": "19",
                "hint": "First compute f(3), then plug that result back into f(x).",
                "concept": "Functions",
                "difficulty": 3,
                "common_errors": ["only computing f(3) once", "arithmetic error in composition"],
            },
            {
                "q": "Solve the inequality: -3x + 6 > 15",
                "answer": "x < -3",
                "hint": "When dividing by a negative number, flip the inequality sign.",
                "concept": "Inequalities",
                "difficulty": 2,
                "common_errors": ["forgetting to flip inequality sign when dividing by negative"],
            },
        ],
    },
    "Geometry": {
        "icon": "📏",
        "concepts": ["Triangles", "Circles", "Area & Perimeter", "Angles", "Pythagorean Theorem"],
        "questions": [
            {
                "q": "A right triangle has legs of length 3 and 4. What is the hypotenuse?",
                "answer": "5",
                "hint": "Use the Pythagorean theorem: a² + b² = c²",
                "concept": "Pythagorean Theorem",
                "difficulty": 1,
                "common_errors": ["adding instead of squaring", "not taking square root"],
            },
            {
                "q": "Find the area of a circle with radius 7. (Use π ≈ 3.14)",
                "answer": "≈ 153.86 square units",
                "hint": "Area of circle = π × r²",
                "concept": "Circles",
                "difficulty": 2,
                "common_errors": ["using diameter instead of radius", "forgetting to square the radius"],
            },
            {
                "q": "Two angles in a triangle are 45° and 75°. What is the third angle?",
                "answer": "60°",
                "hint": "The interior angles of a triangle always sum to 180°.",
                "concept": "Triangles",
                "difficulty": 1,
                "common_errors": ["assuming angles sum to 90", "arithmetic error"],
            },
            {
                "q": "Find the perimeter of a rectangle with length 12 cm and width 7 cm.",
                "answer": "38 cm",
                "hint": "Perimeter = 2(length + width)",
                "concept": "Area & Perimeter",
                "difficulty": 1,
                "common_errors": ["computing area instead of perimeter", "only adding two sides"],
            },
            {
                "q": "If two parallel lines are cut by a transversal, and one alternate interior angle is 65°, what is the other?",
                "answer": "65°",
                "hint": "Alternate interior angles are equal when lines are parallel.",
                "concept": "Angles",
                "difficulty": 2,
                "common_errors": ["confusing alternate interior with co-interior angles", "subtracting from 180"],
            },
        ],
    },
    "Statistics": {
        "icon": "📊",
        "concepts": ["Mean", "Median", "Mode", "Standard Deviation", "Probability"],
        "questions": [
            {
                "q": "Find the mean of: 4, 8, 6, 5, 3, 2, 8, 9, 2, 5",
                "answer": "5.2",
                "hint": "Add all values and divide by the count.",
                "concept": "Mean",
                "difficulty": 1,
                "common_errors": ["arithmetic error in sum", "dividing by wrong count"],
            },
            {
                "q": "What is the median of: 3, 7, 2, 9, 4, 1, 8?",
                "answer": "4",
                "hint": "Sort the values first, then find the middle one.",
                "concept": "Median",
                "difficulty": 1,
                "common_errors": ["not sorting before finding middle", "confusing median with mean"],
            },
            {
                "q": "A bag has 3 red, 5 blue, 2 green marbles. What is P(blue)?",
                "answer": "1/2 or 0.5",
                "hint": "Probability = favorable outcomes / total outcomes",
                "concept": "Probability",
                "difficulty": 2,
                "common_errors": ["not computing total correctly", "inverting the fraction"],
            },
            {
                "q": "What is the mode of: 4, 5, 4, 6, 7, 4, 8, 5, 5, 4?",
                "answer": "4",
                "hint": "The mode is the most frequently occurring value.",
                "concept": "Mode",
                "difficulty": 1,
                "common_errors": ["confusing mode with mean", "not counting frequencies"],
            },
            {
                "q": "Two fair dice are rolled. What is the probability both show 6?",
                "answer": "1/36 ≈ 0.028",
                "hint": "Multiply individual probabilities for independent events.",
                "concept": "Probability",
                "difficulty": 3,
                "common_errors": ["adding instead of multiplying probabilities", "not recognizing independence"],
            },
        ],
    },
}

FLAWED_EXPLANATIONS = {
    "Algebra": {
        "Linear Equations": {
            "flawed": """To solve 2x + 5 = 13, I simply need to subtract 5 from one side:
x = 13 - 5 = 8
Therefore, x = 8. ✓""",
            "errors": ["forgot to subtract 5 from BOTH sides", "didn't divide by the coefficient 2"],
            "correct": "Subtract 5 from BOTH sides: 2x = 8, then divide both sides by 2: x = 4",
        },
        "Quadratic Equations": {
            "flawed": """For x² - 4x - 12 = 0, I'll factor:
I need two numbers that multiply to -12 and add to +4.
Those are -6 and +2: (x - 6)(x + 2) = 0
So x = 6 or x = -2. Wait, let me re-check: +6 and -2 multiply to -12 ✓ and add to +4 ✓
Therefore x = 6 or x = -2. ✓""",
            "errors": ["mixed up the signs — should look for numbers adding to -4, not +4"],
            "correct": "Need numbers multiplying to -12 and adding to -4: those are -6 and +2, giving (x-6)(x+2)=0, so x=6 or x=-2 (same answers, but wrong reasoning path)",
        },
    },
    "Geometry": {
        "Pythagorean Theorem": {
            "flawed": """To find the hypotenuse with legs 3 and 4:
c = a + b = 3 + 4 = 7
The hypotenuse is 7. ✓""",
            "errors": ["used addition instead of the Pythagorean theorem", "should be c² = a² + b², so c = √(9+16) = √25 = 5"],
            "correct": "Apply a² + b² = c²: 3² + 4² = 9 + 16 = 25, so c = √25 = 5",
        },
        "Circles": {
            "flawed": """Area of a circle with radius 7:
Area = π × d = 3.14 × 7 = 21.98 square units""",
            "errors": ["used diameter formula for circumference, not area", "Area = π × r², not π × r"],
            "correct": "Area = π × r² = 3.14 × 7² = 3.14 × 49 ≈ 153.86 square units",
        },
    },
    "Statistics": {
        "Mean": {
            "flawed": """To find the mean of 4, 8, 6, 5, 3, 2, 8, 9, 2, 5:
I'll add them up: 4+8+6+5+3+2+8+9+2+5 = 52
There are 9 numbers, so mean = 52 ÷ 9 ≈ 5.78""",
            "errors": ["miscounted the numbers — there are 10 values, not 9"],
            "correct": "Sum = 52, count = 10 numbers, so mean = 52 ÷ 10 = 5.2",
        },
        "Probability": {
            "flawed": """For a bag with 3 red, 5 blue, 2 green marbles:
P(blue) = blue marbles / (red + green) = 5 / (3+2) = 5/5 = 1""",
            "errors": ["divided by non-blue marbles only, not total marbles"],
            "correct": "P(blue) = blue / total = 5 / (3+5+2) = 5/10 = 1/2",
        },
    },
}
