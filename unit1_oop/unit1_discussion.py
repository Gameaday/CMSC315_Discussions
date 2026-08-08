"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    # Class variable
    system_type = "Core Infrastructure"

    def __init__(self, name: str, version: float, metadata: list = None):
        # Instance variables
        self.name = name
        self.version = version
        self.metadata = metadata if metadata is not None else ["active", "standard"]

    def get_info(self) -> str:
        """Returns details about the parent object."""
        return f"[{ParentClass.system_type}] Name: {self.name}, Version: {self.version}, Metadata: {self.metadata}"

# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    # New class variable
    subsystem_type = "Extended Module"

    def __init__(self, name: str, version: float, metadata: list = None, module_id: int = 101, security_level: str = "High"):
        # Call parent constructor
        super().__init__(name, version, metadata)
        # New instance variables
        self.module_id = module_id
        self.security_level = security_level

    # New method
    def execute_task(self, task_name: str):
        """Simulate running a task within the subsystem."""
        print(f"Module {self.module_id} executing '{task_name}' [Security Level: {self.security_level}]")

    # Overridden method
    def get_info(self) -> str:
        """Override parent method to display subsystem details."""
        parent_info = super().get_info()
        return f"{parent_info} | Subsystem ID: {self.module_id}, Security: {self.security_level}"

# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # Create two ChildClass objects
    child1 = ChildClass("Module Alpha", 1.0, ["v1.0"], module_id=201, security_level="Medium")
    child2 = ChildClass("Module Beta", 2.0, ["v2.0"], module_id=202, security_level="High")

    # Access class variable through class and through object
    print(f"Class variable via Class (ChildClass.subsystem_type): {ChildClass.subsystem_type}")
    print(f"Class variable via Object (child1.subsystem_type)    : {child1.subsystem_type}")

    # Add a new attribute dynamically to child1 only
    child1.custom_tag = "Hotfix_Applied"
    print("\n[Action] Added dynamic attribute 'custom_tag' to child1 only.")

    # Display instance namespaces
    print("\n--- Instance Namespaces (__dict__) ---")
    print(f"child1 namespace: {child1.__dict__}")
    print(f"child2 namespace: {child2.__dict__}")

    # Display class namespace
    print("\n--- Class Namespace (ChildClass.__dict__) ---")
    for key, value in ChildClass.__dict__.items():
        if not key.startswith("__"):
            print(f"  {key}: {value}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # Original object containing nested mutable data (list within metadata)
    original = ChildClass("Data Engine", 3.5, metadata=["auth_enabled", ["sub_config_a", "sub_config_b"]])

    # Shallow Copy: Copies top-level object structure, but shares references to nested mutable objects.
    shallow_obj = copy(original)

    # Deep Copy: Recursively duplicates the top-level object AND all nested mutable objects inside it.
    deep_obj = deepcopy(original)

    print("--- Initial State ---")
    print(f"Original: {original.get_info()}")
    print(f"Shallow : {shallow_obj.get_info()}")
    print(f"Deep    : {deep_obj.get_info()}")

    # Modify nested mutable list in the original object
    print("\n[Action] Modifying original's nested data: appending 'MUTATED_VAL' to metadata[1]...")
    original.metadata[1].append("MUTATED_VAL")

    # Display results
    print("\n--- State After Modifying Original Nested Data ---")
    print(f"Original: {original.get_info()}")
    print(f"Shallow : {shallow_obj.get_info()}  <-- Modified! Shared nested reference.")
    print(f"Deep    : {deep_obj.get_info()}  <-- Unchanged! Independent object reference.")

# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n--- Parent Object ---")
    parent_obj = ParentClass("Base System", 1.0, ["stable", "production"])
    print(parent_obj.get_info())

    print("\n--- Child Object ---")
    child_obj = ChildClass("Secure Subsystem", 2.1, ["beta"], module_id=505, security_level="Top Secret")
    print(child_obj.get_info())

    print("\n--- Method Call & Inheritance ---")
    child_obj.execute_task("Data Integrity Scan")

    # Execute namespace and copy demonstrations
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()