# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

# Unit 1 Discussion: Python Object-Oriented Programming, Namespaces, and Memory Copying
Object-Oriented Programming in Python 

## Overview
This repository contains the completed implementation for the Unit 1 programming assignment. The project evaluated core object-oriented programming (OOP) principles in Python, including single inheritance, method overriding, runtime namespace dynamics via `__dict__`, and memory reference management using shallow and deep copying techniques.

---

## Implementation Details

### 1. Class Design & Inheritance
* **Base Infrastructure (`ParentClass`):** Constructed a base class featuring a class-level variable (`system_type = "Core Infrastructure"`) and encapsulated instance properties (`name`, `version`, `metadata`). Included a string output method `get_info()` to report instance state.
* **Derived Subsystem (`ChildClass`):** Derived a child class inheriting from `ParentClass`. Introduced a specialized class variable (`subsystem_type = "Extended Module"`) and additional instance properties (`module_id`, `security_level`). 
* **Method Overriding & Extensions:** Overrode `get_info()` using `super().get_info()` to retain parent representation while appending subsystem details:
  ```python
  def get_info(self) -> str:
      parent_info = super().get_info()
      return f"{parent_info} | Subsystem ID: {self.module_id}, Security: {self.security_level}"
  ```
  Task Execution Method: Implemented execute_task() to simulate operational task execution under defined security controls:
    ```python
    def execute_task(self, task_name: str):
    print(f"Module {self.module_id} executing '{task_name}' [Security Level: {self.security_level}]")
    ```
    

### 2. Namespace Analysis (`demonstrate_namespaces()`)
* **Scope Resolution:** Demonstrated access to shared class attributes both via class references (`ChildClass.subsystem_type`) and instance bindings (`child1.subsystem_type`).
* **Dynamic Attribute Binding:** Appended a dynamic attribute (`custom_tag`) strictly to a single instance at runtime.
  ```python
  child1.custom_tag = "Hotfix_Applied"
  ```
* **Inspection:** Inspected instance namespaces using `__dict__` to verify that dynamic modification only impacted the targeted instance dictionary without polluting other instances or the base class dictionary.

### 3. Memory & Copy Behavior (`demonstrate_copying()`)
* **Data Structure:** Built an instance containing a nested mutable data structure (`metadata` list containing a sub-list).
* **Reference Isolation:** Executed both `copy.copy()` (shallow) and `copy.deepcopy()` (deep) on the target instance.
  ```python
  shallow_obj = copy(original)
  deep_obj = deepcopy(original)
  ```
* **Mutation Testing:** Modified the nested list within the original instance and printed all three states:
  ```python
  original.metadata[1].append("MUTATED_VAL")
  ```
  * **Shallow Copy:** Reflected the mutation due to shared memory references to the nested sub-list.
  * **Deep Copy:** Remained completely isolated, retaining its original state due to recursive allocation of new memory structures.

---

## Edge Case Handling & Testing Strategy

* **Defensive Parameter Initialization (Mutable Default Guard)**: Avoided Python's standard mutable default parameter trap (def __init__(self, metadata=[])) by explicitly checking for None before assigning default lists inside constructors:
```python
# Defensive check preventing shared mutable state across instances
def __init__(self, name: str, version: float, metadata: list = None):
    self.metadata = metadata if metadata is not None else ["active", "standard"]
```
* **Nested Object Mutations:** Verified boundary behavior when modifying nested elements. Tested boundary behavior when mutating sub-containers to prove reference isolation:
```python
# Modifying nested element directly to test reference pointer propagation
original.metadata[1].append("MUTATED_VAL")
```
* **Output Formatting:** Enhanced print statements with section headers and clear status messages to make namespace states and memory modifications easily auditable in the console.

---

## Real-World Application & System Architecture

* **Modular System Design:** Encapsulation and inheritance mirror enterprise technical architectures where core modules establish baseline protocols, and specialized sub-modules extend behavior without altering foundational logic.
* **System Resilience:** Isolated component structures prevent localized failures from cascading across shared environments.Proper defensive checks, such as metadata if metadata is not None else [...], ensure system stability when handling uninitialized parameters or processing runtime updates.
