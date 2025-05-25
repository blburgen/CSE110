with open("books_and_chapters.txt") as books:
    
    largest_chapters = 0
    largest_book = ""
    
    print("\nWhich volume of scriptures they would like to learn about \n(for example, Old Testament, New Testament, ")
    user_choice = input("  Book of Mormon, Doctrine and Covenants, \n  Pearl of Great Price)? ")
    print("")
    
    for book in books:
        book_info = book.strip().split(":")
        if book_info[2].lower() == user_choice.lower():
            print(f"Scripture: {book_info[2] + ',':<25} Book: {book_info[0]+',':<25} Chapters: {book_info[1]}")
            if int(book_info[1]) > largest_chapters:
                largest_chapters = int(book_info[1])
                largest_book = book_info[0]
        if user_choice == "":
            print(f"Scripture: {book_info[2] + ',':<25} Book: {book_info[0]+',':<25} Chapters: {book_info[1]}")
            if int(book_info[1]) > largest_chapters:
                largest_chapters = int(book_info[1])
                largest_book = book_info[0]
            
    print(f"\nThe book with the most chapters is {largest_book} with {largest_chapters} chapters.\n")
        