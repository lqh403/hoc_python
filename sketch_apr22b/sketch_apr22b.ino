// Khai báo biến và hàm
int arr[10];
int len = sizeof(arr)/sizeof(arr[0]);
int average = 0;

// Hàm hiển thị mảng trên máy tính
void displayArray() {
  Serial.println("Mang ngau nhien:");
  for (int i=0; i<len; i++) {
    Serial.print(arr[i]);
    Serial.print(" ");
  }
  Serial.println();
}

// Hàm tính trung bình cộng các phần tử lẻ
void computeAverage() {
  int sum = 0;
  int count = 0;
  for (int i=0; i<len; i++) {
    if (arr[i]%2 != 0) {
      sum += arr[i];
      count++;
    }
  }
  if (count > 0) {
    average = sum/count;
  }
  else {
    average = 0;
  }
}

// Hàm sắp xếp mảng theo thứ tự tăng dần các phần tử lẻ
void sortArray() {
  for (int i=0; i<len-1; i++) {
    for (int j=i+1; j<len; j++) {
      if (arr[i]%2 != 0 && arr[j]%2 != 0 && arr[i] > arr[j]) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
      }
    }
  }
}

// Hàm setup
void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(0));
}

// Hàm loop
void loop() {
  // Tạo mảng ngẫu nhiên khi bật nguồn hoặc reset
  for (int i=0; i<len; i++) {
    arr[i] = random(1, 100);
  }
  
  // Hiển thị mảng trên máy tính
  displayArray();
  
  // Đợi nhấn phím
  while (!Serial.available());
  int key = Serial.read();
  
  // Tính trung bình cộng các phần tử lẻ khi nhấn KEY1
  if (key == '1') {
    computeAverage();
    Serial.print("Trung binh cong cac phan tu le: ");
    Serial.println(average);
  }
  
  // Sắp xếp mảng theo thứ tự tăng dần các phần tử lẻ khi nhấn KEY2
  if (key == '2') {
    sortArray();
    displayArray();
  }
}
