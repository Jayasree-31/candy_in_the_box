def find_box_index(boxes, candies):
  print(boxes, candies)
  b = 1
  cx = candies - boxes
  cb = cx/(boxes - 1)
  loop = cb + 1
  if (loop%2 == 0):
    max_value = ((boxes - 1) * loop) + boxes
    print(boxes - (max_value - candies))
  else:
    max_value = ((boxes - 1) * loop) + boxes
    print((max_value - candies) + 1)


boxes = raw_input("Enter Your boxes!\n")
candies = raw_input("Enter Your candies!\n")
find_box_index(int(boxes), int(candies))
