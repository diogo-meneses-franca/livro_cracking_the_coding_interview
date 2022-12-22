import 'dart:ffi';

void main(){
  List<int> myList = [1,5, 8, 9, 11, 13, 15, 19, 21];

  binarySearch(myList, 9, 0,  myList.length - 1);




}



binarySearch(List<int> arr, int userValue, int min, int max) {
  if (max >= min) {
    int mid = ((max + min) / 2).floor();
    if (userValue == arr[mid]) {
      print('your item is at index: ${mid}');
    } else if (userValue > arr[mid]) {
      binarySearch(arr, userValue, mid + 1, max);
    } else {
      binarySearch(arr, userValue, min, mid - 1);
    }
  }
  return null;
}