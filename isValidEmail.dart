void main() {
  if (isValidEmail("up2196059@myport.ac.uk") != true) {
    print("You did not input a valid email");
  }
  else {
    print("You inputted a valid email");
  }
}

bool isValidEmail(String email) {
  if (email.substring(0, 2) != "up") {
    print("Your email does not have up at the beginning.");
    return false;
  }
  int startOfNumber = 2, endOfNumber = 9;
  String number = (email.substring(startOfNumber, endOfNumber));
  if (isValidNumber(number) == false) {
    print("You do not have a valid number");
    return false;
  }
  if (email.substring(9) != "@myport.ac.uk") {
    print("Your inputted email does not have the right address");
    return false;
  }
  return true;
}

bool isValidNumber(String number) {
  int intNumber = int.parse(number);
  if (int.parse(number) == intNumber) {
    return true;
  }
  else {
    return false;
  }
}