def main():
    print([x*2 for x in [1,2,3,4]])
    print([x*2 for x in [1,2,3,4] if x % 2 == 0])
    print([x*2 if x % 2 == 0 else x+1 for x in [1,2,3,4]])
    # print([x*2 for x in [1,2,3,4] if x % 2 == 0 else x+1])



if __name__ == "__main__":
    main()