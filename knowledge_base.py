"""
Curated Technical Knowledge Base for Technical Learning Content Generator.
Provides verified, high-quality technical content across Python, SQL, OOP,
Data Structures, Machine Learning, and Generative AI for Beginner, Intermediate,
and Advanced difficulty levels.
"""

from typing import Dict, Any, Optional

KNOWLEDGE_BASE: Dict[str, Dict[str, Dict[str, Any]]] = {
    "Python": {
        "List Comprehensions": {
            "Beginner": {
                "definition": "A list comprehension is a concise and elegant way in Python to create new lists from existing iterables like lists, tuples, or ranges in a single line of code.",
                "how_it_works": "Python evaluates an expression for each element in an iterable loop, optionally filtering items with an 'if' clause, and constructs the resulting list in optimized C-level bytecode.",
                "important_points": [
                    "Syntax: `[expression for item in iterable if condition]`",
                    "More readable and concise than traditional `for` loops with `.append()`",
                    "Often executes faster than standard loops due to internal optimization",
                    "Returns a new list without modifying the original data source"
                ],
                "code": (
                    "# Creating a list of even squares using List Comprehension\n"
                    "numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n\n"
                    "# Traditional approach:\n"
                    "# evens = []\n"
                    "# for x in numbers:\n"
                    "#     if x % 2 == 0:\n"
                    "#         evens.append(x ** 2)\n\n"
                    "# Pythonic List Comprehension:\n"
                    "even_squares = [x ** 2 for x in numbers if x % 2 == 0]\n\n"
                    "print('Original numbers:', numbers)\n"
                    "print('Even squares:', even_squares)  # Output: [4, 16, 36, 64, 100]\n"
                ),
                "code_explanation": [
                    "Line 2: We define a list of integers from 1 to 10.",
                    "Line 11: `for x in numbers` iterates over every element `x`.",
                    "Line 11: `if x % 2 == 0` filters out odd numbers, keeping only evens.",
                    "Line 11: `x ** 2` squares the filtered elements and packages them into a new list."
                ],
                "common_mistakes": [
                    "Over-nesting multiple comprehensions into one unreadable line (violates PEP 8 readability).",
                    "Using list comprehensions for side-effects (like calling `print()`) instead of a regular `for` loop.",
                    "Forgetting that list comprehensions consume memory immediately; for massive data, use generator expressions `(...)`."
                ],
                "mcq": {
                    "question": "What is the primary output of `[x * 2 for x in range(4) if x > 1]`?",
                    "options": [
                        "A) [0, 2, 4, 6]",
                        "B) [4, 6]",
                        "C) [2, 4, 6]",
                        "D) [2, 4]"
                    ],
                    "correct_answer": "B",
                    "explanation": "range(4) produces 0, 1, 2, 3. The condition `x > 1` selects 2 and 3. Multiplying each by 2 yields `[4, 6]`."
                },
                "short_question": {
                    "question": "How does a generator expression differ from a list comprehension in terms of memory usage?",
                    "answer": "A list comprehension builds the entire list in memory immediately in square brackets `[]`, whereas a generator expression with parentheses `()` yields items lazily on demand, using constant memory O(1)."
                },
                "summary": [
                    "List comprehensions offer a clean syntax: `[expr for item in iter if cond]`.",
                    "They replace multi-line boilerplate `for` loops and `.append()` calls.",
                    "Keep them readable and avoid cramming complex logic into a single line."
                ]
            },
            "Intermediate": {
                "definition": "Intermediate list comprehensions encompass nested iteration, multi-condition filtering, and flattening two-dimensional matrices into single-dimensional vectors efficiently.",
                "how_it_works": "Nested loops in comprehensions execute from left to right, exactly matching the order of nested standard `for` loops, creating Cartesian products or flattened sequences.",
                "important_points": [
                    "Left-to-right clause ordering: outer loop first, then inner loop.",
                    "Can be used for matrix transpositions and flattening nested structures.",
                    "Can combine ternary conditional expressions: `[x if x > 0 else 0 for x in nums]`.",
                    "Supports dictionary comprehensions `{k: v for k, v in pairs}` as well."
                ],
                "code": (
                    "# Flattening a 2D matrix (list of lists)\n"
                    "matrix = [\n"
                    "    [1, 2, 3],\n"
                    "    [4, 5, 6],\n"
                    "    [7, 8, 9]\n"
                    "]\n\n"
                    "# Outer loop: 'for row in matrix', Inner loop: 'for val in row'\n"
                    "flattened = [val for row in matrix for val in row]\n\n"
                    "print('Original Matrix:', matrix)\n"
                    "print('Flattened:', flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
                ),
                "code_explanation": [
                    "Line 2: A 3x3 two-dimensional list representing a matrix.",
                    "Line 9: First `for row in matrix` iterates through each row.",
                    "Line 9: Second `for val in row` iterates through each integer in that row.",
                    "Line 9: `val` collects each integer into the flat 1D list."
                ],
                "common_mistakes": [
                    "Inverting the order of nested loops (putting the inner loop first causes `NameError: name 'row' is not defined`).",
                    "Confusing filtering `if` at the end with ternary replacement `if-else` before the `for` keyword."
                ],
                "mcq": {
                    "question": "Which comprehension correctly replaces negative numbers with 0 in `[-1, 2, -3, 4]`?",
                    "options": [
                        "A) [x for x in nums if x > 0 else 0]",
                        "B) [x if x >= 0 else 0 for x in nums]",
                        "C) [0 if x < 0 for x in nums]",
                        "D) [x for x in nums if x >= 0]"
                    ],
                    "correct_answer": "B",
                    "explanation": "When using `if-else` as an expression to transform values, it must precede the `for` clause: `[x if x >= 0 else 0 for x in nums]`."
                },
                "short_question": {
                    "question": "What is the order of execution in `[item for sublist in main_list for item in sublist]`?",
                    "answer": "It executes strictly from left to right: first iterates over `sublist` in `main_list`, and for each `sublist`, iterates over `item` in that `sublist`."
                },
                "summary": [
                    "Order of nested loops mirrors standard nested loop syntax (outer first, inner second).",
                    "Use ternary expressions `x if cond else y` before the `for` keyword for value transformation.",
                    "For deep nesting (>2 levels), favor explicit functions or generator pipelines for readability."
                ]
            },
            "Advanced": {
                "definition": "Advanced list comprehensions involve bytecode disassembly, AST optimizations, profiling memory ceilings vs generator pipelines, and handling thread-safety in shared scopes.",
                "how_it_works": "In Python 3, comprehensions run in their own isolated function scope (creating a frame at compile time) preventing variable leaking into outer namespaces.",
                "important_points": [
                    "Scope isolation: iterator variables do not leak into outer function/global namespace in Python 3.",
                    "Generates specialized `LIST_APPEND` bytecode instructions in CPython.",
                    "Direct pre-allocation optimizations occur when iterable size hint is known.",
                    "Heavy parallel data transforms should transition to `multiprocessing.Pool.imap` or Vectorized NumPy."
                ],
                "code": (
                    "import dis\n\n"
                    "def comprehension_demo():\n"
                    "    return [x * 2 for x in range(1000)]\n\n"
                    "# Inspect bytecode disassembly\n"
                    "print('Bytecode instructions:')\n"
                    "dis.dis(comprehension_demo)\n"
                ),
                "code_explanation": [
                    "Line 1: Imports Python's built-in `dis` module for inspecting CPython bytecode.",
                    "Line 4: Defines a standard list comprehension function.",
                    "Line 8: Disassembles the function, revealing `BUILD_LIST` and fast `LIST_APPEND` instructions."
                ],
                "common_mistakes": [
                    "Expecting comprehension loop variables to remain accessible outside the comprehension (isolated scope in Python 3).",
                    "Attempting asynchronous comprehension without `async for` inside an `async def` context."
                ],
                "mcq": {
                    "question": "Why does a list comprehension in Python 3 prevent variable leakage into the enclosing scope?",
                    "options": [
                        "A) It uses global variables with random suffixes",
                        "B) It executes in its own specialized compiler-generated function scope",
                        "C) It converts all variables into immutable tuples",
                        "D) It runs as a separate OS process"
                    ],
                    "correct_answer": "B",
                    "explanation": "In Python 3, comprehensions are compiled with their own code object and run in an isolated local frame, preventing iterator variable leakage."
                },
                "short_question": {
                    "question": "Under what condition would a list comprehension outperform `map()` with a lambda function?",
                    "answer": "List comprehensions avoid the overhead of repeated Python function call stack frames incurred by `lambda` inside `map()`, utilizing C-level `LIST_APPEND` instructions."
                },
                "summary": [
                    "CPython optimizes comprehensions using specialized `BUILD_LIST` and `LIST_APPEND` opcodes.",
                    "Comprehensions are scope-isolated in Python 3, ensuring clean namespaces.",
                    "Benchmark against NumPy or generator expressions when scaling to millions of items."
                ]
            }
        },
        "Decorators": {
            "Beginner": {
                "definition": "A decorator in Python is a design pattern and language feature that allows you to dynamically modify or extend the behavior of a function without altering its actual source code.",
                "how_it_works": "A decorator takes a target function as an argument, defines an inner 'wrapper' function that adds behavior before and after calling the target, and returns this wrapper.",
                "important_points": [
                    "Denoted using the `@decorator_name` syntactic sugar syntax above function definitions",
                    "Functions in Python are 'first-class citizens', meaning they can be passed as arguments, assigned to variables, and returned from other functions",
                    "Commonly used for logging, access control, timing execution, and caching"
                ],
                "code": (
                    "def my_logger(func):\n"
                    "    def wrapper(*args, **kwargs):\n"
                    "        print(f'[LOG] Executing function: {func.__name__}')\n"
                    "        result = func(*args, **kwargs)\n"
                    "        print(f'[LOG] Completed function: {func.__name__}')\n"
                    "        return result\n"
                    "    return wrapper\n\n"
                    "@my_logger\n"
                    "def greet(name):\n"
                    "    print(f'Hello, {name}!')\n\n"
                    "greet('Alice')\n"
                ),
                "code_explanation": [
                    "Line 1: `my_logger` accepts a function `func` as an input.",
                    "Line 2: `wrapper(*args, **kwargs)` accepts any positional and keyword arguments.",
                    "Line 3-5: Logs before and after executing the wrapped function `func`.",
                    "Line 7: Returns the `wrapper` function object.",
                    "Line 9: `@my_logger` is equivalent to writing `greet = my_logger(greet)`."
                ],
                "common_mistakes": [
                    "Forgetting to `return result` from inside the wrapper, causing the decorated function to return `None`.",
                    "Omitting `*args, **kwargs`, which breaks compatibility when decorating functions with parameters."
                ],
                "mcq": {
                    "question": "What is `@my_decorator` placed directly above `def calculate():` functionally equivalent to?",
                    "options": [
                        "A) calculate.decorate(my_decorator)",
                        "B) calculate = my_decorator(calculate)",
                        "C) my_decorator = calculate()",
                        "D) import my_decorator"
                    ],
                    "correct_answer": "B",
                    "explanation": "The `@` decorator syntax is syntactic sugar for passing the defined function into the decorator and reassigning the identifier: `calculate = my_decorator(calculate)`."
                },
                "short_question": {
                    "question": "Why is `functools.wraps` recommended when authoring custom decorators?",
                    "answer": "`functools.wraps` preserves the original function's metadata, such as its name (`__name__`), docstring (`__doc__`), and module."
                },
                "summary": [
                    "Decorators wrap functions to extend functionality cleanly.",
                    "Syntactic sugar: `@decorator` equals `func = decorator(func)`.",
                    "Always capture `*args, **kwargs` and return the inner result."
                ]
            }
        }
    },
    "SQL": {
        "Joins": {
            "Beginner": {
                "definition": "An SQL JOIN is an operation used to combine rows from two or more relational tables based on a related common column between them.",
                "how_it_works": "The database query engine evaluates the join condition (such as matching primary and foreign keys) and constructs a virtual result set containing combined records.",
                "important_points": [
                    "INNER JOIN: Returns only rows that have matching values in both tables.",
                    "LEFT JOIN (or LEFT OUTER JOIN): Returns all rows from the left table, plus matched rows from the right table (NULL if no match).",
                    "RIGHT JOIN: Returns all rows from the right table, plus matched rows from the left table.",
                    "FULL OUTER JOIN: Returns all records when there is a match in either left or right table."
                ],
                "code": (
                    "-- Schema: Students(id, name), Enrollments(id, student_id, course_name)\n\n"
                    "-- 1. INNER JOIN: Only students enrolled in courses\n"
                    "SELECT s.id, s.name, e.course_name\n"
                    "FROM Students s\n"
                    "INNER JOIN Enrollments e ON s.id = e.student_id;\n\n"
                    "-- 2. LEFT JOIN: All students, even if not enrolled in any course\n"
                    "SELECT s.name, COALESCE(e.course_name, 'No Course Enrolled') AS course\n"
                    "FROM Students s\n"
                    "LEFT JOIN Enrollments e ON s.id = e.student_id;\n"
                ),
                "code_explanation": [
                    "Line 4: Selects specific columns using table aliases `s` and `e`.",
                    "Line 6: `INNER JOIN Enrollments e ON s.id = e.student_id` joins on matching student IDs.",
                    "Line 10: `LEFT JOIN` preserves all rows in `Students` even if an enrolled course doesn't exist.",
                    "Line 9: `COALESCE` handles `NULL` values gracefully by substituting default text."
                ],
                "common_mistakes": [
                    "Forgetting the `ON` clause, which inadvertently produces a Cartesian product (CROSS JOIN) multiplying all rows.",
                    "Filtering the right table of a `LEFT JOIN` in the `WHERE` clause instead of the `ON` clause, unintentionally turning it into an `INNER JOIN`."
                ],
                "mcq": {
                    "question": "Which JOIN returns all records from Table A and only the matching records from Table B?",
                    "options": [
                        "A) RIGHT JOIN",
                        "B) FULL OUTER JOIN",
                        "C) LEFT JOIN",
                        "D) CROSS JOIN"
                    ],
                    "correct_answer": "C",
                    "explanation": "A LEFT JOIN keeps every single row from the left table (Table A) regardless of whether a match exists in the right table (Table B)."
                },
                "short_question": {
                    "question": "What value appears in columns from the right table when a LEFT JOIN finds no match?",
                    "answer": "`NULL` is inserted for all non-matching columns originating from the right table."
                },
                "summary": [
                    "JOINs combine relational data across normalized tables.",
                    "INNER JOIN filters for exact matches in both tables.",
                    "LEFT JOIN retains all left records and pads missing right records with NULL."
                ]
            },
            "Intermediate": {
                "definition": "Intermediate SQL joins involve multi-table joins, self-joins for hierarchical tree data, cross joins, and query optimization via indexing foreign keys.",
                "how_it_works": "The query optimizer uses execution plans (Hash Join, Nested Loop, or Merge Join) based on table statistics, cardinalities, and existing index coverage.",
                "important_points": [
                    "Self Join: Joining a table to itself (e.g. Employee table with Manager ID).",
                    "Hash Join vs Nested Loop: Database execution strategies chosen by the query planner.",
                    "Foreign key indexing is critical for preventing full-table scans during joins.",
                    "Anti-joins: Using `LEFT JOIN ... WHERE right.id IS NULL` to find unmatched records."
                ],
                "code": (
                    "-- Self-Join: Finding each Employee and their Manager's name\n"
                    "-- Table: Employees(emp_id, emp_name, manager_id)\n\n"
                    "SELECT \n"
                    "    e.emp_name AS Employee,\n"
                    "    COALESCE(m.emp_name, 'Top Executive') AS Manager\n"
                    "FROM Employees e\n"
                    "LEFT JOIN Employees m ON e.manager_id = m.emp_id;\n"
                ),
                "code_explanation": [
                    "Line 5: Alias `e` represents the employee row.",
                    "Line 6: Alias `m` represents the manager row from the same table.",
                    "Line 8: Joins where employee's `manager_id` matches the manager's `emp_id`.",
                    "Line 6: `COALESCE` handles top executives who have no manager (manager_id is NULL)."
                ],
                "common_mistakes": [
                    "Failing to alias tables in self-joins, causing column ambiguity errors.",
                    "Ignoring index creation on foreign key columns, causing severe query degradation on large tables."
                ],
                "mcq": {
                    "question": "How do you retrieve records from Table A that have NO corresponding entry in Table B?",
                    "options": [
                        "A) SELECT * FROM A INNER JOIN B ON A.id = B.id",
                        "B) SELECT * FROM A LEFT JOIN B ON A.id = B.id WHERE B.id IS NULL",
                        "C) SELECT * FROM A RIGHT JOIN B ON A.id = B.id WHERE A.id IS NOT NULL",
                        "D) SELECT * FROM A CROSS JOIN B"
                    ],
                    "correct_answer": "B",
                    "explanation": "A LEFT JOIN combined with a `WHERE B.id IS NULL` filter is an Anti-Join pattern that finds orphaned records in Table A."
                },
                "short_question": {
                    "question": "What is the computational complexity difference between a Nested Loop Join and a Hash Join?",
                    "answer": "A Nested Loop Join takes O(M * N) in the worst unindexed case, whereas a Hash Join builds an in-memory hash table in O(M) and probes in O(N), totaling O(M + N)."
                },
                "summary": [
                    "Self-joins resolve hierarchical or recursive relationships within a single table.",
                    "Anti-joins find unmatched records using `LEFT JOIN ... WHERE right.id IS NULL`.",
                    "Always index foreign keys to ensure the optimizer can choose Hash or Merge joins."
                ]
            }
        }
    },
    "OOP": {
        "Polymorphism": {
            "Beginner": {
                "definition": "Polymorphism (meaning 'many forms' in Greek) is an OOP concept where different classes can implement the same method name, allowing uniform interaction through a shared interface.",
                "how_it_works": "Python uses duck typing ('if it walks like a duck and quacks like a duck, it is a duck') and dynamic method dispatch to resolve method calls on objects at runtime.",
                "important_points": [
                    "Allows client code to call the same method name on diverse object instances",
                    "Eliminates clumsy `if-elif` type-checking cascades",
                    "Achieved through method overriding in subclasses or duck typing in Python",
                    "Core foundation of writing extensible, loosely coupled software"
                ],
                "code": (
                    "class PaymentProcessor:\n"
                    "    def process_payment(self, amount: float):\n"
                    "        raise NotImplementedError('Subclasses must implement process_payment')\n\n"
                    "class CreditCardPayment(PaymentProcessor):\n"
                    "    def process_payment(self, amount: float):\n"
                    "        return f'Charged ${amount:.2f} to Credit Card.'\n\n"
                    "class UPIPayment(PaymentProcessor):\n"
                    "    def process_payment(self, amount: float):\n"
                    "        return f'Transferred ${amount:.2f} via UPI Instant Transfer.'\n\n"
                    "# Polymorphic execution\n"
                    "methods = [CreditCardPayment(), UPIPayment()]\n"
                    "for method in methods:\n"
                    "    print(method.process_payment(49.99))\n"
                ),
                "code_explanation": [
                    "Line 1: `PaymentProcessor` acts as an abstract base contract.",
                    "Line 5, 9: Subclasses override `process_payment` with custom implementations.",
                    "Line 14-16: Loop treats both objects uniformly without checking their specific types."
                ],
                "common_mistakes": [
                    "Writing extensive `isinstance(obj, TypeA)` checks instead of relying on polymorphic dispatch.",
                    "Changing method signatures (different parameter counts) in subclasses, breaking the expected contract."
                ],
                "mcq": {
                    "question": "Which phrase describes Python's approach to polymorphism without requiring explicit interfaces?",
                    "options": [
                        "A) Static typing",
                        "B) Duck typing",
                        "C) Monomorphic binding",
                        "D) Explicit casting"
                    ],
                    "correct_answer": "B",
                    "explanation": "Python relies on duck typing: if an object provides the expected method or attribute, Python executes it regardless of class inheritance."
                },
                "short_question": {
                    "question": "What is the difference between method overloading and method overriding?",
                    "answer": "Overriding occurs when a subclass replaces a method inherited from its parent. Overloading is defining multiple methods with the same name but different parameters (simulated in Python via default arguments or `functools.singledispatch`)."
                },
                "summary": [
                    "Polymorphism enables interchangeable components with consistent method signatures.",
                    "Subclasses override base methods to supply specialized behavior.",
                    "Reduces coupling and makes systems easy to extend without altering existing caller logic."
                ]
            }
        }
    },
    "Data Structures": {
        "Binary Search Trees": {
            "Beginner": {
                "definition": "A Binary Search Tree (BST) is a hierarchical node-based data structure where each node has at most two children, and all values in the left subtree are smaller than the node, while all values in the right subtree are greater.",
                "how_it_works": "Search, insertion, and deletion operate by comparing target keys with the current node and traversing either left or right, halving search space at each step in balanced trees.",
                "important_points": [
                    "BST property: Left Child < Current Node < Right Child",
                    "Average time complexity: O(log N) for Search, Insertion, and Deletion",
                    "Worst-case time complexity: O(N) if elements are inserted in sorted order (skewed tree)",
                    "In-order traversal of a BST visits nodes in strictly ascending sorted order"
                ],
                "code": (
                    "class Node:\n"
                    "    def __init__(self, key):\n"
                    "        self.left = None\n"
                    "        self.right = None\n"
                    "        self.val = key\n\n"
                    "def insert(root, key):\n"
                    "    if root is None:\n"
                    "        return Node(key)\n"
                    "    if key < root.val:\n"
                    "        root.left = insert(root.left, key)\n"
                    "    else:\n"
                    "        root.right = insert(root.right, key)\n"
                    "    return root\n\n"
                    "# In-order traversal produces sorted output\n"
                    "def inorder(root):\n"
                    "    return inorder(root.left) + [root.val] + inorder(root.right) if root else []\n\n"
                    "# Build sample tree\n"
                    "root = Node(50)\n"
                    "for val in [30, 70, 20, 40, 60, 80]:\n"
                    "    insert(root, val)\n\n"
                    "print('Sorted traversal:', inorder(root))  # [20, 30, 40, 50, 60, 70, 80]\n"
                ),
                "code_explanation": [
                    "Line 1-5: Defines tree node storing `left`, `right`, and `val`.",
                    "Line 7-14: Recursively inserts keys: smaller values go left, larger go right.",
                    "Line 17: In-order traversal (Left, Root, Right) naturally extracts sorted keys."
                ],
                "common_mistakes": [
                    "Inserting strictly sorted data into an unbalanced BST, degrading it into a linked list with O(N) operations.",
                    "Confusing a standard Binary Tree (any children arrangement) with a Binary Search Tree (strict ordering property)."
                ],
                "mcq": {
                    "question": "Which traversal of a Binary Search Tree produces values in ascending sorted order?",
                    "options": [
                        "A) Pre-order (Root, Left, Right)",
                        "B) Post-order (Left, Right, Root)",
                        "C) In-order (Left, Root, Right)",
                        "D) Level-order (BFS)"
                    ],
                    "correct_answer": "C",
                    "explanation": "In-order traversal visits the left subtree (all smaller keys), then the node itself, then the right subtree (larger keys), resulting in sorted order."
                },
                "short_question": {
                    "question": "What is the worst-case time complexity of searching in an unbalanced BST, and why?",
                    "answer": "O(N), because if elements are inserted in ascending or descending sorted order, the tree degenerates into a single linear chain resembling a linked list."
                },
                "summary": [
                    "BST maintains Left < Parent < Right invariant across all subtrees.",
                    "Average search is O(log N), ideal for fast lookup and dynamic sets.",
                    "Self-balancing trees (AVL, Red-Black) prevent O(N) degeneration."
                ]
            }
        }
    },
    "Machine Learning": {
        "Bias-Variance Tradeoff": {
            "Beginner": {
                "definition": "The Bias-Variance Tradeoff is a fundamental machine learning principle describing the conflict between a model's simplicity (bias) and sensitivity to training data fluctuations (variance).",
                "how_it_works": "Total prediction error decomposes into Bias² + Variance + Irreducible Noise. Increasing model complexity reduces bias but increases variance; optimal generalization lies at the minimum of total test error.",
                "important_points": [
                    "High Bias (Underfitting): Model is overly simplistic and misses underlying patterns (e.g., linear regression on quadratic data).",
                    "High Variance (Overfitting): Model memorizes training noise and fails to generalize to unseen test data.",
                    "Goal: Balance complexity to minimize total validation error.",
                    "Techniques to reduce variance: Regularization (L1/L2), Cross-Validation, Ensembling, Feature Pruning."
                ],
                "code": (
                    "# Conceptual demonstration using scikit-learn\n"
                    "import numpy as np\n"
                    "from sklearn.linear_model import LinearRegression\n"
                    "from sklearn.preprocessing import PolynomialFeatures\n"
                    "from sklearn.metrics import mean_squared_error\n\n"
                    "# Synthetic non-linear data\n"
                    "X = np.linspace(-3, 3, 30).reshape(-1, 1)\n"
                    "y = X.ravel()**2 + np.random.normal(0, 1, 30)\n\n"
                    "# High Bias Model (Degree 1 - Linear)\n"
                    "linear_model = LinearRegression().fit(X, y)\n"
                    "print('Degree 1 MSE:', round(mean_squared_error(y, linear_model.predict(X)), 2))\n\n"
                    "# Balanced Model (Degree 2 - Quadratic)\n"
                    "poly = PolynomialFeatures(degree=2)\n"
                    "X_poly = poly.fit_transform(X)\n"
                    "quad_model = LinearRegression().fit(X_poly, y)\n"
                    "print('Degree 2 MSE:', round(mean_squared_error(y, quad_model.predict(X_poly)), 2))\n"
                ),
                "code_explanation": [
                    "Line 8-9: Generates noisy quadratic data ($y = x^2 + \\epsilon$).",
                    "Line 12-13: Linear fit shows high bias (underfitting) with high training error.",
                    "Line 16-19: Degree 2 polynomial captures the underlying physics accurately without over-memorizing noise."
                ],
                "common_mistakes": [
                    "Assuming high training accuracy implies a great model (often indicates severe overfitting / high variance).",
                    "Thinking bias can be reduced without any risk of increasing variance."
                ],
                "mcq": {
                    "question": "A model with very low training error but very high test error is suffering from what problem?",
                    "options": [
                        "A) High Bias (Underfitting)",
                        "B) High Variance (Overfitting)",
                        "C) Zero Irreducible Error",
                        "D) Data Leakage only"
                    ],
                    "correct_answer": "B",
                    "explanation": "High variance means the model learned spurious noise in the training set, causing significant failure on unseen test data (overfitting)."
                },
                "short_question": {
                    "question": "Name two methods commonly used to mitigate high variance in deep neural networks or tree models.",
                    "answer": "1. Dropout and L2 weight decay in neural networks; 2. Bagging/Random Forests, tree depth limits, or pruning in decision trees."
                },
                "summary": [
                    "Total Error = Bias² + Variance + Irreducible Noise.",
                    "Underfitting = high bias; Overfitting = high variance.",
                    "Optimal model complexity yields minimum test set error."
                ]
            }
        }
    },
    "Generative AI": {
        "Transformers and Attention": {
            "Beginner": {
                "definition": "The Transformer is a deep learning neural architecture introduced in 2017 that processes sequential text using self-attention mechanisms in parallel, forming the foundation of modern Large Language Models (LLMs).",
                "how_it_works": "Instead of processing words step-by-step like RNNs, self-attention computes query, key, and value vectors for all tokens simultaneously, allowing each word to weigh its contextual relevance to every other word in the sequence.",
                "important_points": [
                    "Self-Attention calculates relevance weights between pairs of tokens in parallel.",
                    "Positional Encodings inject token order information into parallel representations.",
                    "Eliminates sequential bottleneck of recurrent networks (RNNs/LSTMs), enabling massive GPU parallelization.",
                    "Powers GPT-4, Gemini, Claude, LLaMA, and FLAN-T5 models."
                ],
                "code": (
                    "# Inspecting PyTorch MultiheadAttention conceptually\n"
                    "import torch\n"
                    "import torch.nn as nn\n\n"
                    "# Sequence length: 4 tokens, Embedding dim: 16, 2 attention heads\n"
                    "embed_dim = 16\n"
                    "num_heads = 2\n"
                    "attention_layer = nn.MultiheadAttention(embed_dim, num_heads, batch_first=True)\n\n"
                    "# Batch of 1 sequence with 4 tokens\n"
                    "token_embeddings = torch.randn(1, 4, embed_dim)\n\n"
                    "# Self-attention: Query, Key, and Value are all from the same input\n"
                    "attn_output, attn_weights = attention_layer(\n"
                    "    query=token_embeddings,\n"
                    "    key=token_embeddings,\n"
                    "    value=token_embeddings\n"
                    ")\n\n"
                    "print('Output shape:', attn_output.shape)    # [1, 4, 16]\n"
                    "print('Attention weights shape:', attn_weights.shape)  # [1, 4, 4]\n"
                ),
                "code_explanation": [
                    "Line 8: Instantiates PyTorch's `MultiheadAttention` module.",
                    "Line 11: Creates synthetic token embeddings representing 4 words in a sentence.",
                    "Line 14-18: Performs self-attention where Query, Key, and Value matrices derive from the same embeddings.",
                    "Line 21: Attention weights indicate how much token i attends to token j."
                ],
                "common_mistakes": [
                    "Thinking transformers process words sequentially one-by-one during training (they process entire sequences concurrently).",
                    "Confusing encoder-only models (BERT), decoder-only models (GPT), and encoder-decoder models (T5 / FLAN-T5)."
                ],
                "mcq": {
                    "question": "What is the primary computational advantage of Transformers over RNNs during training?",
                    "options": [
                        "A) They require zero memory",
                        "B) They allow parallel processing of all tokens rather than sequential recurrence",
                        "C) They don't require training data",
                        "D) They only work with English text"
                    ],
                    "correct_answer": "B",
                    "explanation": "Self-attention enables parallel processing of full sequences during training on GPUs, removing the sequential step-by-step dependency of RNNs."
                },
                "short_question": {
                    "question": "What are the three core vectors computed for each token in scaled dot-product attention?",
                    "answer": "Query (Q), Key (K), and Value (V) vectors."
                },
                "summary": [
                    "Transformers rely on Self-Attention to capture long-range contextual relationships.",
                    "Parallel sequence processing enables training on massive internet-scale datasets.",
                    "Serves as the foundational architecture for modern generative language models."
                ]
            }
        }
    }
}


def get_curated_subjects() -> list:
    """Return list of supported technical subjects."""
    return list(KNOWLEDGE_BASE.keys())


def get_curated_topics(subject: str) -> list:
    """Return available curated topics for a given subject."""
    return list(KNOWLEDGE_BASE.get(subject, {}).keys())


def get_curated_pack(subject: str, topic: str, difficulty: str) -> Optional[Dict[str, Any]]:
    """Retrieve curated pack if available for subject, topic, and difficulty."""
    sub_data = KNOWLEDGE_BASE.get(subject, {})
    # Case-insensitive topic search
    for top_key, diff_dict in sub_data.items():
        if top_key.lower() == topic.strip().lower():
            if difficulty in diff_dict:
                return diff_dict[difficulty]
            # Fallback to Beginner if level not exact
            if "Beginner" in diff_dict:
                return diff_dict["Beginner"]
    return None
