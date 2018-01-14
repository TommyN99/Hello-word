def main():
        page = int(input("Enter number of pages:"))
        if page % 2 == 0:
                print("")
        else:
                print("%60s%d" % (" ", page))
main()
