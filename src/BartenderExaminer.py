import csv

def importRecipes(reader):
    for row in reader:
        print(row)

def main():
    with open('../data/cocktails.csv', newline='') as file:
        reader = csv.reader(file)
        importRecipes(reader)

if __name__ == "__main__": main()