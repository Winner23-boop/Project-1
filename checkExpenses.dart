void main() {
  List<double> expenses = [2.43, 3.33, 5.32, 100];
  if (checkExpenses(expenses, 25) == 1) {
    print("There is a value that goes above the limit");
  }
  else {
    print("All the values are below the limit");
  }
}

int checkExpenses(List<double> expenses, double maximumSpend) {
  int limitBreached = 0;
  for (int i = 0; i <= 3; i++) {
    if (expenses[i] >= maximumSpend) {
      limitBreached = 1;
    }
  }
  return limitBreached;
}