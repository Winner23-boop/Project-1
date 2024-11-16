void main() {
  Person alice = Person('Alice', 20);
  alice.age = 21;
  print('Alice is ${alice.age} years old');

  print('Next year, Alice will be ${alice.ageNextYear()} years old');
  print('Alice has a valid name: ${alice.hasValidName()}');

  print(alice);
  print(alice.runtimeType);

  print("Alice ${alice.isAdult()}");

}

class Person {
  String name = 'unknown';
  int age = 0;

  Person(String name, int age) {
    this.name = name;
    this.age = age;
  }

  int ageNextYear() {
    return age + 1;
  }

  bool hasValidName() {
    if (name.length > 2 && name.length < 100) {
      return true;
    } else {
      return false;
    }
  }

  String isAdult() {
    if (age >= 18) {
      return ("is an adult");
    } else {
      return ("is not an adult");
    }
  }

  String toString() {
    return 'Person(name: $name, age: $age)';
  }
}