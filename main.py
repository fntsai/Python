

def writeFile(filename, msg):

    file = open(filename, "w")
    file.write(msg)
    file.close()

def readFile(filename):
    file = open(filename, "r")
    content = file.read()
    print(content)


def main():
    filename = "fnt.txt"
    content  = "hello world in the new file" + " and another line"
    writeFile(filename, content)


    filename = "/Users/FuNien/Documents/2016_RNA-seq/comparisons/20161015/Bim.LysMBim.Trif/differential expressed data/test_python.txt"
    print("=== Begin to read the file ===")
    print("Filename: ", filename)
    readFile(filename)

if __name__ == "__main__":
    main()