def main():
    midterm = [90, 80, 100, 75, 82, 80]
    for m in midterm:
        print(m)
    
    print(midterm[1])
    
    print(len(midterm))

    print(midterm[2:4])
    print(midterm[3:])
    print(midterm[:2])
    
    print(max(midterm))
    
    midterm.append(93)
    midterm.insert(2, 70)
    
    print(midterm)
    midterm.remove(80)
    
    print(midterm)
main()