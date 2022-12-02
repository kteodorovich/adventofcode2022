def update_top3(cals, top3):
  top3.append(cals)
  top3.sort(reverse=True)
  return top3[0:3]


def main():
  max_cals = 0
  curr_cals = 0
  top3 = [0, 0, 0]

  with open('input.txt', 'r') as file:
    for line in file.readlines():
      if line == '\n':
        top3 = update_top3(curr_cals, top3)
        curr_cals = 0
      else:
        curr_cals += int(line)

  print(sum(top3))

if __name__ == '__main__':
  main()
