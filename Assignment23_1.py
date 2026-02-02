class BookStore:

    NoOfBooks = 0

    def __init__(self,M,N):
        
        self.BookName = M
        self.AuthorName = N
        self.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):

        print("BookStore :", self.BookName ,self.AuthorName ,self.NofBooks)
    
obj1 = BookStore()
obj1.Display()

obj2 = BookStore()
obj2.Display()