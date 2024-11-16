class Car {
  String colour;
  double speed;
  double distance;

  Car(this.colour, this.speed, this.distance);

  void accelerate(double inc) {
    speed += inc;
  }

  void distanceMeasure(double inc) {
    distance = speed * inc;
  }

  void brake() {
    speed = 0;
  }

  String toString() {
    return 'Car(colour: $colour, speed: $speed)';
  }
}