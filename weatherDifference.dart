void main() {
  List<double> weathers = [10.0, 12.5, 14.0, 16.5, 15.0, 12.0];
  print(weatherDifference(weathers));
}

double weatherDifference(List<double> weathers) {
  double latestDifference = 0;
  for (int i = 0; i <= weathers.length - 1; i++) {
    if (weathers[i] - weathers[0] > 0) {
      latestDifference = weathers[i] - weathers[0];
    }
    if (weathers[0] - weathers[i] > 0) {
      latestDifference = weathers[0] - weathers[i];
    }
  }
  return latestDifference;
}