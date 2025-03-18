import pandas as pd
import time

url_dataset = 'https://raw.githubusercontent.com/Hackeddog/DSA-PROGRAMMING-ACT1/refs/heads/main/diabetes.csv'

def line(): # to create line
  print(f"{'-':-^90}")

#CREATE CLASS GENERAL (grandparent)--------------------------------------------------------------------------------------
'''
naa dri ang reading ug writing csv
'''
class General():
  def __init__(self, dataset, column):
    self.dataset = dataset
    self.column = column
    self.df = self.getdataframe()
    self.arr = []
    self.reading()

  def reading(self):
    for i in self.df[self.column]:
      self.arr.append(i)

  def writing(self, data):
    data.to_csv('sorted-diabetes.csv', index = False)

  def getdataframe(self):
    self.df = pd.read_csv(self.dataset, encoding = 'unicode_escape')# reading and storing the CSV in a data frame
    self.df.columns = self.df.columns.str.upper()#converting the column of the df into capitals
    return self.df


#CREATE SORTING CLASS (parent)----------------------------------------------------------------------------------------
'''
naa dri ang mga sorting functions
'''
class Sorting(General):
  def __init__(self, dataset, column, sorting_type):

    super().__init__(dataset, column)
    self.sorting_type = sorting_type
    self.sorted, self.exec_time = time_execution(self.sort)

  def sort(self):
    if self.sorting_type == 1:#bubble sort
      n = len(self.arr)
      for i in range(n):
          for j in range(0, n - i - 1):
            if self.arr[j] > self.arr[j + 1]:
              self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
      self.df.sort_values(self.column, ascending=True, inplace = True)
      self.writing(self.df)


    elif self.sorting_type == 2:#selection sort
      n = len(self.arr)
      for i in range(n):
          min_idx = i
          for j in range(i+1, n):
              if self.arr[j] < self.arr[min_idx]:
                  min_idx = j
          self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]
      self.df.sort_values(self.column, ascending=True, inplace = True)
      self.writing(self.df)




    elif self.sorting_type == 3:#insertion sort
      n = len(self.arr)
      for i in range(1, n):
          key = self.arr[i]
          j = i-1
          while j >= 0 and self.arr[j] > key:
              self.arr[j + 1] = self.arr[j]
              j -= 1
          self.arr[j + 1] = key
      self.df.sort_values(self.column, ascending=True, inplace = True)
      self.writing(self.df)



    elif self.sorting_type == 4:#quick sort

      def quickSort(arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]

        left = []
        middle = []
        right = []

        for x in arr:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            elif x > pivot:
                right.append(x)

        return quickSort(left) + middle + quickSort(right)

      self.arr = quickSort(self.arr)
      self.df.sort_values(self.column, ascending=True, inplace = True)
      self.writing(self.df)



#CREATE SEARCHING CLASS (child)------------------------------------------------------------------------------------------


class Searching(Sorting):
  def __init__(self, url_dataset, column, searching_type, target):
    super().__init__(url_dataset,column,sorting_type=0)
    self.target = target
    self.searching_type = searching_type
    self.result, self.exec_time = time_execution(self.search)

  def search(self):
    if self.searching_type == 1:#linear search
      n = len(self.arr)
      for x in range(n):
        if self.arr[x] == self.target:
          return x
      return -1 # Target not found

    elif self.searching_type == 2:#binary search
      super().__init__(url_dataset, column = self.column, sorting_type = 4)
      print(f'Sorting "{self.column}" column before Binary Search...')
      low = 0
      high = len(self.arr) - 1
      while low <= high:
            mid = (low + high) // 2
            if self.arr[mid] == self.target:
                for idx, val in enumerate(self.arr):
                    if val == self.target:
                        return idx
            elif self.arr[mid] < self.target:
                low = mid + 1
            else:
                high = mid - 1
      return -1  # Target not found

#CREATE UG MEASURING TIME EXECUTION-------------------------------------------------------------------------------------------

def time_execution(func):
    start_time = time.time()
    result = func()
    end_time = time.time()
    return result, end_time - start_time

#MAIN-------------------------------------------------------------------------

def main():
  sorting_type_names = {
    1: "Bubble Sort",
    2: "Selection Sort",
    3: "Insertion Sort",
    4: "Quick Sort"
  }
  searching_type_names = {
    1: "Linear Search",
    2: "Binary Search"
  }


  line()
  general = General(url_dataset,'AGE')#kaning age dri para lng naay instance
  print(f"{'Welcome to our program':^90}")
  while True:
    try:
      line()
      choice = int(input("Enter (1) - SORT or (2) - SEARCH. Enter (0) to exit: "))
      if choice == 1:
          while True:
            line()
            column = input("Choose a column to sort (Glucose, Age, BMI, etc.): ").upper()
            if column in general.df.columns:
              break
            else:
              line()
              print("Invalid column name. Please try again.")
          line()
          print("Choose sorting algorithm: \n(1) Bubble Sort\n(2) Selection Sort\n(3) Insertion Sort\n(4) Quick Sort")
          while True:
            line()
            try:
              sorting_type = int(input("Enter choice: "))
              if sorting_type in [1, 2, 3, 4]:
                break
              else:
                line()
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
            except ValueError:
              line()
              print("Invalid input. Please enter a number.")

          sorting = Sorting(url_dataset, column, sorting_type)
          line()
          print(f'Sorting by "{column}" using {sorting_type_names[sorting_type]}')
          print(f'Time taken: {sorting.exec_time:.6f} seconds')

      elif choice == 2:

          while True:
            line()
            column = input("Choose a column to search (Glucose, Age, BMI, etc.): ").upper()
            if column in general.df.columns:
              break
            else:
              line()
              print("Invalid column name. Please try again.")

          target = int(input("Enter the value to search: "))
          line()
          print("Choose searching algorithm: \n(1) Linear Search\n(2) Binary Search")

          while True:
            line()
            try:
              searching_type = int(input("Enter choice: "))
              if searching_type in [1, 2]:
                break
              else:
                line()
                print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
              line()
              print("Invalid input. Please enter a number.")
          searching = Searching(url_dataset, column, searching_type, target)
          line()
          print(f'Searching for "{target}" in "{column}" using {searching_type_names[searching_type]}')

          if searching.result == -1:
            line()
            print("Search not found.")
          else:
            line()
            print(f"Search found at row index {searching.result}")
          print(f'Time taken: {searching.exec_time:.6f} seconds')

      elif choice == 0:
          break
      else:
          print("Invalid choice. Please enter 1 or 2 and 0 for exit.")
    except ValueError:
      line()
      print("Invalid input. Please enter a number.")



main()#commencing program

