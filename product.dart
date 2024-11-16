void main() {
  Product product = Product('Washing-up liquid', 1.5);
  Product product2 = Product('b', 2.5);
  Product product3 = Product('c', 2.5);
  shoppingList list1 = shoppingList([], true);
  list1.addProduct(product);
  list1.addProduct(product2);
  list1.addProduct(product3);
  list1.checkClubcard();
  list1.printList();
}

class shoppingList {
  List<Product> productList = [];
  bool clubcard = false;

  shoppingList(this.productList, bool clubcard) {
    this.clubcard = clubcard;
  }

  void checkClubcard() {
    if (clubcard == true) {
      changePrices();
    }
    else {
      print("You do not have a clubcard");
    }
  }

  void changePrices() {
    for (int i = 0; i <= productList.length - 1; i++) {
      productList[i].changePrice(0.75);
    }
  }

  void addProduct(product) {
    productList.add(product);
  }

  double getTotal() {
    double total = 0;
    for (int i = 0; i <= productList.length -1 ; i++) {
      total = total + productList[i].returnPrice();
    }
    return total;
  }

  void printList() {
    print("Shopping Cart:");
    for (int i = 0; i <= productList.length - 1; i++) {
      print("${productList[i].returnName()}: ${productList[i].returnPrice()}");
    }
    print("Total: ${getTotal()}");
  }

}

class Product {
  String name = "";
  double price = 0.0;

  Product(String name, double price) {
    this.name = name;
    this.price = price;
  }

  void changePrice(double priceChange) {
    price = price * 0.75;
  }

  String returnName() {
    return name;
  }

  double returnPrice() {
    return price;
  }

  String toString() {
    return '$name: £$price';
  }

}