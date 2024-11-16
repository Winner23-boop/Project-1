void main() {
  Rectangle myRectangle = Rectangle(0, 0, 5, 5);
  print(myRectangle);
  print(myRectangle.getArea());
}


class Shape {
  double x = 0.0;
  double y = 0.0;

  Shape(this.x, this.y);

  void move(double dx, double dy) {
    x += dx;
    y += dy;
  }

  String toString() => 'x: $x, y: $y';
}

class Rectangle extends Shape {
  double width = 0.0;
  double height = 0.0;

  Rectangle(double x, double y, double width, double height) : super(x, y) {
    this.width = width;
    this.height = height; }

    double getArea() {
      double area = width * height;
      return area;
    }

    double getPerimeter() {
      double perimeter = (width * 2) + (height * 2);
      return perimeter;
    }

    String toString() => '${super.toString()}, width: $width height: $height';
  }